## IMPORT LIBRARIES
import streamlit as st
from sidebar import mysidebar


## -------------------------------------------------------------------------
##  PAGE CONFIGURATION & SETUP
## -------------------------------------------------------------------------

## SET PAGE CONFIGURATION(S)
st.set_page_config(layout="wide", page_title='Forecasting Time Series Data')

## GET STYLE GUIDES
with open ("style.css" ) as css:
        st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
        st.write(f'<style>{css.read()}</style>', unsafe_allow_html=True)

## SET SIDEBAR
mysidebar()


## -------------------------------------------------------------------------
##  THIS IS THE MAIN PAGE
## -------------------------------------------------------------------------
     
# Cusomtize Main Page
st.title('Forecasting Time Series Data') 

st.write('Time series forecasting is a difficult problem with no easy answer. \
          There are countless forecasting models and methods which claim to \
          outperform each other, yet it is never clear which model is truly best.')
            
st.write('This multi-page app provides a comprehensive, beginner friendly guide to help you \
          understand, deploy and tune your very own forecasts so that you \
          can walk away having the best possible forecast in hand.')
          
st.markdown('---')
          
st.header('Forecasting Models')
st.write('It would be impossible to provide exploration into all possible \
         forecasting methods. For that reason, this will focus on the most popular models.')

markdown = """
1. Autoregressive Integrated Moving Average (__ARIMA__) --> *In development*
2. ARIMA with Exogenous Variables (__ARIMAX__) --> In development
3. Seasonal Autoregressive Integrated Moving Average (__SARIMA__) --> *In development*
4. SARIMA with Exogenous Variables (__SARIMAX__) --> *In development*
5. __Holt-Winters__ --> *In development*
6. __Holt-Winters with Exogoneous Variables__ --> *In development*
"""

st.markdown(markdown)


st.write('')
st.write('')
st.write('This is an open-source project created with [Streamlit](https://streamlit.io) \
         and you are very welcome to contribute to the \
         [GitHub repository](https://github.com/bhoyle48/streamlit-projection-app).')
