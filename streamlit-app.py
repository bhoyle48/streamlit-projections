import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
import time


st.title('This is my first application')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

iris = datasets.load_iris()

d = pd.DataFrame(data=iris.data, columns=iris.feature_names)

data = d
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


st.subheader('Raw Iris Data')
st.write(data)
