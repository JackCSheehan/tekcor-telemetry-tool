# TEKCOR at UT Dallas Model Rocket Telemetry Visualization Tool
## Overview
TEKCOR is a division of AIAA at UT Dallas. TEKCOR is a student-led program to build and fly a model rocket from scratch. The rocket is powered by a class H model rocket motor and flies with a small electronics payload designed to collect telemetry data during the flight. This repository contains the code needed to visualize all of the telemetry data written by the electronics payload during the flight. The visualization tool is driven by [Streamlit](https://streamlit.io/), [Altair](https://altair-viz.github.io/), and [Pandas](https://pandas.pydata.org/).

During the flight, the [TEKCOR Telemetry Computer](https://github.com/JackCSheehan/tekcor-telemetry-computer) collects the telemetry data and writes it to a .csv file so that it can be analyzed and visualized by this tool.
