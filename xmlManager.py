import xml.etree.ElementTree as ET
class xmlManager:
    root = None
    tree = None
    currentValue = None
    def __init__(self):
        self.tree = ET.parse("HighScores/HScores.xml")
        self.root = self.tree.getroot()
    def getplayerName(self , number):
        return str(self.root[number].tag)
    def getplayerScore(self , number): #inneficcient af , but works , needs to be redone later
        i=0
        valor = None
        for value in self.root.iter('score'):
            valor = value
            i+=1
            if i==number:
                break
        return valor.text
    def updateScore(self , score , name):
        #this need more thinking, bc if a score is higher than the rest, then change it
        valor= 0
        for value in self.root.iter('score'):
            if int(value.text) <= score:
                print("entre aca")
                print(str(value.text))
                value.text=str(score)
                value.set('updated' , 'yes')

                break
            valor+=1
        self.root[valor].tag = name
        self.tree.write("HighScores/HScores.xml") #the update
        #self.tree.write('Hscores.xml')