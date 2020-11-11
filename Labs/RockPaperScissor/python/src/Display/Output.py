from abc import ABC, abstractmethod


class Output(ABC):
    outputlist = []

    @abstractmethod
    def print(self, request):
        pass
