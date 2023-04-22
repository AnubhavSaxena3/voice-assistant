import requests
# from ss import *
api_address = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4f6d30bde984468cbca5c70b04077b48"
json_data = requests.get(api_address).json()
ar=[]
def news():
    for i in range(3):
        ar.append("Number " + str(i+1) + " " +json_data["articles"][i]["title"]+ "-")

    return ar

# arr=news()
# print(arr)