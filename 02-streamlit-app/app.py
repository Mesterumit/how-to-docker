import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Insights Dashboard",
    page_icon="�",
    layout="wide"
)

st.title("Data Insights Dashboard")
st.markdown("*A containerized Streamlit application for data visualization*")

st.sidebar.header("Configuration")

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=['csv'])

# Use default data if no file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("File uploaded successfully!")
else:
    # Create sample data
    st.sidebar.info("Using sample data. Upload a CSV to analyze your own data.")
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
        'age': [25, 30, 35, 27, 28, 32, 29, 31],
        'city': ['New York', 'San Francisco', 'Chicago', 'Seattle', 'Boston', 'Austin', 'Denver', 'Portland'],
        'score': [85.5, 92.3, 78.9, 88.1, 91.2, 95.7, 82.4, 89.2]
    })

# Display dataset info
st.header("Dataset Overview")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Rows", len(df))

with col2:
    st.metric("Total Columns", len(df.columns))

with col3:
    numeric_cols = df.select_dtypes(include=['number']).columns
    st.metric("Numeric Columns", len(numeric_cols))

# Display raw data
with st.expander("View Raw Data"):
    st.dataframe(df, use_container_width=True)

# Statistical summary
st.header("Statistical Summary")
st.dataframe(df.describe(), use_container_width=True)

# Visualizations
st.header("Visualizations")

# Get numeric columns for plotting
numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

if len(numeric_columns) >= 1:
    tab1, tab2, tab3 = st.tabs(["Distribution", "Comparison", "Correlation"])
    
    with tab1:
        st.subheader("Distribution Plot")
        col_to_plot = st.selectbox("Select column", numeric_columns, key='dist')
        
        fig = px.histogram(
            df, 
            x=col_to_plot,
            nbins=20,
            title=f"Distribution of {col_to_plot}",
            color_discrete_sequence=['#636EFA']
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Column Comparison")
        
        if len(numeric_columns) >= 2:
            col1, col2 = st.columns(2)
            with col1:
                x_col = st.selectbox("X-axis", numeric_columns, key='x')
            with col2:
                y_col = st.selectbox("Y-axis", [c for c in numeric_columns if c != x_col], key='y')
            
            fig = px.scatter(
                df,
                x=x_col,
                y=y_col,
                title=f"{x_col} vs {y_col}",
                color_discrete_sequence=['#EF553B']
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need at least 2 numeric columns for comparison plots.")
    
    with tab3:
        st.subheader("Correlation Heatmap")
        
        if len(numeric_columns) >= 2:
            corr_matrix = df[numeric_columns].corr()
            
            fig = px.imshow(
                corr_matrix,
                text_auto='.2f',
                aspect='auto',
                title="Correlation Matrix",
                color_continuous_scale='RdBu_r'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need at least 2 numeric columns for correlation analysis.")

else:
    st.warning("No numeric columns found in the dataset.")

# Data filtering
st.header("Data Filtering")

if len(numeric_columns) > 0:
    filter_col = st.selectbox("Select column to filter", numeric_columns)
    
    min_val = float(df[filter_col].min())
    max_val = float(df[filter_col].max())
    
    range_val = st.slider(
        f"Filter by {filter_col} range",
        min_value=min_val,
        max_value=max_val,
        value=(min_val, max_val)
    )
    
    filtered_df = df[(df[filter_col] >= range_val[0]) & (df[filter_col] <= range_val[1])]
    
    st.write(f"Showing {len(filtered_df)} of {len(df)} rows")
    st.dataframe(filtered_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
**Tip**: This Streamlit app is running inside a Docker container! 
The container isolates the application and its dependencies, making it portable across any environment.

You can also load data from the course repository by mounting it as a volume when running the container.
""")
