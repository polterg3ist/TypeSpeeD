import requests
from bs4 import BeautifulSoup


def parse():
    url = "https://puzzle-english.com/directory/1000-popular-words"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    word_block = soup.find("ol")
    word_text = word_block.text
    word_lines = word_text.split('\n')[1:-1:]  # Last and first elements was empty
    words = []

    for line in word_lines:
        line_splitted = line.split(' ')
        # there is no russian word if not len > 3
        if len(line_splitted) > 3:
            # checking is last element is whitespace
            if not line_splitted[-1]:
                words.append(line_splitted[-2])
            else:
                words.append((line_splitted[-1]))

    return words
