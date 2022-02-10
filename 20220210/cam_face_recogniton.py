import cv2

# 사진 검출기
def imgDetector(img, cascade):
    # 영상 압축
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)
    # 그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cascade 얼굴 탐지 알고리즘
    results = cascade.detectMultiScale(gray,
    scaleFactor= 1.5,
    minNeighbors= 5,
    minSize= (20,20)
    )

    for box in results:
        x, y, w, h = box
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), thickness=2)

    # 사진 출력
    cv2.imshow('facenet', img)



cap = cv2.VideoCapture(0)
print('width : %d, height : %d' % (cap.get(3), cap.get(4)))


# 가중치 파일 경로
cascade_filename = 'haarcascade_frontalface_default.xml'
# 모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)


while(True):   # 실시간 영상
    ret, frame = cap.read()

    if(ret):
        imgDetector(frame, cascade) # 사진 탐지기
        
        if cv2.waitKey(1) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()