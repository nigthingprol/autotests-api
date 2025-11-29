import httpx

login_payload = {
    "email": "nalivayko2018@mail.ru",
    "password": "Region54"
}

login_responce = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_responce_data = login_responce.json()

get_user_headers = {
    "Authorization": f"Bearer {login_responce_data['token']['accessToken']}"
    }
get_user_responce = httpx.get('http://localhost:8000/api/v1/users/me', headers=get_user_headers)
get_user_responce_data = get_user_responce.json()

print("Get user status code:", get_user_responce.status_code)
print("Get user responce:", get_user_responce_data)