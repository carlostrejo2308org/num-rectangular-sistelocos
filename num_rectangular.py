
from audioop import mul


def periocidad( arr , m):
    m -=1
    aux = 0                         
    
    for x in arr:
        if arr.count(x) > 1:            
            aux = arr.index(x,arr.index(x)+1)
            break
    if aux == m:
        return 'Número de Periosidad : {}'.format(aux)
    else :
        nArr = []   
        for x in range(m+1):
            if x in arr:
                print('', end="")
            else:                
                nArr.append(x)
        return nArr

def mixto(Xo, lim,a,c,m):
    lis = []
    for i in range(lim):
        lis.append('')
    lis[0] = Xo
    for i in range(lim-1):
        lis[i+1] = (a*lis[i]+c)%m
    return lis

def multiplicador(Xo, lim,a,m):
    lisMul = []
    for i in range(lim):
        lisMul.append('')
    lisMul[0] = Xo
    for i in range(lim-1):
        lisMul[i+1]= (a*lisMul[i])%m
    return lisMul

def probMixto(arr,Xo,lim,a,c,m):
    print(f"Con 'a' = {a} 'c' = {c} y 'm' = {m}")
    if( arr== []):
        print(f"Periocidad Completa. \nMixto: {mixto(Xo,lim,a,c,m)}\n")
    else:
        print(f"Periocidad incompleta. \nMixto: {mixto(Xo,lim,a,c,m)}\nFaltante: {periocidad(mixto(Xo,lim,a,c,m),m)}\n")

def probMultiplicador(arr,Xo,lim,a,m):
    print(f"Con 'a' = {a} y 'm' = {m}")
    if(arr==[]):
        print(f"Periocidad Completa. \nMultiplicador: {multiplicador(Xo,lim,a,m)}\n")
    else:
        print(f"Periocidad Incompleta. \nMultiplicador: {multiplicador(Xo,lim,a,m)} \nFaltante: {periocidad(multiplicador(Xo,lim,a,m),m)}\n")

    pass
if __name__ == '__main__':
    
    ##Probando Mixto con a = 5, c = 7 y m = 8
    semilla = 4
    a = 5
    c = 7
    m = 8
    n = m
    print(f"Datos ingresados en Mixto y Multiplicador: \nSemilla: {semilla} \nn: {n}\n")
    ##Probando Mixto con a = 5, c = 7 y m = 8
    arrmix = periocidad(mixto(semilla,n,a,c,m),m)
    probMixto(arrmix,semilla,n,a,c,m)

    #Probando multiplicador con a = 5, m = 39
    a= 5
    m = 39
    n= m
    arrmul = periocidad(multiplicador(semilla,n,a,m),m)
    probMultiplicador(arrmul,semilla,n,a,m)
    
    #Mixto con valores de prueba
    lis_a = [8,50,9]
    lis_c = [16,17,13]
    lis_m = [100,64,32]
    lis_Xo = [15,13,8]
    n_mix = lis_m

    print(f"#####################\nMixto\n#####################\n")
    #Ciclo para probar todos los ejemplos Mixto
    for i in range(len(lis_a)):
        arrCom = periocidad(mixto(lis_Xo[i],n_mix[i],lis_a[i],lis_c[i],lis_m[i]),lis_m[i])
        print(f"Semilla: {lis_Xo[i]} \nn: {n_mix[i]}")
        probMixto(arrCom,lis_Xo[i],n_mix[i],lis_a[i],lis_c[i],lis_m[i])


    
    print(f"#####################\nMultiplicativo\n#####################\n")
    #Valores para ejemplos de Multiplicativo
    lis_a = [203,221,5]
    lis_m = [10**5,10**3,64]
    lis_Xo = [17,3,7]
    n_mul = lis_m

    #Ciclo para probar todos los ejemplos Multiplicativo
    for i in range(len(lis_a)):
        arrCom = periocidad(multiplicador(lis_Xo[i],n_mul[i],lis_a[i],lis_m[i]),lis_m[i])
        print(f"Semilla: {lis_Xo[i]} \nn: {n_mul[i]}")
        probMultiplicador(arrCom,lis_Xo[i],n_mul[i],lis_a[i],lis_m[i])