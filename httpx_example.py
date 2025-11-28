import httpx

# responce = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

# print(responce.status_code)
# print(responce.json())


# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
# responce = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)

# print(responce.status_code)
# print(responce.json())

# data = {"username": "test_user", "password": "123456"}

# responce = httpx.post('https://httpbin.org/post', data=data)

# print(responce.status_code)
# print(responce.json())

# headers = {"Authorization": "Bearer my_secret_token"}
# responce = httpx.get('https://postman-echo.com/get', headers=headers)

# print(responce.request.headers)
# print(responce.json())


# params = {"userId": 1}
# responce = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)

# print(responce.url)
# print(responce.json())

# files = {"file": ("example.txt", open("example.txt", "rb"))}
# responce = httpx.post('https://postman-echo.com/post', files=files)

# print(responce.json())

# with httpx.Client() as client:
#     responce1 = client.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
#     responce2 = client.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")

# print(responce1.json())
# print(responce2.json())

# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# responce = client.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")

# print(responce.json())

# try:
#     responce = httpx.get('https://jsonplaceholder.typicode.com/todos/invalid-url')
#     responce.raise_for_status()
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса: {e}")

try:
    responce = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
