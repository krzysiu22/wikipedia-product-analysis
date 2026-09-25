# Wikipedia as a Product | Analiza Akwizycji i Retencji Twórców

![Podgląd Raportu](dashboard_preview.png)

## 📌 O projekcie
Cześć! Wrzuciłem tu mój projekt z wyzwania analitycznego #BI_NGO. Zamiast patrzeć na polską Wikipedię po prostu jak na zbiór artykułów, potraktowałem ją jak pełnoprawny produkt cyfrowy. 

Chciałem sprawdzić, jak platforma radzi sobie z pozyskiwaniem i utrzymywaniem twórców (edytorów). Przeanalizowałem, ilu nowych użytkowników zakłada konta, ilu z nich faktycznie edytuje (MAU) i jak wygląda ich retencja na przestrzeni lat.

## 🛠 Wykorzystane technologie
* **Wizualizacja:** Microsoft Power BI
* **Przygotowanie danych (ETL):** Python (Pandas)
* **Logika i zapytania:** DAX, SQL

## 🏗 Architektura danych i DAX
Od strony technicznej zależało mi na tym, żeby raport po prostu szybko działał i nie sypał błędami podczas klikania:
* **Model Gwiazdy (Star Schema):** Rozdzieliłem tabele faktów (rejestracje, edycje) od wymiarów (zbudowałem od zera własną tabelę Kalendarza). Dzięki temu filtrowanie po datach śmiga bez opóźnień.
* **Obsługa błędów w DAX:** Chciałem uniknąć sytuacji, w której po wyczyszczeniu filtrów na ekranie wyskakuje brzydkie `NaN` albo `(Puste)`. Do miary `MAU YoY %` dorzuciłem funkcję `HASONEVALUE` – jeśli ktoś nie wybierze konkretnego roku, raport po prostu grzecznie czeka na wybór i zachowuje czysty interfejs.

## 🎨 UI/UX i praca z Brand Bookiem
Wizualnie projekt jest w 100% zgodny z oficjalnym Brand Bookiem Wikimedii. Zamiast dobierać kolory "na oko":
* **Kolorystyka:** Zrezygnowałem z domyślnych palet Power BI i użyłem dokładnych kodów HEX z księgi znaku (Główny niebieski: `#0C57A8`, Szary: `#7F7F7F`, Tekst: `#404040`).
* **Czcionka (Custom JSON):** Power BI domyślnie nie ma wbudowanego oficjalnego fontu fundacji (Montserrat). Żeby to obejść, wstrzyknąłem go globalnie przez własny plik konfiguracyjny `.json`.
* **Układ:** Postawiłem na klasyczny F-Pattern. Najważniejsze liczby (KPI) i logotypy rzucają się w oczy od razu na górze, a szczegółowe trendy są nieco niżej.

## 📊 Czego dowiedziałem się z danych?
* **Złote lata:** Największy ruch i zaangażowanie edytorów na polskiej Wikipedii to lata 2007-2009. Potem zaczął się powolny, ale bardzo stały trend spadkowy.
* **Anomalia 2020:** Ten spadek zatrzymał się w zasadzie tylko raz – w 2020 roku podczas pandemii. Wskaźnik MAU podskoczył wtedy o 6,27%, a średnia liczba edycji na osobę wróciła do bardzo wysokich poziomów.
* **Wniosek:** Rok 2020 pokazał, że ludzie chętnie edytują Wikipedię, gdy mają na to czas i odcięto im inne rozpraszacze. Żeby dzisiaj wygrać walkę o uwagę twórców z algorytmami social mediów, platforma prawdopodobnie potrzebuje nowych sposobów na angażowanie i grywalizację.
