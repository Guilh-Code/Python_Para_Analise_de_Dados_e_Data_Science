from funcionalidades import *

tv = Televisor("SONY", "Sony-123")
controle = ControleRemoto(tv)

controle.sintonizaCanal("SBT")
controle.trocaCanal("SBT")

print(tv.canal_atual)
print(tv.volume)
tv.aumentaVolume(50)
print(tv.volume)
