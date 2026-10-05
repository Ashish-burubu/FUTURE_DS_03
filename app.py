import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('bank-full.csv', sep=';')

# 1. Overall Funnel Conversion Metrics
total_contacts = len(df)
engaged_leads = len(df[df['duration'] > 180]) # Contact duration > 3 mins
converted_customers = len(df[df['y'] == 'yes'])

funnel_summary = pd.DataFrame({
    'Stage': ['1. Total Contacts (Top Funnel)', '2. Engaged Leads (Mid Funnel)', '3. Converted Customers (Bottom Funnel)'],
    'Users': [total_contacts, engaged_leads, converted_customers],
    'Conversion_Rate_%': [
        100.0,
        round((engaged_leads / total_contacts) * 100, 2),
        round((converted_customers / total_contacts) * 100, 2)
    ],
    'Stage_to_Stage_Dropoff_%': [
        0.0,
        round((1 - engaged_leads / total_contacts) * 100, 2),
        round((1 - converted_customers / engaged_leads) * 100, 2)
    ]
})

print("=== FUNNEL STAGE METRICS ===")
print(funnel_summary.to_string(index=False))

# 2. Channel/Contact Method Performance
channel_perf = df.groupby('contact').agg(
    Total_Leads=('y', 'count'),
    Converted=('y', lambda x: (x == 'yes').sum()),
    Conversion_Rate=('y', lambda x: round((x == 'yes').mean() * 100, 2)),
    Avg_Duration_Sec=('duration', 'mean')
).reset_index().sort_values(by='Conversion_Rate', ascending=False)

print("\n=== PERFORMANCE BY CONTACT METHOD ===")
print(channel_perf.to_string(index=False))

# 3. Campaign Contacts vs Conversion (Frequency Analysis)
campaign_perf = df.groupby('campaign').agg(
    Total=('y', 'count'),
    Converted=('y', lambda x: (x == 'yes').sum()),
    Conversion_Rate=('y', lambda x: round((x == 'yes').mean() * 100, 2))
).reset_index().head(10)

print("\n=== CONVERSION BY NUMBER OF CONTACTS (CAMPAIGN FREQUENCY) ===")
print(campaign_perf.to_string(index=False))

# 4. Previous Outcome Performance (Retargeting Funnel)
poutcome_perf = df.groupby('poutcome').agg(
    Total=('y', 'count'),
    Converted=('y', lambda x: (x == 'yes').sum()),
    Conversion_Rate=('y', lambda x: round((x == 'yes').mean() * 100, 2))
).reset_index().sort_values(by='Conversion_Rate', ascending=False)

print("\n=== PERFORMANCE BY PREVIOUS CAMPAIGN OUTCOME ===")
print(poutcome_perf.to_string(index=False))
