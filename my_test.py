from locust import User, between, task
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    # Аннотации (оставляем, это хорошо)
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    create_user_response: CreateUserResponse

    def on_start(self) -> None:
        print("DEBUG: Starting on_start()")
          # Точка останова 1

        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)

        print("DEBUG: Calling create_user()")
          # Точка останова 2

        self.create_user_response = self.users_gateway_client.create_user()
        print(f"DEBUG: User created with ID: {self.create_user_response.user.id}")

    @task
    def open_debit_card_account(self):
        print(f"DEBUG: Opening account for user: {self.create_user_response.user.id}")
          # Точка останова 3

        result = self.accounts_gateway_client.open_debit_card_account(
            self.create_user_response.user.id
        )

        print(f"DEBUG: Result: {result}")
          # Точка останова 4
        return result


# ДОБАВЬТЕ ЭТО В КОНЕЦ ФАЙЛА
if __name__ == "__main__":
    from locust import run_single_user

    run_single_user(OpenDebitCardAccountScenarioUser)