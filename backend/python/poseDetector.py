import cv2
import time
import mediapipe as mp
import math
import physiotherapyAssessment as pta


class poseDetector():

    class landmark():
        def __init__(self, x, y, id):
            self.x = x
            self.y = y
            self.id = id

    def __init__(self, mode=False, upBodyOnly=False, smooth=True, conDet=0.5, conTrack=0.5):
        self.mode = mode
        self.upBodyOnly = upBodyOnly
        self.smooth = smooth
        self.conDet = conDet
        self.conTrack = conTrack
        self.mpPose = mp.solutions.pose
        # self.pose = self.mpPose.Pose(self.mode, self.upBodyOnly, self.smooth, self.conDet, self.conTrack)
        self.pose = self.mpPose.Pose(self.mode, self.upBodyOnly, self.smooth)
        # self.landmarks = self.landmarks()


    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                mp.solutions.drawing_utils.draw_landmarks(
                    img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self, img, draw=True):
        # landmarks = []

        # if self.results.pose_landmarks:
        #     for id, l in enumerate(self.results.pose_landmarks.landmark):
        #         h, w, c = img.shape
        #         # print(id, l)
        #         x, y = int(l.x*w), int(l.y*h)

        #         landmarks.append([id, x, y])
        #         if draw:
        #             cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
        # return(landmarks)

        l1 = ['NOSE', 'LEFT_EYE_INNER', 'LEFT_EYE', 'LEFT_EYE_OUTER', 'RIGHT_EYE_INNER', 'RIGHT_EYE', 'RIGHT_EYE_OUTER', 'LEFT_EAR', 'RIGHT_EAR', 'MOUTH_LEFT', 'MOUTH_RIGHT',
              'LEFT_SHOULDER', 'RIGHT_SHOULDER', 'LEFT_ELBOW', 'RIGHT_ELBOW', 'LEFT_WRIST', 'RIGHT_WRIST', 'LEFT_PINKY', 'RIGHT_PINKY', 'LEFT_INDEX', 'RIGHT_INDEX', 'LEFT_THUMB',
              'RIGHT_THUMB', 'LEFT_HIP', 'RIGHT_HIP', 'LEFT_KNEE', 'RIGHT_KNEE', 'LEFT_ANKLE', 'RIGHT_ANKLE', 'LEFT_HEEL', 'RIGHT_HEEL', 'LEFT_FOOT_INDEX', 'RIGHT_FOOT_INDEX']

        landmarks = {}

        if self.results.pose_landmarks:
            for id, l in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, l)
                xc, yc = int(l.x*w), int(l.y*h)
                name = l1[id]
                landmarks[name] = self.landmark(xc, yc, id)

                if draw:
                    cv2.circle(img, (xc, yc), 2, (0, 0, 255), -1)
        return(landmarks)

    def getResults(self):
        return self.results.pose_landmarks.landmark
    

    
    def getAngle(self, a, b, c):
        # slope of ab and bc
        if b.x == a.x:
            m1 = math.atan(math.inf)
        else:
            m1 = math.atan((b.y-a.y)/(b.x-a.x))
        if b.x == c.x:
            m2 = math.atan(math.inf)
        else:
            m2 = math.atan((c.y-b.y)/(c.x-b.x))
        # angle between ab and bc
        angle = math.degrees((m1-m2))
        if angle < 0:
            angle = 180 + angle

        return(angle)
    
    def getScale(self):
        return self.scale


def main():
    model = poseDetector()

    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture("1.mp4")

    pt = 0
    while True:
        success, img = cap.read()
        img = model.findPose(img)
        landmarks = model.getPosition(img)
        if len(landmarks) != 0:
            print(landmarks[14])
        ct = time.time()
        fps = 1/(ct-pt)
        pt = ct
        cv2.putText(img, str(int(fps)), (70, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
