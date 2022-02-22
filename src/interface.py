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
accelerationVis = getAccelerationVis()

with col1:
    "#### Altitude"
    st.altair_chart(altitudeVis, use_container_width = True)
    r"#### Velocity"
    st.altair_chart(velocityVis, use_container_width = True)

with col2:
    "#### Temperature"
    st.altair_chart(tempVis, use_container_width = True)
    r"#### Acceleration"
    st.altair_chart(accelerationVis, use_container_width = True)

"#### Flight Ground Track"
st.pydeck_chart(getMapVis())

"#### Raw Flight Data"
st.table(getRawData())
