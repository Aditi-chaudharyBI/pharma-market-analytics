-- Module B: Patient Adherence Cohort Analysis
-- Medication Possession Ratio by initiation month

WITH patient_mpr AS (
    SELECT 
        patient_id,
        DATE_TRUNC('month', MIN(fill_date)) as init_month,
        SUM(days_supply) as total_days_supply,
        COUNT(*) as fills
    FROM claims
    GROUP BY patient_id
),
monthly_cohort AS (
    SELECT 
        init_month,
        COUNT(*) as patient_count,
        AVG(total_days_supply::float / 365) as avg_mpr
    FROM patient_mpr
    GROUP BY init_month
)
SELECT * FROM monthly_cohort
ORDER BY init_month;
