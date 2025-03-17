import pandas as pd

def txt_to_excel(txt_file, excel_file):
    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            nombres = [line.strip() for line in file if line.strip()]
        
        df = pd.DataFrame({'Nombres': nombres})
        df.to_excel(excel_file, index=False, engine='openpyxl')
        print(f"Archivo guardado como {excel_file}")
    except Exception as e:
        print(f"Error: {e}")


txt_to_excel('ListaEstudiantes.txt', 'ListaEstudiantes.xlsx')
