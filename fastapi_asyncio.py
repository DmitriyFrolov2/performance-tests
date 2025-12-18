import datetime
from datetime import datetime
import httpx



def fetch_url(url: str) -> tuple[int, str]:
    with httpx.Client() as client:
        print("Hello fetch_url")
        response = client.get(url)
        return response.status_code, response.text[:50]


def main():
    urls = [
        "https://postman-echo.com/delay/1",
        "https://postman-echo.com/delay/2",
        "https://postman-echo.com/delay/3",
    ]

    results = []
    for url in urls:
        results.append(fetch_url(url))

    for status, text in results:
        print(f"Статус ответа: {status},начало текста: {text}")

#if __name__ == "__main__":
start_time = datetime.now()
main()
print(datetime.now() - start_time)