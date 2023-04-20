from yahoo_fin.stock_info import get_data
import pandas as pd

#Obtenemos datos diarios de YPF desde enero de 2019 a diciembre de 2022
ypf_daily= get_data("YPFD.BA", start_date="01/01/2019", end_date="12/12/2022", index_as_date = False, interval="1d")
print(ypf_daily.dtypes)
print("------------- Datos diarios -------------")
print(ypf_daily.head())

#convertimos a df
ypf_daily_df = pd.DataFrame(ypf_daily)

#Guardamos el archivo csv
ypf_daily_df.to_csv('ypf_daily.csv')

#Obtenemos datos semanales de YPF desde enero de 2019 a diciembre de 2022
ypf_weekly= get_data("ypf", start_date="01/01/2019", end_date="12/12/2022", index_as_date = False, interval="1wk")

print(ypf_weekly.dtypes)
print("------------- Datos semanales -------------")
print(ypf_weekly.head())

#convertimos a df
ypf_weekly_df = pd.DataFrame(ypf_weekly)

#Guardamos el archivo csv
ypf_weekly_df.to_csv('ypf_weekly.csv')

