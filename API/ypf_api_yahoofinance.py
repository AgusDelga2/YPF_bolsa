from yahoo_fin.stock_info import get_data
import pandas as pd

"""
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
ypf_daily_df.to_csv('ypf_daily_23_api.csv')"""

#------------------------------------------------------------------------------------------------------
#Obtenemos datos semanales de YPF desde enero de 2023 hasta la actualidad
ypf_weekly_23= get_data("YPFD.BA", start_date="01/01/2023", end_date="05/26/2023", index_as_date = False, interval="1wk")

print(ypf_weekly_23.dtypes)
print("------------- Datos semanales de 2023 -------------")
print(ypf_weekly_23.head())
print(".......................................................................")
print(ypf_weekly_23.tail())
#convertimos a df
ypf_weekly_23_df = pd.DataFrame(ypf_weekly_23)

#Guardamos el archivo csv
ypf_weekly_23_df.to_csv('ypf_weekly_23_api.csv')

"""#------------------------------------------------------------------------------------------------------
#Obtenemos datos semanales de YPF desde enero de 2019 a diciembre de 2022
ypf_weekly= get_data("YPFD.BA", start_date="01/01/2019", end_date="31/12/2022", index_as_date = False, interval="1wk")

print(ypf_weekly.dtypes)
print("------------- Datos semanales de 2019 a 2022 -------------")
print(ypf_weekly.head())
print(".......................................................................")
print(ypf_weekly.tail())
#convertimos a df
ypf_weekly_df = pd.DataFrame(ypf_weekly)

#Guardamos el archivo csv
ypf_weekly_df.to_csv('ypf_weekly_19-22_api.csv')
"""