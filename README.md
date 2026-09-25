# Wikipedia as a Product | Analiza Akwizycji i Retencji Twórców

![Podgląd Raportu](dashboard_preview.png)

## 📌 O projekcie
Cześć! To mój projekt przygotowany w ramach wyzwania analitycznego #BI_NGO. Zamiast analizować Wikipedię jako zwykłą encyklopedię, podszedłem do niej jak do klasycznego produktu cyfrowego w modelu SaaS. 

Skupiłem się na przebadaniu lejka zaangażowania twórców (edytorów). Chciałem sprawdzić, jak na przestrzeni lat wyglądała akwizycja nowych kont, ilu z tych użytkowników faktycznie było aktywnych (MAU) i jak wyglądał wskaźnik ich retencji.

## 🛠 Wykorzystane technologie
* **Wizualizacja:** Microsoft Power BI
* **Przygotowanie danych (ETL):** Python (Pandas)
* **Logika i zapytania:** DAX, SQL

## 🏗 Architektura danych i DAX
Zależało mi na tym, żeby raport działał płynnie i był odporny na błędy użytkownika:
* **Model Gwiazdy (Star Schema):** Oddzieliłem tabele faktów (rejestracje, edycje) od tabel wymiarów (zbudowałem osobną, rozbudowaną tabelę Kalendarza). Dzięki temu filtrowanie po datach działa bez opóźnień i błędów w kalkulacjach.
* **Czysty UX w miarach DAX:** Spędziłem trochę czasu nad obsługą pustych wartości (tzw. edge cases). Moja miara `MAU YoY %` wykorzystuje funkcję `HASONEVALUE`. Jeśli użytkownik nie wybierze konkretnego roku na filtrze, raport nie wypluwa technicznych błędów typu `NaN` czy `(Puste)`, tylko elegancko wyświetla pauzę lub prosi o wybór daty.

## 🎨 UI/UX i praca z Brand Bookiem
Raport w 100% opiera się na oficjalnym Brand Booku Wikimedii. Zamiast dobierać kolory na oko, wdrożyłem konkretne wymogi klienta:
* **Kolorystyka:** Zrezygnowałem z domyślnych palet Power BI na rzecz dokładnych kodów HEX (Główny niebieski: `#0C57A8`, Szary: `#7F7F7F`, Tekst: `#404040`).
* **Typografia (Custom JSON):** Power BI domyślnie nie obsługuje oficjalnej czcionki fundacji. Aby to obejść, napisałem własny plik konfiguracyjny `.json` z motywem, który wymusił globalne użycie fontu **Montserrat** dla wszystkich nagłówków i wskaźników KPI.
* **Układ:** Zastosowałem klasyczny "F-Pattern" – logotypy i najważniejsze metryki zagregowane są na samej górze, a szczegółowe trendy na dole.

## 📊 Co wynika z danych? (Wniosek makro)
* **Złote lata platformy:** Największe zaangażowanie twórców na polskiej Wikipedii przypada na lata 2007-2009. Potem widać długoletni, konsekwentny trend spadkowy.
* **Anomalia 2020:** Ten spadek został przerwany w zasadzie tylko raz – w 2020 roku przez globalną pandemię. Wskaźnik MAU YoY podskoczył wtedy o 6,27%, a średnia liczba edycji na użytkownika wróciła do bardzo stabilnych poziomów.
* **Wnioski biznesowe:** Rok 2020 udowodnił, że użytkownicy mają czas na edytowanie, gdy znikają inne rozpraszacze. Aby dzisiaj skutecznie konkurować z social mediami o czas twórców, platforma potrzebuje całkowicie przedefiniować sposób ich angażowania i prawdopodobnie wprowadzić nowe mechanizmy grywalizacji, które odtworzą tę motywację w normalnych warunkach.