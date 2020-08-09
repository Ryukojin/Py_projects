import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader('3325_week_0.pdf')

# get number of pages
NumPages = object.getNumPages()

# define keyterms
listString = ["Agius, Julian","Al Jahangir, Fahim"]
found = []
# extract text to display the matches and then append them to found list
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("Page " + str(i)) 
    Text = PageObj.extractText()
    for j in iter_string:
        if re.findall(j, Text) == []:
            print('Not Found\n')
        else:
            print(re.findall(j, Text), 'Match found \n')
            found.append(j)

found.sort(reverse=True)
orderedList = set(found)

#Give counts of matches found out of total 

#method for Add or remove from list

#Sort list and save to pdf