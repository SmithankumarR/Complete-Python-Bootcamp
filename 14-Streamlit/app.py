import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello Streamlit, i am developing a simple web application using streamlit")

## Diplay a Simple Text
st.write("This is my first web application using streamlit")

# ##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Display the Dataframe
st.write("Here is the dataframe created using pandas library")
st.write(df)


# ##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['name','party','category']
)
st.line_chart(chart_data)