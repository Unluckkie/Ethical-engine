import streamlit as st
import pandas as pd

st.set_page_config(page_title="Eowyn Ethical Engine", layout="wide")
st.title("⚖️ Eowyn's Ethical Engine")
st.markdown("A four-quadrant load balancer for moral decision-making.")

# Inputs
col1, col2 = st.columns(2)
with col1:
    q1 = st.slider("Q1: Material/Environmental Constraints", 0, 10, 5)
    q2 = st.slider("Q2: Individual Rights & Sanctity", 0, 10, 5)
with col2:
    q3 = st.slider("Q3: Societal Net P&L", 0, 10, 5)
    q4 = st.slider("Q4: The Legal Frame", 0, 10, 5)

# Processing
humanist = q1 + q2
institutional = q3 + q4

# Visualization
df = pd.DataFrame({'Score': [humanist, institutional]}, index=['Humanist (Q1+Q2)', 'Institutional (Q3+Q4)'])
st.bar_chart(df)

# Resolution Kernel
if abs(humanist - institutional) < 1:
    st.warning("⚠️ Deadlock detected: Tiebreaker Kernel Triggered.")
    if max([q1, q2, q3, q4]) > 7:
        st.success("Resolution: Ethical override granted by Critical Variable (Amplitude > 7).")
    else:
        st.info("Resolution: System inconclusive. Requires human input.")
else:
    winner = "Humanist" if humanist > institutional else "Institutional"
    st.write(f"Engine Verdict: **{winner} Dominant**")
