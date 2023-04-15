import tkinter as tk

def calculate_bmi(height, weight):
    height = height / 100.0
    bmi = weight / (height ** 2)
    return bmi

def suggest_workout_plan(bmi):
    if bmi < 18.5:
        return "Your BMI is underweight. You should focus on strength training and building muscle mass."
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Your BMI is within the healthy range. You should focus on maintaining your fitness level with regular exercise."
    elif bmi >= 25.0 and bmi <= 29.9:
        return "Your BMI is overweight. You should focus on cardio exercises such as running, cycling, or swimming to burn calories."
    else:
        return "Your BMI is in the obese range. You should focus on high-intensity interval training (HIIT) and exercises that help you burn fat."

def calculate_bmi_gui():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    except ValueError:
        error_label.config(text="Please enter valid values for height and weight.", fg="red")
        return
    bmi = calculate_bmi(height, weight)
    bmi_text.set(f"Your BMI is {bmi:.2f}")
    workout_plan_text.set(suggest_workout_plan(bmi))
    error_label.config(text="")

# Create the GUI
root = tk.Tk()
root.title("BMI Calculator")

# Create the header label
header_label = tk.Label(root, text="BMI Calculator", font=("Arial", 24), pady=10)
header_label.pack()

# Create the input fields for height and weight
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

height_label = tk.Label(input_frame, text="Height (cm):", font=("Arial", 14))
height_label.grid(row=0, column=0, padx=5)

height_entry = tk.Entry(input_frame, font=("Arial", 14))
height_entry.grid(row=0, column=1, padx=5)

weight_label = tk.Label(input_frame, text="Weight (kg):", font=("Arial", 14))
weight_label.grid(row=1, column=0, padx=5)

weight_entry = tk.Entry(input_frame, font=("Arial", 14))
weight_entry.grid(row=1, column=1, padx=5)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14), command=calculate_bmi_gui)
calculate_button.pack()

# Create the BMI and workout plan labels
bmi_text = tk.StringVar()
bmi_label = tk.Label(root, textvariable=bmi_text, font=("Arial", 18), pady=10)
bmi_label.pack()

workout_plan_text = tk.StringVar()
workout_plan_label = tk.Label(root, textvariable=workout_plan_text, font=("Arial", 14), wraplength=500)
workout_plan_label.pack()

# Create the error label
error_label = tk.Label(root, fg="red")
error_label.pack()

root.mainloop()
