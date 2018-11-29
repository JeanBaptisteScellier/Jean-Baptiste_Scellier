# coding: utf-8
import requests
import re
from bs4 import BeautifulSoup


acer = "https://www.darty.com/nav/recherche?p=200&s=relevence&text=acer&fa=756"
dell = "https://www.darty.com/nav/recherche?p=200&s=relevence&text=dell&fa=756"

def main():
    print("acer : " + get_discount_for_company(acer))
    print("dell : " + get_discount_for_company(dell))


def get_discount_for_company(company):
    res = requests.get(company)
    soup = BeautifulSoup(res.text, "lxml")
    liste = []
    for tag in soup.find_all("p", class_="darty_prix_barre_remise darty_small separator_top"):
        value = tag.text.replace("-", "").replace(" ", "").replace("%", "")
        liste.append(int(value))
    return str(sum(liste) / len(liste))



main()