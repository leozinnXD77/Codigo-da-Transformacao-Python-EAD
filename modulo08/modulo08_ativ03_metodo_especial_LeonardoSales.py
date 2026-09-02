import time
class Carro:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        time.sleep(1)
        return f"\n{info_base} | Autonomia da Bateria: {self.autonomia} km"

meu_carro = CarroEletrico("BYD", "Dolphin", 600)
print('\n','=' * 48)
print(meu_carro.exibir_info())
time.sleep(2)
print('\n','=' * 48,'\n')