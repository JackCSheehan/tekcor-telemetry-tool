import altair as alt
import pandas as pd

# CSV column names
TIME_FIELD = "time"
TEMP_FIELD = "temp"
ALT_FIELD = "alt"
PRES_FIELD = "pres"
VEL_FIELD = "vel"

# Load/derive data
DATA = pd.read_csv("../data/t.csv")
DIFF_DATA = DATA.diff()
VEL_DATA = DIFF_DATA[ALT_FIELD] / DIFF_DATA[TIME_FIELD]

# Clean data
DATA = DATA.drop(index = 0)
DIFF_DATA = DIFF_DATA.drop(index = 0)
VEL_DATA = VEL_DATA.drop(index = 0)

# Add calculated velocity data to main dataframe
DATA[VEL_FIELD] = VEL_DATA

# Visualizes altitude
def getAltitudeVis():
    altitude = alt.Chart(DATA).mark_line().encode(
        x = alt.X(TIME_FIELD, axis = alt.Axis(title = "time (s)")),
        y = alt.Y(ALT_FIELD, axis = alt.Axis(title = "altitude (m)")),
        tooltip = [TIME_FIELD, ALT_FIELD]
    ).interactive()
    return altitude
    
# Visualizes vertical velocity
def getVelocityVis():
    velocity = alt.Chart(DATA).mark_line().encode(
        x = alt.X(TIME_FIELD, axis = alt.Axis(title = "time (s)")),
        y = alt.Y(VEL_FIELD, axis = alt.Axis(title = "vertical velocity (m/s)")),
        tooltip = [TIME_FIELD, VEL_FIELD]
    ).interactive()

    return velocity

# Visualizes temperature
def getTempVis():
    temp = alt.Chart(DATA).mark_line().encode(
        x = alt.X(TIME_FIELD, axis = alt.Axis(title = "time (s)")),
        y = alt.Y(TEMP_FIELD, axis = alt.Axis(title = "temperature (°C)")),
        tooltip = [TIME_FIELD, TEMP_FIELD]
    ).interactive()
    return temp

# Visualizes pressure
def getPressureVis():
    pres = alt.Chart(DATA).mark_line().encode(
        x = alt.X(TIME_FIELD, axis = alt.Axis(title = "time (s)")),
        y = alt.Y(PRES_FIELD, axis = alt.Axis(title = "pressure (pa)")),
        tooltip = [TIME_FIELD, PRES_FIELD]
    ).interactive()
    return pres

def getRawData():
    return DATA