import matplotlib.pyplot as plt
sabores = ["Muçarela","Calabresa","Portuguesa","Catupiry", "Frango","4 queijos"]
consumo = [20,15,2,8,50,2]

#plt.bar(sabores,consumo)
plt.pie(consumo,labels=sabores)
plt.show()