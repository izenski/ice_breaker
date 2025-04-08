import os
import requests
from dotenv import load_dotenv

PROFILE_GIST_URL: str = (
    "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
)

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """scrape information from LinkedIn profiles"""

    linkedin_profile_url = PROFILE_GIST_URL
    response = requests.get(
        linkedin_profile_url,
        timeout=10,
    )

    data: dict = response.json().get("person")
    data_subset: dict[str, str] = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) 
        and k not in ["certifications"]
    }
    return data_subset


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco"
        )
    )
