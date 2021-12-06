from pais import Pais
import requests
def imprime(paises):
    count_user = 0
    while count_user < len(paises):
        
        print('-'*5, count_user+1, '-'*5)
	    #print('Pais: ',paises[count_user].nombre, 'Enfermos: ',paises[count_user].confirmados , 'Muertos: ',paises[count_user].muertos, 'Curados: ',paises[count_user].recuperados)
        print(paises[count_user].mostrar())
        count_user += 1
        #set(paises[count_user].nombre)
def main():
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
        
        paises=[]
        for i in variable:
            paises.append(Pais(i['province'],i['country'], int(i['confirmed']), int(i['deaths']),int(i['recovered'])))

        while True:
            menu=input('''
            1 - Estadisticas de un pais o Estadisticas globales de CODVID-19
            2 - TOP 10 de los paises con mas infectados de COVID-19
            3 - TOP 10 de los paises con mas recuperados de COVID-19
            4 - TOP 10 de los paises con mas muertos de COVID-19
            
            ''')
            if menu=='1':
                paises=[]
                pais=input('Ingrese un pais: ')
                querystring["country"]=pais
                response = requests.request("GET", url, headers=headers, params=querystring)
                dic= response.json()
                variable=dic['data']['covid19Stats']
                for i in variable:
                    paises.append(Pais(i['province'],i['country'], int(i['confirmed']), int(i['deaths']),int(i['recovered'])))
                imprime(paises)
                break
main()