import streamlit as st
from vis import *


# Streamlit settings
st.set_page_config(layout = "wide")

'''
# TECKOR Telemetry Tool
'''

col1, col2 = st.columns(2)

altitudeVis = getAltitudeVis()
velocityVis = getVelocityVis()
tempVis = getTempVis()
pressureVis = getPressureVis()

with col1:
    "#### Altitude (m)"
    st.altair_chart(altitudeVis, use_container_width = True)
    r"#### Vertical Velocity (m/s)"
    st.altair_chart(velocityVis, use_container_width = True)

with col2:
    "#### Temperature (°C)"
    st.altair_chart(tempVis, use_container_width = True)
    r"#### Pressure (Pa)"
    st.altair_chart(pressureVis, use_container_width = True)

"#### Raw Flight Data"
st.table(getRawData())
