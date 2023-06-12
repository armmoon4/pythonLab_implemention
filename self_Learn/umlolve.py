class Lock():
    def __init__(self , locked , locatinId ,securityLevel):
        self.locked = locked
        self.locatiId = locatinId
        self.securityLevel = securityLevel
        self.status = "Locked"

    def getlocked(self):
        return self.locked
    def getlocatinId(self):
        return self.locatiId
    def getsecurityLevel(self):
        return self.securityLevel
    def getStatus(self):
        return self.status    
    def setStatus(self , status):
        self.status = status
    def __str__(self):
        return self.locked + ' ' + self.status



