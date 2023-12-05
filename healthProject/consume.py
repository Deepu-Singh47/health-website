import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":"wat"}

headers = {
	"X-RapidAPI-Key": "1f92f43f87mshd730fa2c49d8b3cp139d68jsn19c960c6ad5a",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())