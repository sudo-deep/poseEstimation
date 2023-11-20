# from asyncio import staggered
from turtle import right
import cv2
import json

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
situpSound = mixer.Sound("situp.mp3")
congoShoulder = mixer.Sound("congoShoulder.mp3")
congoNeck = mixer.Sound("congoNeck.mp3")


def show_frame(frame):
    frame.tkraise()

def postureCode(page=None):

    # show_frame(page)
    # videoLabel = tk.Label(posturePage)
    # videoLabel.pack(padx=20)

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
        # cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGBA)
        # img = Image.fromarray(cv2image)

        # imgtk = ImageTk.PhotoImage(image=img)
        # videoLabel.imgtk = imgtk
        # videoLabel.configure(image=imgtk)
        # videoLabel.after(20, showVideoFrame)

        
        # check if the posture is correct
        if not mixer.get_busy():
            if corrector.checkSlump():
            
                print("Sit up, you are slumping!")
                
                situpSound.play()

    # read the frame
    _, img = cap.read()
    img = model.findPose(img)

    showVideoFrame()



def shoulderCode(frame):
    show_frame(frame)
    # initialize the mixer
    mixer.init()
    # videoLabel = tk.Label(shoulderPage)
    # videoLabel.pack(padx=20)
    # counterVar = tk.StringVar()
    # counterVar.set("Counter: "+"0")
    # counterLabel = tk.Label(shoulderPage, textvariable=counterVar, font=("Helvetica", 20))
    # counterLabel.pack()
    
    # loading the model
    model = pd.poseDetector(conDet=0.75, conTrack=0.75)

    # selecting video source
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture("1.mp4")
    pt = 0
    dictStage = {"stage": "None", "counter": 0}
    def showVideoFrame():

        landmarks = model.getPosition(model.findPose(cap.read()[1]))
        # print(cap.read()[0])
        # cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGBA)
        # img = Image.fromarray(cv2image)

        # imgtk = ImageTk.PhotoImage(image=img)
        # videoLabel.imgtk = imgtk
        # videoLabel.configure(image=imgtk)
        # videoLabel.after(40, showVideoFrame)
        # check shoulder movement score
        if not mixer.get_busy():
            if dictStage["counter"] == 15:
                congoShoulder.play()
                # counterVar.set("Congrats! You did great!")
            
                return
            if "LEFT_SHOULDER" in landmarks and "RIGHT_SHOULDER" in landmarks and "LEFT_ELBOW" in landmarks and "RIGHT_ELBOW" in landmarks:
                
                
                leftAngle = model.getAngle(landmarks["LEFT_HIP"], landmarks["LEFT_SHOULDER"], landmarks["LEFT_ELBOW"])
                # print("Shoulder Score: ", leftAngle)
                rightAngle = 180 - model.getAngle(landmarks["RIGHT_HIP"], landmarks["RIGHT_SHOULDER"], landmarks["RIGHT_ELBOW"])
                # print("Shoulder Score: ", rightAngle)
                # if leftAngle and rightAngle:
                   # beepSound.play()
                # print(int(leftAngle), int(rightAngle))
                
                if leftAngle > 160 and rightAngle > 160:
                    
                    # beepSound.play()

                    dictStage["stage"] = "Up"
                if leftAngle < 30 and rightAngle < 30 and dictStage["stage"] == "Up":
                    beepSound.play()
                    dictStage["stage"] = "Down"
                    dictStage["counter"] += 1
                    # print(f"Shoulder Counter: {dictStage['counter']}")
                    with open("database.json") as f:
                        json.dump(f, dictStage)
                    
                    
                    print("Counter: ", dictStage["counter"])
                    # counterVar.set("Counter: "+str(dictStage["counter"]))
                    # window.update_idletasks()

    showVideoFrame()


def neckCode(frame):
    show_frame(frame)
    # initialize the mixer
    mixer.init()
    # videoLabel = tk.Label(neckPage)
    # videoLabel.pack(padx=20)
    # counterVar = tk.StringVar()
    # counterVar.set("Counter: "+"0")
    # counterLabel = tk.Label(neckPage, textvariable=counterVar, font=("Helvetica", 20))
    # counterLabel.pack()
    
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
        # videoLabel.imgtk = imgtk
        # videoLabel.configure(image=imgtk)
        # videoLabel.after(40, showVideoFrame)
        

        if not mixer.get_busy():
            if dictStage["counter"] == 15:
                congoNeck.play()
                # counterVar.set("Congrats! You did great!")
                
                # time.sleep(2)
                return
            try:
                if not corrector.checkSlump():
                    # beepSound.play()
                    dictStage["stage"] = "Up"
                elif corrector.checkSlump() and dictStage["stage"] == "Up":
                        beepSound.play()
                        dictStage["stage"] = "Down"
                        dictStage["counter"] += 1
                        with open("database.json", "w") as f:
                            json.dump(f, dictStage)
                        print("Counter: ", dictStage["counter"])
                        # counterVar.set("Counter: "+str(dictStage["counter"]))
                        # window.update_idletasks()                        
            except:
                pass
    # initialise loop variables



    # read the frame
    _, img = cap.read()
    img = model.findPose(img)

    showVideoFrame()


print("Welcome To REHABIFY my frandd")
print("Let's fix your posture")
while True:
    postureCode()