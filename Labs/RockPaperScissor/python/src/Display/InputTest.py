from python.src.Display.Input import Input


class InputTest(Input):
    inputList = []

    def getInputString(self, request):
        return self.inputList.pop(0)
