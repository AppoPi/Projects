

class Stuff:
    apples = 0
    oranges = 0
    
    def pickApple(self):
        self.apples = self.apples + 1
        
    def giveApple(self):
        self.apples = self.apples - 1
        
    def getApple(self):
        return self.apples
        
    def pickOrange(self):
        self.orange = self.orange + 1
        
    def giveOrange(self):
        self.orange = self.orange - 1
        
    def getOrange(self):
        return self.oranges