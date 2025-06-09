import random

class Train:
    def __init__(self,train_no):
        self.train_no=train_no
        
    def book(self,train_no,fro,to):
        print(f"your ticket has been booked  in {self.train_no} from {fro} to {to} ")
    
    def status(self,fro,to):

        status =random.choice(["waiting","confirmed"])

        
        print(f"status for your train no.{self.train_no} from {fro} to {to} is {status}")
    
    def fare(self,fro,to):
        print(f"fare from {fro} to {to} is {randrange(500,4500)}")

 
n=int(input("Enter the train number:::"))   
obj=Train(n)

obj.status("allahabad","delhi")
