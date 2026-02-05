import pandas as pd
import streamlit as st
from sqlalchemy import text
from db import get_engine
from queries import queries

st.set_page_config(page_title = "National Parks Data Dashboard", layout = "wide")

@st.cache_data(ttl=300)
def run_query(sql: str) -> pd.DataFrame:
    engine = get_engine()
    return pd.read_sql(text(sql), engine)

st.title("National Parks - Species & Biodiversity Dashboard")

#sideBar contents
st.sidebar.header("Controls")

selected_key = st.sidebar.selectbox(
    "Choose Analysis",
    options = list(queries.keys()),
    format_func = lambda k: f"{k}. {queries[k][0]}",
)

row_limit = st.sidebar.selectbox(
    "Rows to Show",
    options = [10, 25, 50, 100, 250, 1000, "All"],
    index = 1,
)

name, sql = queries[selected_key]

st.subheader(name)

with st.expander("Show SQL"):
    st.code(sql, language="sql")
df = run_query(sql)

#Display Controls
if df.shape == (1, 1):
    st.metric(label = name, value=df.iloc[0,0])
else:
    show_df = df if row_limit == "All" else df.head(int(row_limit))
    st.dataframe(show_df, width="stretch")

    numeric_cols = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
    non_numeric_cols = [c for c in df.columns if c not in numeric_cols]

    if numeric_cols and non_numeric_cols:
        x = non_numeric_cols[0]
        y = numeric_cols[0]
        chart_df = df[[x , y]].copy()

        if len(chart_df) > 25:
                chart_df = chart_df.sort_values(y, ascending=False).head(20)

        st.bar_chart(chart_df.set_index(x)[y])

    st.download_button(
        "Download CSV",
        df.to_csv(index= False).encode("utf-8"),
        file_name=f"{name.replace(' ', '_').lower()}.csv",
        mime="text/csv",
    )        




