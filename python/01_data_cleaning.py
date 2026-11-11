# python/01_data_cleaning.py
import pandas as pd
import numpy as np

# Load data
claims = pd.read_csv('../data/prescription_claims.csv', parse_dates=['fill_date'])
patients = pd.read_csv('../data/patient_outcomes.csv')
formulary = pd.read_csv('../data/payer_formulary.csv')

# Clean claims
claims = claims.drop_duplicates(subset=['claim_id'])
claims['fill_date'] = pd.to_datetime(claims['fill_date'])
claims['days_supply'] = claims['days_supply'].fillna(30)

# Calculate MPR per patient
mpr = claims.groupby('patient_id').agg(
    total_days=('days_supply', 'sum'),
    first_fill=('fill_date', 'min')
).reset_index()

mpr['mpr'] = (mpr['total_days'] / 365).clip(0, 1)

# Merge with outcomes
df = mpr.merge(patients, on='patient_id', how='left')

print(df.head())
print(f"Average MPR: {df['mpr'].mean():.2f}")
print(f"Discontinuation rate: {df['discontinuation_flag'].mean():.2%}")
