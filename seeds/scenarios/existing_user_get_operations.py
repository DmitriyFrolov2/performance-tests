from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который получает информацию об операциях.
    Создаём 300 пользователей, каждому из которых открывается один кредитный счёт с операциями.
    Данный сценарий предназначен для подготовки тестовой нагрузки с 300 виртуальными пользователями,
    которые загружают список операций и просматривают статистику по кредитному счёту.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Создаём 300 пользователей, каждый получает один кредитный счёт
        с 5 операциями покупки, 1 операцией пополнения и 1 операцией снятия наличных.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Создаём 300 пользователей для нагрузочного тестирования
                credit_card_accounts=SeedAccountsPlan(
                    count=1,  # Один кредитный счёт на пользователя
                    purchase_operations=SeedOperationsPlan(count=5),  # 5 операций покупки
                    top_up_operations=SeedOperationsPlan(count=1),    # 1 операция пополнения счёта
                    cash_withdrawal_operations=SeedOperationsPlan(count=1)  # 1 операция снятия наличных
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга