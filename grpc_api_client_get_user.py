from clients.grpc.gateway.users.client import build_users_gateway_grpc_client

# Инициализируем GRPC клиент
users_gateway_client = build_users_gateway_grpc_client()

# Отправляем запрос на создание пользователя
create_user_response = users_gateway_client.create_user()
print('Create user data:', create_user_response)

# Отправляем запрос на получение данных пользователя
get_user_response = users_gateway_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)
