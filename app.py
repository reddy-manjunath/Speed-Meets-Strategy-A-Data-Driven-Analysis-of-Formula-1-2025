import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="F1 2025 Analytics & Strategy",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
def apply_custom_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
            
            html, body, [class*="css"] {
                font-family: 'Outfit', sans-serif;
            }
            
            /* Dark Theme with F1 Red Accents */
            .stApp {
                background-color: #0d0d0d;
                color: #ffffff;
            }
            
            h1, h2, h3, h4, h5, h6 {
                color: #ffffff;
                font-weight: 800;
            }
            
            .metric-card {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                transition: transform 0.3s ease;
            }
            
            .metric-card:hover {
                transform: translateY(-5px);
                border-color: #e10600;
            }
            
            .metric-title {
                font-size: 1.1rem;
                color: #a0a0a0;
                text-transform: uppercase;
                letter-spacing: 2px;
                margin-bottom: 10px;
            }
            
            .metric-value {
                font-size: 2.5rem;
                font-weight: 800;
                color: #e10600;
            }
            
            .stButton>button {
                background-color: #e10600;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 0.5rem 2rem;
                font-weight: 600;
                letter-spacing: 1px;
                transition: all 0.3s ease;
            }
            
            .stButton>button:hover {
                background-color: #ff1e15;
                color: white;
                box-shadow: 0 0 15px rgba(225, 6, 0, 0.5);
            }
            
            /* Sidebar */
            [data-testid="stSidebar"] {
                background-color: #15151e;
                border-right: 1px solid #333;
            }
            
            /* Tables */
            .dataframe {
                width: 100%;
                border-collapse: collapse;
            }
            .dataframe th {
                background-color: #1a1a1a;
                color: #e10600;
                padding: 10px;
                border-bottom: 2px solid #e10600;
            }
            .dataframe td {
                padding: 10px;
                border-bottom: 1px solid #333;
            }
        </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# --- CONSTANTS ---
MODELS_DIR = "Trained_tuned_models"
DATA_DIR = "."
EDA_DIR = "EDA_Data_Retrieved"

# --- HELPER FUNCTIONS ---
@st.cache_data
def load_results():
    try:
        return pd.read_csv(os.path.join(DATA_DIR, "results_2025.csv"))
    except Exception as e:
        st.error(f"Error loading results data: {e}")
        return pd.DataFrame()

@st.cache_resource
def load_models():
    models = {}
    try:
        models['count'] = joblib.load(os.path.join(MODELS_DIR, 'f1_pit_count_model_2025.pkl'))
        models['lap'] = joblib.load(os.path.join(MODELS_DIR, 'f1_pit_lap_model_2025.pkl'))
        models['strat'] = joblib.load(os.path.join(MODELS_DIR, 'f1_strat_model_2025.pkl'))
        return models
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None

def build_input_df(grid_pos, early_pace, pace_std, tire_deg, track_temp, rain, start_tyre, feature_names):
    input_dict = {
        'GridPosition_Est': grid_pos,
        'AvgEarlyPace': early_pace,
        'PaceStdDev': pace_std,
        'TireDegSlope': tire_deg,
        'AvgTrackTemp': track_temp,
        'RainDetected': 1 if rain else 0
    }
    
    for col in feature_names:
        if col.startswith("StartTyre_"):
            tyre_type = col.replace("StartTyre_", "")
            input_dict[col] = 1 if tyre_type == start_tyre else 0
            
    return pd.DataFrame([input_dict])[feature_names]

def render_input_form():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Track & Driver Conditions")
        grid_pos = st.number_input("Grid Position (1-20)", min_value=1, max_value=20, value=1)
        
        pace_category = st.selectbox("Driver Pace Category", ["Fast (Front-runner)", "Average (Midfield)", "Slow (Backmarker)"], index=1)
        pace_mapping = {"Fast (Front-runner)": 80.0, "Average (Midfield)": 85.5, "Slow (Backmarker)": 90.0}
        early_pace = pace_mapping[pace_category]
        
        consistency_category = st.selectbox("Driver Consistency", ["High (Very Consistent)", "Medium (Average)", "Low (Erratic)"], index=1)
        consistency_mapping = {"High (Very Consistent)": 0.5, "Medium (Average)": 1.2, "Low (Erratic)": 2.5}
        pace_std = consistency_mapping[consistency_category]
        
    with col2:
        st.subheader("Weather & Tyre")
        track_temp = st.slider("Track Temperature (°C)", min_value=20.0, max_value=60.0, value=35.0)
        
        deg_category = st.selectbox("Tyre Degradation Expected", ["Low", "Medium", "High"], index=1)
        deg_mapping = {"Low": 0.02, "Medium": 0.05, "High": 0.09}
        tire_deg = deg_mapping[deg_category]
        
        rain = st.checkbox("Is it raining?")
        start_tyre = st.selectbox("Starting Tyre Compound", ["SOFT", "MEDIUM", "HARD", "INTERMEDIATE"])
        
    return grid_pos, early_pace, pace_std, tire_deg, track_temp, rain, start_tyre

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg", width=150)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "🏁 Race Summary & Leaderboard", 
    "🛑 Model 1: Pit Stop Count", 
    "⏱️ Model 2: First Pit Lap", 
    "🏎️ Model 3: Strategy Type"
])

st.sidebar.markdown("---")
st.sidebar.info("Data-Driven Formula 1 Strategy Analysis for the 2025 Season.")

models = load_models()
feature_names = models['count'].feature_names_in_ if models else []

