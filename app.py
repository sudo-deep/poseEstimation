import cv2
import time
import physiotherapyAssessment as pta
import poseDetector as pd
import postureCorrector as pc
from pygame import mixer
import tkinter as tk


root = tk.Tk()
root.title("AI Powered Remote Physiotherapy Assessment And Posture Corrector".upper())
root.geometry("800x600")

physioButton = tk.Button(root, text="Physiotherapy Assessment")
physioButton.pack(pady=20)
postureButton = tk.Button(root, text="Posture Correction")
postureButton.pack(pady=50)

root.mainloop()


# # initialize the mixer
# mixer.init()

# # loading the model
# model = pd.poseDetector(conDet=0.75, conTrack=0.75)

# # selecting video source
# cap = cv2.VideoCapture(0)
# # cap = cv2.VideoCapture("1.mp4")

# # initialise loop variables
# pt = 0
# i = 0
# while True:
#     i += 1

#     # read the frame
#     success, img = cap.read()
#     img = model.findPose(img)

#     # get the landmarks
#     landmarks = model.getPosition(img)
#     corrector = pc.postureCorrector(landmarks=landmarks)

#     # draw neck landmark
#     if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks:
#         nx = int((landmarks["RIGHT_SHOULDER"].x + landmarks["LEFT_SHOULDER"].x)/2)
#         ny = int((landmarks["RIGHT_SHOULDER"].y + landmarks["LEFT_SHOULDER"].y)/2)
#         cv2.circle(img, (nx, ny), 2, (0, 0, 255), -1)
    

#     # check posture every 60 frames
#     # if i % 60 == 0:

#     #     # check if the posture is correct
#     #     if corrector.checkSlump():
#     #         print("Sit up, you are slumping!")
#     #         situpSound = mixer.Sound("situp.mp3")
#     #         situpSound.play()
        
#     #     # check shoulder movement score
#     #     if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and "LEFT_ELBOW" in landmarks and "RIGHT_ELBOW" in landmarks:
            
#     #         shoulderAssessment = pta.shoulderAssessment(landmarks=landmarks)
#     #         shoulderScore = int(shoulderAssessment.getScore())
#     #         print("Shoulder Score: ", shoulderScore)



#     # check fps 
#     ct = time.time()
#     fps = 1/(ct-pt)
#     pt = ct
#     cv2.putText(img, str(int(fps)), (70, 50),
#                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)

#     # end code after 1000 frames
#     if i == 1000:
#         break