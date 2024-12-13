#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

def calculate_miles_remaining(battery_capacity_ah, motor_power_watts, battery_voltage, battery_percent, rider_weight_equipment):
  """
  Calculates the estimated miles remaining on a battery based on given inputs.

  Args:
    battery_capacity_ah: Battery capacity in Ampere-hours (Ah).
    motor_power_watts: Motor power in Watts.
    battery_voltage: Battery voltage in Volts.
    battery_percent: Remaining battery percentage (0-100).
    rider_weight_equipment: Total rider weight with equipment in pounds.

  Returns:
    Estimated miles remaining on the battery.
  """

  # Base watts_per_mile value
  base_watts_per_mile = 19.95

  # Rider weight adjustment factor
  
  weight_factor = 1 + (rider_weight_equipment / 700) 

  # Motor power adjustment factor
  motor_power_factor = 1 + (motor_power_watts / 2000) 

  # Combined adjustment
  watts_per_mile = base_watts_per_mile * weight_factor * motor_power_factor

  total_energy_wh = battery_capacity_ah * battery_voltage
  remaining_energy_wh = total_energy_wh * (battery_percent / 100)
  estimated_miles = remaining_energy_wh / watts_per_mile 

  return estimated_miles

def calculate_and_display():
  try:
    battery_capacity_ah = float(battery_capacity_entry.get())
    motor_power_watts = float(motor_power_entry.get())
    battery_voltage = float(battery_voltage_entry.get())
    battery_percent = float(battery_percent_entry.get())
    rider_weight_equipment = float(rider_weight_entry.get())

    estimated_miles = calculate_miles_remaining(battery_capacity_ah, motor_power_watts, 
                                              battery_voltage, battery_percent, rider_weight_equipment)

    result_label.config(text=f"Estimated miles remaining: {estimated_miles:.2f} miles")
  except ValueError:
    result_label.config(text="Invalid input. Please enter numerical values.")

# Create the main window
window = tk.Tk()
window.title("E-Bike Range Estimator")

# Create labels and entry fields
battery_capacity_label = ttk.Label(window, text="Battery Capacity (Ah):")
battery_capacity_entry = ttk.Entry(window)

motor_power_label = ttk.Label(window, text="Motor Power (Watts):")
motor_power_entry = ttk.Entry(window)

battery_voltage_label = ttk.Label(window, text="Battery Voltage (Volts):")
battery_voltage_entry = ttk.Entry(window)

battery_percent_label = ttk.Label(window, text="Remaining Battery (%):")
battery_percent_entry = ttk.Entry(window)

rider_weight_label = ttk.Label(window, text="Rider Weight + Equipment (lbs):")
rider_weight_entry = ttk.Entry(window)

calculate_button = ttk.Button(window, text="Calculate", command=calculate_and_display)
result_label = ttk.Label(window, text="")

# Arrange the widgets using grid layout
battery_capacity_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
battery_capacity_entry.grid(row=0, column=1, padx=5, pady=5)

motor_power_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
motor_power_entry.grid(row=1, column=1, padx=5, pady=5)

battery_voltage_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
battery_voltage_entry.grid(row=2, column=1, padx=5, pady=5)

battery_percent_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
battery_percent_entry.grid(row=3, column=1, padx=5, pady=5)

rider_weight_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
rider_weight_entry.grid(row=4, column=1, padx=5, pady=5)

calculate_button.grid(row=5, columnspan=2, padx=5, pady=5)
result_label.grid(row=6, columnspan=2, padx=5, pady=5)

window.mainloop()
