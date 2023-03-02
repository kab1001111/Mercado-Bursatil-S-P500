import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SP500_df = pd.read_csv('sp_500.csv',index_col=0, parse_dates=True)
sp_500II = pd.read_csv('constituents-financials.csv')
close_prices_tec = pd.read_csv('tecnologia.csv',index_col=0, parse_dates=True)
close_prices_HEALTH = pd.read_csv('health.csv',index_col=0, parse_dates=True)


st.markdown('Evolución del índice S&P500 en los últimos 23 años')

fig = plt.figure(figsize=(8,3))
sns.lineplot(x="Date", y='Close', data=SP500_df)
st.pyplot(fig)

st.markdown('Crecimiento por Sector del SP&500')

fig = plt.figure(figsize=(8,4))
sns.barplot(x="Price", y='Sector', data=sp_500II)
st.pyplot(fig)

st.markdown('Crecimiento Histórico por acciones de Tecnología')

fig = plt.figure(figsize=(8,3))
sns.lineplot(x='Date', y='AAPL', data=close_prices_tec,color='orange')
sns.lineplot(x='Date', y='AMZN', data=close_prices_tec,color='red')
sns.lineplot(x='Date', y='GOOGL', data=close_prices_tec,color='blue')
sns.lineplot(x='Date', y='MSFT', data=close_prices_tec,color='green')
sns.lineplot(x='Date', y='NFLX', data=close_prices_tec,color='gold')
sns.set_style("darkgrid")
plt.title('Comparación de las empresas de Tecnología del S&P500 más grandes')
st.pyplot(fig)


st.markdown('''APPLE-Naranja/ AMAZON-Rojo/ GOOGLE-Azul/ MICROSOFT-Verde/ NETFLIX-Dorado''')

st.markdown('Crecimiento Histórico por acciones de la Salud')
fig = plt.figure(figsize=(8,3))
sns.lineplot(x='Date', y='JNJ', data=close_prices_HEALTH,color='blue')
sns.lineplot(x='Date', y='LLY', data=close_prices_HEALTH,color='green')
sns.lineplot(x='Date', y='MRK', data=close_prices_HEALTH,color='orange')
sns.lineplot(x='Date', y='NVO', data=close_prices_HEALTH,color='red')
sns.set_style("darkgrid")
plt.title('Comparación de las empresas de la salud del S&P500 más grandes')
st.pyplot(fig)

st.markdown('''JNJ-Azul/ LLY-Verde/ MRK-Naranja/ NVO-Rojo''')