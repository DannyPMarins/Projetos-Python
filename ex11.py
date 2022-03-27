# Parte 1 - escrever arquivo
import csv

def escrever_arquivo(filename):
    planilha = [['Aluno', 'Nota1', 'Nota2', 'Nota3'],
                ['Luke', 7, 9, 9],
                ['Han', 4, 7, 10],
                ['Leia', 9, 9 , 9],
                ['JarJarBinks', 1, 2, 1]]

arquivo = open(filename ,'w' , encoding='uft-8')
csv.writer(arquivo, delimiter = ';' , lineterminator= '\n').writerow(planilha)
arquivo.close()

