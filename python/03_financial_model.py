# ROI model for copay assistance program
program_cost = 500_000
revenue_per_adherent_patient = 2400
break_even_patients = program_cost / revenue_per_adherent_patient
projected_patients = 1200
projected_roi = (projected_patients * revenue_per_adherent_patient - program_cost) / program_cost

print(f"Break-even patients: {break_even_patients:.0f}")
print(f"Projected ROI: {projected_roi:.1f}x")
