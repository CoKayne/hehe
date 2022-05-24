import urllib.request as req
import tkinter as tk
import webbrowser
import os
import json
import bs4

window = tk.Tk()
window.title("建功高中新訊息")

def save_data(td, dictionary):
    date = td.select("tr > td")[3].get_text(strip=True)
    li = date.split("-")
    days = int(li[0] + li[1])
    s = td.find("span")
    title = s.a["title"]
    link = s.a["href"]
    data[title] = [days, link]

def callback(link1):
    webbrowser.open_new(link1)

def create_label(txt, link):
    bt = tk.Button(window, text=txt, bg="#373C38", fg='#FEDFE1', font=('Fira Code', 12), width=80, height=1)
    bt.bind("<Button-1>", lambda e:callback(link))
    bt.bind('<Enter>', on_enter)
    bt.bind('<Leave>', on_leave)
    bt.pack()

def on_enter(e):
    e.widget['fg'] = '#FBE251'

def on_leave(e):
    e.widget['fg'] = '#FEDFE1'

url = "https://www.cksh.hc.edu.tw/files/40-1000-13-1.php?Lang=zh-tw"

request = req.Request(url, headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")
tree1 = root.find_all("tr", class_ = "row_01")
tree2 = root.find_all("tr", class_ = "row_02")

data = dict()

for td in tree1:
    save_data(td, data)

for td in tree2:
    save_data(td, data)

sorted_data = dict(sorted(data.items(), key=lambda item:item[1]))

for i in sorted_data:
    title = i
    link = sorted_data[i][1]
    create_label(title, link)

window.mainloop()