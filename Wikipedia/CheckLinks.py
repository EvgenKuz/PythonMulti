import concurrent.futures
from urllib.request import Request, urlopen


def load_url(url):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    resp = urlopen(request, timeout=5)
    code = resp.code
    resp.close()

    return code


links = open('res.txt', encoding='utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(load_url, url): url for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        try:
            print(future.result())
        except Exception as e:
            print(future_to_url[future], e)
