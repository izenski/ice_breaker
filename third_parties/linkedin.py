"""A LinkedIn page scraping utility"""
from typing import Any
import requests
from dotenv import load_dotenv

load_dotenv()


PROFILE_GIST_URL: str = (
    "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
)


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool):
    """scrape information from LinkedIn profiles"""

    if mock is True:
        linkedin_profile_url = PROFILE_GIST_URL

    response = requests.get(
        linkedin_profile_url,
        timeout=10,
    )

    data = response.json().get("person")
    person_data: dict[Any, Any] = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }
    for group_dict in person_data.get("groups") or []:
        group_dict.pop("profile_pic_url")
    return person_data


if __name__ == "__main__":
    # "https://www.linkedin.com/in/eden-marco"
    print(
        scrape_linkedin_profile(
            linkedin_profile_url=PROFILE_GIST_URL,
            mock=True
        )
    )
