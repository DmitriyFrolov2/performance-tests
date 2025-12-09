from locust import HttpUser, between, task, SequentialTaskSet

# TaskSet - задачи выполняются произвольно
# class MyTaskSet(TaskSet):
#     @task
#     def task_one(self):
#         return self.client.get("/page1")
#
#     @task
#     def task_two(self):
#         return self.client.get("/page2")
#
#
# class MyUser(HttpUser):
#     tasks = [MyTaskSet]
#     wait_time = between(1,3)


# SequentialTaskSet - задачи выполняются в той последовательности которую мы указываем
# class MyTaskSet(SequentialTaskSet):
#     @task
#     def task_one(self):
#         return self.client.get("/page1")
#
#     @task
#     def task_two(self):
#         return self.client.get("/page2")
#
#     @task
#     def task_three(self):
#         return self.client.get("/page3")
#
#
# class MyUser(HttpUser):
#     tasks = [MyTaskSet]
#     wait_time = between(1, 3)


class MySimpleUser(HttpUser):
    host = "https://api.example.com"

    # Время ожидания между задачами: случайное значение от 1 до 2 секунд
    wait_time = between(1, 2)

    @task(4) # 4 * 20% = 80% - процент нагрузки
    def get_home(self):
        """
        Задача №1: отправляет GET-запрос на /home
        Частота выполнения — выше, чем у второй задачи
        """
        self.client.get("/home")

    @task(1) # 1 * 20% = 20% - процент нагрузки
    def get_dashboard(self):
        """
        Задача №2: отправляет GET-запрос на /dashboard
        Выполняется реже, с меньшим приоритетом
        """
        self.client.get("/dashboard")


from locust import HttpUser, TaskSet, task, between

# сумма весов задач 3 + 2 = 5
# Группа задач: просмотр каталога
class BrowseCatalog(TaskSet):
    @task(3) # 3 * 20 = 60% В рамках TaskSet
    def get_product(self):
        self.client.get("/product/123")

    @task(2) # 2 * 20 = 40%
    def get_category(self):
        self.client.get("/category/456")


# Группа задач: просмотр корзины
# 1 вес задачи == 100% нагрузки
class BrowseBucket(TaskSet):
    @task
    def get_product(self):
        self.client.get("/bucket")


# Пользователь, который выполняет задачи из двух групп
class ShopUser(HttpUser):
    host = "https://api.example.com"
    tasks = [BrowseCatalog, BrowseBucket]
    # на каждый taskset приходится половина нагрузки
    #BrowseCatalog = 50%
    # = get_product 0.6 * 0.5 = 0.3, 0.3 * 100% = 30%
    # Занимает задача от все доли нагрузки виртуального пользователя ShopUser
    # = get_category = 0.4 * 0.5 = 0.2, 0.2 * 100% = 20%

    # BrowseBucket = 50%
    # = get_product 1 * 0.5 = 0.5 * 100% = 50%
    wait_time = between(1, 3)
