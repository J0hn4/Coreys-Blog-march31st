from bs4 import BeautifulSoup
import lxml
import requests

response= requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name='a', class_="titlelink")
# for entry in link_text:
#     print(entry.string)

article_upvotes = [score.getText()  for score in soup.find_all(name='span', class_="score")]

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)


print(article_texts)
print(article_links)
print(article_upvotes[0])

score_num = []

for score in article_upvotes:
    num = score.split()
    score_num.append(int(num[0]))

# print(score_num)

new_list = [int(score.split()[0]) for score in article_upvotes  ]
print(new_list)

# max_value = max(new_list)
# print(max_value)
max_index = new_list.index(max(new_list))
print(max_index)

print(article_texts[max_index])
print(article_links[max_index])

# for entry in link_text:
#     print(link_text.text)



#print(soup.select(selector="a", class_="storylink"))

# with open("website.html", "r") as file:
#     contents = file.read()
#
# # print(contents)
#
# soup = BeautifulSoup(contents, 'lxml')
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #      print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# #print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))
#
# name = soup.select_one(selector="#name")
# # print(name)
#
# headings = soup.select(".heading")
# print(headings)