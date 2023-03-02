import streamlit as st
from PIL import Image


image = Image.open('./images/bursatil_image.jpg')
st.image(image, None)

st.title('Recomendación para la Inversión en el Mercado Bursatil con Base al S&P500') 
st.markdown('## Por. Bernardo Mantilla')
st.markdown('### nzberman@gmail.com')


st.markdown('***')

st.sidebar.markdown('## Introducción al mercado de Capitales')
st.sidebar.markdown('## Qué es el índice S&P500?')
st.sidebar.markdown('## Sectores de Interes')
st.sidebar.markdown('## Que es un KPI de Rendimiento?')


st.markdown('## ¿Qué es el S&P500 y para qué sirve?')
st.markdown('''El índice S&P 500 es un índice bursátil que mide el desempeño de las 500 mayores empresas que cotizan en bolsa en los Estados Unidos. El índice se compone de empresas de diversos sectores, incluyendo tecnología, finanzas, salud, energía y más, y se considera una medida amplia del mercado de valores estadounidense.''')
st.markdown('''El S&P 500 es ampliamente seguido por inversores, analistas y medios de comunicación como un indicador de la salud y el rendimiento del mercado de valores de los Estados Unidos. Los cambios en el valor del índice pueden reflejar las tendencias económicas y políticas, así como el desempeño de las empresas que lo componen.''')


st.markdown('## Sectores de Interes')


image = Image.open('./images/sectores.png')
st.image(image, None)

st.markdown('''Sector Informática-Tecnología''')


image = Image.open('./images/health1.png')
st.image(image, None)

st.markdown('''Sector Salud ''')

image = Image.open('./images/health.png')
st.image(image, None)



st.markdown('## ¿Qué es un KPI de rendimiento?')
st.markdown('''Los KPI (Key Performance Indicators) o indicadores clave de rendimiento son una herramienta importante para medir el éxito y el progreso de una inversión. Aquí hay algunos ejemplos de KPI comúnmente utilizados en el ámbito de las inversiones:
Retorno sobre la inversión.''' )
st.markdown(''' ROI:  Este KPI mide el rendimiento financiero de una inversión en términos de la cantidad de dinero que se ganó o perdió en relación con la cantidad invertida.''')

image = Image.open('./images/Roi.png')
st.image(image, None)

st.markdown('## Objetivo: Superior al 2.2 por ciento anual de rentabilidad')
