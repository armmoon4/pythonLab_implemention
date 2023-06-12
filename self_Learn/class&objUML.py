class Animal():
    def __init__(self , name , colour):
        self.name = name
        self.colour = colour
    def running(self):
        print(f'hey i am {self.name} , i am running now')

    def drinknig(self):
        print(f'hey i am {self.name} my colour is {self.colour} and i am drinking')

tom = Animal('tom' , 'gray')
jerry = Animal('Jerry' , 'orange')

tom.running()
tom.drinknig()

jerry.running()
jerry.drinknig()