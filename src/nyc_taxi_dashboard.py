import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="NYC Yellow Taxi Analytics", layout="wide")

st.title("🚕 NYC Yellow Taxi Data Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_parquet("yellow_tripdata_2015-01.parquet")
    zones = pd.read_csv("taxi_zone_lookup.csv")
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_day'] = df['tpep_pickup_datetime'].dt.day_name()
    df = df.merge(zones, left_on="PULocationID", right_on="LocationID", how="left")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter")
selected_day = st.sidebar.selectbox("Select Day of Week", options=df['pickup_day'].unique())
selected_hour = st.sidebar.slider("Select Hour", 0, 23)

filtered_df = df[(df['pickup_day'] == selected_day) & (df['pickup_hour'] == selected_hour)]

# Visuals
st.subheader(f"Pickups on {selected_day} at {selected_hour}:00")

col1, col2 = st.columns(2)

with col1:
    top_zones = filtered_df['Zone'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(y=top_zones.index, x=top_zones.values, ax=ax)
    ax.set_title("Top Pickup Zones")
    st.pyplot(fig)

with col2:
    fig2, ax2 = plt.subplots()
    sns.histplot(df['pickup_hour'], bins=24, ax=ax2, color='orange')
    ax2.set_title("Hourly Pickup Distribution (All Days)")
    st.pyplot(fig2)

st.markdown("Built by Patrick Vincent. Supervised by Dr. Innocent Nyalala. © IIT Madras Zanzibar 2025 • Powered by Open NYC Taxi Data")
