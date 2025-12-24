# Práctica II: Visualización de datos
### Igualdad de Género: Ley vs. Realidad (1971-2024)

Este proyecto analiza la brecha entre la igualdad de jure (lo que dicen las leyes) y la igualdad de facto (la realidad observable) en el ámbito del empoderamiento femenino a nivel global. A través de un dashboard interactivo, se explora si las reformas legales realmente se traducen en una mayor participación de las mujeres en espacios de toma de decisiones.

## Descripción

El análisis se articula en torno a dos dimensiones fundamentales:

1. Dimensión Legal: Utiliza el índice Women, Business and the Law (WBL) del Banco Mundial, que mide cómo las leyes afectan la autonomía económica de las mujeres en 190 economías.
   
2. Dimensión Práctica: Utiliza la proporción de escaños ocupados por mujeres en los parlamentos nacionales como indicador de empoderamiento real.

Preguntas clave:

- ¿Cómo ha evolucionado la igualdad legal en el mundo? (Mapa coroplético animado).

- ¿Qué regiones progresan más rápido? (Gráfico de líneas temporal).

- ¿En qué leyes fallan los países con notas bajas? (Gráfico de radar comparativo por sectores).

- ¿Se traducen las buenas leyes en una realidad igualitaria? ¿Y cómo afecta el nivel de ingresos (Income Group) a esta relación? (Gráfico de dispersión animado).

## Estructura del proyecto

```
Práctica_II/
├── data/
│   ├── API_SG.GEN.PARL.ZS_...csv       # Datos de representación parlamentaria 
│   └── WBL2024-1-0-Historical...xlsx    # Panel histórico de leyes (1971-2024) [cite: 18]
├── src/
│   ├── __init__.py
│   ├── chart_generator.py              # Lógica de creación de gráficos Plotly
│   ├── data_loader.py                  # Pipeline de carga y limpieza (ETL)
│   └── report_generator.py             # Generador del dashboard HTML
├── main.py                             # Script principal de ejecución
├── index.html                          # Dashboard interactivo final
├── requirements.txt                    # Dependencias del proyecto
└── README.md                           # Documentación
```

## Instalación y ejecución

1. Clonar el repositorio.
2. Instalación de dependencias.
3. Ejecutación del script princiapl `main.py`.
4. Abrir el archivo `index.html` en la raíz del proyecto que contiene el dashboard completo.

## Origen de los datasets:
- Dataset principal: Women, Business and the Law (WBL) 1971-2024 (Banco Mundial).

- Dataset Secundario: Proportion of seats held by women in national parliaments (%) (Banco Mundial).

# Autoría
- Carmen Travel Alarcón 

- Visualización de Datos (M2.859) del Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC) 2025/2026

## Licencia
Este proyecto se distribuye bajo la Licencia MIT. Los datos pertenecen al Banco Mundial.
