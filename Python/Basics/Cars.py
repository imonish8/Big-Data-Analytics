# multiple interitance

# car petrol
#car EV
# Car Hybrid

class cPetrol:
    def __init__(self, pSpeed, pMileage, pCO2):
        self.pSpeed = pSpeed
        self.pMileage = pMileage
        self.pCO2 = pCO2

    def PetrolCar(self):
        print(f"Petrol Car speed is : {self.speed},  Petrol Car Mileage is : {self.pMileage},  Petrol Car CO2 Contribution is : {self.CO2}")


class cEV:
    def __init__(self, evSpeed, evMileage, evCO2):
        self.evSpeed = evSpeed
        self.evMileage = evMileage
        self.evCO2 = evCO2

    def EVCar(self): 
        print(f"Electric Vehicle :{self.evSpeed}, Electric Vehicle Mileage : {self.evMileage}, Electric vehicle C02 Combustion : {self.evCO2}")

class cHybrid(cPetrol, cEV):
    def __init__(self,pSpeed, pMileage, pCO2, evSpeed, evMileage, evCO2,model):
        self.model = model
        cPetrol.__init__(self, pSpeed, pMileage, pCO2)
        cEV.__init__(self, evSpeed, evMileage, evCO2)

    def Hybrid(self):
        print()
        print(f"Hybrid Car Details")
        print(f"Model Name : {self.model}, Hybrid Car Mileage on Petrol : {self.pMileage}, Hybrid Car Mileage on Electric : {self.evMileage}")
        print(f"Car Speed on Electric : {self.evSpeed}, Car Speed on Petrol : {self.pSpeed}")
        print(f"Combustion on Electric : {self.evCO2}, On Petrol : {self.pCO2}")
        print()


objHyb = cHybrid(180, 39, "22%", 120, 30, "0%", "BMW 330e")
objHyb.Hybrid()
