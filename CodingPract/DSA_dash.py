# import streamlit as st
# from pymongo import MongoClient
# import pandas as pd
# import dash
# from dash import dcc, html
# import plotly.express as px

# # MongoDB connection
# client = MongoClient('mongodb://localhost:27017/')
# db = client['DSA_code_app_db']
# collection = db['submissions']

# # Function to fetch data based on username
# def fetch_data(username):
#     query = {"username": username}
#     cursor = collection.find(query)
#     data = list(cursor)
#     return pd.DataFrame(data)

# st.header("DSA Submission Overview")

# # Streamlit input for username
# username = st.text_input("Enter Username")

# if username:
#     # Fetch data based on the input username
#     df = fetch_data(username)

#     # Display the dataframe (optional for testing)
#     # st.write(df)

#     # Calculate submission counts
#     submission_count = len(df)
#     st.write(f"Total Submissions: {submission_count}")

#     # Date-wise submission counts
#     df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert timestamp to datetime
#     df['date'] = df['timestamp'].dt.date  # Extract the date (ignoring time)

#     # Count submissions per date
#     date_counts = df['date'].value_counts().sort_index().reset_index()
#     date_counts.columns = ['Date', 'Submission Count']

#     st.write("Submissions Date-wise:")
#     # Use line chart instead of bar chart for date-wise submissions
#     submission_date_chart = px.line(date_counts, x="Date", y="Submission Count", 
#                                     title="Submissions Date-wise", markers=True)
#     submission_date_chart.update_layout(xaxis_tickangle=45)  # Horizontal x-axis labels
#     st.plotly_chart(submission_date_chart)

#     # Difficulty-wise submissions (pie chart)
#     difficulty_counts = df['difficulty'].value_counts().reset_index()
#     difficulty_counts.columns = ['Difficulty', 'Count']
#     st.write("Difficulty-wise Submissions:")
#     st.plotly_chart(px.pie(difficulty_counts, names='Difficulty', values='Count', title='Difficulty-wise Submissions'))

#     # Topic-wise submissions (bar chart)
#     topic_counts = df.explode('topics')['topics'].value_counts().reset_index()
#     topic_counts.columns = ['Topic', 'Count']
#     st.write("Topic-wise Submissions:")
#     topic_bar_chart = px.bar(topic_counts, x="Topic", y="Count", title="Topic-wise Submissions")
#     topic_bar_chart.update_layout(xaxis_tickangle=0)  # Horizontal x-axis labels
#     st.plotly_chart(topic_bar_chart)

#     # Coding language used (pie chart)
#     coding_lang_counts = df['coding_lang'].value_counts().reset_index()
#     coding_lang_counts.columns = ['Coding Language', 'Count']
#     st.write("Coding Language Used:")
#     st.plotly_chart(px.pie(coding_lang_counts, names='Coding Language', values='Count', title='Coding Language Used'))

#     # Create a Dash app instance
#     app = dash.Dash(__name__)

#     # Build the layout for the Dash dashboard
#     app.layout = html.Div([
#         html.H1(f"Dashboard for {username}"),
#         dcc.Graph(
#             id="submission_date_graph",
#             figure=submission_date_chart  # Include the date-wise submission graph
#         ),
#         dcc.Graph(
#             id="difficulty_pie_chart",
#             figure=px.pie(difficulty_counts, names='Difficulty', values='Count', title='Difficulty-wise Submissions')
#         ),
#         dcc.Graph(
#             id="topic_bar_chart",
#             figure=px.bar(topic_counts, x="Topic", y="Count", title="Topic-wise Submissions")
#         ),
#         dcc.Graph(
#             id="coding_lang_pie_chart",
#             figure=px.pie(coding_lang_counts, names='Coding Language', values='Count', title='Coding Language Used')
#         )
#     ])

#     # Run the Dash app inside Streamlit
#     app.run_server(debug=False, use_reloader=False, port=8051)
#===========================================================================
# import streamlit as st
# from pymongo import MongoClient
# import pandas as pd
# import plotly.express as px

# # ------------------ MongoDB connection ------------------
# client = MongoClient("mongodb://localhost:27017/")
# db = client["DSA_code_app_db"]
# collection = db["submissions"]

# # ------------------ Helper function ------------------
# def fetch_data(username):
#     data = list(collection.find({"username": username}))
#     return pd.DataFrame(data)

# # ------------------ UI ------------------
# st.set_page_config(page_title="DSA Submission Overview", layout="wide")
# st.header("📊 DSA Submission Overview")

# username = st.text_input("Enter Username")

# # ------------------ Guard: username ------------------
# if not username:
#     st.info("Please enter a username to view analytics.")
#     st.stop()

# # ------------------ Fetch data ------------------
# df = fetch_data(username)

# if df.empty:
#     st.warning("No submissions found for this user.")
#     st.stop()

# # ------------------ Guard: timestamp ------------------
# if "timestamp" not in df.columns:
#     st.error("❌ 'timestamp' field missing in database submissions.")
#     st.stop()

