import requests

def post_device_info():
    # r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
    # print(r.status_code, r.reason)

    r = requests.post("https://jsonplaceholder.typicode.com/posts", data={'userId': 454543, 'id': 454543, 'title': 'hello', 'completed': 'false'})
    print(r.status_code, r.reason)
    #
    # response = requests.get("https://jsonplaceholder.typicode.com/posts/454543/title")
    # print(response.content)

    # r = requests.post("https://gorest.co.in/public-api/users", data={'id': 454543, 'name': 'vikash', 'email': 'pvikash167@gmail.com','gender': 'Male','status': 'active'})
    # print(r.status_code, r.reason)
    #
    # response = requests.get("https://gorest.co.in/public-api/users/454543")
    # print(response.content)

post_device_info()