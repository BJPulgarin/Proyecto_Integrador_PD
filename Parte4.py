import requests

def ObtenerCsv(url: str):
    response = requests.get(url)
    try:
        api_data = response.text
        with open('data.csv', 'w') as f:
            f.write(api_data)
            print('Se ha generado el archivo!')
    except requests.exceptions.RequestException:
        print('Ocurrió un problema con la solicitud HTTP')
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


ObtenerCsv("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv")
