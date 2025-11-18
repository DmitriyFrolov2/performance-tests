from enum import StrEnum
from pydantic import BaseModel, Field, ConfigDict,HttpUrl


class OperationType(StrEnum):
    """Типы операций."""
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    """Статусы операций."""
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Модель данных операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationResponseSchema(BaseModel):
    """
    Структура ответа с одной операцией.
    """
    operation: OperationSchema


class OperationsSummarySchema(BaseModel):
    """
    Структура сводки по операциям.
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class OperationsSummaryResponseSchema(BaseModel):
    """
    Структура ответа со сводкой по операциям.
    """
    summary: OperationsSummarySchema


class OperationsListResponseSchema(BaseModel):
    """
    Структура ответа со списком операций.
    """
    operations:  list[OperationSchema]


class OperationReceiptSchema(BaseModel):
    """
    Структура ответа чека по операции
    """
    url: HttpUrl
    document: str


class OperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения информации об операциях по accountId.
    """
    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения сводки по операциям.
    """
    account_id: str = Field(alias="accountId")


class MakeFeeOperationsRequestSchema(BaseModel):
    """
    Структура данных для создания операции комиссии.
    """
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура ответа при создании операции комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции пополнения счета.
    """
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashBackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбэка.
    """
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода.
    """
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции покупки.
    """
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str

class MakeBillPaymentOperationsRequestSchema(BaseModel):
    """
    Структура данных для создания операции оплаты счета.
    """
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции снятия наличных.
    """
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура ответа при создании операции пополнения.
    """
    operation: OperationSchema

class MakeCashBackOperationResponseSchema(BaseModel):
    """Структура ответа при создании операции кэшбэка."""
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """Структура ответа при создании операции перевода."""
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """Структура ответа при создании операции покупки."""
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Структура ответа при создании операции оплаты счета."""
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Структура ответа при создании операции снятия наличных."""
    operation: OperationSchema