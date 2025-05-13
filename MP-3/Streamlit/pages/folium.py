import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# -------------------------
# Load Data
# -------------------------
st.title("🎤 Eurovision Ranking Map")

uploaded_file = st.file_uploader("Upload your Eurovision CSV", type="csv")
if not uploaded_file:
    st.stop()

df = pd.read_csv(uploaded_file)

# -------------------------
# Country Coordinates (expand as needed)
# -------------------------
country_coords = {
    "Albania": [41.3275, 19.8189],
    "Andorra": [42.5078, 1.5211],
    "Armenia": [40.1792, 44.4991],
    "Australia": [-35.2809, 149.1300],
    "Austria": [48.2082, 16.3738],
    "Azerbaijan": [40.4093, 49.8671],
    "Belarus": [53.9006, 27.5590],
    "Belgium": [50.8503, 4.3517],
    "Bosnia and Herzegovina": [43.8563, 18.4131],
    "Bulgaria": [42.6977, 23.3219],
    "Croatia": [45.8150, 15.9819],
    "Cyprus": [35.1856, 33.3823],
    "Czech Republic": [50.0755, 14.4378],
    "Denmark": [55.6761, 12.5683],
    "Estonia": [59.4370, 24.7536],
    "Finland": [60.1695, 24.9354],
    "France": [48.8566, 2.3522],
    "Georgia": [41.7151, 44.8271],
    "Germany": [52.5200, 13.4050],
    "Greece": [37.9838, 23.7275],
    "Hungary": [47.4979, 19.0402],
    "Iceland": [64.1355, -21.8954],
    "Ireland": [53.3498, -6.2603],
    "Israel": [31.7683, 35.2137],
    "Italy": [41.9028, 12.4964],
    "Latvia": [56.9496, 24.1052],
    "Lithuania": [54.6872, 25.2797],
    "Luxembourg": [49.6117, 6.1319],
    "Malta": [35.8997, 14.5146],
    "Moldova": [47.0105, 28.8638],
    "Monaco": [43.7384, 7.4246],
    "Montenegro": [42.4304, 19.2594],
    "Netherlands": [52.3676, 4.9041],
    "North Macedonia": [41.9981, 21.4254],
    "Norway": [59.9139, 10.7522],
    "Poland": [52.2297, 21.0122],
    "Portugal": [38.7169, -9.1399],
    "Romania": [44.4268, 26.1025],
    "Russia": [55.7558, 37.6173],
    "San Marino": [43.9333, 12.4500],
    "Serbia": [44.7866, 20.4489],
    "Slovakia": [48.1486, 17.1077],
    "Slovenia": [46.0569, 14.5058],
    "Spain": [40.4168, -3.7038],
    "Sweden": [59.3293, 18.0686],
    "Switzerland": [46.9481, 7.4474],
    "Turkey": [39.9208, 32.8541],
    "Ukraine": [50.4501, 30.5234],
    "United Kingdom": [51.5074, -0.1278],
    "Yugoslavia": [44.7866, 20.4489]
    # Add more countries as needed
}

# -------------------------
# UI Controls
# -------------------------
year = st.selectbox("Select year", sorted(df["year"].unique(), reverse=True))
max_rank = st.slider("Show countries ranked up to place:", min_value=1, max_value=26, value=10)

# -------------------------
# Filter Data
# -------------------------
filtered_df = df[(df["year"] == year) & (df["final_place"] <= max_rank)]

# -------------------------
# Build Map
# -------------------------
m = folium.Map(location=[54, 15], zoom_start=4)

# Add markers for each country
for _, row in filtered_df.iterrows():
    country = row["country"]
    if country in country_coords:
        folium.Marker(
            location=country_coords[country],
            popup=f"{country} (Place: {row['final_place']})",
            icon=folium.Icon(color="blue")
        ).add_to(m)

folium_static(m)
