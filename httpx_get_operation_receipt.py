import time
import httpx

# Шаг 1: создаём пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2: открываем кредитный счёт
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()


#  Шаг 3 совершаем операцию покупки

make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "category": "taxi",
    "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],
    "accountId": open_credit_card_account_response_data["account"]["id"]

}

make_purchase_operation = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_operation_payload)

make_purchase_operation_data = make_purchase_operation.json()


make_operation_receipt  = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_operation_data['operation']['id']}")
make_operation_receipt_data = make_operation_receipt.json()
print(make_operation_receipt_data)
print(make_operation_receipt.status_code)