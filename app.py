from asyncio import staggered
from turtle import right
import cv2
import time

from matplotlib import container
import physiotherapyAssessment as pta
import poseDetector as pd
import postureCorrector as pc
from pygame import mixer, event
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

mixer.init()
beepSound = mixer.Sound("beep.mp3")
situpSound = mixer.Sound("situp.mp3")\


def show_frame(frame):
    frame.tkraise()

def postureCode(page):

    show_frame(page)
    videoLabel = tk.Label(posturePage)
    videoLabel.pack(padx=20)

    # initialize the mixer
    mixer.init()

    # loading the model
    model = pd.poseDetector(conDet=0.75, conTrack=0.75)

    # selecting video source
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("1.mp4")

    def showVideoFrame():
        landmarks = model.getPosition(model.findPose(cap.read()[1]))
        corrector = pc.postureCorrector(landmarks=landmarks)
        # time.sleep(0.1)        
        cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image=img)
        videoLabel.imgtk = imgtk
        videoLabel.configure(image=imgtk)
        videoLabel.after(20, showVideoFrame)

        
        # check if the posture is correct
        if not mixer.get_busy():
            if corrector.checkSlump():
            
                # print("Sit up, you are slumping!")
                
                situpSound.play()
            
        
    # initialise loop variables
    # while True:
    # i += 1

    # read the frame
    success, img = cap.read()
    img = model.findPose(img)

    # get the landmarks
    



    # # check fps 
    # ct = time.time()
    # fps = 1/(ct-pt)
    # pt = ct
    # cv2.putText(img, str(int(fps)), (70, 50),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # showVideoFrame(i)
    showVideoFrame()



def shoulderCode(frame):
    show_frame(frame)
    # initialize the mixer
    mixer.init()
    videoLabel = tk.Label(shoulderPage)
    videoLabel.pack(padx=20)
    counterVar = tk.StringVar()
    counterVar.set("0")
    counterLabel = tk.Label(shoulderPage, textvariable=counterVar, font=("Helvetica", 20))
    counterLabel.pack()
    
    # loading the model
    model = pd.poseDetector(conDet=0.75, conTrack=0.75)

    # selecting video source
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("1.mp4")
    pt = 0
    dictStage = {"stage": "None", "counter": 0}
    def showVideoFrame():

        landmarks = model.getPosition(model.findPose(cap.read()[1]))
        corrector = pc.postureCorrector(landmarks=landmarks)        
        cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image=img)
        videoLabel.imgtk = imgtk
        videoLabel.configure(image=imgtk)
        videoLabel.after(40, showVideoFrame)
        # check shoulder movement score
        if not mixer.get_busy():
            if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and "LEFT_ELBOW" in landmarks and "RIGHT_ELBOW" in landmarks:
                
                
                leftAngle = model.getAngle(landmarks["LEFT_HIP"], landmarks["LEFT_SHOULDER"], landmarks["LEFT_ELBOW"])
                # print("Shoulder Score: ", leftAngle)
                rightAngle = 180 - model.getAngle(landmarks["RIGHT_HIP"], landmarks["RIGHT_SHOULDER"], landmarks["RIGHT_ELBOW"])
                # print("Shoulder Score: ", rightAngle)
                # if leftAngle and rightAngle:
                   # beepSound.play()
                print(int(leftAngle), int(rightAngle))
                
                if leftAngle > 160 and rightAngle > 160:
                    
                    # beepSound.play()

                    dictStage["stage"] = "Up"
                if leftAngle < 30 and rightAngle < 30 and dictStage["stage"] == "Up":
                    beepSound.play()
                    dictStage["stage"] = "Down"
                    dictStage["counter"] += 1
                    
                    print("Counter: ", dictStage["counter"])
                    counterVar.set(str(dictStage["counter"]))
                    window.update_idletasks() 


