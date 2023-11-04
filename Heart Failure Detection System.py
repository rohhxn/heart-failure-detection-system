import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("heart.csv")

def get_prediction():
    # Get values from GUI inputs
    anaemia = var_anaemia.get() == 1
    creatinine_phosphokinase = var_cpk.get()
    diabetes = var_diabetes.get() == 1
    ejection_fraction = var_ef.get()
    high_blood_pressure = var_hbp.get() == 1
    platelets = var_platelets.get()
    serum_creatinine = var_sc.get()
    serum_sodium = var_ss.get()
    sex = var_sex.get()
    smoking = var_smoking.get() == 1
    age = var_age.get()
    # No time input provided, so I'm commenting it out for now
    # time = var_time.get()

    # Use the same conditions
    conditions = (df['anaemia'] == int(anaemia)) & \
                 (df['creatinine_phosphokinase'] == creatinine_phosphokinase) & \
                 (df['diabetes'] == int(diabetes)) & (df['ejection_fraction'] == ejection_fraction) & \
                 (df['high_blood_pressure'] == int(high_blood_pressure)) & (df['platelets'] == platelets) & \
                 (df['serum_creatinine'] == serum_creatinine) & (df['serum_sodium'] == serum_sodium) & \
                 (df['sex'] == int(sex)) & (df['smoking'] == int(smoking)) & (df['age'] == age)
                 #& (df['time'] == time)

    filtered_data = df[conditions]

    if not filtered_data.empty:
        death_event_column = filtered_data['DEATH_EVENT']
        prediction = death_event_column.mode().iloc[0]
        if prediction == 1:
            result = "Heart Attack chance is higher."
        else:
            result = "Low chance of having a heart attack."
    else:
        result = "No matching data found in the CSV. Unable to make a prediction."

    messagebox.showinfo("Prediction Result", result)

# Create main window
root = tk.Tk()
root.title("Heart Prediction")

# Variables for input fields
var_anaemia = tk.IntVar()
var_cpk = tk.IntVar()
var_diabetes = tk.IntVar()
var_ef = tk.IntVar()
var_hbp = tk.IntVar()
var_platelets = tk.DoubleVar()
var_sc = tk.DoubleVar()
var_ss = tk.IntVar()
var_sex = tk.IntVar()
var_smoking = tk.IntVar()
var_age = tk.IntVar()
# var_time = tk.IntVar()

# Create input fields
tk.Checkbutton(root, text="Anaemia?", variable=var_anaemia).pack()
tk.Label(root, text="Creatinine Phosphokinase").pack()
tk.Entry(root, textvariable=var_cpk).pack()
tk.Checkbutton(root, text="Diabetes?", variable=var_diabetes).pack()
tk.Label(root, text="Ejection Fraction (%)").pack()
tk.Entry(root, textvariable=var_ef).pack()
tk.Checkbutton(root, text="High Blood Pressure?", variable=var_hbp).pack()
tk.Label(root, text="Platelet Count").pack()
tk.Entry(root, textvariable=var_platelets).pack()
tk.Label(root, text="Serum Creatinine Level").pack()
tk.Entry(root, textvariable=var_sc).pack()
tk.Label(root, text="Serum Sodium Level").pack()
tk.Entry(root, textvariable=var_ss).pack()
tk.Label(root, text="Sex (0 for female, 1 for male)").pack()
tk.Entry(root, textvariable=var_sex).pack()
tk.Checkbutton(root, text="Smoker?", variable=var_smoking).pack()
tk.Label(root, text="Age").pack()
tk.Entry(root, textvariable=var_age).pack()

# Button to get prediction
tk.Button(root, text="Get Prediction", command=get_prediction).pack()

# Run the application
root.mainloop()
