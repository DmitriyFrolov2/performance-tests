from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """Модель данных документа."""
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """Модель ответа на запрос тарифного документа."""
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Модель ответа на запрос договора."""
    contract: DocumentSchema
