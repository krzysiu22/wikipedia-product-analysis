*[🇬🇧 Read documentation in English](README.md)*

# Wikipedia jako Cyfrowy Produkt | Analiza Akwizycji i Retencji Twórców

![Python](https://img.shields.io/badge/Python-ETL_Pipeline-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Cleansing-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-Defensive_Programming-00599C?style=for-the-badge&logo=powerbi&logoColor=white)

## Opis Projektu
Ten projekt analityczny został stworzony w ramach wyzwania **#BI_NGO**. Zamiast traktować Wikipedię jako zwykłą bazę wiedzy, analiza ta ocenia platformę jako klasyczny produkt cyfrowy typu SaaS (Software as a Service). 

Dashboard śledzi długoterminowy cykl życia twórców polskiej Wikipedii, skupiając się na akwizycji użytkowników (Nowe Rejestracje), aktywnym zaangażowaniu (Monthly Active Users - MAU) oraz strategiach utrzymania (retencji).

## Podgląd Raportu
<p>
  <img src="dashboard_preview.png" alt="Wikipedia Dashboard Preview" width="100%">
</p>

## Architektura Techniczna i Proces

### 1. Inżynieria Danych i ETL (Python / Pandas)
* **Czyszczenie Danych z API:** Surowe dane pobrane z API Wikimedii zawierały uszkodzone formaty dat (np. `2001--0-9-T`). Opracowałem skrypt w Pythonie wykorzystujący **Wyrażenia Regularne (RegEx)** do ujednolicenia dat do standardu `YYYY-MM-DD`, co zapobiegło błędom importu w Power BI.
* **Izolacja Ruchu:** Odfiltrowałem zautomatyzowane działania maszyn/botów, aby wyizolować wyłącznie ludzkie zaangażowanie, zapewniając wiarygodność kluczowych wskaźników retencji (KPI).
* **Agregacja Tabeli Faktów:** Połączyłem kilka oczyszczonych zbiorów danych w pojedynczą, zoptymalizowaną Tabelę Faktów `wikipedia_product_metrics.csv`, gotową do modelowania wielowymiarowego.

### 2. Modelowanie Danych i DAX (Defensive Programming)
* **Schemat Gwiazdy (Star Schema):** Oddzieliłem zagregowaną Tabelę Faktów od wymiarów, wdrażając dedykowaną, wewnętrzną tabelę Kalendarza, co zapewniło stabilne filtrowanie danych w czasie (time-intelligence).
* **Odporne na błędy miary DAX:** Zastosowałem zasady "defensive programming" w kalkulacjach DAX. Przykładowo, miara `MAU YoY %` używa funkcji `HASONEVALUE`, prosząc użytkownika o wybranie konkretnego roku, zamiast zwracać błędy `NaN`. Puste okresy operacyjne obsłużyłem funkcją `BLANK()`, dzięki czemu wykresy liniowe urywają się naturalnie, zamiast sztucznie spadać do zera.

### 3. UI/UX i Zgodność z Brand Bookiem
* **Niestandardowy Motyw JSON:** Ponieważ Power BI natywnie ogranicza możliwość wgrywania własnych czcionek, przygotowałem i zaimportowałem niestandardowy plik motywu `.json`, aby wymusić czcionkę **Montserrat** (oficjalny font Wikimedia Foundation) na wszystkich wskaźnikach i nagłówkach.
* **Ścisła Paleta Kolorów:** Dashboard jest w pełni zgodny z Wikimedia Brand Book, z wykorzystaniem dokładnych kodów HEX (Niebieski: `#0C57A8`, Jasnoszary: `#7F7F7F`, Ciemnoszary: `#404040`).
* **Hierarchia Wizualna:** Zastosowałem układ F-Pattern. Najważniejsze metryki biznesowe są natychmiast widoczne na samej górze, przechodząc płynnie w szczegółowe trendy historyczne poniżej.

---

## Kluczowe Wnioski Biznesowe i Rekomendacje

* **Historyczny Szczyt:** Największe zaangażowanie twórców na polskiej Wikipedii miało miejsce w latach 2007–2009, po czym nastąpił długi, stały trend spadkowy.
* **Anomalia 2020:** Jedynym znaczącym zaburzeniem tego spadku był rok 2020 (globalny lockdown). Wskaźnik MAU wzrósł wówczas o **6,27%**, a średnia liczba edycji na użytkownika drastycznie wystrzeliła.
* **Rekomendacja Strategiczna:** Dane z 2020 roku dowodzą, że użytkownicy chętnie edytują platformę, gdy dysponują czasem i brakuje im zewnętrznych "rozpraszaczy". Aby skutecznie konkurować o uwagę twórców z nowoczesnymi algorytmami mediów społecznościowych, platforma musi ewoluować poza stary model oparty wyłącznie na pasji i wprowadzić nowoczesne mechanizmy angażowania (np. grywalizację interfejsu).
