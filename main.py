from src.data_loader import prepare_data
from src.chart_generator import (
    create_map_chart, 
    create_line_chart, 
    create_radar_chart, 
    create_scatter_chart
)
from src.report_generator import generate_html_report
import sys

FILE_LEY = "data/WBL2024-1-0-Historical-Panel-Data.xlsx"
FILE_REALIDAD = "data/API_SG.GEN.PARL.ZS_DS2_en_csv_v2_216057.csv"

if __name__ == "__main__":
    try:
        df_ley, df_merged = prepare_data(FILE_LEY, FILE_REALIDAD)
    except Exception as e:
        print(f"Error {e} al preparpar datos")
        sys.exit(1)

    print("\nGenerando gráficos")
    
    charts = {
        'mapa': create_map_chart(df_ley),
        'linea': create_line_chart(df_ley),
    }

    charts['radar_1'] = create_radar_chart(
        df_ley, 
        paises_comparar=['Spain', 'Afghanistan'], 
        chart_title="3A. Comparativa extrema: máxima igualdad vs. mínima igualdad (2024)"
    )
    charts['radar_2'] = create_radar_chart(
        df_ley, 
        paises_comparar=['Colombia', 'Uganda', 'China'], 
        chart_title="3B. Comparativa de economías emergentes (2024)"
    )
    charts['radar_3'] = create_radar_chart(
        df_ley, 
        paises_comparar=['United States', 'Germany', 'Japan'], 
        chart_title="3C. Comparativa G7 (2024)"
    )
    
    charts['scatter'] = create_scatter_chart(df_merged)
    
    print("Gráficos generados")

    generate_html_report(charts, output_filename="index.html")

    print("\nProceso completado")