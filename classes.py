from bs4 import BeautifulSoup
import requests

class Page:
    def __init__(self, url):
    	self.url = url

    def page_title(self):
        page_source = requests.get(self.url).text
        soup = BeautifulSoup(page_source, 'html.parser')
        page_title = soup.find('title').get_text()
        return page_title

    def meta_description(self):
        page_source = requests.get(self.url).text
        soup = BeautifulSoup(page_source, 'html.parser')
        meta_description = soup.find('meta',attrs={'name':'description'})["content"]
        return meta_description
    
    def get_word_count(argument):
        full_url = argument
        page_source = requests.get(full_url).text
        soup = BeautifulSoup(page_source, 'lxml')
        paragraph_list = [element.text for element in soup.find_all('p')]
        list_list = [element.text for element in soup.find_all('li')]
        word_count = len(str(paragraph_list).split()) + len(str(list_list).split())
        return word_count

    def content(self):
        page_source = requests.get(self.url).text
        soup = BeautifulSoup(page_source, 'html.parser')
        paragraph_list = [element.text for element in soup.find_all('p')]
        content = " ".join(paragraph_list)
        return content
