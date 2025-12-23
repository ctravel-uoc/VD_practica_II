import pandas as pd
import sys

def load_data(file_path, sheet_name=None, skiprows=None):
    try:
        if file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        elif file_path.endswith('.csv'):
            df = pd.read_csv(file_path, skiprows=skiprows)
        else:
            raise ValueError("Formato de archivo no soportado.")
        return df
    except Exception as e:
        print(f"Error FATAL cargando {file_path}: {e}")
        sys.exit(1)

def prepare_data(file_ley, file_realidad):
    print("Cargando y procesando datos...")

    df_ley = load_data(file_ley, sheet_name='WBL Panel 2024')
    df_parl_ancho = load_data(file_realidad, skiprows=4)

    id_vars = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']
    year_columns = [col for col in df_parl_ancho.columns if str(col).isdigit()]
    df_parl_largo = df_parl_ancho.melt(
        id_vars=id_vars,
        value_vars=year_columns,
        var_name='Year',
        value_name='Parliament %'
    )
    df_parl_largo['Year'] = pd.to_numeric(df_parl_largo['Year'], errors='coerce')

    df_ley_renombrado = df_ley.rename(columns={'Report Year': 'Year'})
    df_parl_renombrado = df_parl_largo[['Country Code', 'Year', 'Parliament %']]

    df_merged = pd.merge(
        df_ley_renombrado,
        df_parl_renombrado,
        left_on=['ISO Code', 'Year'],
        right_on=['Country Code', 'Year'],
        how='inner'
    ).dropna(subset=['WBL INDEX', 'Parliament %', 'Economy', 'Income Group'])

    df_merged['Year'] = df_merged['Year'].astype(int)
    df_ley = df_ley.sort_values(by='Report Year')
    df_merged = df_merged.sort_values(by='Year')

    print("Datos listos.")
    return df_ley, df_merged

SECTORES = ['MOBILITY', 'WORKPLACE', 'PAY', 'MARRIAGE', 'PARENTHOOD', 'ENTREPRENEURSHIP', 'ASSETS', 'PENSION']