import pandas as pd
def data_load(data):
    data = pd.read_csv(r"C:\Users\Dell\Niologic\Seattle_Real_Time_Fire_911_Calls-v.csv")
    return 'Data loaded'

data_load(pd.read_csv(r"C:\Users\Dell\Niologic\Seattle_Real_Time_Fire_911_Calls-v.csv"))