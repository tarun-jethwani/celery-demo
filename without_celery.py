import requests
import time


def fetch_urls(urls):
    start = time.time()
    for url in urls:
        response = requests.get(url)
        print(response.status_code)

    print("Total elapsed time ", time.time() - start, "seconds")

if __name__ == "__main__":
	fetch_urls(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])