import pandas as pd

data_original = pd.read_csv("./data.csv")


def LimpiarData(data: pd.DataFrame):
    # hay faltantes?
    faltantes = data.isna().sum()
    print('Datos faltantes por columna: ')
    print(faltantes)
    print('\n')

    # hay registros duplicados?
    duplicados = data.duplicated().sum()
    if duplicados == 0:
        print('No hay registros duplicados')
    else:
        print('Existen registros duplicados')
    print('\n')

    # valores atípicos

    # tipos de datos
    print('Tipos de datos: ')
    print(data.dtypes)
    data['age'] = data['age'].astype(int)
    data['platelets'] = data['platelets'].astype(int)
    data['serum_creatinine'] = data['serum_creatinine'].astype(int)
    data['time'] = data['time'].astype(int)
    data['creatinine_phosphokinase'] = data['creatinine_phosphokinase'].astype(int)
    print('\n')
    print('Tipos de datos luego de conversión: ')
    print(data.dtypes)
    print('\n')

    # atipicos según IQR
    def EliminarAtipicos(nombre_columna, df: pd.DataFrame):
        q1 = df[nombre_columna].quantile(0.25)
        q3 = df[nombre_columna].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        print(nombre_columna, ': ', str(lower_bound), ', ', str(upper_bound))
        df_cleaned = df[(df[nombre_columna] >= lower_bound) & (df[nombre_columna] <= upper_bound)]
        return df_cleaned.reset_index(drop=True)

    print('Rangos típicos según IQR: ')
    data = EliminarAtipicos('age', data)
    data = EliminarAtipicos('creatinine_phosphokinase', data)
    data = EliminarAtipicos('ejection_fraction', data)
    data = EliminarAtipicos('platelets', data)
    data = EliminarAtipicos('serum_sodium', data)
    data = EliminarAtipicos('time', data)
    print('\n')
    print('Datos atípicos eliminados!')
    print('\n')

    # verificando columnas de (1 y 0)
    def VerificarBinarios(columna, df: pd.DataFrame):
        conteo_valores = df[columna].value_counts()
        if len(conteo_valores) == 2 and conteo_valores.sum() == len(df):
            print(f'La columna {columna} no tiene problemas')
        else:
            print(f'La columna {columna} tiene valores atípicos')

    print('Verificación de columnas binarias:')
    VerificarBinarios('anaemia', data)
    VerificarBinarios('smoking', data)
    VerificarBinarios('diabetes', data)
    VerificarBinarios('high_blood_pressure', data)
    VerificarBinarios('sex', data)
    VerificarBinarios('DEATH_EVENT', data)
    print('\n')

    def CategorizarEdad(edad):
        if edad <= 12:
            return 'Niño'
        elif edad <= 19:
            return 'Adolescente'
        elif edad <= 39:
            return 'Joven adulto'
        elif edad <= 59:
            return 'Adulto'
        else:
            return 'Adulto mayor'

    data['Grupo de Edad'] = data['age'].apply(CategorizarEdad)
    print('Edades categorizadas!')
    print('\n')

    data.to_csv('./resultado_limpieza.csv', index=False)
    print('Limpieza realizada!')


LimpiarData(data_original)
