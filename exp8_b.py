import pandas as pd

# Load dataset
def load_data():
    return pd.read_csv("ScreevsmentalH.csv")

# Apply filters for gender and work mode
def filter_data(df, gender="All", work_mode="All"):
    filtered_df = df.copy()
    if gender != "All":
        filtered_df = filtered_df[filtered_df["gender"] == gender]
    if work_mode != "All":
        filtered_df = filtered_df[filtered_df["work_mode"] == work_mode]
    return filtered_df

# Optional: Add summary stats function
def get_summary_stats(df):
    return {
        "Average Stress": df["stress_level_0_10"].mean(),
        "Average Sleep Hours": df["sleep_hours"].mean(),
        "Average Wellness Index": df["mental_wellness_index_0_100"].mean()
    }
