import requests


# API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
def api_url(api_lan: str = "en") -> str:
    return f"https://{api_lan}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str):
    with requests.get(api_url(language)) as response:
        response.raise_for_status()
        return response.json()
