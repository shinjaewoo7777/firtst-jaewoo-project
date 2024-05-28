class Car:
    color = ""
    speed = 0
    count = 0

    def __init__(self, val):
        self.speed = val
        Car.count += 1

    def speedUp(self, val):
        self.speed += val
        print("자동차의 속도는 %dkm/h입니다" % (self.speed))

    def speedDown(self, val):
        self.speed -= val
        print("자동차의 속도는 %dkm/h입니다" % (self.speed))

    def __del__(self):
   		 Car.count-= 1

class SpdLimtdCar(Car):
	def speedUp(self,val):
		self.speed += val
		if self.speed >200:
			self.speed=200
		print('자동차의 속도는 %dkm/h입니다.'%(self.speed))

    def speedDown(self,val):
    	self.speed += val
	    if self.speed <0:
		    self.speed=0
	    print('자동차의 속도는 %dkm/h입니다.'%(self.speed))

    def printNum0fCars(self):
 	print("현제 등록가능한 자동차 수는 %d대입니다."%(Car.count))

myCar = Car(60)
dadCar = SpdLimtdCar(80)

myCar.speedUp(100)
myCar.speedDown(10)
myCar.speedDown(200)
dadCar.speedUp(80)
dadCar.speedUp(50)
dadCar.speedDown(250)
dadCar.printNumOfCars()
del(myCar)
dadCar.printNumOfCars()