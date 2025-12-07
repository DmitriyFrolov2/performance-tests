from grpc import Channel
from locust.env import Environment
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptRequest, \
    GetOperationReceiptResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryRequest, \
    GetOperationsSummaryResponse
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import \
    MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest, \
    MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest, \
    MakeFeeOperationResponse
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationRequest, \
    MakePurchaseOperationResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest, \
    MakeTopUpOperationResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationRequest, \
    MakeBillPaymentOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest, \
    MakeTransferOperationResponse
from tools.fakers import fake
from contracts.services.operations.operation_pb2 import OperationStatus


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет методы для получения информации об операциях.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)
        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetOperation через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с данными операции.
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с чеком операции.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetOperations через gRPC.

        :param request: gRPC-запрос с ID аккаунта.
        :return: Ответ от сервиса со списком операций.
        """
        return self.stub.GetOperations(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.

        :param request: gRPC-запрос с ID аккаунта.
        :return: Ответ от сервиса со статистикой операций.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.

        :param request: gRPC-запрос на создание операции комиссии.
        :return: Ответ от сервиса с созданной операцией.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.

        :param request: gRPC-запрос на создание операции пополнения.
        :return: Ответ от сервиса с созданной операцией.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.

        :param request: gRPC-запрос на создание операции кэшбэка.
        :return: Ответ от сервиса с созданной операцией.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.

        :param request: gRPC-запрос на создание операции перевода.
        :return: Ответ от сервиса с созданной операцией.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.

        :param request: gRPC-запрос на создание операции покупки.
        :return: Ответ от сервиса с созданной операцией.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self,
                                        request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.

        :param request: gRPC-запрос на создание операции оплаты по счету.
        :return: Ответ от сервиса с созданной операцией.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self,
                                           request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashWithdrawalOperation через gRPC.

        :param request: gRPC-запрос на создание операции снятия наличных.
        :return: Ответ от сервиса с созданной операцией.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Получение информации об операции по её ID.

        :param operation_id: Идентификатор операции.
        :return: Ответ с данными операции.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Получение чека операции по её ID.

        :param operation_id: Идентификатор операции.
        :return: Ответ с чеком операции.
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Получение списка операций для определённого счета.

        :param account_id: Идентификатор аккаунта.
        :return: Ответ со списком операций.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Получение статистики по операциям для определённого счета.

        :param account_id: Идентификатор аккаунта.
        :return: Ответ со статистикой операций.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
        Создание операции комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с созданной операцией.
        """
        request = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """
        Создание операции пополнения.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с созданной операцией.
        """
        request = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """
        Создание операции кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с созданной операцией.
        """
        request = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """
        Создание операции перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с созданной операцией.
        """
        request = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """
        Создание операции покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с созданной операцией.
        """
        request = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            category=fake.category(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """
        Создание операции оплаты по счету.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с созданной операцией.
        """
        request = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Создание операции снятия наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор аккаунта.
        :return: Ответ с созданной операцией.
        """
        request = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабричная функция для создания экземпляра OperationsGatewayGRPCClient.

    :return: Готовый экземпляр gRPC-клиента для работы с операциями.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())


def build_operations_gateway_locust_grpc_client(environment: Environment) -> OperationsGatewayGRPCClient:
    """
    Функция создаёт экземпляр OperationsGatewayGRPCClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayGRPCClient с хуками сбора метрик.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))
