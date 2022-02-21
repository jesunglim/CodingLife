import cv2
import numpy as np
import os.path

# 동영상 프레임 카운트
frameCount = 0

# Yolo 로드
net = cv2.dnn.readNet("yolov2.weights","yolov2.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

while(True):
    # Unity Recoder 이미지 파일 불러오기
    file_path = 'C:\\Users\\jesung\\Digital-twin\\Recordings\\' + str(frameCount).zfill(4) + '.jpg'

    if os.path.isfile(file_path):
        cap = cv2.VideoCapture(file_path)

        ret, frame = cap.read()

        if(ret):
            # 이미지 가져오기
            img = frame
            #img = cv2.resize(img, None, fx=0.4, fy=0.4)
            height, width, channels = img.shape

            # Detecting objects
            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            # 정보를 화면에 표시
            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        # Object detected
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        # 좌표
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)

            font = cv2.FONT_HERSHEY_PLAIN
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    color = colors[i]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 5)
                    cv2.putText(img, label, (x, y - 20), font, 1, color, 1)

            # 화면에 영상 출력
            cv2.imshow('YOLOv2', img)
            # 프레임 카운트 추가
            frameCount += 1

            if cv2.waitKey(1) == ord('q'):
                break


cap.release()
cv2.destroyAllWindows()