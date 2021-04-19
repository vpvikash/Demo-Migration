import requests

def delete_device_detail():

    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print(response.status_code)

delete_device_detail()