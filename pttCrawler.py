import urllib.request as req
import bs4

def getURL(url):

    request = req.Request(url, headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_ = "title")

    for name in titles:
        if name.a != None:
            print(name.a.string)
            print("https://www.ptt.cc" + name.a["href"])

    backLink = root.find("a", string = "‹ 上頁")
    return backLink["href"]

url = "https://www.ptt.cc/bbs/movie/index.html"
times = 0
while times < 5:
    url = "https://www.ptt.cc" + getURL(url)
    times += 1