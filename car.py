"""
Original: "Python crash course - Hands on - Project-Bases Introduction to programming"
Editado por,: Prof. adjunto Mag. Bioing. BALDEZZARI Lucas.
"""

class Car:
    """Clase para intentar representar un auto"""
    def __init__(self, fabricante:str, modelo:str, year:int):
        self.fabricante = fabricante
        self.modelo = modelo
        self.year = year
        self.odometer_reading = 0 #si es cero indica que el auto es 0km
        
    def getDescriptiveName(self):
        """Info del auto"""
        return f"{self.fabricante} - {self.modelo} - {self.year}"
    
    def readOdometer(self):
        """Kilometraje actual"""
        return self.odometer_reading
        
    def updateOdometer(self, kilometraje:int):
        """Se actualiza los kilómetros recorrido por el vehículo"""
        if kilometraje >= self.odometer_reading:
            self.odometer_reading = kilometraje
        else:
            print("No puede volver a atrás el odómetro, pillin!")
        
    def incrementOdometer(self, kms:int):
        """Aumento del kilometraje en una determinada cantidad de kms
        Params:
            - kms: Kilómetros recorridos
        """
        self.odometer_reading += kms

    def carAutonomy(self, consumo:int):
        """Cálculo de autonomía según el tipo de vehículo"""
        print("Aún no tengo definido qué tipo de vehículo soy")
        return None

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, fabricante, modelo, year, batterySize = 75):
        """Iniciamos atributos"""
        super().__init__(fabricante, modelo, year)
        self.battery = BatteryBank(batterySize = batterySize)

    def carAutonomy(self, consumo:int) -> float:
        """Cálculo de autonomía según el tipo de vehículo"""
        return self.battery.batteryAutonomy(consumo)

class BatteryBank:
    """Clase para simular un banco de baterías"""
    def __init__(self, batterySize:int = 75):
        """Iniciamos atributos del banco de baterías"""
        self._batterySize = batterySize
        self._batteryCharge = 1 # 1 = 100%

    def getBatteryInfo(self):
        """Info de la batería"""
        return f"El banco de batería es de {self._batterySize}kWh"

    def getBatteryCharge(self):
        """Retorna carga de la batería"""
        return self._batteryCharge

    def updateBatteryCharge(self, charge:int):
        """Actualiza la carga de la batería"""
        if charge <0 or charge >1:
            print("La carga de la batería debe ser un valor entre 0 y 1")
            return None #se podría retornar un error
        else: 
            self._batteryCharge = charge #%

    def batteryAutonomy(self, consumo:int) -> float:
        """Cálculo de autonomía según el tipo de vehículo. 
        Retorna la estimación de cuantos km puede hacer el vehículo.
        Params:
            - consumo: consumo actual en kWh/100km
        Return:
            - autonomía
        """
        return (self._batterySize/consumo*self._batteryCharge)*100#km

def main():
## Testeando baterías
    print("GRACIAS POR USAR ESTA LIBRERÍA")
    battery = BatteryBank(75)
    print(battery.getBatteryInfo())
    battery.updateBatteryCharge(0.8)
    print(battery.getBatteryCharge())
    print(f"La aunomoía es de {battery.batteryAutonomy(20)}kms")

    mitesla = ElectricCar('Tesla', 'modelo s', 2021)
    print(f"La carga de la batería es {battery.getBatteryCharge()}")
    print(f"Autnomía de {mitesla.carAutonomy(29):0.2f}kms")

    teslita = ElectricCar("BMW","Xi",2022)
    teslita.carAutonomy(20)

if __name__ == "__main__":
    main()