import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


try:
    with open("movies.txt","r") as data_file:
        data = data_file.read()
except FileNotFoundError:
    with open("movies.txt", "w") as data_file:
        data = data_file.write("100 Best Movies List")
    print("movies.txt file was created.")


response = requests.get(URL)
movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")


movie_titles = soup.find_all(name="h3", class_="title")
#print(movie_titles)

movie_list = []

for movie in movie_titles:
    text = movie.getText()
    movie_list.append(text)

#print(movie_list)
movie_list.reverse()
#print(movie_list)

with open("movies.txt", "w") as data_file:
    for items in movie_list:
        data_file.writelines(items+'\n')
print("List was written to text file 'movies.txt'")



# for movie in movie_titles:
#     text = movie.getText()
#     # print(text)
#     # split_index = text.index(")") + 1
#     if ")" in text:
#         movie_name = text.split(")")[1]
#     else:
#         movie_name = text.split(":")[1]
#     movie_list.append(movie_name)
#
# print(movie_list)
# movie_list.reverse()
# print(movie_list)
# for movie in movie_title:
#     movie.find(name="h3", class_="title")
#     print(movie.getText())
#

# articles = soup.find_all(name='a', class_="titlelink")





