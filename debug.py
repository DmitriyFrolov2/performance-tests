from locust import task, run_single_user

from clients.http.gateway.cards.schema import IssuePhysicalCardResponseSchema
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema

from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    create_user_response: CreateUserResponseSchema | None = None
    open_open_debit_card_account_response: OpenDebitCardAccountResponseSchema | None = None
    issue_physical_card_response: IssuePhysicalCardResponseSchema | None = None

    @task
    def create_user(self):
        print("\n[DEBUG] create_user START")

        self.create_user_response = self.users_gateway_client.create_user()

        print("[DEBUG] create_user RESPONSE:", self.create_user_response)
        breakpoint()  #тут смотри user.id

    @task
    def open_debit_card_account(self):
        if not self.create_user_response:
            print("[DEBUG] open_debit_card_account SKIPPED (no user)")
            return

        print("\n[DEBUG] open_debit_card_account START")

        self.open_open_debit_card_account_response = (
            self.accounts_gateway_client.open_debit_card_account(
                user_id=self.create_user_response.user.id
            )
        )

        print(
            "[DEBUG] open_debit_card_account RESPONSE:",
            self.open_open_debit_card_account_response
        )
        breakpoint()  #тут смотри account.id

    @task
    def create_physical_card(self):
        if not self.open_open_debit_card_account_response:
            print("[DEBUG] create_physical_card SKIPPED (no account)")
            return

        print("\n[DEBUG] create_physical_card START")

        self.issue_physical_card_response = (
            self.cards_gateway_client.issue_physical_card(
                user_id=self.create_user_response.user.id,
                account_id=self.open_open_debit_card_account_response.account.id
            )
        )

        print(
            "[DEBUG] create_physical_card RESPONSE:",
            self.issue_physical_card_response
        )
        breakpoint()  #финальный контроль

        print("\n[DEBUG] SCENARIO FINISHED — STOP LOCUST")
        self.user.environment.runner.quit()  #останавливаем Locust


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]


if __name__ == "__main__":
    run_single_user(IssuePhysicalCardScenarioUser)
