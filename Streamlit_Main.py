import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
import statsmodels.api as sm
import plotly.graph_objects as go
from streamlit_lottie import st_lottie  
from datetime import date, timedelta
import json



#make page-layout wide
st.set_page_config(layout="wide")


#function to import animation
def load_Animationfile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# Sidebar
start_date = st.sidebar.date_input('Start Date', date(2023, 1, 1))
end_date = st.sidebar.date_input('End Date', date(2023, 12, 31))
ticker_lst = ["AMZN","AAPL", "GOOG", "GOOGL", "META", "TSLA", "NVDA", "ADBE", "PYPL", "INTC", "CMCSA", "NFLX", "PEP"]
ticker = st.sidebar.selectbox("Select the Company", ticker_lst)
with st.sidebar:
    Animation_sidebar= load_Animationfile("Animations/sidebarAnimation.json")
    st_lottie(
        
    Animation_sidebar,
    speed=1,
    reverse=False,
    loop=True,
    quality="medium", # medium ; high
    height='400px',
    width='250px',
    key=None,
)




    



# Top headings 
st.markdown("<div style='margin-left: 180px; margin-right: 150px '><h1>Real-Time Stock Forecasting 📈</h1></div>", unsafe_allow_html=True)
st.markdown("<div style='margin-left: 180px; margin-right: 180px; margin-bottom: 0px'><h3 style='  font-style: italic; font-size:20px'>Real-time stock forecasting with customizable date range selection and intuitive future value visualization for informed decisions.</h3></div>", unsafe_allow_html=True)
st.markdown("<div style='margin-left: 180px; margin-right: 180px; margin-top: 0px'; margin-bottom: 0px'><hr style='border: 1px solid #3BB9B1;'></div>", unsafe_allow_html=True)


#starting Animation
Animation_1= load_Animationfile("Animations/Animation1.json")
st_lottie(
    Animation_1,
    speed=1,
    reverse=False,
    loop=True,
    quality="medium", # medium ; high
    height='500px',
    width='1000px',
    key=None,
)




st.markdown("""
    <div style='display: flex; justify-content: center; align-items: center; margin-bottom:80px'>
        <div>
            <h1 style='font-size: 50px;'>Fetching data </h1>
        </div>
    </div>
""", unsafe_allow_html=True)


# Fetching data
data = yf.download(ticker, start_date, end_date)
data.insert(0, "Date", data.index, True)
data.reset_index(drop=True, inplace=True)


#disply data
col1, col2 = st.columns([3, 3])

# Display the first component in the first column
with col1:
    st.markdown('<div class="stDataFrame"><div class="text" style="font-size: 20px;">Data from {} to {}</div></div>'.format(start_date, end_date), unsafe_allow_html=True)
    st.write(data)

# Display the second component in the second column
with col2:
    Animation_2= load_Animationfile("Animations/Animation2.json")
    st_lottie(
        Animation_2,
        speed=1,
        reverse=False,
        loop=True,
        quality="medium", # medium ; high
        height='500px',
        width='700px',
        key=None,
    )
    
    
    
    

# Data visualization
st.header("Data Visualization")
st.subheader("Plot of Data")
plot = px.line(data, x='Date', y=data.columns, title='Price of Stock')
plot.update_layout(height=600, width=800)  # Adjust height and width as needed
st.plotly_chart(plot, use_container_width=True)



# Select column for forecasting
st.header("Select Column for Forecasting")
st.markdown("""<style>.css-2b097c-container {width:80% !important;}</style>""", unsafe_allow_html=True)
column = st.selectbox("Select Column", data.columns[1:])
data = data[['Date', column]]


#disply selected column
col2_1, col2_2 = st.columns([3, 3])

with col2_1:
    st.write(data)

# Display the second component in the second column
with col2_2:
    Animation_3= load_Animationfile("Animations/Animation3.json")
    st_lottie(
        Animation_3,
        speed=1,
        reverse=False,
        loop=True,
        quality="medium", # medium ; high
        height='400px',
        width='500px',
        key=None,
    )
    


# Parameters for model
p = st.slider('Select the value of p', 0, 5, 2)
d = st.slider('Select the value of d', 0, 5, 1)
q = st.slider('Select the value of q', 0, 5, 2)
seasonal_order = st.number_input('Select the value of seasonal period', 0, 24, 12)



#We are using SARIMAX model b/c data is seasonal
# model fitting
model = sm.tsa.statespace.SARIMAX(data[column], order=(p, d, q), seasonal_order=(p, d, q, seasonal_order))
model = model.fit()


# Display model summary
st.header("Model Summary")
st.write(model.summary())




# Forecasting
st.header("Select Forecasting Days")
forecast_period = st.number_input('Select the number of days to forecast', 1, 365, 10)
prediction = model.get_prediction(start=len(data), end=len(data) + forecast_period)
prediction = prediction.predicted_mean
prediction.index = pd.date_range(start=end_date, periods=len(prediction), freq='D')
prediction = pd.DataFrame(prediction)
prediction.insert(0, 'Date', prediction.index, True)



#disply predicted values
col3_1, col3_2 = st.columns([3, 3])

with col3_1:
    st.write("Predictions", prediction)

# Display the second component in the second column
with col3_2:
    Animation_4= load_Animationfile("Animations/Animation4.json")
    st_lottie(
        Animation_4,
        speed=1,
        reverse=False,
        loop=True,
        quality="medium", # medium ; high
        height='400px',
        width='500px',
        key=None,
    )
    
    


# Actual vs Predicted plot
st.header("Actual & Predicted")
fig = go.Figure()
fig.add_trace(go.Scatter(x=data["Date"], y=data[column], mode='lines', name='Actual', line=dict(color='#2ECC71')))
fig.add_trace(go.Scatter(x=prediction["Date"], y=prediction['predicted_mean'], mode='lines', name='Predicted', line=dict(color='#F09E1F')))
fig.update_layout(xaxis_title='Date', yaxis_title='Price', width=1000, height=800)
st.plotly_chart(fig)


#disply buttons
disply_plots = False
if st.button('Display Seperate Plot'):
    if not disply_plots:
        st.write(px.line(x=data["Date"], y=data[column], title='Actual', height=600, width=1000).update_traces(line_color='#2ECC71'))
        st.write(px.line(x=prediction["Date"], y=prediction['predicted_mean'], title='Predicted', height=800, width=1000).update_traces(line_color='#F09E1F'))

        disply_plots = True
    else:
        disply_plots = False


#hide button
hide_plots = False
if st.button('Hide Plots'):
    if not hide_plots:
        hide_plots = True
    else:
        hide_plots = False
        