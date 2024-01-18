# Importējam nepieciešāmas bibliotēkas no Selenium
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

# Konfigurējam Selenium un Chrome pārlūkprogrammu
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# Izveidojam sarakstus, lai glabātu datus par videokartēm
all_graphics_cards = []
lapaspuse = 1
videokartes_s = []
atbilst = []
best_video_card = None
best_gpu_speed = 0
best_memory = 0

# Norādītais interneta veikala URL
url = "https://www.dateks.lv"
driver.get(url)
time.sleep(2)

# Navigējam uz videokartes sadaļu
find = driver.find_element(By.CLASS_NAME, "button").click()
find = driver.find_element(By.CLASS_NAME, "ico").click()
find = driver.find_element(By.XPATH, "//li[@class='sads']//p[@class='click'][contains(text(), 'Komponentes')]").click()
time.sleep(1)
find = driver.find_element(By.LINK_TEXT, "Videokartes").click()
find = driver.find_element(By.ID, "srt").click()
find = driver.find_element(By.XPATH, "//option[text()='Lētākie vispirms']").click()

# Sākam ciklu, lai apmeklētu visus lapas numurus
while True:
    videokartes_konteineri = driver.find_elements(By.CSS_SELECTOR, 'div.prod')
    for konteineri in videokartes_konteineri:
        specs = konteineri.find_elements(By.CSS_SELECTOR, 'div.fv')

        kartes_info = []

        # Iegūstam videokartes specifikāciju datus
        for spec in specs:
            key = spec.find_element(By.CSS_SELECTOR, 'span.k').text.strip(': ')
            value = spec.find_element(By.CSS_SELECTOR, 'span.v').text
            kartes_info.append((key, value))
        
        # Iegūstam un pārveidojam cenu datus
        price = konteineri.find_element(By.CSS_SELECTOR, 'div.price-info').text.replace('€', '').replace(',', '.').replace(' ', '')
        kartes_info.append(('Cena', float(price)))
        
        all_graphics_cards.append(kartes_info)

    time.sleep(2)

    # Pārejam uz nākamo lapu, ja tāda ir
    if lapaspuse < 17:
        nakamaspogas = driver.find_elements(By.CLASS_NAME, "prevnext")
        if nakamaspogas:
            nakamalapa = nakamaspogas[-1].get_attribute('href')
            driver.get(nakamalapa)
            lapaspuse += 1
        else:
            break
    else:
        break

# Aizveram pārlūkprogrammu
driver.quit()

# Saglabājam visus videokartes datus tekstovā failā
with open('videokartes_saraksts.txt', 'w', encoding='utf-8') as file:
    for card_info in all_graphics_cards:
        card_info_str = ', '.join(f"{key}: {value}" for key, value in card_info)
        file.write(card_info_str + "\n")

time.sleep(2)

# Atkal nolasām datus no tekstovā faila
with open("videokartes_saraksts.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Apstrādājam un saglabājam videokartes specifikācijas
for line in lines:
    parametri = line.strip().split(', ')

    vidkartes = []
    for par in parametri:
        key, value = par.split(': ')

        if key == 'Dzinēja ātrums (GPU speed)' and value.endswith(' MHz'):
            value = int(value.replace(' MHz', ''))
        elif key == 'Operatīvā atmiņa' and value.endswith(' GB'):
            value = int(value.replace(' GB', ''))
        elif key == 'Cena':
            value = float(value)

        vidkartes.append((key, value))

    videokartes_s.append(vidkartes)

# Lietotājs norāda budžetu
budget_min = float(input("Jusu minimalais budžets: "))
budget_max = float(input("Jusu maksimalais budžets: "))

# Atliek tikai tās videokartes, kas iekļaujas budžetā
for vk in videokartes_s:
    for k, v in vk:
        if k == 'Cena' and v <= budget_max and v >= budget_min:
            atbilst.append(vk)
            break

# Atrodam labāko videokarti
for karte in atbilst:
    for item in karte:
        if item[0] == 'Dzinēja ātrums (GPU speed)':
            gpu_speed = item[1]
        elif item[0] == 'Operatīvā atmiņa':
            memory = item[1]

    if isinstance(gpu_speed, int) and isinstance(memory, int):
        if gpu_speed > best_gpu_speed or memory > best_memory:
            best_video_card = karte
            best_gpu_speed = gpu_speed
            best_memory = memory

# Izvadām rezultātus
print("Labaka videokarte:")
for item in best_video_card:
    print(f"{item[0]}: {item[1]}")
