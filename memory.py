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


