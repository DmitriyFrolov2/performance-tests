from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient

class IssueVirtualCardDict(TypedDict):
    """
    Структура данных для создания виртуальной карты
    """
    userId: str
    accountId: str

class IssuePhysicalCardDict(TypedDict):
    """
    Структура данных для создания физической карты
    """
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):
    """
    HTTP клиент для работы с API карт
    """

    def issue_virtual_card_api(self,request:IssueVirtualCardDict)->Response:
        """
        Создание виртуальной карты
        :param request: Идентификаторы пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card",json=request)



    def issue_physical_card_api(self,request:IssuePhysicalCardDict)->Response:
        """
        Создание физической(дебетовой) карты
        :param request: Идентификаторы пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)