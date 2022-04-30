import requests
from bs4 import BeautifulSoup


def extract_job(search, data):
    result = requests.get(
        f"https://weworkremotely.com/remote-jobs/search?term={search}"
    )

    soup = BeautifulSoup(result.text, "html.parser")
    tags = soup.select(".jobs ul li > a")

    for tag in tags:
        try:
            link = ("https://weworkremotely.com" +
                    tag.attrs["href"])
            company = tag.select_one(".company").get_text()
            title = tag.select_one(".title").get_text()
        except:
            continue

        data.append({
            'title': title,
            'company': company,
            'link': link
        })
