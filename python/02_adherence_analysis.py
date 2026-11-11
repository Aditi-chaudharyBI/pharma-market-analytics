# Discontinuation analysis
disc = df[df['discontinuation_flag'] == 1]
print(disc['discontinuation_reason'].value_counts(normalize=True) * 100)

# Adherence by age band
df['age_band'] = pd.cut(df['age'], bins=[0, 64, 120], labels=['<65', '65+'])
print(df.groupby('age_band')['mpr'].mean())
