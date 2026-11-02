
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# PRODUCTPULSE - PRODUCT ANALYTICS
# ---------------------------------

st.set_page_config(
    page_title="ProductPulse",
    page_icon="📊",
    layout="wide"
)

# Sample dataset (synthetic)
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Active Users": [1200, 1450, 1800, 2100, 2500, 3100],
    "New Users": [300, 350, 420, 480, 550, 700],
    "Revenue": [12000, 14500, 18000, 21000, 25000, 31000],
    "Retention": [65, 68, 70, 73, 76, 80]
}

df = pd.DataFrame(data)

features = pd.DataFrame({
    "Feature": ["Search", "Wishlist", "Recommendations", "Checkout", "Reviews"],
    "Users": [2400, 1600, 2100, 2800, 1100]
})

feedback = pd.DataFrame({
    "Customer": ["User 1", "User 2", "User 3", "User 4", "User 5"],
    "Feedback": [
        "The app is easy to use and fast",
        "Checkout is slow and frustrating",
        "I love the product recommendations",
        "Search results are confusing",
        "Excellent experience, very helpful app"
    ]
})

# Sidebar
st.sidebar.title("📊 ProductPulse")
st.sidebar.caption("Product Intelligence Platform")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "User Analytics", "Feature Performance",
     "Customer Insights", "Feature Prioritisation"]
)

st.sidebar.divider()
st.sidebar.caption("Portfolio project | Synthetic demo data")

# OVERVIEW
if page == "Overview":

    st.title("ProductPulse")
    st.subheader("Product Analytics Dashboard")
    st.write("Make smarter product decisions using data.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Active Users", "3,100", "+24%")
    col2.metric("Monthly Revenue", "₹31,000", "+24%")
    col3.metric("Retention Rate", "80%", "+4 pp")
    col4.metric("New Users", "700", "+27%")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("User Growth")

        fig = px.line(
            df,
            x="Month",
            y="Active Users",
            markers=True,
            title="Monthly Active Users"
        )
        st.plotly_chart(fig, width="stretch")

    with right:
        st.subheader("Revenue Performance")

        fig = px.bar(
            df,
            x="Month",
            y="Revenue",
            title="Monthly Revenue"
        )
        st.plotly_chart(fig, width="stretch")

    st.subheader("Monthly Product Performance")
    st.dataframe(df, width="stretch", hide_index=True)

# USER ANALYTICS
elif page == "User Analytics":

    st.title("User Analytics")
    st.write("Understand how users interact with the product.")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            df,
            x="Month",
            y="New Users",
            title="New User Acquisition"
        )
        st.plotly_chart(fig, width="stretch")

    with col2:
        fig = px.line(
            df,
            x="Month",
            y="Retention",
            markers=True,
            title="User Retention (%)"
        )
        st.plotly_chart(fig, width="stretch")

    st.subheader("User Data")
    st.dataframe(df, width="stretch", hide_index=True)

# FEATURE PERFORMANCE
elif page == "Feature Performance":

    st.title("Feature Performance")
    st.write("Discover which product features attract users.")

    fig = px.bar(
        features.sort_values("Users", ascending=True),
        x="Users",
        y="Feature",
        orientation="h",
        title="Feature Adoption"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("Feature Usage Table")
    st.dataframe(features, width="stretch", hide_index=True)

    st.info(
        "Checkout has the highest usage in this sample. "
        "Further analysis is needed to understand conversion."
    )

# CUSTOMER INSIGHTS
elif page == "Customer Insights":

    st.title("Customer Insights")
    st.write("Explore customer feedback and sentiment.")

    def analyse_sentiment(text):
        text = text.lower()

        positive = [
            "love", "excellent", "easy", "fast",
            "helpful", "great", "good"
        ]

        negative = [
            "slow", "frustrating", "confusing",
            "bad", "difficult", "poor"
        ]

        positive_score = sum(word in text for word in positive)
        negative_score = sum(word in text for word in negative)

        if positive_score > negative_score:
            return "Positive"
        elif negative_score > positive_score:
            return "Negative"
        return "Neutral"

    feedback["Sentiment"] = feedback["Feedback"].apply(
        analyse_sentiment
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Positive",
        len(feedback[feedback["Sentiment"] == "Positive"])
    )
    col2.metric(
        "Negative",
        len(feedback[feedback["Sentiment"] == "Negative"])
    )
    col3.metric(
        "Neutral",
        len(feedback[feedback["Sentiment"] == "Neutral"])
    )

    fig = px.pie(
        feedback,
        names="Sentiment",
        title="Customer Sentiment Distribution"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("Customer Feedback")
    st.dataframe(feedback, width="stretch", hide_index=True)

# FEATURE PRIORITISATION
elif page == "Feature Prioritisation":

    st.title("Feature Prioritisation")
    st.write("Use the RICE framework to rank product ideas.")

    st.caption(
        "RICE = Reach × Impact × Confidence ÷ Effort"
    )

    ideas = pd.DataFrame({
        "Feature": [
            "Improve Search",
            "Faster Checkout",
            "AI Recommendations",
            "Dark Mode"
        ],
        "Reach": [900, 800, 600, 300],
        "Impact": [2, 3, 3, 1],
        "Confidence": [0.9, 0.95, 0.8, 0.9],
        "Effort": [3, 4, 6, 2]
    })

    ideas["RICE Score"] = (
        ideas["Reach"] *
        ideas["Impact"] *
        ideas["Confidence"] /
        ideas["Effort"]
    ).round(2)

    ideas = ideas.sort_values(
        "RICE Score",
        ascending=False
    )

    st.dataframe(
        ideas,
        width="stretch",
        hide_index=True
    )

    fig = px.bar(
        ideas,
        x="Feature",
        y="RICE Score",
        title="Feature Priority Ranking"
    )

    st.plotly_chart(fig, width="stretch")

    st.success(
        "Use RICE scores as a decision-support tool, "
        "not as a replacement for product judgment."
    )

st.divider()

st.caption(
    "ProductPulse | Built with Python, Pandas, Streamlit and Plotly"
)
