# -*- coding: utf-8 -*-
"""meds_agent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cd6St-fOsbTPz7OQYPMx-IusuMBK_9XI
"""

import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# For this project synthetic dataset is being used
medications = ['Metformin', 'Lisinopril', 'Aspirin', 'Atorvastatin', 'Amoxicillin',
               'Ibuprofen', 'Losartan', 'Omeprazole', 'Levothyroxine', 'Albuterol']
dosages = ['500mg', '10mg', '20mg', '100mg', '250mg', '5mg', '75mg', '40mg']
times = ['08:00', '12:00', '14:00', '18:00', '20:00']

schedule = []
start_date = datetime.today()

for day in range(30):
    date = (start_date + timedelta(days=day)).strftime('%Y-%m-%d')
    num_meds = random.randint(1, 3)

    for _ in range(num_meds):
        med = random.choice(medications)
        dose = random.choice(dosages)
        time = random.choice(times)

        schedule.append({
            'Date': date,
            'Medication': med,
            'Dosage': dose,
            'Time': time
        })

df_schedule = pd.DataFrame(schedule)
df_schedule.to_csv('meds_schedule_30days.csv', index=False)
print("CSV file 'meds_schedule_30days.csv' created!")

df = pd.read_csv('meds_schedule_30days.csv')

st.set_page_config(page_title="Medication Agent", layout="wide")
st.title("💊 Personalized Medication Reminder Agent")
st.markdown("Built with synthetic 30-day schedule. Future versions will include FDA data integration.")

selected_date = st.date_input("Select a date to view medication schedule:", datetime.today()).strftime('%Y-%m-%d')
filtered_df = df[df['Date'] == selected_date]

st.subheader(f"📅 Medication Schedule for {selected_date}")
st.dataframe(filtered_df)

if selected_date == datetime.today().strftime('%Y-%m-%d'):
    now = datetime.now().strftime('%H:%M')
    due_now = filtered_df[filtered_df['Time'] == now]
    st.markdown("## ⏰ Medications Due Now")
    if not due_now.empty:
        for _, row in due_now.iterrows():
            st.success(f"🔔 Take {row['Medication']} ({row['Dosage']}) at {row['Time']}")
    else:
        st.info(f"No medication due at {now}.")
else:
    st.info("Viewing a different date. Reminders only run for today.")

def check_interactions(med_list):
    interactions = {
        ('Lisinopril', 'Aspirin'): 'May increase the risk of kidney problems.',
        ('Metformin', 'Aspirin'): 'May increase the risk of lactic acidosis.'
    }
    reported = set()
    for i in range(len(med_list)):
        for j in range(i+1, len(med_list)):
            pair = (med_list[i], med_list[j])
            rev_pair = (pair[1], pair[0])
            if pair in interactions and pair not in reported:
                st.error(f"⚠️ {pair[0]} + {pair[1]}: {interactions[pair]}")
                reported.add(pair)
            elif rev_pair in interactions and rev_pair not in reported:
                st.error(f"⚠️ {pair[1]} + {pair[0]}: {interactions[rev_pair]}")
                reported.add(rev_pair)
            else:
                st.success(f"✅ No known interaction between {pair[0]} and {pair[1]}.")

st.markdown("## 🧠 Drug Interaction Warnings")
meds_list = filtered_df['Medication'].tolist()
if meds_list:
    check_interactions(meds_list)
else:
    st.info("No medications scheduled for this date.")

st.markdown("## 📊 Medication Frequency Over 30 Days")
st.line_chart(df['Date'].value_counts().sort_index())