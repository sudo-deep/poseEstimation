import cv2
import time
import mediapipe as mp
import math


class poseDetector():
    def __init__(self, mode=False, upBodyOnly=False, smooth=True, conDet=0.5, conTrack=0.5):
        self.mode = mode
        self.upBodyOnly = upBodyOnly
        self.smooth = smooth
        self.conDet = conDet
        self.conTrack = conTrack
        self.mpPose = mp.solutions.pose
        # self.pose = self.mpPose.Pose(self.mode, self.upBodyOnly, self.smooth, self.conDet, self.conTrack)
        self.pose = self.mpPose.Pose(self.mode, self.upBodyOnly, self.smooth)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                mp.solutions.drawing_utils.draw_landmarks(
                    img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self, img, draw=True):
        lmList = []

        if self.results.pose_landmarks:
            for id, l in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, l)
                x, y = int(l.x*w), int(l.y*h)

                lmList.append([id, x, y])
                if draw:
                    cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
        return(lmList)

    
    def getAngle(self, a, b, c):
        # slope of ab and bc
        if b[1] == a[1]:
            m1 = math.atan(math.inf)
        else:
            m1 = math.atan((b[2]-a[2])/(b[1]-a[1]))
        if b[1] == c[1]:
            m2 = math.atan(math.inf)
        else:
            m2 = math.atan((c[2]-b[2])/(c[1]-b[1]))
        # angle between ab and bc
        angle = math.degrees((m1-m2))
        if angle < 0:
            angle = 180 + angle

        return(angle)



def main():
    model = poseDetector()

    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("1.mp4")

    pt = 0
    while True:
        success, img = cap.read()
        img = model.findPose(img)
        lmList = model.getPosition(img)
        if len(lmList) != 0:
            print(lmList[14])
        ct = time.time()
        fps = 1/(ct-pt)
        pt = ct
        cv2.putText(img, str(int(fps)), (70, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
