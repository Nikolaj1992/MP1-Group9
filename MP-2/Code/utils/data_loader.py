import pandas as pd

def load_excel(file_path, na_values=['NA'], sheet_name=0, skiprows=1):
    return pd.read_excel(file_path, sheet_name=sheet_name, index_col=None, na_values=na_values, skiprows=skiprows)

def merge_wine_data(df_red, df_white):
    df_red['type'] = 'red'
    df_white['type'] = 'white'
    return pd.concat([df_red, df_white], ignore_index=True)

def remove_missing(df):
    return df.dropna()

def remove_duplicates(df):
    return df.drop_duplicates()