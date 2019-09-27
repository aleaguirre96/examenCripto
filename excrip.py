import re
encriptado = 'xqxpwggoyffaoeqjjvmaefyjpvouuvnfalvfgtujuvqbñhxeuqbfrmrrcqwwwekqñfjwrrpqqhftvguxwsrmpfhrfeccitededntjñsothgffaoepupwwrjuktuaoebiyhñadbjfosnlqdjufokqdrxwslequrlitufrxfpgofqdlpvefwhuodqdidkirdljrxrvmsfohsrxwtssrryfxwkajñljpsvgxlrwsdhhuxuwacyurwwnvouxlmadbjjñsctqjtddoklqhleivzktvvecuknrluxuuwrjuvcfideokbvwhuejxqihñochsnrfdvxfxwwrjuktuaoknsfotigpuzpmrrgflhfejbjtssrrxqjailggqhlhnuqbtvqatucnhftgftjñlacnifssrvzkjownlqupmwfvzulruirpfwwaeeqqxsarroytpwsheuxlveeoyfñwshbiprjuvxuhrfvzqdjrttvzuwxftjulrihpgclplltrcfwñhqmqswhhqmqqhhitreyfgsrebjzpmrrgfahftrvfxrlivygwhjuvnblxfakpupdlccnlxxdakzfxhsnhhrpluaktqxwsdgztjvwnzzwzphdvxfxwwrjuktuaokbszssdgfknhfezygtumaeoyfhltjnkjjacrcfwñhqmqjzjaejbhzhioueyfohstqtjudokpupwhdgburssrlqqlxsrubyrvmrmosnrfek'

def repetidasGrupo(tam,encriptad2):
    listaSub = []
    for indice in range(len(encriptad2)- (tam-1)): ##grupo de 2
        grupo = encriptad2[indice:indice + tam]
        if grupo in listaSub:
            continue
        else:
            listaSub.append(grupo)
    print(len(listaSub))
    segundaLista = []

    for key in listaSub:
        encontrado = re.findall(key,encriptad2)
        if len(encontrado) > 1:
            if not (key in segundaLista):
                segundaLista.append([encontrado[0],len(encontrado)])

    for sub in segundaLista:
        print("Patron: "+sub[0]+" cantidad:"+str(sub[1]))
    print("Cantidad de palabras que se repiten:" +str(len(segundaLista))+ " tamaño de grupos: "+str(tam))
#repetidasGrupo(4,encriptado)
def dividirText(encriptad2):
    tam = 7
    listaGrupos = []
    indice = 0
    while indice != len(encriptad2):
        grupo = encriptad2[indice:indice + tam]
        listaGrupos.append(grupo)
        indice = indice + tam
    matrix = []
    for i in range(0,21):
        fila = []
        for j in range(0,5):
            grupo = listaGrupos[(i*5)+j]
            fila.append(grupo)
        matrix.append(fila)
    #print(matrix)
    print("\nCriptogramaordenado en grupos de 7 caracteres:\n")
    for i in range(0,21):
        fila = ' '
        for j in range(0,5):
            fila = fila+"  "+matrix[i][j]
        print(fila)
    print("")
    #print(listaGrupos)
    #print(len(listaGrupos))
    return matrix

def crearSubcri(matr):
    cont = 0
    for h in range(0,7):
        subcripto = ''
        for i in range(0,21):
            subcripto = subcripto+matr[i][0][h]+matr[i][1][h]+matr[i][2][h]+matr[i][3][h]+matr[i][4][h]
        cont+=1
        print("\nSubcriptograma "+str(cont)+"\n")
        print(subcripto)
        print("_________________________________________________________________________________________________________")


matr = dividirText(encriptado)
crearSubcri(matr)
##print (match_pattern.group(0))
