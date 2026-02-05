# National Parks Biodiversity Dashboard

Interactive data analytics dashboard built with Streamlit and SQL to explore biodiveristy trends across the U.S. National Parks using a MySQL database.

## Features
- Prebuilt analytical SQL queries selectable via UI
- KPI metrics for aggregate statistics 
- Automatic visualization for park-level results
- CSV export for downstream analysis

## Tech Stack
- Python (pandas, SQLAlchemy)
- MySQL
- Streamlit
- Docker (database)

## Project Structure
- app/ -> Streamlit Dashboard + DB logic
- cli/ -> Command-line Query Runner
- screenshots/ -> UI examples

## How To Run
'''bash
pip install -r requirments.txt
streamlit run app/streamlit_app.py

