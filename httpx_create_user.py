import httpx
from tools.fakers import get_random_email

payload = {
  "email": get_random_email(),
  "password": "Region54",
  "lastName": "Nalivayko",
  "firstName": "Maksim",
  "middleName": "None"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(create_user_response.status_code)
print(create_user_response.json())

