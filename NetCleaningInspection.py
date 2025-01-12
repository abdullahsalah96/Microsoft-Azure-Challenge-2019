from cognitiveServices import Server


class NetCleaning(Server):
    def __init__(self):
        #change subAddress
        self.httpAddress = 'australiaeast.api.cognitive.microsoft.com'
        self.subAddress = "/customvision/v3.0/Prediction/8803f1fd-5690-4ed9-8a95-6097586fcf46/classify/iterations/Iteration1/image"
        self.predKey = 'bd5db334ffa249f1bd8ca2d43ccf5da3'
        self.contentType = 'application/octet-stream'
        self.predkey = '/subscriptions/16e8c7d2-4877-4c8f-bb77-ae2931dd33eb/resourceGroups/Test/providers/Microsoft.CognitiveServices/accounts/Test_Prediction'
        super().__init__(self.httpAddress, self.subAddress, self.predKey, self.contentType, self.predkey)

    def predict(self, imgPath):
        """
        a function that returns:
            * 1 if the fishnet doesn't need cleaning
            * 2 if the fishnet needs cleaning
            * 0 otherwise
        """
        pred = self.getPrediction(imgPath).decode()
        print(pred)
        tag_index = pred.find("tagId") + 8
        if(pred[tag_index:tag_index+1] == '3'): #change this to start of clean tag
            return 'No'
        elif(pred[tag_index:tag_index+1] == '1'): #change this to start of not clean tag
            return 'Yes'
        else:
            return "Can't Determine"
