from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client

# Создаем клиенты для сервисов
users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
documents_gateway_client = build_documents_gateway_http_client()
operations_gateway_client = build_operations_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# Открываем дебетовый счет
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response['user']['id']
)
print('Open debit card account response:', open_debit_card_account_response)

# Создаем операцию пополнения счета
make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    status="COMPLETED",
    amount=1500.50,  # Сумма пополнения
    card_id=open_debit_card_account_response['account']['cards'][0]['id'],
    account_id=open_debit_card_account_response['account']['id']
)
print('Make top up operation response:', make_top_up_operation_response)

# Выводим сводную информацию о созданных сущностях
print(f"Создан пользователь: {create_user_response['user']['id']}")
print(f"Открыт счет: {open_debit_card_account_response['account']['id']}")
print(f"Привязана карта: {open_debit_card_account_response['account']['cards'][0]['id']}")
print(f"Создана операция пополнения: {make_top_up_operation_response['operation']['id']}")
print(f"Сумма пополнения: {make_top_up_operation_response['operation']['amount']} руб.")
print(f"Статус операции: {make_top_up_operation_response['operation']['status']}")
print(f"Тип операции: {make_top_up_operation_response['operation']['type']}")