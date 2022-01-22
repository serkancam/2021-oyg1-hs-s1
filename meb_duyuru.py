from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import pandas as pd
import time

ayarlar = FirefoxOptions()
ayarlar.add_argument("--headless"),
surucu = webdriver.Firefox(options=ayarlar, executable_path="/home/serkan/Belgeler/2021-oyg1-hs-s1/geckodriver")
surucu.get("https://www.meb.gov.tr/meb_duyuruindex.php")
# sayfadan çekilecek bilgiler için listeler
tarih = []
aciklama = []
adres = []
sayfa = 1
son = 61
# icerik = surucu.page_source
# print(icerik)
while sayfa<=son:
    icerik=surucu.page_source
    agac = BeautifulSoup(icerik,"lxml")
    duyuru_listesi= agac.find_all("tr",attrs={"role":"row"})
    for haber in duyuru_listesi:
        try:
            duyuru_baslik=haber.find_all("td")[1].text
            duyuru_adres=haber.find_all("td")[1].find("a").get("href")
            duyuru_tarih =haber.find_all("td")[2].text
            tarih.append(duyuru_tarih)
            aciklama.append(duyuru_baslik)
            adres.append(duyuru_adres)
        except:
            continue
    
    surucu.find_element_by_xpath("/html/body/section[2]/div/div/div/div/div/div/div[3]/div[2]/div/ul/li[9]/a").click()    
    sayfa+=1
    time.sleep(1)  
surucu.close()
#veriyi csv dosyasına yazma
veri = {"aciklama":aciklama,"adres":adres,"tarih":tarih}
df = pd.DataFrame(veri)
df.to_csv("meb_duyuru_hepsi.csv",index=False)
print("İşlem bitti.")
