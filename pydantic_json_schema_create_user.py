from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.fakers import fakeimport jsonschema
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email = fake.email(),
    password = 'Region54',
    last_name = 'Nalivayko',
    first_name = 'Maksim',
    middle_name = 'None'
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()
create_user_response_schema = CreateUserResponseSchema.model_json_schema()


validate_json_schema(instance=create_user_response_json, schema=create_user_response_schema)