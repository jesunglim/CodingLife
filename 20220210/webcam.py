import cv2

cap = cv2.VideoCapture(0)

print('width : %d, height : %d' % (cap.get(3), cap.get(4)))


while(True):
    ret, frame = cap.read()

    if(ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame_color', frame)
        cv2.imshow('frame_gray', gray)
        if cv2.waitKey(1) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()