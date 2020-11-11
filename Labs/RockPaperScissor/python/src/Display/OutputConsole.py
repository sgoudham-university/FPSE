from python.src.DataSource.WriteToFile import WriteToFile
from python.src.Display.Output import Output


class OutputConsole(Output):
    writeToFile = True
    outputWriteToFile = WriteToFile("userOutputLog.csv")

    def print(self, output):
        if self.writeToFile:
            self.outputWriteToFile.writeToFile(output)
        print(output)
