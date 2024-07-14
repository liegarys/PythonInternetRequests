import requests

# "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"


def get_crypto_data(url) :
    response = requests.get(url= url)

    if response.status_code == 200 :
        return response.json()


url = "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"
response = get_crypto_data(url= url)

user_input = input("Enter your crypto currency: ")

for crypto in response :
    if crypto["currency"] == user_input:
        print("Price : ", crypto["price"])
        break


