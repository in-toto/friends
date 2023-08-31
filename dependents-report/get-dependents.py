import json
import os
import requests
import sys


API_URL = "https://api.github.com"
SEARCHED_REPOSITORY = "github.com/in-toto/in-toto-golang"


def main():
    text = """
# Top Dependents

This file lists the top 50 dependents of in-toto-golang sorted by GitHub stars.

| Repository | Stars |
|------------|-------|
"""
    search_query = f"{SEARCHED_REPOSITORY} filename:go.mod"
    url = f"{API_URL}/search/code?q={search_query}&per_page=100"
    print(f"Looking up '{url}'")
    response = requests.get(
        url,
        headers={"authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"},
    )
    if response.status_code != 200:
        sys.exit(1)
    response_obj = json.loads(response.text)

    items = response_obj["items"]

    total_pages = response_obj["total_count"] // 100 + 1
    for i in range(2, total_pages + 1):
        url = f"{API_URL}/search/code?q={search_query}&per_page=100&page={i}"
        print(f"Looking up '{url}'")
        response = requests.get(
            url,
            headers={"authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"},
        )
        if response.status_code != 200:
            sys.exit(1)
        items.extend(json.loads(response.text)["items"])

    repositories = {}
    for item in items:
        repo_path = item["repository"]["full_name"]
        url = f"{API_URL}/repos/{repo_path}"
        print(f"Looking up '{url}'")
        # TODO: asyncio -> parallelize
        stars_response = requests.get(
            f"{API_URL}/repos/{repo_path}",
            headers={"authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"},
        )
        stars_response_obj = json.loads(stars_response.text)

        repositories[repo_path] = stars_response_obj["stargazers_count"]
    
    sorted_by_stars = sorted(
        repositories.items(),
        key=lambda x: x[1],
        reverse=True,
    )[:50]

    for repo, star in sorted_by_stars:
        text += f"| {repo} | {star} |\n"

    with open("dependents-report/README.md", "w+") as fp:
        fp.write(text)


if __name__ == "__main__":
    main()
