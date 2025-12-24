import plotly.express as px
import pandas as pd
from .data_loader import SECTORES

def create_map_chart(df_ley):
    print("Generando gráfico 1")
    return px.choropleth(
        df_ley,
        locations="ISO Code",
        color="WBL INDEX",
        hover_name="Economy",
        color_continuous_scale=px.colors.sequential.YlGnBu,
        range_color=[0, 100],
        title="1. Análisis geográfico: Evolución del Índice WBL (Marco Legal)",
        animation_frame="Report Year",
        animation_group="Economy",
    )

def create_line_chart(df_ley):
    print("Generando gráfico 2")
    
    df_linea_promedio = df_ley.groupby(['Report Year', 'Region'])['WBL INDEX'].mean().reset_index()
    
    fig = px.line(
        df_linea_promedio, 
        x='Report Year', 
        y='WBL INDEX', 
        color='Region',
        line_group='Region',
        hover_name='Region',
        title="2. Evolución media del Índice WBL (1971-2024) por Región",
        labels={'WBL INDEX': 'Índice WBL (media regional)', 'Report Year': 'Año del reporte'}
    )
    
    fig.update_layout(
        xaxis_title="Año", 
        yaxis_title="Índice WBL promedio",
        yaxis_range=[0, 100]
    )
    
    return fig

def create_radar_chart(df_ley, paises_comparar, chart_title):
    df_radar_data = df_ley[df_ley['Economy'].isin(paises_comparar) & (df_ley['Report Year'] == 2024)]
    
    if df_radar_data.empty or len(df_radar_data) < len(paises_comparar):
        print(f"Datos de 2024 incompletos para {paises_comparar}")
        return {} 
        
    df_radar_long = pd.melt(
        df_radar_data, 
        id_vars=['Economy'], 
        value_vars=SECTORES, 
        var_name='Sector', 
        value_name='Puntuación'
    )

    fig = px.line_polar(
        df_radar_long,
        r='Puntuación',
        theta='Sector',
        color='Economy',
        line_close=True,
        range_r=[0, 100],
        title=chart_title
    )
    fig.update_traces(fill='toself')
    return fig

def create_scatter_chart(df_merged):
    print("Generando gráfico 4")
    fig = px.scatter(
        df_merged,
        x="WBL INDEX",
        y="Parliament %",
        hover_name="Economy",
        color="Income Group",
        animation_frame="Year",
        animation_group="Economy",
        title="4. Correlación: Ley (WBL) vs. Realidad (% parlamento femenino)",
        range_x=[-5, 105],
        range_y=[-5, 70]
    )
    fig.update_traces(marker=dict(size=10, opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_layout(xaxis_title="WBL INDEX (Igualdad legal 0-100)", yaxis_title="% mujeres en el parlamento")
    return fig