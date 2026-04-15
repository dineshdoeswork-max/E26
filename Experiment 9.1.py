#9.1

import matplotlib.pyplot as plt

# 1. Data Setup
roll_numbers = list(range(1, 11))  # Numbers 1 to 10
marks = [45, 78, 62, 89, 34, 90, 76, 85, 92, 58]

# Find the highest mark to highlight it later
max_mark = max(marks)

# --- FIGURE 1: LINE GRAPH ---
plt.figure(figsize=(8, 4))
plt.plot(roll_numbers, marks, marker='o', color='blue', label='Marks')
plt.title('Mathematics Marks Analysis (Line Graph)')
plt.xlabel('Roll Number')
plt.ylabel('Marks')
plt.grid(True)
plt.show()

# --- FIGURE 2: BAR CHART ---
plt.figure(figsize=(8, 4))

# Create a list of colors (blue for everyone, red for the highest)
colors = ['blue' if m < max_mark else 'red' for m in marks]

plt.bar(roll_numbers, marks, color=colors)
plt.title('Mathematics Marks Analysis (Bar Chart)')
plt.xlabel('Roll Number')
plt.ylabel('Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
