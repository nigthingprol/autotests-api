from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import fake
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import GetUserResponseSchema
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email = fake.email(),
    password = 'Region54',
    last_name = 'Nalivayko',
    first_name = 'Maksim',
    middle_name = 'None'
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиент
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password   
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)

