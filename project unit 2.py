# Medication Dose

name= (input("Enter your name:"))
weight= (float(input("Enter your weight:")))
Medicine_name = (input("Enter your Medicine:"))
dose_per_kg = (float(input("Enter your dose per (mg\kg):")))
num_of_done_per_day= int(input("Enter your number of done per day:"))
num_of_treatment_days= int(input("Enter your number of treatment days:"))

print("Medication plan for :",name)
print("Medicine:",Medicine_name, "\n")

dose_per_administration = weight * dose_per_kg
print("Dose per administration:",dose_per_administration)

print("Done per day",num_of_done_per_day)

daily_dose= dose_per_administration * num_of_done_per_day
print("Daily total:",daily_dose)

print("treatment days:",num_of_treatment_days)
total_treatment_days= daily_dose * num_of_treatment_days
print("Total amount for full course :",total_treatment_days)
print("\n This is an educational tool. Always confirm medical decisions with a professional.")