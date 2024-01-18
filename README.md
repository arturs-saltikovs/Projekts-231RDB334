# Video Kartes Meklēšanas un Salīdzināšanas Rīks

## Projekta Nosaukums
Video Kartes Meklēšanas un Salīdzināšanas Rīks

## Projekta Apraksts
Šis projekts ir izstrādāts, lai piedāvātu lietotājam efektīvu un ērtu veidu, kā meklēt un salīdzināt video kartes tiešsaistes veikalos. Mūsdienu datorspēles un strādāšana ar grafiku prasa augstu veiktspēju video kartes, tāpēc šāds rīks varētu būt ļoti noderīgs tiem, kas cenšas atrast labu videokarti, ievērojot savu budžetu.

## Projekta Uzdevums
Šo projektu raksturo daži galvenie uzdevumi un darbības soļi:

1. **Tīmekļa Veikala Atvēršana:** Pirmkārt, programma atver norādīto interneta veikalu. Mēs izmantojam "dateks.lv" kā piemēru, bet rīks varētu tikt pielāgots citiem veikaliem.

2. **Navigācija uz Videokartes Sadaļu:** Programma veic automatizētu pārvietošanos uz videokartes sadaļu vietnē. Tas tiek izdarīts, lai nodrošinātu, ka mēs strādājam tikai ar videokartēm.

3. **Visu Pieejamo Videokaršu Saraksta Iegūšana:** Rīks meklē un iegūst visu pieejamo videokaršu sarakstu tīmekļa vietnē. Šie dati tiek saglabāti lokālā tekstovā failā turpmākai analīzei.

4. **Budžeta Norādīšana:** Lietotājs tiek lūgts ievadīt minimālo un maksimālo budžetu, lai atlasītu videokartes, kas atbilst šiem kritērijiem.

5. **Videokaršu Atlase:** Programma salīdzina katras videokartes cenu ar lietotāja norādīto budžetu un atlasa tās, kas iekļaujas šajā diapazonā. Šīs atlases rezultāti tiek saglabāti atsevišķā sarakstā.

6. **Labākās Videokartes Izvēle:** Visbeidzot, programma izvēlas labāko videokarti no atbilstošajiem piedāvājumiem, ņemot vērā tos kritērijus, kas lietotājam ir svarīgākie. Šie kritēriji var būt GPU (grafiskā procesora) ātrums un operatīvā atmiņa (RAM).

## Izmantotās Python Bibliotēkas
Šim projektam tiek izmantota Python programmēšanas valoda kopā ar Selenium bibliotēku. Selenium piedāvā automatizētu pārlūkošanas un datu ieguves rīkus, kas ir lieliski piemēroti šādam uzdevumam. Selenium ļauj automatizēti pārvietoties pa tīmekļa vietnēm, iegūt informāciju un veikt darbības tīmekļa lapās.

## Programmatūras Izmantošana
Lai izmantotu šo programmu, jums būs nepieciešams izpildāms Python kods un instalēta Selenium bibliotēka. Lūdzu, sekojiet šiem soļiem:

1. **Python Instalācija:** Ja vēl neesat instalējis Python, pārliecinieties, ka to lejupielādējat un uzstādāt savā datorā no [Python oficiālās vietnes](https://www.python.org/downloads/).

2. **Selenium Instalācija:** Instalējiet Selenium bibliotēku, izmantojot šo komandu: `pip install selenium`.

3. **Chrome Pārlūkprogrammas Instalācija:** Rīks ir izstrādāts, izmantojot Chrome pārlūkprogrammu. Pārliecinieties, ka jums ir instalēta Chrome pārlūkprogramma un tā ir atjaunināta līdz jaunākajai versijai.

4. **Koda Izpilde:** Izpildiet Python kodu, lai meklētu un salīdzinātu video kartes.

5. **Budžeta Norādīšana:** Programma jums pieprasīs ievadīt minimālo un maksimālo budžetu.

6. **Rezultāti:** Programma izvēlēsies labāko atbilstošo videokarti un parādīs to kā rezultātu.

## Video Prezentācija
Lai labāk saprastu, kā šī programma darbojas, esmu sagatavojis video prezentāciju, kurā parādīts visas darbības sākums līdz beigām. Jūs varat noskatīties video prezentāciju, sekojot šai [https://youtu.be/yv3DsGI4ecI].

