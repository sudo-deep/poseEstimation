import cv2
import time
import physiotherapyAssessment as pta
import poseDetector as pd
import postureCorrector as pc
# import sys
# import winsound
from pygame import mixer


mixer.init()


model = pd.poseDetector(conDet=0.75, conTrack=0.75)

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("1.mp4")

pt = 0
i = 0
while True:
    i+=1
    success, img = cap.read()
    img = model.findPose(img)
    landmarks = model.getPosition(img)
    corrector = pc.postureCorrector(landmarks=landmarks)
    if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks:
        nx = int((landmarks["RIGHT_SHOULDER"].x + landmarks["LEFT_SHOULDER"].x)/2)
        ny = int((landmarks["RIGHT_SHOULDER"].y + landmarks["LEFT_SHOULDER"].y)/2)
        cv2.circle(img, (nx, ny), 2, (0, 0, 255), -1)
    
    # for k, v in landmarks.items():
    #     print(k, v.id, v.x, v.y)
    # # break

    # if len(landmarks) != 0:
    #     print(landmarks)
    # if len(landmarks) != 0:
    #     print(model.getAngle(landmarks[12], landmarks[14], landmarks[16]))
  
    # if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and \
    #        "MOUTH_RIGHT" in landmarks and "MOUTH_LEFT" in landmarks:
    #     ny = (landmarks["LEFT_SHOULDER"].y + landmarks["RIGHT_SHOULDER"].y) / 2
    #     my = (landmarks["MOUTH_RIGHT"].y + landmarks["MOUTH_LEFT"].y) / 2
    #     print(ny - my)

    if i % 60 == 0:
        if corrector.checkSlump():
            print("Sit up, you are slumping!")
            # print("\a")
            # winsound.Beep(440, 500)
            situpSound = mixer.Sound("situp.mp3")
            situpSound.play()
        #     sys.stdout.write("\rSit up, you are slumping!")
        # else:
        #     sys.stdout.flush()

        # if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and "LEFT_ELBOW" in landmarks and "RIGHT_ELBOW" in landmarks:
            
        #     shoulderAssessment = pta.shoulderAssessment(landmarks=landmarks)
        #     shoulderScore = int(shoulderAssessment.getScore())
        #     # print("Shoulder Score: ", shoulderScore)
        #     sys.stdout.write("\rShoulder Score: " + str(shoulderScore))
        #     sys.stdout.flush()
    
    ct = time.time()
    fps = 1/(ct-pt)
    pt = ct
    cv2.putText(img, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if i == 1000:
        break