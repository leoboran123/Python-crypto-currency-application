import requests
from requests.api import request

api = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,ADA,DOGE,RVN,XLM,HOLO&tsyms=USD,EUR")
news = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
result_news = news.json()
result = api.json()


# print(result_news["Data"][1]["body"])
while True:
    print("*"*50)
    print("1- Anlık Kripto Fiyatları")
    print("2- Kripto Haberleri")
    print("3- Çıkış")
    secim = int(input("Seçim: "))

    if secim==1:
        print("1 BTC = " + str(result["BTC"]["USD"]) + " Dolar" )
        print("1 ETH = " + str(result["ETH"]["USD"]) + " Dolar" )
        print("1 ETH = " + str(result["ADA"]["USD"]) + " Dolar" )
        print("1 ETH = " + str(result["DOGE"]["USD"]) + " Dolar" )
        print("1 ETH = " + str(result["RVN"]["USD"]) + " Dolar" )
        print("1 ETH = " + str(result["XLM"]["USD"]) + " Dolar" )
        print("1 ETH = " + str(result["HOLO"]["USD"]) + " Dolar" )

    elif secim==2:
        j=1
        for i in result_news["Data"]:
            print(str(j) + ". Başlık- " + str(i["title"]) + "\n" + str(i["body"]) + "\n")
            j+=1
    elif secim==3:
        break
    else:
        print("Yanlış bir giriş yaptınız!")
