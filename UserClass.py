import TankClass


class User:
    # userTankList: TankClass

    def __init__(self, firstName, lastName ,username, password, email, faceID,reportLink, userID, userTankList):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.userID = userID
        self.userTankList = userTankList
        self.email = email
        self.faceID = faceID
        self.reportLink = reportLink

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getFirstName(self):
        '''a function that returns user's first name'''
        return self.firstName

    def getLastName(self):
        '''a function that returns user's last name'''
        return self.lastName

    def getUserID(self):
        '''a function that returns user ID'''
        return self.userID

    def getEmail(self):
        return self.email

    def setFaceID(self, faceID):
        '''a function that sets face ID'''
        self.faceID = faceID

    def setReportLink(self, reportLink):
        '''a function that sets report link'''
        self.reportLink = reportLink

    def getFaceID(self):
        '''a function that returns face ID'''
        return self.faceID

    def getReportLink(self):
        return self.reportLink

    def creatTank(self, tankID, typeOfFish,feedingSchedule, waterSalinityUpperThresh,waterSalinityLowerThresh, tempUpperThresh, tempLowerThresh,
                 pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing, waterQualityHistory):
        '''a function that appends a tank object to the user's tanks list
        and returns this newly created object'''
        newTank = TankClass.Tank(tankID, typeOfFish,feedingSchedule, waterSalinityUpperThresh,waterSalinityLowerThresh, tempUpperThresh, tempLowerThresh,
                 pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing, waterQualityHistory,None)
        self.userTankList.append(newTank)
        return newTank

    def getTankList(self):
        '''a function that returns a list of the user's tanks'''
        return self.userTankList

    def removeTank(self, tankID):
        '''a function that checks if the tank id exists and removes it
        returns 0 when the tank removal is successfull
        returns 1 when the tank doesn't exist'''
        tankIndex = -1
        for tank in range(0, len(self.userTankList)):
            if(self.userTankList[i].tankID) == tankID:
                tankIndex = tank
            else:
                tankIndex = -1
        if(tankIndex != -1):
            self.userTankList.remove()
            return 0
        else:
            return 1

    def getWaterQualityHistory(self):
        '''a function that returns a full list of
        all the user's tanks' water quality entries'''
        userWaterQualityHistory = []
        for tank in range(0, len(self.userTankList)):
            for entry in range (0, self.userTankList[tank].numOfWaterQualityEntries):
                userWaterQualityHistory.append(self.userTankList[tank].getWaterQualityHistory)
        return userWaterQualityHistory
