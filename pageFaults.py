import subprocess


# cria arquivo com informacoes dos processos ativos
subprocess.call(["ps -ef -o pid,min_flt,maj_flt > pageFaults.txt"], shell=True)



# abre arquivo com informacoes
arc = open('pageFaults.txt', 'r')
# le cada linha do arquivo
text = arc.readlines()

print(text)

# fecha arquivo
arc.close()
