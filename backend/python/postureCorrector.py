import cv2

class postureCorrector():
    def __init__(self, landmarks={}, scale=1.0):
        self.landmarks = landmarks
        self.scale = scale

    def setLandmarks(self, landmarks):
        self.landmarks = landmarks

    def getLandmarks(self):
        return self.landmarks
    
    def setMessage(self, message):
        self.message = message
    
    def getMessage(self):
        return self.message
    
    def setScale(self, scale):
        self.scale = scale
    
    def getScale(self):
        return self.scale
    
    def checkLeanForward(self):
        if "LEFT_SHOULDER" in self.landmarks and "LEFT_EAR" in self.landmarks \
            and self.landmarks["LEFT_SHOULDER"].x >= (self.landmarks["LEFT_EAR"].x +
                                                        (self.scale * 150)):
            return False
        
        if "RIGHT_SHOULDER" in self.landmarks and "RIGHT_EAR" in self.landmarks \
            and self.landmarks["RIGHT_SHOULDER"].x >= (self.landmarks["RIGHT_EAR"].x +
                                                        (self.scale * 160)):
            return False
        return True

    def checkSlump(self):
        if "LEFT_SHOULDER" in self.landmarks and "RIGHT_SHOULDER" in self.landmarks and \
           "MOUTH_RIGHT" in self.landmarks and "MOUTH_LEFT" in self.landmarks:
            ny = (self.landmarks["LEFT_SHOULDER"].y + self.landmarks["RIGHT_SHOULDER"].y) / 2
            my = (self.landmarks["MOUTH_RIGHT"].y + self.landmarks["MOUTH_LEFT"].y) / 2
            
            if ny - my >= self.scale*90:
                return False
        return True
    
    # def checkHeadDrop(self):
    #     if "LEFT_EYE" in self.landmarks and "LEFT_EAR" in self.landmarks \
    #         and self.landmarks["LEFT_EYE"].y > (self.landmarks["LEFT_EAR"].y +
    #                                                 (self.scale * 15)):
    #         return False
    #     if "RIGHT_EYE" in self.landmarks and "RIGHT_EAR" in self.landmarks \
    #         and self.landmarks["RIGHT_EYE"].y > (self.landmarks["RIGHT_EAR"].y +
    #                                                 (self.scale * 15)):
    #         return False
    
    def correctPosture(self):
        return all([self.checkLeanForward(), self.checkSlump()])
