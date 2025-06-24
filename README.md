# Personalized Medication Reminder Agent
## Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://medicationreminderapp-h2gga62porvbqxeogtyv2e.streamlit.app/)

This is a simple agentic app that helps patient especially seniors, manage their medications by providing:

- Time-based reminders
- Drug interaction warnings
- Date-based filtering
- Daily medication dashboard

## Features

- View medication schedules for any date (past, present, future)
- Get alerts if it's time to take a medication (if viewing today's date)
- Basic interaction check between medications (e.g., Lisinopril + Aspirin)
- Line chart showing number of medications per day

## Dataset

The dataset `meds_schedule_30days.csv` is **synthetic**, simulating 30 days of medication schedules using realistic medication names and dosages.

### Plan for Expansion
Future versions will:
- Integrate with FDA Drug Interaction APIs
- Track medication history per user
- Include alerts via email or mobile
