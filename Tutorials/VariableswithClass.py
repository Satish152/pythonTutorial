class car:
    wheels=4

    def car_spec(self,cname,mil):
        self.city="hyderabad"  #we call it as instance var which is based on the instance of the object
        print(cname,mil,self.wheels)

c1=car()
c1.car_spec("bmw",20)
print(c1.city)
c2=car()
c2.city="Vijayawada"
print(c2.city)
c2.car_spec("audi",20)