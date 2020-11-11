from abc import ABC, abstractmethod


class Config(ABC):

    @abstractmethod
    def getConfig(self):
        pass
