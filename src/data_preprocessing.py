import pandas as pd
import re

# 1. Wczytanie surowych plików
df_new_reg = pd.read_csv('3-nowe_rejestracje_monthly.csv')
df_active_ed = pd.read_csv('4-aktywni_edytorzy_monthly.csv')
df_edits = pd.read_csv('8-edycje_uzytkownikow_monthly.csv')

# Zmiana nazw kolumn z domyślnego "total.total" na biznesowe
df_new_reg = df_new_reg.rename(columns={'total.total': 'nowe_rejestracje'})
df_active_ed = df_active_ed.rename(columns={'total.total': 'aktywni_edytorzy'})

# 2. NAPRAWA ZEPSUTEJ DATY W PLIKU NR 8
# Format w pliku to np. "2001--0-9-T...", regexem zmieniamy to na normalne "2001-09-01T..."
def fix_date(date_str):
    if pd.isna(date_str):
        return date_str
    return re.sub(r'--(\d)-(\d)-T', r'-\1\2-01T', str(date_str))

df_edits['month'] = df_edits['month'].apply(fix_date)

# 3. Czyszczenie ruchu: Odrzucamy boty ("group-bot", "name-bot")
# Chcemy badać zachowanie prawdziwych ludzi (zalogowanych i anonimowych)
df_edits_humans = df_edits[df_edits['editor_type'].isin(['user', 'anonymous'])]

# Grupujemy po miesiącu i sumujemy edycje
df_edits_grouped = df_edits_humans.groupby('month')[['total.content', 'total.non-content']].sum().reset_index()
df_edits_grouped['wszystkie_edycje_ludzi'] = df_edits_grouped['total.content'] + df_edits_grouped['total.non-content']

# 4. MERGE: Łączenie 3 tabel w jedną hurtownię (Master Table)
df_master = pd.merge(df_new_reg, df_active_ed, on='month', how='outer')
df_master = pd.merge(df_master, df_edits_grouped[['month', 'wszystkie_edycje_ludzi']], on='month', how='outer')

# 5. Formatowanie ostateczne (obcinamy "T00:00:00.000Z" żeby Power BI miał czystą Datę)
df_master['month'] = pd.to_datetime(df_master['month']).dt.date
df_master = df_master.sort_values('month')

# 6. Zapis do nowego pliku
df_master.to_csv('wikipedia_product_metrics.csv', index=False)

print("Gotowe! Wygenerowano czysty plik: wikipedia_product_metrics.csv")