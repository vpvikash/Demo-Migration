import requests

def get_device_detail():

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(response.content)

get_device_detail()