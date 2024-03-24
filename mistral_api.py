import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

jwt_code = "TWfVrlX659GSTS9hcsgUcPZ8uNzfoQsg"

session = requests.session()
session.headers = {
    "Accept": "application/json",
    "Accept-Encoding": "deflate, gzip",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {jwt_code}",
}

session.mount(
    "https://",
    HTTPAdapter(
        max_retries=Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    ),
)

text = ...

url = "https://api.mistral.ai/v1/chat/completions"
model = "mistral-large-latest"
messages = [{"role": "user", "content": text}]

response = session.post(url, json={"model": model, "messages": messages})
response.raise_for_status()

print(response.json()["choices"][0]["message"]["content"])