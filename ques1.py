class Animal:
    def animal_attribute(self):
        self.eye = "eye"
        self.ear = "ear"
        self.sakin ="skin"
        print("eye: {}\n ear:{}\n skin: {}".format(self.eye,self.ear,self.skin))


class Tiger(Animal):
    print("dangerous")

a=Animal()
b=Tiger()
b.animal_attribute()

