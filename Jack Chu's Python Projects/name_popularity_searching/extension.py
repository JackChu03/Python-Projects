"""
Name: Jack Chu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html

Print the number of top200 male and female on Console
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find_all('table', {'class': 't-stripe'})
        n = 0
        total_m = 0
        total_w = 0
        for item in items:
            while n < 200:
                number = item.tbody.text
                number_lst = number.split()
                number_m = number_lst[2+n*5]
                number_m = int_manipulation(number_m)
                total_m = total_m + int(number_m)
                number_w = number_lst[4+n*5]
                number_w = int_manipulation(number_w)
                total_w = total_w + int(number_w)
                n = n+1
            print('Male Number:', total_m)
            print('Female Number:', total_w)
        ##################


def int_manipulation(x):
    # to get the real number without ','
    ans = ''
    for ch in x:
        if ch.isdigit():
            ans = ans + ch
    return ans


if __name__ == '__main__':
    main()
