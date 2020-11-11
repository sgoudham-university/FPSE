from python.src.DataSource.Config import Config


class ConfigFromStub(Config):

    def getConfig(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star Wars:Darth Vadar,Emperor,Luke Skywalker")
        return propertyData
