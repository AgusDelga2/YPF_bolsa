from yahoo_fin.stock_info import get_data
import pandas as pd

#Obtenemos datos diarios de YPF desde el 1 de enero de 2023 hasta el día de la fecha, 18 de mayo
ypf_daily= get_data("YPFD.BA", start_date="01/01/2023", end_date="05/18/2023", index_as_date = False, interval="1d")

print(ypf_daily.dtypes)
print("------------- Datos por día de 2023-------------")
print(ypf_daily.head())
print(".......................................................................")
print(ypf_daily.tail())

#convertimos a df
ypf_daily_df = pd.DataFrame(ypf_daily)

#Guardamos el archivo csv
ypf_daily_df.to_csv('ypf_daily_23_api.csv')
