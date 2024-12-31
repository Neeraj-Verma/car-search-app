import streamlit as st
import requests
import pandas as pd
import xml.etree.ElementTree as ET

# Function to convert DataFrame to XML
def dataframe_to_xml(df):
    root = ET.Element("cars")
    for _, row in df.iterrows():
        car_elem = ET.SubElement(root, "car")
        for col_name in df.columns:
            ET.SubElement(car_elem, col_name).text = str(row[col_name])
    return ET.tostring(root, encoding="unicode")

# Streamlit App
st.title("Car Search Application")

st.sidebar.header("Filter Criteria")
length = st.sidebar.number_input("Length (meters)", min_value=4.2, max_value=4.7, step=0.1, format="%.1f")
weight = st.sidebar.number_input("Weight (kg)", min_value=1200, max_value=2200, step=200)
velocity = st.sidebar.number_input("Velocity (km/h)", min_value=120, max_value=170, step=10)
color = st.sidebar.selectbox(
    "Select a Color",
    options=["", "red", "blue", "green", "black", "white", "yellow"],
    format_func=lambda x: "Choose a color" if x == "" else x
)

# Search button
if st.sidebar.button("Search"):
    query_url = "http://127.0.0.1:8000/search_cars"
    params = {
        "length": length if length > 0 else None,
        "weight": weight if weight > 0 else None,
        "velocity": velocity if velocity > 0 else None,
        "color": color.strip() if color else None,
    }

    response = requests.get(query_url, params=params)
    if response.status_code == 200:
        data = response.json()["cars"]
        if data:
            df = pd.DataFrame(data)
            st.success(f"Found {len(data)} car(s) matching the criteria.")
            st.dataframe(df)

            # Convert DataFrame to XML
            xml_data = dataframe_to_xml(df)

            # Add a download button for XML
            st.download_button(
                label="Download Results as XML",
                data=xml_data,
                file_name="search_results.xml",
                mime="application/xml"
            )
        else:
            st.warning("No cars found matching the criteria.")
    else:
        st.error("Failed to retrieve data from the API.")

# View All Cars button
if st.sidebar.button("View All Cars"):
    query_url = "http://127.0.0.1:8000/all_cars"
    response = requests.get(query_url)
    if response.status_code == 200:
        data = response.json()["cars"]
        df = pd.DataFrame(data)
        st.dataframe(df)

        # Convert DataFrame to XML
        xml_data = dataframe_to_xml(df)

        # Add a download button for XML
        st.download_button(
            label="Download All Cars as XML",
            data=xml_data,
            file_name="all_cars.xml",
            mime="application/xml"
        )
    else:
        st.error("Failed to retrieve all cars.")
