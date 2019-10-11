
from bs4 import BeautifulSoup
import requests
import re


def test_ono():
    for i in range(1, 100):
        if i % 3 == 0 and i % 7 == 0:
            print('OpenSource')
        elif i % 3 == 0:
            print('Open')
        elif i % 7 == 0:
            print('Source')
        else:
            print(i)

test_ono()

"""
Returns:
     0 if the guess is the solution, your program won
     -1 if the solution is smaller than the guess parameter
     1  if the solution is bigger than the guess parameter
"""


def verify(guess):

    return -1


def test_three(list):
    sum = 0

    for item in list:
        try:
            number = int(item)
            sum += number
        except:
            print('not a number')

    return sum


print(test_three(['1', 'we', '2', '7', 'er', '4l']))
print(test_three([]))


def test_three_recursive(list):
    sum = 0

    if not list:
        return 0

    try:
        item = list.pop(0)
        number = int(item)
        sum += number
    finally:
        return sum + test_three_recursive(list)


print(test_three_recursive(['1', 'we', '2', '7', 'er', '4l']))
print(test_three_recursive([]))


def read_file():
    with open('data.bin', 'r+') as f:
        while True:
            byte = f.read(7)
            if byte:
                f.truncate(7)
            else:
                break

read_file()


def readHtml(link):
    page_response = requests.get(link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    replace_string = "Odoo"
    # text_remplace = str(page_content).replace("SAP", replace_string)

    text_remplace = re.sub("SAP", "Odoo", str(page_content))
    file = open('myFile.txt', 'w', encoding="utf-8")
    file.write(text_remplace)
    file.close()

# readHtml('http://www.sap.com/belgique/index.html')


str_to_check = "Adsdsds sds s #rulesOdoo sdsds Odoo es #rules muy bueno pero Odoo tiene sus #rules"
print(re.search("(Odoo*|#rules*)|(#rules*|Odoo*)", str_to_check).groups())

print(re.search(r"Odoo*|#rules*", str_to_check))