# # ------------------ Data preparation ------------------
# df["timestamp"] = pd.to_datetime(df["timestamp"])
# df["date"] = df["timestamp"].dt.date

# st.success(f"Total Submissions: {len(df)}")

# # ------------------ Date-wise submissions ------------------
# date_counts = (
#     df["date"]
#     .value_counts()
#     .sort_index()
#     .reset_index()
# )
# date_counts.columns = ["Date", "Submission Count"]

# st.subheader("📅 Submissions Date-wise")
# fig_date = px.line(
#     date_counts,
#     x="Date",
#     y="Submission Count",
#     markers=True
# )
# st.plotly_chart(fig_date, use_container_width=True)

# # ------------------ Difficulty-wise ------------------
# if "difficulty" in df.columns:
#     st.subheader("📌 Difficulty-wise Submissions")
#     diff_counts = df["difficulty"].value_counts().reset_index()
#     diff_counts.columns = ["Difficulty", "Count"]
#     st.plotly_chart(
#         px.pie(diff_counts, names="Difficulty", values="Count"),
#         use_container_width=True
#     )

# # ------------------ Topic-wise ------------------
# if "topics" in df.columns:
#     st.subheader("📚 Topic-wise Submissions")
#     topic_counts = (
#         df.explode("topics")["topics"]
#         .value_counts()
#         .reset_index()
#     )
#     topic_counts.columns = ["Topic", "Count"]
#     st.plotly_chart(
#         px.bar(topic_counts, x="Topic", y="Count"),
#         use_container_width=True
#     )

# # ------------------ Coding language ------------------
# if "coding_lang" in df.columns:
#     st.subheader("💻 Coding Language Usage")
#     lang_counts = df["coding_lang"].value_counts().reset_index()
#     lang_counts.columns = ["Language", "Count"]
#     st.plotly_chart(
#         px.pie(lang_counts, names="Language", values="Count"),
#         use_container_width=True
#     )
# ===========================================================================
import streamlit as st
from pymongo import MongoClient
import pandas as pd
import plotly.express as px

# -----------------------------
# MongoDB Connection
# -----------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["DSA_code_app_db"]
collection = db["submissions"]

# -----------------------------
# Helper Function
# -----------------------------
def fetch_data(username):
    data = list(collection.find({"username": username}))
    if not data:
        return pd.DataFrame()
    return pd.DataFrame(data)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="DSA Submission Overview", layout="wide")
st.title("📊 DSA Submission Overview")

username = st.text_input("Enter Username")

if not username:
    st.info("Please enter your username to view submissions.")
    st.stop()

df = fetch_data(username)

# -----------------------------
# Total Submissions
# -----------------------------
st.subheader("Overview")
st.write(f"**Total Submissions:** {len(df)}")

if df.empty:
    st.warning("No submissions found for this user.")
    st.stop()

# -----------------------------
# Timestamp Handling
# -----------------------------
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
else:
    df["timestamp"] = pd.Timestamp.now()

df["date"] = df["timestamp"].dt.date

# -----------------------------
# Date-wise Submissions
# -----------------------------
st.subheader("📅 Submissions Date-wise")

date_counts = df["date"].value_counts().sort_index().reset_index()
date_counts.columns = ["Date", "Submission Count"]

st.plotly_chart(
    px.line(
        date_counts,
        x="Date",
        y="Submission Count",
        markers=True,
        title="Submissions Over Time"
    ),
    use_container_width=True
)

# -----------------------------
# Difficulty-wise Submissions
# -----------------------------
st.subheader("🎯 Difficulty-wise Submissions")

if "difficulty" in df.columns:
    difficulty_counts = df["difficulty"].value_counts().reset_index()
    difficulty_counts.columns = ["Difficulty", "Count"]

    st.plotly_chart(
        px.pie(
            difficulty_counts,
            names="Difficulty",
            values="Count",
            title="Difficulty Distribution"
        ),
        use_container_width=True
    )
else:
    st.info("No difficulty data available.")

# -----------------------------
# Topic-wise Submissions
# -----------------------------
st.subheader("🧩 Topic-wise Submissions")

if "topics" in df.columns:
    topic_counts = (
        df.explode("topics")["topics"]
        .value_counts()
        .reset_index()
    )
    topic_counts.columns = ["Topic", "Count"]

    st.plotly_chart(
        px.bar(
            topic_counts,
            x="Topic",
            y="Count",
            title="Topic Distribution"
        ),
        use_container_width=True
    )
else:
    st.info("No topic data available.")

# -----------------------------
# Coding Language Used
# -----------------------------
st.subheader("💻 Coding Language Usage")

if "coding_lang" in df.columns:
    coding_lang_counts = df["coding_lang"].value_counts().reset_index()
    coding_lang_counts.columns = ["Coding Language", "Count"]

    st.plotly_chart(
        px.pie(
            coding_lang_counts,
            names="Coding Language",
            values="Count",
            title="Languages Used"
        ),
        use_container_width=True
    )
else:
    st.info("No coding language data available.")

