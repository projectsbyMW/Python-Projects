import streamlit as sl
import plotly.express as px
from backend import get_data

sl.title("Weather Forecast for the next days")
place = sl.text_input("Place: ")
days = sl.slider("Forecast Days", min_value=1, 
                 max_value= 5, 
                 help= "Select the number of forecasted days")
option = sl.selectbox("Select data to view",("Temperature","Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")

if place:
    #Get data from API
    try:
        filtered_data = get_data(place,days)

        if option == "Temperature":
            dates = [dict["dt_txt"] for dict in filtered_data]
            temperatures = [dict["main"]["temp"]-273 for dict in filtered_data]
            figure = px.line(x = dates, y = temperatures,
                            labels = {"x":"Date","y":"Temperature (C)"})
            sl.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
                    "Rain":"images/rain.png","Snow":"images/snow.png"}
            sky = [dict["weather"][0]["main"] for dict in filtered_data]
            paths = [images[condition] for condition in sky]
            sl.image(paths,width=150)

    except KeyError:
        sl.info("Please Enter a valid place name.")