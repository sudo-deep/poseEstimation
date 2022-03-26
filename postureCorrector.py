class checkPosture():
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
        if self.landmarks[11][1] != -1 and self.landmarks[7][1] != -1 \
            and self.landmarks[11][1] >= (self.landmarks[7][1] +
                                                        (self.scale * 150)):
            return False
        
        if self.landmarks[12][1] != -1 and self.landmarks[8][1] != -1 \
            and self.landmarks[12][1] >= (self.landmarks[8][1] +
                                                        (self.scale * 160)):
            return False
        return True

