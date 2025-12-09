from locust import HttpUser, TaskSet, task, between


# Группа задач: просмотр каталога
class BrowseCatalog(TaskSet):
    @task(3)
    def get_product(self):
        self.client.get("/product/123")

    @task(2)
    def get_category(self):
        self.client.get("/category/456")


# Группа задач: просмотр корзины
class BrowseBucket(TaskSet):
    @task
    def get_product(self):
        self.client.get("/bucket")


# Пользователь, которому заданы веса для TaskSet в формате словаря
class ShopUser(HttpUser):
    host = "https://api.example.com"
# Как считается нагрузка 3 + 7 = 10, 100% / 10%, 1=10%
    tasks = {
        BrowseCatalog: 3, # 3 *10% = 30%
        BrowseBucket: 7 # 7 * 10% = 70%
    }

    # BrowseCatalog = 30%
    # - get_product = 0.6 * 0.3 = 0.18, 0.18 * 100% = 18%
    # - get_category = 0.4 * 0.3 = 0.12, 0,12 * 100% = 12%

    # BrowseBucket = 70%
    # - get_product = 1 * 0.7 = 0.7, 0.7 * 100% = 70%
    wait_time = between(1, 3)
