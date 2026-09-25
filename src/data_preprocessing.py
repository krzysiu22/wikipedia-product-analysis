import pandas as pd
import re

df_new_reg = pd.read_csv('3-nowe_rejestracje_monthly.csv')
df_active_ed = pd.read_csv('4-aktywni_edytorzy_monthly.csv')
df_edits = pd.read_csv('8-edycje_uzytkownikow_monthly.csv')

df_new_reg = df_new_reg.rename(columns={'total.total': 'nowe_rejestracje'})
df_active_ed = df_active_ed.rename(columns={'total.total': 'aktywni_edytorzy'})


def fix_date(date_str):
    if pd.isna(date_str):
        return date_str
    return re.sub(r'--(\d)-(\d)-T', r'-\1\2-01T', str(date_str))

df_edits['month'] = df_edits['month'].apply(fix_date)


df_edits_humans = df_edits[df_edits['editor_type'].isin(['user', 'anonymous'])]


df_edits_grouped = df_edits_humans.groupby('month')[['total.content', 'total.non-content']].sum().reset_index()
df_edits_grouped['wszystkie_edycje_ludzi'] = df_edits_grouped['total.content'] + df_edits_grouped['total.non-content']


df_master = pd.merge(df_new_reg, df_active_ed, on='month', how='outer')
df_master = pd.merge(df_master, df_edits_grouped[['month', 'wszystkie_edycje_ludzi']], on='month', how='outer')


df_master['month'] = pd.to_datetime(df_master['month']).dt.date
df_master = df_master.sort_values('month')


df_master.to_csv('wikipedia_product_metrics.csv', index=False)

print("Wygenerowano plik: wikipedia_product_metrics.csv")
