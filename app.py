import cv2
import time
import poseDetector as pd

model = pd.poseDetector()

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("1.mp4")

pt = 0
while True:
    success, img = cap.read()
    img = model.findPose(img)
    lmList = model.getPosition(img)
    # if len(lmList) != 0:
    #     print(lmList[14])
    if len(lmList) != 0:
        print(model.getAngle(lmList[12], lmList[14], lmList[16]))
    ct = time.time()
    fps = 1/(ct-pt)
    pt = ct
    cv2.putText(img, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)