# coding: utf-8
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

chromedriver = "/Applications/chromedriver"
driver = webdriver.Chrome(chromedriver)

prix = []
modele = []
annee = []
kilometrage = []
vendeur = []

url0 = "https://www.lacentrale.fr/listing?makesModelsCommercialNames=RENAULT%3AZOE&regions=FR-IDF"
url = "https://www.lacentrale.fr/listing?makesModelsCommercialNames=RENAULT%3AZOE&options=&page=2&regions=FR-IDF"

driver.get(url0)

for i in range(2, 15):
    results = driver.find_elements_by_class_name('fieldPrice')
    prix.extend(map(lambda x: x.text, results))

    results = driver.find_elements_by_class_name('typeSeller')
    vendeur.extend(map(lambda x: x.text, results))

    results = driver.find_elements_by_class_name('version')
    modele.extend(map(lambda x: x.text, results))
    
    results = driver.find_elements_by_class_name('fieldYear')
    annee.extend(map(lambda x: x.text, results))
    
    results = driver.find_elements_by_class_name('fieldMileage')
    kilometrage.extend(map(lambda x: x.text, results))

    driver.get(url.format(i))

driver.close()

columns = ["Prix", "Modèle", "Année", "Kilométrage", "Type de vendeur"]
df = pd.DataFrame(columns=columns)

df["Prix"] = prix
df["Modèle"] = modele
df["Année"] = annee
df["Kilométrage"] = kilometrage
df["Type de vendeur"] = vendeur

print(df)