def legCode(frame):
    show_frame(frame)
    # initialize the mixer
    mixer.init()
    videoLabel = tk.Label(shoulderPage)
    videoLabel.pack(padx=20)
    counterVar = tk.StringVar()
    counterVar.set("0")
    counterLabel = tk.Label(shoulderPage, textvariable=counterVar, font=("Helvetica", 20))
    counterLabel.pack()
    
    # loading the model
    model = pd.poseDetector(conDet=0.75, conTrack=0.75)

    # selecting video source
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("1.mp4")
    pt = 0
    dictStage = {"stage": "None", "counter": 0}
    def showVideoFrame():

        landmarks = model.getPosition(model.findPose(cap.read()[1]))
        corrector = pc.postureCorrector(landmarks=landmarks)        
        cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image=img)
        videoLabel.imgtk = imgtk
        videoLabel.configure(image=imgtk)
        videoLabel.after(40, showVideoFrame)
        # check shoulder movement score
        if not mixer.get_busy():
            if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and "LEFT_ELBOW" in landmarks and "RIGHT_ELBOW" in landmarks:
                
                
                leftAngle = model.getAngle(landmarks["LEFT_HIP"], landmarks["LEFT_SHOULDER"], landmarks["LEFT_ELBOW"])
                # print("Shoulder Score: ", leftAngle)
                rightAngle = 180 - model.getAngle(landmarks["RIGHT_HIP"], landmarks["RIGHT_SHOULDER"], landmarks["RIGHT_ELBOW"])
                # print("Shoulder Score: ", rightAngle)
                # if leftAngle and rightAngle:
                   # beepSound.play()
                print(int(leftAngle), int(rightAngle))
                
                if leftAngle > 160 and rightAngle > 160:
                    
                    # beepSound.play()

                    dictStage["stage"] = "Up"
                if leftAngle < 30 and rightAngle < 30 and dictStage["stage"] == "Up":
                    beepSound.play()
                    dictStage["stage"] = "Down"
                    dictStage["counter"] += 1
                    
                    print("Counter: ", dictStage["counter"])
                    counterVar.set(str(dictStage["counter"]))
                    window.update_idletasks()

    # initialise loop variables



    # read the frame
    success, img = cap.read()
    img = model.findPose(img)

    # get the landmarks


    


  





    showVideoFrame()

window = tk.Tk()
window.title("Physiotherapy Assessment")
window.state('zoomed')

window.rowconfigure(0, weight = 1)
window.columnconfigure(0, weight = 1)

homePage, posturePage, shoulderPage, legPage = tk.Frame(window), tk.Frame(window), tk.Frame(window), tk.Frame(window)

for frame in (homePage, shoulderPage, legPage, posturePage):
    frame.grid(row = 0, column = 0, sticky = 'nsew')

# code for Home Page
homeTitle = ttk.Label(homePage, text = "Physiotherapy Assessment", font = ("Helvetica", 30))
homeTitle.pack(fill="both", expand=True)

shoulderAssessmentButton = ttk.Button(homePage, text = "Shoulder Assessment", command = lambda:shoulderCode(shoulderPage))
shoulderAssessmentButton.pack(pady = 50)
postureCorrectorButton = ttk.Button(homePage, text = "Posture Corrector", command = lambda:postureCode(posturePage))
postureCorrectorButton.pack(pady = 80)

# code for Shoulder Page
shoulderTitle = ttk.Label(shoulderPage, text = "Shoulder Assessment", font = ("Helvetica", 50))
shoulderTitle.pack(fill="both")

# code for Posture Page
postureTitle = ttk.Label(posturePage, text = "Posture Corrector", font = ("Helvetica", 50))
postureTitle.pack(fill="both")

show_frame(homePage)
window.mainloop()



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
# counter = 0
# dictStage["stage"] = None
# while cap.isopened():
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
    

#     # # check posture every 60 frames
#     # if i % 60 == 0:

#         # # check if the posture is correct
#         # if corrector.checkSlump():
#         #     print("Sit up, you are slumping!")
#         #     situpSound = mixer.Sound("situp.mp3")
#         #     situpSound.play()
#     # if i % 30 == 0:
#     # check shoulder movement score
#     if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and "LEFT_ELBOW" in landmarks and "RIGHT_ELBOW" in landmarks:
        
#         shoulderAssessment = pta.shoulderAssessment(landmarks=landmarks)
#         shoulderScore = shoulderAssessment.getScoreList()
#         leftAngle = int(180-shoulderScore["leftShoulderScore"])
#         # print("Shoulder Score: ", leftAngle)
#         rightAngle = int(shoulderScore["rightShoulderScore"])
#         # print("Shoulder Score: ", rightAngle)
#         if leftAngle > 160 and rightAngle > 160:
#             dictStage["stage"] = "Up"
#         if leftAngle < 30 and rightAngle < 30 and dictStage["stage"] == "Up":
#             dictStage["stage"] = "Down"
#             counter += 1
#             print("Counter: ", counter)


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
