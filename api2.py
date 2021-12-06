import requests
from pais import Pais
import matplotlib.pyplot as plt

def existe(lista, valor):
    '''
    Verifica que el usuario exista
    variables predefinidad>
    count_user --- se utiliza para interar cada elemento del diccionario
    exite --- se utiliza para encontrar el elemento del diccionario
    return 
    existe--- retorna la posicion del nombre correspondiente
    
    '''
    count_user = 0
    existe = -1
    while count_user < len(lista):
        if lista[count_user].nombre == valor:
            existe = count_user
            break
        else:
            count_user += 1

    return existe

def imprime(paises):
    '''
    variable>
    paises--- lista de objetos
    count_user--- Va sumando mientras sea menor que el tamaño de paises
    '''
    count_user = 0
    while count_user < len(paises):
        
        print('-'*5, count_user+1, '-'*5)
        print(paises[count_user].mostrar())
        count_user += 1
        



def imprime_top_10_recuperados(paises):
    '''
    Imprime el top 10 de los recuperados
    variables>
    count_user--- se suma 1 mientras sea menor al tamaño de la lista
    paises--- lista de objetos


    '''
    count_user = 0
    nombres_paises=[]
    valores_recuperados=[]
    while count_user<10 and count_user < len(paises):
        
        nombres_paises.append(paises[count_user].nombre)
        valores_recuperados.append(int(paises[count_user].recuperados))
        
        print('-'*5, count_user+1, '-'*5)
        print(paises[count_user].recuperado())
        count_user += 1
    while True:
        validez=input('Para ver la grafica presione ENTER. En caso contrario presiona la tecla Espacio')
        if validez=='':
            plt.ylabel('Valores')
            plt.xlabel('Paises')
            plt.plot(nombres_paises, valores_recuperados, 'g-')
            plt.show()
            break
        elif validez==' ':
            break
        else:
            'Eleccion incorrecta'
            
        
def imprime_top_10_muertos(paises):
    '''
    Imprime el top 10 de los muertos
    variables>
    count_user--- se suma 1 mientras sea menor al tamaño de la lista
    paises--- lista de objetos


    '''
    count_user = 0
    nombres_paises=[]
    valores_muertos=[]
    while count_user<10 and count_user < len(paises):
        nombres_paises.append(paises[count_user].nombre)
        valores_muertos.append(int(paises[count_user].muertos))
        
        print('-'*5, count_user+1, '-'*5)
        print(paises[count_user].muerto())
        count_user += 1
    while True:
        validez=input('Para ver la grafica presione ENTER. En caso contrario presiona la tecla Espacio')
        if validez=='':
            plt.ylabel('Valores')
            plt.xlabel('Paises')
            plt.plot(nombres_paises, valores_muertos, 'r--')
            plt.show()
            break
        elif validez==' ':
            break
        else:
            'Eleccion incorrecta'
        
    

def imprime_top_10_enfermos(paises):
    '''
    Imprime el top 10 de los confirmados
    variables>
    count_user--- se suma 1 mientras sea menor al tamaño de la lista
    paises--- lista de objetos


    '''
    count_user = 0
    valores_enfermos = []
    nombres_paises = []
    while count_user<10 and count_user < len(paises):
        nombres_paises.append(paises[count_user].nombre)
        valores_enfermos.append(int(paises[count_user].confirmados))
        print('-'*5, count_user+1, '-'*5)
	    
        print(paises[count_user].confirmado())
        count_user += 1
    while True:
        validez=input('Para ver la grafica presione ENTER. En caso contrario presiona la tecla Espacio')
        if validez=='':
            plt.ylabel('Valores')
            plt.xlabel('Paises')
            plt.plot(nombres_paises, valores_enfermos, 'y-')
            plt.show()
            break
        elif validez==' ':
            break
        else:
            'Eleccion incorrecta'
    

def grafica(paises):
    count_user=0
    nombres_paises = []
    valores_enfermos = []
    valores_muertos = []
    valores_curados = []
    while count_user < 10 and count_user < len(paises):
        nombres_paises.append(paises[count_user].nombre)
        valores_enfermos.append(int(paises[count_user].confirmados))
        valores_muertos.append(int(paises[count_user].muertos))
        valores_curados.append(int(paises[count_user].recuperados))
        count_user += 1
    plt.ylabel('Valores')
    plt.xlabel('Paises')
    plt.plot(nombres_paises, valores_enfermos, '-', nombres_paises, valores_curados, '-', nombres_paises, valores_muertos, '-')
    plt.show()



