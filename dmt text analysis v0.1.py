# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

#get the initial HTML of the page with all the links
#to all the different trip reports from erowid.org
html = requests.get("https://erowid.org/experiences/subs/exp_DMT.shtml").text
soup = BeautifulSoup(html, "html.parser")


##found the soution on stack exchange, this limits it to href
##links starting with whatever is in the re.compile parentheses
allReportLinks = soup.find_all('a', attrs={'href': re.compile("^/experiences/exp.php")})
allReportLinksList = []
for link in allReportLinks:
    x = str(link)
    split_string = x.split("href=\"", 1)    
    substring = split_string[1]
    split_string2 = substring.split("\"")
    substring2 = split_string2[0]
    
    string3 = "https://erowid.org/" + substring2
    
    allReportLinksList.append(string3)
    
##allReportLinksList is now a list composed of links to all the trip reports


allReportWords = []

counter = 0
for link in allReportLinksList:
    ##get the html for the individual link
    html = requests.get(link).text
    soup = BeautifulSoup(html, "html.parser")
    
    text = soup.find_all(text=True)
    text = str(text)
    
    split_string = text.split("Start Body", 1)
    substring = split_string[1]
    split_string = substring.split("End Body", 1)
    substring = split_string[0]
    text = str(substring)
   
    #getting rid of punctuation and whatnot
    text = text.replace("\'", "")
    text = text.replace("\\n", "")
    text = text.replace("\\r", "")
    text = text.replace("\"", "")
    text = text.replace(",", "")
    text = text.replace("\'", "")
    ##need this for phrases like "alter-ego" and "life-force"
# =============================================================================
#     text = text.replace("-", "")
# =============================================================================
    text = text.replace(".", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("\', \'", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace("#", "")
    text = text.replace("~", "")
    text = text.replace("\\x91", "")
    text = text.replace("\\x92", "")
    text = text.replace("\\x96", "")
    text = text.replace("\\x85", "")
    text = text.replace("\\x94", "")
    
    text = text.lower()
            
    split_string = text.split(" ")
    for i in split_string:
        allReportWords.append(i)

# =============================================================================
# allReportWords is now a list with all the individual words from all
# the trip reports
# =============================================================================

f = open("dmtallwords.txt", "x")

for i in allReportWords:
    f.write(i + "\n")

f.close()

Counter = Counter(allReportWords)
most_occur = Counter.most_common(30)
print(most_occur)






