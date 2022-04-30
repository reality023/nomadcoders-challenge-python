# https://remoteok.io/remote-dev+python-jobs

import requests
from bs4 import BeautifulSoup


def extract_job(search, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Geko) Version/15.4 Safari/605.1.15'}
    result = requests.get(
        f"https://remoteok.io/remote-dev+{search}-jobs", headers=headers
    )

    soup = BeautifulSoup(result.text, "html.parser")
    tags = soup.select("#jobsboard tr.job")

    for tag in tags:
        company = tag.select_one(".companyLink h3").get_text().strip()
        link = ("https://remoteok.com" +
                tag.select_one(".preventLink").attrs['href']).strip()
        title = tag.select_one(".preventLink h2").get_text().strip()

        data.append({
            'title': title,
            'company': company,
            'link': link
        })
