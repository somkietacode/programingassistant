import requests
from bs4 import BeautifulSoup


class programingassistant():
    """docstring for programingassistant."""

    def __init__(self, name):
        self.name = name
        print(" Hi, my name is ",self.name,". Ask me something about how to program something i would be glad to help you...")

    def search_on_google(self,query):
        find = False
        query = "site:stackoverflow.com "+ query
        url = f"https://www.google.com/search?q={query}"
        # send a GET request to the Google search page
        response = requests.get(url)
        # parse the response using beautifulsoup
        soup = BeautifulSoup(response.text, "html.parser")
        # extract the search results
        results = soup.select("a")
        for result in results:
            if "/url?q=https://stackoverflow.com/" in result.get("href") and find == False :
                find = True
                url = f"https://www.google.com"+result.get("href")
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                posts = soup.select(".js-post-body")
                print(self.name,"> ",posts[1].text)


if __name__ == '__main__':
    my_pa = programingassistant("Eliot")
    print(my_pa.name,"> So, how could i help you today ?")
    while True :
        query = input("User >")
        try:
            my_pa.search_on_google(query)
        except Exception as e:
            print(my_pa.name,"> Sory i didn't understand...")
