import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from exp8_b import load_data, filter_data, get_summary_stats

st.set_page_config(page_title="Screen Time vs Mental Wellness Survey Data Analysis", layout="wide")

sns.set(style="whitegrid", palette="muted", font_scale=1.1)

st.title("Screen Time vs Mental Wellness Survey Data Analysis")
st.markdown("### Visual Analysis of Stress, Sleep, and Screen Habits")

df = load_data()

st.sidebar.header("🔍 Visualization Filters")
gender_options = ["All"] + list(df["gender"].dropna().unique())
work_mode_options = ["All"] + list(df["work_mode"].dropna().unique())

selected_gender = st.sidebar.selectbox("Select Gender", gender_options)
selected_work_mode = st.sidebar.selectbox("Select Work Mode", work_mode_options)

filtered_df = filter_data(df, selected_gender, selected_work_mode)

stats = get_summary_stats(filtered_df)
st.sidebar.markdown("### 📊 Summary Stats")
for key, value in stats.items():
    st.sidebar.write(f"**{key}:** {value:.2f}")

if st.sidebar.checkbox("Show Raw Data", False):
    st.subheader("📋 Filtered Dataset Preview")
    st.dataframe(filtered_df, use_container_width=True, height=400)

# Line Plot
st.subheader("Stress Level vs Age")
fig1 = plt.figure(figsize=(8,5))
sns.lineplot(x='age', y='stress_level_0_10', data=filtered_df, marker='o', color='royalblue')
plt.title('Stress Level vs Age', fontsize=14, weight='bold')
st.pyplot(fig1)

# Bar Chart
st.subheader("Average Stress Level by Occupation")
fig2 = plt.figure(figsize=(8,5))
sns.barplot(x='occupation', y='stress_level_0_10', data=filtered_df, estimator='mean', ci=None, palette='coolwarm')
plt.title('Average Stress Level by Occupation', fontsize=14, weight='bold')
st.pyplot(fig2)

# Box Plot
st.subheader("Sleep Hours by Occupation")
fig3 = plt.figure(figsize=(8,5))
sns.boxplot(x='occupation', y='sleep_hours', data=filtered_df, palette='pastel')
plt.title('Sleep Hours by Occupation', fontsize=14, weight='bold')
st.pyplot(fig3)

# Pie Chart
st.subheader("Sleep Quality Distribution (1–5)")
fig4 = plt.figure(figsize=(7,7))
sleep_quality_counts = filtered_df['sleep_quality_1_5'].value_counts().sort_index()
colors = sns.color_palette('pastel')[0:5]
plt.pie(
    sleep_quality_counts,
    labels=[f'Quality {i}' for i in sleep_quality_counts.index],
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops={'fontsize': 11}
)
plt.title('Sleep Quality Distribution (1–5)', fontsize=14, weight='bold')
st.pyplot(fig4)

# Scatter Plot
st.subheader("Screen Time vs Mental Wellness Index")
fig5 = plt.figure(figsize=(8,5))
sns.scatterplot(
    x='screen_time_hours',
    y='mental_wellness_index_0_100',
    data=filtered_df,
    color='seagreen',
    s=70,
    alpha=0.7
)
plt.title('Screen Time vs Mental Wellness Index', fontsize=14, weight='bold')
st.pyplot(fig5)

# Histogram
st.subheader("Distribution of Sleep Hours")
fig6 = plt.figure(figsize=(8,5))
sns.histplot(filtered_df['sleep_hours'], bins=10, kde=True, color='mediumorchid')
plt.title('Distribution of Sleep Hours', fontsize=14, weight='bold')
st.pyplot(fig6)
