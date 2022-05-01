import torch
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

#데이터 불러오기, 학습여부  o
trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)

#학습용 셋은 섞어서 뽑기
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)
#데이터 불러오기, 학습여부  x
testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
#테스트 셋은 굳이 섞을 필요가 없음
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)
#클래스들
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


import matplotlib.pyplot as plt
import numpy as np

def imshow(img):
    img = img / 2 + 0.5     # 정규화 해제
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

# 윈도우에선 에러나서 이렇게 해야됨
def run():
    torch.multiprocessing.freeze_support()

    # 학습용 이미지 뽑기
    dataiter = iter(trainloader)
    images, labels = dataiter.next()

    import torch.nn as nn
    import torch.nn.functional as F

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()

            # input = 3, output = 6, kernal = 5
            self.conv1 = nn.Conv2d(3, 6, 5)
            # kernal = 2, stride = 2, padding = 0 (default)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            # input feature, output feature
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        # 값 계산
        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 * 5)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = Net()

    import torch.optim as optim

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(2):  # 데이터셋 2번 받기

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # 입력 받기 (데이터 [입력, 라벨(정답)]으로 이루어짐)
            inputs, labels = data

            # 학습
            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # 결과 출력
            running_loss += loss.item()
            if i % 2000 == 1999:  # print every 2000개마다
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 2000))
                running_loss = 0.0

    print('Finished Training')

    # 여기에 학습한 모델 저장
    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)

    # optimizer의 기울기를 0으로 만들기 (변화도가 누적되지 않게 하기 위해)
    optimizer.zero_grad()
    # output 구하기
    outputs = net(inputs)
    # loss 계산
    loss = criterion(outputs, labels)
    # backpropagation (기울기 계산)
    loss.backward()
    # 업데이트
    optimizer.step()

    dataiter = iter(testloader)
    images, labels = dataiter.next()

    # 학습한 모델로 예측값 뽑아보기
    net = Net()
    net.load_state_dict(torch.load(PATH))
    outputs = net(images)

    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
            100 * correct / total))

if __name__ == '__main__':
    # 학습용 이미지 뽑기
    run()