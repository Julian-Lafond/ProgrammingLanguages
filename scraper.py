import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=40563283"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="comment") #find all the div elements that are called comment
    print("Elements", len(elements))
        
    


if __name__ == "__main__":
    main()