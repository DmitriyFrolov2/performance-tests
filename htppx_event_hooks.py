from httpx import Client, Response, Request


def log_request(request: Request):
    print(f"Request: {request.method}")


def log_response(response: Response):
    print(f"Response: {response.status_code}")


def log(event_name, info):
    print(event_name, info)


client = Client(base_url="http://localhost:8003", event_hooks={"request": [log_request], "response": [log_response]}, )
response = client.get("/api/v1/users/{9f61633f-9412-471b-a979-ae46b2c299fd}", extensions={"trace": log})
print(response)
