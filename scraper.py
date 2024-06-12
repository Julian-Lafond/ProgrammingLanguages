import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt 

def main():
    url = "https://news.ycombinator.com/item?id=29782099"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent = 0) #find all the div elements that are called comment which have an indent class and indent of 0
    comments = [e.find_next(class_="comment") for e in elements] #iterate through elements list and find the next div that is called comment to get a list of all top level comments
    
    keywords = {"python": 0, "javascript": 0, "typescript": 0, "ruby": 0, "java": 0, "rust": 0, "c#": 0}    #create dictionary to scan 
    
    for comment in comments:    ##prints all top level comments
        comment_text = comment.get_text().lower()   ##removes html tags and lowercase everything
        words = comment_text.split(" ")
        words = {w.strip(".,/;'!@-|+") for w in words}  #removes certain characters in a set
        for k in keywords:  #now at each iteration go through each key in dictionary to see if it matches 
            if k in words:      
                keywords[k] += 1
    
    plt.bar(keywords.keys(), keywords.values()) #specify x and y axis
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")    
    plt.show()

if __name__ == "__main__":
    main()