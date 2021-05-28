import requests 

BASE = "http://127.0.0.1:5000/"

data = [
    {'likes': 78, 'name': 'Joe', 'views': 1000},
    {'likes': 8, 'name': 'Pogi', 'views': 10100},
    {'likes': 10, 'name': 'Udemy', 'views': 20100},

]
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.get(BASE+ "video/6")
print(response.json())

