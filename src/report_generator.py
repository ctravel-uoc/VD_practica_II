def generate_html_report(charts, output_filename="index.html"):
    mapa_html = charts['mapa'].to_html(full_html=False, include_plotlyjs='cdn')
    linea_html = charts['linea'].to_html(full_html=False)
    
    radar_1_html = charts['radar_1'].to_html(full_html=False)
    radar_2_html = charts['radar_2'].to_html(full_html=False)
    radar_3_html = charts['radar_3'].to_html(full_html=False)
    
    scatter_html = charts['scatter'].to_html(full_html=False)

    html_template = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ley vs. Realidad</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 20px; 
            padding: 0; 
            background-color: #f4f4f9; 
            color: #333;
        }}
        .container {{ 
            max-width: 1200px; 
            margin: auto; 
            background-color: #ffffff; 
            padding: 20px; 
            border-radius: 8px; 
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
        }}
        h1, h2, h3 {{ text-align: center; color: #1a1a1a; }}
        hr {{ border: 0; height: 1px; background-color: #ccc; margin: 30px 0; }}
        .chart-section {{ 
            margin-bottom: 40px; 
            border: 1px solid #ddd; 
            padding: 15px; 
            border-radius: 6px; 
            background-color: #fff; 
        }}
        .plotly-graph-div {{ height: 600px !important; width: 100% !important; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Igualdad de Género: Ley vs. Realidad</h1>
        <h3>Informe interactivo generado a partir de datos del Banco Mundial (WBL)</h3>
        <hr>
        <div class="chart-section">
            <h2 style="text-align: left;">1. Análisis geográfico: Evolución del marco legal</h2>
            <p>El mapa muestra la puntuación legal (Índice WBL) por país. Utiliza el control de animación para ver la evolución de 1971 a 2024.</p>
            {mapa_html}
        </div>
        <hr>
        <div class="chart-section">
            <h2 style="text-align: left;">2. Análisis temporal: Evolución media del marco legal</h2>
            <p>Gráfico de líneas que muestra la media del Índice WBL a lo largo del tiempo para todas las regiones.</p>
            {linea_html}
        </div>
        <hr>
        <h2 style="text-align: center;">3. Análisis de causa raíz (Múltiples comparativas sectoriales 2024)</h2>
        <div class="chart-section">
            {radar_1_html}
        </div>
        <div class="chart-section">
            {radar_2_html}
        </div>
        <div class="chart-section">
            {radar_3_html}
        </div>
        <hr>
        <div class="chart-section">
            <h2 style="text-align: left;">4. Correlación: Ley (WBL) vs. Realidad (% Parlamento Femenino)</h2>
            <p>Visualiza la relación entre la igualdad legal (Eje X) y la representación parlamentaria (Eje Y).</p>
            {scatter_html}
        </div>
        <hr>
        <p style="text-align: center; font-size: 0.9em; color: #666;">
            Práctica de la asignatura Visualización de Datos del Máster Ciencia de Datos de la UOC - Carmen Travel Alarcón.
        </p>
    </div>
</body>
</html>
    """

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"\n Archivo {output_filename} generado")