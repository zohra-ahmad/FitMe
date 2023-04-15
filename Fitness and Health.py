import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
        messagebox.showerror("Error", "Please enter valid values for height and weight.")
        return
    bmi = calculate_bmi(height, weight)
    bmi_text.set(f"Your BMI is {bmi:.2f}")
    workout_plan_text.set(suggest_workout_plan(bmi))

# Create the GUI
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("500x350")
root.resizable(False, False)

# Create the header label
header_label = tk.Label(root, text="BMI Calculator", font=("Arial", 24), pady=10)
header_label.pack()

# Create the input fields for height and weight
input_frame = tk.Frame(root, padx=20, pady=10)
input_frame.pack()

height_label = tk.Label(input_frame, text="Height (cm):", font=("Arial", 14))
height_label.grid(row=0, column=0, padx=5, pady=5)

height_entry = tk.Entry(input_frame, font=("Arial", 14))
height_entry.grid(row=0, column=1, padx=5, pady=5)
height_entry.focus()

weight_label = tk.Label(input_frame, text="Weight (kg):", font=("Arial", 14))
weight_label.grid(row=1, column=0, padx=5, pady=5)

weight_entry = tk.Entry(input_frame, font=("Arial", 14))
weight_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14), command=calculate_bmi_gui)
calculate_button.pack(pady=10)

# Create the BMI and workout plan labels
bmi_frame = tk.Frame(root, padx=20, pady=10)
bmi_frame.pack()

bmi_text = tk.StringVar()
bmi_label = tk.Label(bmi_frame, textvariable=bmi_text, font=("Arial", 18), pady=5)
bmi_label.pack()

workout_plan_text = tk.StringVar()
workout_plan_label = tk.Label(bmi_frame, textvariable=workout_plan_text, font=("Arial", 14), wraplength=400)
workout_plan_label.pack()

# Create the error label
error_frame = tk.Frame(root)
error_frame.pack()

error_label = tk.Label(error_frame, fg="red")
error_label.pack()

# Create the about button
def show_about():
    about_text = "This app was created by [Zohra Ahmad]."
