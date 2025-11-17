response = {
    "accounts": [
        {
            "id": "acc-001",
            "type": "DEPOSIT",
            "cards": [
                {
                    "id": "card-001",
                    "cardNumber": "1234 5678 9012 3456",
                    "cardHolder": "Иван Иванов",
                    "expiryDate": "2026-01-01",
                    "paymentSystem": "VISA",
                    "status": "ACTIVE",
                    "pin": "1234",
                    "cvv": "999",
                    "type": "DEBIT",
                    "accountId": "acc-001"
                }
            ],
            "status": "ACTIVE",
            "balance": 15000.50
        }
    ]
}

account_data = response["accounts"][0]
balance = account_data["balance"]
print("Баланс счёта:", balance)

first_card_number = account_data["cards"][0]["cardNumber"]
print("Номер карты:", first_card_number)