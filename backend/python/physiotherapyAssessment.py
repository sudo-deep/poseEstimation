import poseDetector as ps

class shoulderAssessment():
    def __init__(self, landmarks={}, scale=1.0):
        self.landmarks = landmarks
        self.scale = scale

    class shoulderAROM():
        def __init__(self, landmarks={}, scale=1.0):
            self.landmarks = landmarks
            self.scale = scale

        def elevAbduction(self):
            model = ps.poseDetector()
            leftShoulderAngle = model.getAngle(self.landmarks["LEFT_ELBOW"], self.landmarks["LEFT_SHOULDER"], self.landmarks["LEFT_HIP"])
            leftElbowAngle = model.getAngle(self.landmarks["LEFT_SHOULDER"], self.landmarks["LEFT_ELBOW"], self.landmarks["LEFT_WRIST"])
            scores = {}
            scores["leftElbowScore"] = leftElbowAngle
            scores["leftShoulderScore"] = leftShoulderAngle
            
            rightShoulderAngle = model.getAngle(self.landmarks["RIGHT_ELBOW"], self.landmarks["RIGHT_SHOULDER"], self.landmarks["RIGHT_HIP"])
            rightElbowAngle = model.getAngle(self.landmarks["RIGHT_SHOULDER"], self.landmarks["RIGHT_ELBOW"], self.landmarks["RIGHT_WRIST"])
            scores["rightElbowScore"] = rightElbowAngle
            scores["rightShoulderScore"] = rightShoulderAngle
            scores["avgScore"] = sum(scores.values())/(len(scores))
            
            return(scores)

    def getScoreList(self):
        arom = self.shoulderAROM(self.landmarks, self.scale)

        score = arom.elevAbduction()
        
        return score
