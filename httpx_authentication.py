import httpx

login_payload = {
    "email": "nalivayko2018@mail.ru",
    "password": "Region54"
}

login_responce = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_responce_data = login_responce.json()

print("Login responce:", login_responce_data)
print("Status code:", login_responce.status_code)

refresh_payload = {
    "refreshToken": login_responce_data['token']['refreshToken']
}

refresh_responce = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_responce_data = refresh_responce.json() 

print("Refresh responce:", refresh_responce_data)
print("Status code:", refresh_responce.status_code)