def main():
    '''Funcion Principal'''
    while True:
        url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
        
        querystring = {"country":""}

        


        headers = {
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
            'x-rapidapi-key': "1249b1d96dmshc9c0203407e96fdp1de27ejsndaf586f59213"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        dic= response.json()
        variable=dic['data']['covid19Stats']
        lista=['']
        unicos=[]
        paises=[]
        
        for i in variable:
            pais_existe=existe(paises, i['country'])
            if pais_existe==-1:
                paises.append(Pais(i['country'],int(i['confirmed']),int(i['deaths']),int(i['recovered'])))
                unicos.append(i['country'])
                lista.append(i['country'].lower())
            else:
                paises[pais_existe].confirmados=paises[pais_existe].confirmados+int(i['confirmed'])
                paises[pais_existe].muertos=paises[pais_existe].muertos+int(i['deaths'])
                paises[pais_existe].recuperados=paises[pais_existe].recuperados+int(i['recovered'])
        
        while True:
            print('''
            Tracker CODVID-19 UNIMET
            ''')
            print('Escoja una opcion')
            menu=input('''
        1 - Estadisticas de un pais o Estadisticas globales de CODVID-19
        2 - TOP 10 de los paises con mas infectados de COVID-19
        3 - TOP 10 de los paises con mas recuperados de COVID-19
        4 - TOP 10 de los paises con mas muertos de COVID-19
            
            ''')
            if menu=='1':
                print(','.join(unicos))
                paises=[]
                print('''
                Ingrese el Nombre del Pais(En ingles) que desea buscar o si quieres una lista global de todos los paises presiona ENTER.
                
                ''')
                
                while True:
                    pais=input('Ingrese un pais: ')
                    if pais==pais.lower() or pais==pais.upper():
                        pais=pais.title()
                    elif (pais==pais.upper() or pais==pais.lower() or pais==pais.title()) and len(pais)<=2 :
                        pais=pais.upper()
                    if pais.lower() not in lista:
                        print('Ese pais no esta en la lista.')
                    else:
                        break  
                querystring["country"]=pais
                response = requests.request("GET", url, headers=headers, params=querystring)
                dic= response.json()
                variable=dic['data']['covid19Stats']
                for i in variable:
                    pais_existe=existe(paises, i['country'])
                    if pais_existe==-1:
                        paises.append(Pais(i['country'],int(i['confirmed']),int(i['deaths']),int(i['recovered'])))
                    else:
                        paises[pais_existe].confirmados=paises[pais_existe].confirmados+int(i['confirmed'])
                        paises[pais_existe].muertos=paises[pais_existe].muertos+int(i['deaths'])
                        paises[pais_existe].recuperados=paises[pais_existe].recuperados+int(i['recovered'])
                imprime(paises)
                
               
                break
            elif menu=='2':
                print('-----TOP 10 INFECTADOS-----')
                enfermos_10 = sorted(paises, key= lambda enfermos: enfermos.confirmados, reverse=True)
                imprime_top_10_enfermos(enfermos_10)
                break
            elif menu=='3':
                print('-----TOP 10 RECUPERADOS-----')
                recuperados_10 = sorted(paises, key= lambda enfermos: enfermos.recuperados, reverse=True)
                imprime_top_10_recuperados(recuperados_10)
                break
            elif menu=='4':
                print('-----TOP 10 MUERTOS-----')
                muertos_10 = sorted(paises, key= lambda enfermos: enfermos.muertos, reverse=True)
                
                imprime_top_10_muertos(muertos_10)
                break
            
            else:
                print('Falso')
        validez3=True
        contador=0
        while validez3==True:
            volver_menu=input('''
    1 - Volver al menu
    2 - Salir del sistema
        ''')
        

    

            if volver_menu.lower()=='1':
                    contador=0
                    validez3=False
        
        
            elif volver_menu.lower()=='2':
                contador+=1
                validez3=False
            else:
                print('\nOPCION INCORRECTA')

        if contador==0:
            continue
        elif contador>=1:
            break


main()


  