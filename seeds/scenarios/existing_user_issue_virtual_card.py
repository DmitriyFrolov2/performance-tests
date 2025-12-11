from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя, который выпускает виртуальную карту.
    Создаём 100 пользователей, каждому из которых открывается один дебетовый счёт.
    Данный сценарий предназначен для подготовки тестовой нагрузки с 100 виртуальными пользователями,
    которые выполняют выпуск виртуальной карты для своего дебетового счёта.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Создаём 300 пользователей, каждый получает один дебетовый счёт
        для последующего выпуска виртуальной карты.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Создаём 300 пользователей
                debit_card_accounts=SeedAccountsPlan(count=1)  # Дебетовый счёт на пользователя
            ),
        )


    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_issue_virtual_card"

if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга