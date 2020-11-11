class WriteToFile:
    # Here will be the instance stored.
    file = ""
    filePath = "C:/Users/sgoud/University/Labs/FPSE/RockPaperScissor/resource/log/"
    fileName = "inputLog.csv"

    def __init__(self, fileName):
        self.fileName = fileName

    def writeToFile(self, logItem):
        if self.file == "":
            self.file = open(self.filePath + self.fileName, "w")
        self.file.write(str(logItem) + "\n")
