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
    landmarks = model.getPosition(img)
    for k, v in landmarks.items():
        print(k, v.id)
    # break

    # if len(landmarks) != 0:
    #     print(landmarks)
    # if len(landmarks) != 0:
    #     print(model.getAngle(landmarks[12], landmarks[14], landmarks[16]))
    ct = time.time()
    fps = 1/(ct-pt)
    pt = ct
    cv2.putText(img, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)