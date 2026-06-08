# Insider Risk Detection System

A Python-based security analytics platform designed to detect anomalous user behavior, identify potential insider threats and generate investigation-ready reports.

## Overview

This project simulates a real-world Insider Risk Management (IRM) workflow by:

- Generating realistic user activity logs
- Detecting suspicious behavior patterns
- Calculating user risk scores
- Classifying users by risk severity
- Producing visual analytics dashboards
- Generating HTML investigation reports

## Features

### Activity Simulation

Generates realistic enterprise activity logs including:

- User logins
- File downloads
- File uploads
- Email activity
- Failed logins
- USB copy events

### Risk Scoring Engine

Analyzes user behavior and calculates risk scores based on:

- Excessive file downloads
- Failed authentication attempts
- After-hours activity
- Suspicious behavioral patterns

### Security Analytics

Provides:

- Risk distribution analysis
- Severity classification
- Top-risk user identification
- Activity trend visualization

### Reporting

Generates:

- HTML security reports
- Visual analytics charts
- Investigation-ready summaries

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Faker

## Example Workflow

python data_generator.py

python charts_generator.py

python report_generator.py

## Project Structure

```text
data/
reports/
reports/charts/

src/
├── data_generator.py
├── analyzer.py
├── risk_engine.py
├── charts_generator.py
└── report_generator.py


