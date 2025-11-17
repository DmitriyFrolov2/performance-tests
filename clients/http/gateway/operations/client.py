from typing import List, TypedDict

from httpx import QueryParams, Response
from clients.http.gateway.client import build_gateway_http_client
from clients.http.client import HTTPClient


class OperationDict(TypedDict):
    """
    Описание структуры операций.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationResponseDict(TypedDict):
    """
    Структура ответа с одной операцией.
    """
    operation: OperationDict


class OperationsSummaryDict(TypedDict):
    """
    Структура сводки по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class OperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа со сводкой по операциям.
    """
    summary: OperationsSummaryDict


class OperationsListResponseDict(TypedDict):
    """
    Структура ответа со списком операций.
    """
    operations: List[OperationDict]


class OperationReceiptDict(TypedDict):
    """
    Структура ответа чека по операции
    """
    url: str
    document: str


class OperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения информации об операциях по accountId.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения сводки по операциям.
    """
    accountId: str


class MakeFeeOperationsRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа при создании операции комиссии.
    """
    operation: OperationDict


class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции пополнения счета.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashBackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str

class MakeBillPaymentOperationsRequestDict(TypedDict):
    """
    Структура данных для создания операции оплаты счета.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа при создании операции пополнения.
    """
    operation: OperationDict

class MakeCashBackOperationResponseDict(TypedDict):
    """Структура ответа при создании операции кэшбэка."""
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """Структура ответа при создании операции перевода."""
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """Структура ответа при создании операции покупки."""
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """Структура ответа при создании операции оплаты счета."""
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Структура ответа при создании операции снятия наличных."""
    operation: OperationDict

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_list_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос для получения СПИСКА операций по accountId.

        :param query: Словарь с параметрами запроса.
        :return: Объект httpx.Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operation_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос для получения сводки по операциям.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со сводкой по операциям.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с чеком операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_single_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения ОДНОЙ операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationsRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными для операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения счета.

        :param request: Словарь с данными для операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashBackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными для операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными для операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными для операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationsRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты счета.

        :param request: Словарь с данными для операции оплаты счета.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных.

        :param request: Словарь с данными для операции снятия наличных.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operations_list(self, account_id: str) -> OperationsListResponseDict:
        """
        Получить СПИСОК операций по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Список операций счета.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_list_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> OperationsSummaryResponseDict:
        """
        Получить сводку по операциям по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Сводка по операциям счета.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operation_summary_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> OperationReceiptResponseDict:
        """
        Получить чек операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Данные чека операции.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_single_operation(self, operation_id: str) -> OperationResponseDict:
        """
        Получить ОДНУ операцию по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Данные операции.
        """
        response = self.get_single_operation_api(operation_id)
        return response.json()

    def make_fee_operation(
            self,
            status: str,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeFeeOperationResponseDict:
        """
        Создать операцию комиссии.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeFeeOperationsRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(
            self,
            status: str,
            amount: float,
            card_id: str,
            account_id: str
    )->MakeTopUpOperationResponseDict:
        """
        Создать операцию пополнения.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeTopUpOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(
            self,
            status: str,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeCashBackOperationResponseDict:
        """
        Создать операцию кэшбэка.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeCashBackOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(
            self,
            status: str,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeTransferOperationResponseDict:
        """
        Создать операцию перевода.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeTransferOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(
            self,
            status: str,
            amount: float,
            card_id: str,
            account_id: str,
            category: str
    ) -> MakePurchaseOperationResponseDict:
        """
        Создать операцию покупки.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :param category: Категория покупки.
        :return: Данные созданной операции.
        """
        request = MakePurchaseOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(
            self,
            status: str,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeBillPaymentOperationResponseDict:
        """
        Создать операцию оплаты счета.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeBillPaymentOperationsRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(
            self,
            status: str,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeCashWithdrawalOperationResponseDict:
        """
        Создать операцию снятия наличных.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()

def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию OperationsGatewayHTTPClient
    """

    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
