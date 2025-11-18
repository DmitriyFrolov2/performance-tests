from httpx import QueryParams, Response
from clients.http.gateway.client import build_gateway_http_client
from clients.http.client import HTTPClient
from clients.http.gateway.operations.schema import (
    OperationResponseSchema,
    OperationsSummaryResponseSchema,
    OperationsListResponseSchema,
    OperationReceiptResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsSummaryQuerySchema,
    MakeFeeOperationsRequestSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeCashBackOperationRequestSchema,
    MakeTransferOperationRequestSchema,
    MakePurchaseOperationRequestSchema,
    MakeBillPaymentOperationsRequestSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashBackOperationResponseSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema, OperationStatus,
)


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос для получения СПИСКА операций по accountId.

        :param query: Словарь с параметрами запроса.
        :return: Объект httpx.Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operation_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос для получения сводки по операциям.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со сводкой по операциям.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос для получения чека операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с чеком операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получает информацию об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationsRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными для операции комиссии.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения счета.

        :param request: Словарь с данными для операции пополнения.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashBackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными для операции кэшбэка.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными для операции перевода.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными для операции покупки.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationsRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты счета.

        :param request: Объект с данными для операции оплаты счета.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных.

        :param request: Объект с данными для операции снятия наличных.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operations(self, account_id: str) -> OperationsListResponseSchema:
        """
        Получить СПИСОК операций по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Список операций счета.
        """
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query)
        return OperationsListResponseSchema(**response.json())

    def get_operations_summary(self, account_id: str) -> OperationsSummaryResponseSchema:
        """
        Получить сводку по операциям по идентификатору счета.

        :param account_id: Идентификатор счета.
        :return: Сводка по операциям счета.
        """
        query = GetOperationsSummaryQuerySchema(accountId=account_id)
        response = self.get_operation_summary_api(query)
        return OperationsSummaryResponseSchema(**response.json())

    def get_operation_receipt(self, operation_id: str) -> OperationReceiptResponseSchema:
        """
        Получить чек операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Данные чека операции.
        """
        response = self.get_operation_receipt_api(operation_id)
        return OperationReceiptResponseSchema(**response.json())

    def get_operation(self, operation_id: str) -> OperationResponseSchema:
        """
        Получить ОДНУ операцию по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Данные операции.
        """
        response = self.get_operation_api(operation_id)
        return OperationResponseSchema(**response.json())

    def make_fee_operation(
            self,
            status: OperationStatus,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeFeeOperationResponseSchema:
        """
        Создать операцию комиссии.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeFeeOperationsRequestSchema(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema(**response.json())

    def make_top_up_operation(
            self,
            status: OperationStatus,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeTopUpOperationResponseSchema:
        """
        Создать операцию пополнения.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeTopUpOperationRequestSchema(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema(**response.json())

    def make_cashback_operation(
            self,
            status: OperationStatus,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeCashBackOperationResponseSchema:
        """
        Создать операцию кэшбэка.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeCashBackOperationRequestSchema(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashBackOperationResponseSchema(**response.json())

    def make_transfer_operation(
            self,
            status: OperationStatus,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeTransferOperationResponseSchema:
        """
        Создать операцию перевода.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeTransferOperationRequestSchema(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema(**response.json())

    def make_purchase_operation(
            self,
            status: OperationStatus,
            amount: float,
            card_id: str,
            account_id: str,
            category: str
    ) -> MakePurchaseOperationResponseSchema:
        """
        Создать операцию покупки.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :param category: Категория покупки.
        :return: Данные созданной операции.
        """
        request = MakePurchaseOperationRequestSchema(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema(**response.json())

    def make_bill_payment_operation(
            self,
            status: OperationStatus,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeBillPaymentOperationResponseSchema:
        """
        Создать операцию оплаты счета.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeBillPaymentOperationsRequestSchema(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema(**response.json())

    def make_cash_withdrawal_operation(
            self,
            status: OperationStatus,
            amount: float,
            card_id: str,
            account_id: str
    ) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создать операцию снятия наличных.

        :param status: Статус операции ("COMPLETED", "FAILED").
        :param amount: Сумма операции.
        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Данные созданной операции.
        """
        request = MakeCashWithdrawalOperationRequestSchema(
            status=status,
            amount=amount,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema(**response.json())


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию OperationsGatewayHTTPClient
    """

    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
