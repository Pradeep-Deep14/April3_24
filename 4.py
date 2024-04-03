class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

dog1=Dog("Dino","Poddle")
print(isinstance(dog1,Dog))

#checks whether dog 1 is an instance of the dog class
#Hence it turns out to be true