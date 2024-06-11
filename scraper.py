import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=40563283"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent = 0) #find all the div elements that are called comment which have an indent class and indent of 0
    comments = [e.find_next(class_="comment") for e in elements] #iterate through elements list and find the next div that is called comment to get a list of all top level comments
    
    
    for comment in comments:    ##prints all top level comments
        comment_text = comment.get_text()   ##removes html tags
        print(comment_text)
    
        
    


if __name__ == "__main__":
    main()