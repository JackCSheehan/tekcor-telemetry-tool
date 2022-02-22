import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk

DATA = pd.read_csv("../data/telem.csv")

def getAltitudeVis():
    altitude = alt.Chart(DATA).mark_line().encode(
        x = alt.X("time", axis = alt.Axis(title = "time (s)")),
        y = alt.Y("altitude", axis = alt.Axis(title = "altitude (m)")),
        tooltip = ["time", "altitude"]
    ).interactive()
    return altitude
    
def getVelocityVis():
    velocity = alt.Chart(DATA).mark_line().encode(
        x = alt.X("time", axis = alt.Axis(title = "time (s)")),
        y = alt.Y("velocity", axis = alt.Axis(title = "velocity (m/s)")),
        tooltip = ["time", "velocity"]
    ).interactive()
    return velocity

def getAccelerationVis():
    acceleration = alt.Chart(DATA).mark_line().encode(
        x = alt.X("time", axis = alt.Axis(title = "time (s)")),
        y = alt.Y("acceleration", axis = alt.Axis(title = "acceleration (m/s²)")),
        tooltip = ["time", "acceleration"]
    ).interactive()
    return acceleration

def getTempVis():
    temp = alt.Chart(DATA).mark_line().encode(
        x = alt.X("time", axis = alt.Axis(title = "time (s)")),
        y = alt.Y("temperature", axis = alt.Axis(title = "temperature (°C)")),
        tooltip = ["time", "temperature"]
    ).interactive()
    return temp

# Generates PyDeck visualization of flight and returns as a PyDeck plot
def getMapVis():
    pointLayer = pdk.Layer(
        "ScatterplotLayer",
        data = DATA,
        get_position = ["lat", "lon"],
        get_color = [255, 0, 0],
        radius_scale = 20,
        get_line_width = 50,
        get_radius = 60,
    )

    return pdk.Deck(pointLayer, map_provider = "mapbox", map_style = pdk.map_styles.SATELLITE)

def getRawData():
    return DATA