import pandas as pd
import re

# Wrzucam surowe dane pobrane z API
df_new_reg = pd.read_csv('3-nowe_rejestracje_monthly.csv')
df_active_ed = pd.read_csv('4-aktywni_edytorzy_monthly.csv')
df_edits = pd.read_csv('8-edycje_uzytkownikow_monthly.csv')

# Domyślne nazwy z API (total.total) są bezużyteczne biznesowo, od razu zmieniam je pod Power BI
df_new_reg = df_new_reg.rename(columns={'total.total': 'nowe_rejestracje'})
df_active_ed = df_active_ed.rename(columns={'total.total': 'aktywni_edytorzy'})

# API Wikimedii przy edycjach wypluwa zepsuty format daty (np. 2001--0-9-T...). 
# Piszę szybkiego regexa, żeby poskładać to do normalnego YYYY-MM-DD, inaczej Power BI się wywali.
def fix_date(date_str):
    if pd.isna(date_str):
        return date_str
    return re.sub(r'--(\d)-(\d)-T', r'-\1\2-01T', str(date_str))

df_edits['month'] = df_edits['month'].apply(fix_date)

# Analizuję Wikipedię jako produkt SaaS, więc odsiewam cały ruch maszynowy (boty).
# Zostawiam tylko prawdziwych ludzi (zalogowanych i anonimów), żeby mieć wiarygodne metryki zaangażowania.
df_edits_humans = df_edits[df_edits['editor_type'].isin(['user', 'anonymous'])]

# Zwijam dane do poziomu miesiąca i sumuję edycje
df_edits_grouped = df_edits_humans.groupby('month')[['total.content', 'total.non-content']].sum().reset_index()
df_edits_grouped['wszystkie_edycje_ludzi'] = df_edits_grouped['total.content'] + df_edits_grouped['total.non-content']

# Sklejam te trzy zbiory w jedną główną tabelę faktów (Master Table) pod model gwiazdy
df_master = pd.merge(df_new_reg, df_active_ed, on='month', how='outer')
df_master = pd.merge(df_master, df_edits_grouped[['month', 'wszystkie_edycje_ludzi']], on='month', how='outer')

# Na sam koniec czyszczę stringa z datą. Ucinam końcówkę "T00:00:00.000Z", 
# żeby po stronie Power BI od razu ustawić czysty typ danych Date.
df_master['month'] = pd.to_datetime(df_master['month']).dt.date
df_master = df_master.sort_values('month')

# Zrzut wyczyszczonych danych do pliku, który bezpośrednio zaczytuję do dashboardu
df_master.to_csv('wikipedia_product_metrics.csv', index=False)
