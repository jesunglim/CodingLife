from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import sys

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import yaml

from recognition.backbones.resnet_v1 import ResNet_v1_50
from recognition.data.generate_data import GenerateData
from recognition.models.models import MyModel
from recognition.predict import get_embeddings

#tf.enable_eager_execution()


class Valid_Data:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    @staticmethod
    def _cal_cos_sim(emb1, emb2):
        return tf.reduce_sum(emb1 * emb2, axis=-1)

    def _get_sim_label(self):
        sims = None
        labels = None
        for image1, image2, label in self.data:
            emb1 = get_embeddings(self.model, image1)
            emb2 = get_embeddings(self.model, image2)
            sim = self._cal_cos_sim(emb1, emb2)
            if sims is None:
                sims = sim
            else:
                sims = tf.concat([sims, sim], axis=0)

            if labels is None:
                labels = label
            else:
                labels = tf.concat([labels, label], axis=0)

        return sims, labels

    @staticmethod
    def _cal_metric(sim, label, thresh):
        tp = tn = fp = fn = 0
        predict = tf.greater_equal(sim, thresh)
        for i in range(len(predict)):
            if predict[i] and label[i]:
                tp += 1
            elif predict[i] and not label[i]:
                fp += 1
            elif not predict[i] and label[i]:
                fn += 1
            else:
                tn += 1
        acc = (tp + tn) / len(predict)
        p = 0 if tp + fp == 0 else tp / (tp + fp)
        r = 0 if tp + fn == 0 else tp / (tp + fn)
        fpr = 0 if fp + tn == 0 else fp / (fp + tn)
        return acc, p, r, fpr

    def _cal_metric_fpr(self, sim, label, below_fpr=0.001):
        acc = p = r = thresh = 0
        for t in np.linspace(-1, 1, 100):
            thresh = t
            acc, p, r, fpr = self._cal_metric(sim, label, thresh)
            if fpr <= below_fpr:
                break

        return acc, p, r, thresh

    def get_metric(self, thresh=0.2, below_fpr=0.001):
        sim, label = self._get_sim_label()
        acc, p, r, fpr = self._cal_metric(sim, label, thresh)
        acc_fpr, p_fpr, r_fpr, thresh_fpr = self._cal_metric_fpr(sim, label, below_fpr)
        return acc, p, r, fpr, acc_fpr, p_fpr, r_fpr, thresh_fpr

    def draw_curve(self):
        P = []
        R = []
        TPR = []
        FPR = []
        sim, label = self._get_sim_label()
        for thresh in np.linspace(-1, 1, 100):
            acc, p, r, fpr = self._cal_metric(sim, label, thresh)
            P.append(p)
            R.append(r)
            TPR.append(r)
            FPR.append(fpr)

        plt.axis([0, 1, 0, 1])
        plt.xlabel("R")
        plt.ylabel("P")
        plt.plot(R, P, color="r", linestyle="--", marker="*", linewidth=1.0)
        plt.show()

        plt.axis([0, 1, 0, 1])
        plt.xlabel("FRP")
        plt.ylabel("TPR")
        plt.plot(FPR, TPR, color="r", linestyle="--", marker="*", linewidth=1.0)
        plt.show()


def parse_args(argv):
    parser = argparse.ArgumentParser(description='valid model')
    parser.add_argument('--config_path', type=str, help='path to config path', default='configs/config.yaml')

    args = parser.parse_args(argv)

    return args


def main():
    args = parse_args(sys.argv[1:])
    # logger.info(args)

    with open(args.config_path) as cfg:
        config = yaml.load(cfg, Loader=yaml.FullLoader)
    gd = GenerateData(config)
    valid_data = gd.get_val_data(config['valid_num'])
    model = MyModel(ResNet_v1_50, embedding_size=config['embedding_size'])
    import os
    ckpt_dir = os.path.expanduser(config['ckpt_dir'])
    ckpt = tf.train.Checkpoint(backbone=model.backbone)
    ckpt.restore(tf.train.latest_checkpoint(ckpt_dir)).expect_partial()
    print("Restored from {}".format(tf.train.latest_checkpoint(ckpt_dir)))

    vd = Valid_Data(model, valid_data)
    acc, p, r, fpr, acc_fpr, p_fpr, r_fpr, thresh_fpr = vd.get_metric(0.2, 0.001)
    print(acc, p, r, fpr, acc_fpr, p_fpr, r_fpr, thresh_fpr)
    vd.draw_curve()


if __name__ == '__main__':
    # logger.info("hello, insightface/recognition")
    main()