# --- PAGE 1: RACE SUMMARY ---
if page == "🏁 Race Summary & Leaderboard":
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>F1 2025 SEASON SUMMARY</h1>", unsafe_allow_html=True)
    
    df_results = load_results()
    
    if not df_results.empty:
        driver_points = df_results.groupby(['Abbreviation', 'FullName'])['Points'].sum().reset_index().sort_values(by='Points', ascending=False)
        team_points = df_results.groupby('TeamName')['Points'].sum().reset_index().sort_values(by='Points', ascending=False)
        
        driver_champ = driver_points.iloc[0] if not driver_points.empty else None
        constructor_champ = team_points.iloc[0] if not team_points.empty else None
        
        col1, col2 = st.columns(2)
        with col1:
            if driver_champ is not None:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Driver Champion 2025</div>
                    <div class="metric-value">{driver_champ['FullName']} ({driver_champ['Abbreviation']})</div>
                    <div style="font-size: 1.2rem; color: #a0a0a0; margin-top: 5px;">{driver_champ['Points']} Pts</div>
                </div>
                """, unsafe_allow_html=True)
        with col2:
            if constructor_champ is not None:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-title">Constructor Champion 2025</div>
                    <div class="metric-value">{constructor_champ['TeamName']}</div>
                    <div style="font-size: 1.2rem; color: #a0a0a0; margin-top: 5px;">{constructor_champ['Points']} Pts</div>
                </div>
                """, unsafe_allow_html=True)
                
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        st.subheader("🏆 Driver Leaderboard")
        st.dataframe(driver_points.head(10).style.background_gradient(cmap="Reds", subset=['Points']), use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 Exploratory Data Analysis (EDA)")
    
    if os.path.exists(EDA_DIR):
        eda_files = [f for f in os.listdir(EDA_DIR) if f.endswith('.csv')]
        if eda_files:
            tabs = st.tabs([f.replace("Untitled spreadsheet - ", "").replace("_retrieved.csv", "").replace(".csv", "").replace("_", " ").title() for f in eda_files])
            for tab, file in zip(tabs, eda_files):
                with tab:
                    df_eda = pd.read_csv(os.path.join(EDA_DIR, file))
                    st.dataframe(df_eda, use_container_width=True)
                    numeric_cols = df_eda.select_dtypes(include=[np.number]).columns
                    categorical_cols = df_eda.select_dtypes(include=['object']).columns
                    if len(numeric_cols) > 0 and len(categorical_cols) > 0:
                        st.bar_chart(df_eda.set_index(categorical_cols[0])[numeric_cols[0]], color="#e10600")

    

# --- PAGE 2: MODEL 1 - PIT STOP COUNT ---
elif page == "🛑 Model 1: Pit Stop Count":
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>MODEL 1: PIT STOP COUNT PREDICTOR</h1>", unsafe_allow_html=True)
    st.markdown("Predict the total number of pit stops required during the race (Classification).")
    
    if models:
        with st.form("count_form"):
            inputs = render_input_form()
            submit = st.form_submit_button("Predict Pit Stop Count")
            
        if submit:
            st.markdown("---")
            input_df = build_input_df(*inputs, feature_names)
            with st.spinner("Predicting..."):
                pred = models['count'].predict(input_df)[0]
                st.markdown(f"""
                <div class="metric-card" style="max-width: 400px; margin: 0 auto;">
                    <div class="metric-title">Predicted Pit Stops</div>
                    <div class="metric-value" style="color: #00d2be;">{int(pred)}</div>
                </div>
                """, unsafe_allow_html=True)

# --- PAGE 3: MODEL 2 - FIRST PIT LAP ---
elif page == "⏱️ Model 2: First Pit Lap":
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>MODEL 2: FIRST PIT LAP PREDICTOR</h1>", unsafe_allow_html=True)
    st.markdown("Predict the exact lap window for the first pit stop (Regression). Note: Assumes at least 1 pit stop.")
    
    if models:
        with st.form("lap_form"):
            inputs = render_input_form()
            submit = st.form_submit_button("Predict First Pit Lap")
            
        if submit:
            st.markdown("---")
            input_df = build_input_df(*inputs, feature_names)
            with st.spinner("Predicting..."):
                pred = models['lap'].predict(input_df)[0]
                st.markdown(f"""
                <div class="metric-card" style="max-width: 400px; margin: 0 auto;">
                    <div class="metric-title">Predicted 1st Pit Window</div>
                    <div class="metric-value" style="color: #ff8000;">Lap {int(pred)}</div>
                </div>
                """, unsafe_allow_html=True)

# --- PAGE 4: MODEL 3 - STRATEGY TYPE ---
elif page == "🏎️ Model 3: Strategy Type":
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem;'>MODEL 3: TYRE STRATEGY PREDICTOR</h1>", unsafe_allow_html=True)
    st.markdown("Predict the optimal overall tyre sequence strategy for the race (Multiclass Classification).")
    
    if models:
        with st.form("strat_form"):
            inputs = render_input_form()
            submit = st.form_submit_button("Predict Strategy Type")
            
        if submit:
            st.markdown("---")
            input_df = build_input_df(*inputs, feature_names)
            
            strat_mapping = {
                0: 'HARD -> MEDIUM',
                1: 'MEDIUM -> HARD',
                2: 'MEDIUM -> HARD -> HARD',
                3: 'MEDIUM -> MEDIUM -> HARD',
                4: 'MEDIUM -> SOFT'
            }
            
            with st.spinner("Predicting..."):
                pred = models['strat'].predict(input_df)[0]
                pred_str = strat_mapping.get(pred, f"Unknown Strategy ({pred})")
                st.markdown(f"""
                <div class="metric-card" style="max-width: 500px; margin: 0 auto;">
                    <div class="metric-title">Optimal Tyre Sequence</div>
                    <div class="metric-value" style="color: #e10600; font-size: 2rem;">{pred_str}</div>
                </div>
                """, unsafe_allow_html=True)
