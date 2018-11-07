import subprocess
from tkinter import *
import matplotlib.pyplot as plt 


# abre arquivo de informacoes sobre memoria
arc = open('/proc/meminfo', 'r')
# le cada linha do arquivo
text = arc.readlines()

# recupera cada palavra da linha
memTotalSplit = text[0].split(" ")
memFreeSplit = text[1].split(" ")
memAvailableSplit = text[2].split(" ")
memCachedSplit = text[4].split(" ")
swapTotalSplit = text[14].split(" ")
swapFreeSplit = text[15].split(" ")

# recupera apenas o valor e transforma pra int
memTotal = int(memTotalSplit[8])
memFree = int(memFreeSplit[10])
memAvailable = int(memAvailableSplit[5])
memCached = int(memCachedSplit[11])
swapTotal = int(swapTotalSplit[7])
swapFree = int(swapFreeSplit[8])

# fecha arquivo
arc.close()


# funcao para plotar grafico de pizza
def plot_pizza( labels, values ):
    labels = [labels[0], labels[1]]
    titles = [values[0], values[1]]
    color = ['lightblue', 'green']
    explode = (0.1, 0)  # somente explode primeiro pedaço
    total = sum(titles)
    plt.pie(titles, explode=explode, labels=labels, colors=color, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90)





# PLOTAR GRAFICO 1: MEMORIA LIVRE X MEMORIA TOTAL 
def plotGraph1():
	labels1 = ['Mem. Livre', 'Mem. Total']
	values1 = [memFree, memTotal-memFree]

	# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
	plot_pizza( labels1, values1 )
	plt.axis('equal') 
	plt.show()




# PLOTAR GRAFICO 2: MEMORIA ACESSIVEL X MEMORIA TOTAL 
def plotGraph2():
	labels2 = ['Mem. Acessivel', 'Mem. Total']
	values2 = [memAvailable, memTotal-memAvailable]

	# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
	plot_pizza( labels2, values2 )
	plt.axis('equal') 
	plt.show()


# PLOTAR GRAFICO 3: MEMORIA CACHE X MEMORIA TOTAL
def plotGraph3():
	labels3 = ['Mem. Cache', 'Mem. Total']
	values3 = [memCached, memTotal-memCached]

	# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
	plot_pizza( labels3, values3 )
	plt.axis('equal') 
	plt.show()


# PLOTAR GRAFICO 4: SWAP TOTAL X MEMORIA TOTAL
def plotGraph4():
	labels4 = ['Swap', 'Mem. Total']
	values4 = [swapTotal, memTotal-swapTotal]

	# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
	plot_pizza( labels4, values4 )
	plt.axis('equal') 
	plt.show()


# PLOTAR GRAFICO 5: SWAP TOTAL X SWAP LIVRE
def plotGraph5():
	labels5 = ['Swap Total', 'Swap Livre']
	values5 = [swapFree, swapTotal-swapFree]

	# Determina que as proporções sejam iguais ('equal') de modo a desenhar o círculo
	plot_pizza( labels5, values5 )
	plt.axis('equal') 
	plt.show()





def pageFaults():
	# cria arquivo com informacoes dos processos ativos
    subprocess.call(["ps -ef -o pid,min_flt,maj_flt > pageFaults.txt"], shell=True)


    # abre arquivo com informacoes
    arc = open('pageFaults.txt', 'r')
    # le cada linha do arquivo
    text = arc.readlines()
    # fecha arquivo
    arc.close()


    # cria nova interface grafica
    pageFault = Tk()
    pageFault.title("PAGE FAULTS")
    pageFault.geometry('350x200')

    scrollbar = Scrollbar(pageFault)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(pageFault, yscrollcommand=scrollbar.set)
    for line in text:
        listbox.insert(END, line)
    listbox.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=listbox.yview)


    pageFault.mainloop()



# tela de visualizacao
window = Tk()
window.title("MEMORIA")
window.geometry('350x200')

btn = Button(window, text="Memória Total x Memória Livre", bg="orange", fg="white", command=plotGraph1)
btn.grid(column=1, row=0)


btn = Button(window, text="Memória Total x Memória Acessivel", bg="orange", fg="white", command=plotGraph2)
btn.grid(column=1, row=1)

btn = Button(window, text="Memória Total x Memória Cache", bg="orange", fg="white", command=plotGraph3)
btn.grid(column=1, row=2)

btn = Button(window, text="Memória Total x Swap Total", bg="orange", fg="white", command=plotGraph4)
btn.grid(column=1, row=3)


btn = Button(window, text="Swap Livre x Swap Total", bg="orange", fg="white", command=plotGraph5)
btn.grid(column=1, row=4)

btn = Button(window, text="Ver Page Faults", bg="orange", fg="white", command=pageFaults)
btn.grid(column=1, row=5)



window.mainloop()
