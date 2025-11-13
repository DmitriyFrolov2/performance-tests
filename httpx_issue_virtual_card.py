import time
import httpx

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user response:",create_user_response_data)
print("Status code:",create_user_response.status_code)


open_debit_card_account = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account")
open_debit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}

open_debit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account", json= open_debit_card_account_payload)
open_debit_card_account_data = open_debit_card_account_response.json()
print("Open debit card response:", open_debit_card_account_data)
print("Open debit card status code:", open_debit_card_account_response.status_code)


issue_virtual_card_payload = {
    "userId": create_user_response_data["user"]["id"],
    "accountId": open_debit_card_account_data["account"]["id"]
}

issue_virtual_card_response = httpx.post("http://localhost:8003/api/v1/cards/issue-physical-card", json=issue_virtual_card_payload)
issue_virtual_card_response_data = issue_virtual_card_response.json()
print(issue_virtual_card_response.status_code)