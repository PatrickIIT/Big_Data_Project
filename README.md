# Big_Data_Project
This project presents a comprehensive analysis of New York City (NYC) Yellow Taxi trip data from January 2015, aimed at uncovering demand patterns, identifying high-traffic zones, and forecasting future taxi trips. An interactive Streamlit dashboard was developed to visualize key trends
# NYC Taxi Data Analytics and Demand Forecasting Dashboard
This repository contains a data science project that analyzes NYC Yellow Taxi trip data from January 2015 to uncover demand patterns, identify high-traffic zones, and forecast future taxi trips using a RandomForestRegressor. An interactive Streamlit dashboard visualizes key insights, enabling stakeholders to explore trends by day and hour.
Project Overview

Objective: Analyze NYC taxi demand, predict trip counts, and provide an interactive dashboard for urban planning and taxi operations.
Dataset: NYC TLC Yellow Taxi Trip Data (Jan 2015) and taxi zone lookup table.
Tools: Python, Pandas, Seaborn, Matplotlib, Scikit-learn, Streamlit.
Model: RandomForestRegressor (R² = 0.947).
Output: Interactive dashboard for real-time insights.

# Prerequisites

Python 3.11
Git
Required libraries (see requirements.txt)

# Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/nyc-taxi-analytics.git
cd nyc-taxi-analytics


# Install Dependencies:
pip install -r requirements.txt


# Download Data:

Obtain the dataset from NYC TLC Trip Record Data.
Place yellow_tripdata_2015-01.parquet and taxi_zone_lookup.csv in the data/raw/ directory.


# Run the Project:

Exploratory Analysis: Open and run notebooks/data_exploration.ipynb.
Model Training: Run python src/model_training.py to train the RandomForestRegressor and save the model.
Dashboard: Launch the Streamlit app:streamlit run src/nyc_taxi_dashboard.py --server.port 8505





Usage

Explore the Jupyter notebooks for data preprocessing, visualization, and modeling steps.
Use the dashboard to filter taxi demand by day and hour, visualizing top pickup zones and hourly trends.
Check outputs/plots/ for generated visualizations and outputs/models/ for the trained model.

Results

Identified major pickup zones (e.g., JFK Airport, Midtown East).
Detected higher tipping trends after 9 PM.
Achieved an R² score of 0.947 with the RandomForestRegressor for demand forecasting.

Challenges

Handled large dataset size (limited to Jan 2015 due to memory constraints).
Resolved Python 3.11 compatibility issues with libraries.
Managed outliers (e.g., negative fares, zero-distance trips).

Future Work

Integrate weather data for improved forecasting.
Add real-time data streams.
Explore deep learning models (e.g., LSTMs).

Contributing
Feel free to fork this repository, submit issues, or create pull requests. Please follow the contribution guidelines (to be added).
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

NYC Taxi & Limousine Commission for providing the dataset.
Streamlit, Scikit-learn, and other open-source communities for their tools.

