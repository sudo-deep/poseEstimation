import cv2
import time

from matplotlib import container
import physiotherapyAssessment as pta
import poseDetector as pd
import postureCorrector as pc
from pygame import mixer
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# LARGEFONT = ("Verdana", 35)

# class tkinterApp(tk.Tk):

#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)

#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}

#         for F in (StartPage, ShoulderTherapy, PostureCorrector):
#             frame = F(container, self)

#             self.frames[F] = frame

#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(StartPage)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()


# class StartPage(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         shoulderButton = ttk.Button(self, text="Shoulder Assessment", command = lambda: controller.show_frame(ShoulderTherapy))
#         shoulderButton.pack(pady=20)
#         postureButton = ttk.Button(self, text="Posture Correction", command=lambda: controller.show_frame(PostureCorrector))
#         postureButton.pack(pady=50)
#     # root = tk.Tk()
#     # root.title("AI Powered Remote Physiotherapy Assessment And Posture Corrector".upper())
#     # root.geometry("800x600")


#     # root.mainloop()

# class ShoulderTherapy(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         label1 = ttk.Label(self, text="Shoulder Assessment", font=LARGEFONT)
#         label1.pack(pady=10, padx=10)

#         button1 = ttk.Button(self, text ="StartPage",
#                             command = lambda : controller.show_frame(StartPage))
#         button1.pack(padx = 20, pady = 20)

# class PostureCorrector(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         label1 = ttk.Label(self, text="Posture Correction", font=LARGEFONT)
#         label1.pack(pady=10, padx=10)

#         button1 = ttk.Button(self, text ="StartPage",
#                             command = lambda : controller.show_frame(StartPage))
#         button1.pack(padx = 20, pady = 20)

        # label = ttk.Label(self)

        # def show_frames():
        #     # Get the latest frame and convert into Image
        #     cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        #     img = Image.fromarray(cv2image)

        #     # Convert image to PhotoImage
        #     imgtk = ImageTk.PhotoImage(image = img)
        #     label.imgtk = imgtk
        #     label.configure(image=imgtk)                
        # # initialize the mixer
        # mixer.init()

        # # loading the model
        # model = pd.poseDetector(conDet=0.75, conTrack=0.75)

        # # selecting video source

        # # cap = cv2.VideoCapture(0)
        # cap = cv2.VideoCapture("1.mp4")

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
        #     if i % 60 == 0:

        #         # check if the posture is correct
        #         if corrector.checkSlump():
        #             print("Sit up, you are slumping!")
        #             situpSound = mixer.Sound("situp.mp3")
        #             situpSound.play()
                
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
        #     # cv2.imshow("Image", img)

        #     label.after(20, show_frames)
        #     show_frames()

        #     cv2.waitKey(1)

        #     # end code after 1000 frames
        #     if i == 1000:
        #         break


# app = tkinterApp()
# app.mainloop()




# initialize the mixer
mixer.init()

# loading the model
model = pd.poseDetector(conDet=0.75, conTrack=0.75)

# selecting video source
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("1.mp4")

# initialise loop variables
pt = 0
i = 0
counter = 0
stage = None
while True:
    i += 1

    # read the frame
    success, img = cap.read()
    img = model.findPose(img)

    # get the landmarks
    landmarks = model.getPosition(img)
    corrector = pc.postureCorrector(landmarks=landmarks)

    # draw neck landmark
    if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks:
        nx = int((landmarks["RIGHT_SHOULDER"].x + landmarks["LEFT_SHOULDER"].x)/2)
        ny = int((landmarks["RIGHT_SHOULDER"].y + landmarks["LEFT_SHOULDER"].y)/2)
        cv2.circle(img, (nx, ny), 2, (0, 0, 255), -1)
    

    # check posture every 60 frames
    if i % 30 == 0:

    #     # check if the posture is correct
    #     if corrector.checkSlump():
    #         print("Sit up, you are slumping!")
    #         situpSound = mixer.Sound("situp.mp3")
    #         situpSound.play()
        
        # check shoulder movement score
        if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and "LEFT_ELBOW" in landmarks and "RIGHT_ELBOW" in landmarks:
            
            shoulderAssessment = pta.shoulderAssessment(landmarks=landmarks)
            shoulderScore = shoulderAssessment.getScoreList()
            leftAngle = int(180-shoulderScore["leftShoulderScore"])
            # print("Shoulder Score: ", leftAngle)
            rightAngle = int(shoulderScore["rightShoulderScore"])
            # print("Shoulder Score: ", rightAngle)
            if leftAngle > 160 and rightAngle > 160:
                stage = "Up"
            if leftAngle < 30 and rightAngle < 30 and stage == "Up":
                stage = "Down"
                counter += 1
                print("Counter: ", counter)


    # check fps 
    ct = time.time()
    fps = 1/(ct-pt)
    pt = ct
    cv2.putText(img, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # end code after 1000 frames
    if i == 1000:
        break