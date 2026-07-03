import tkinter as tk
from collections import deque
import psutil
import threading
import time

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# --- Shared Data ---
data = deque([0]*100, maxlen=100)
running = True

# --- Worker Thread ---
def cpu_worker():
    while running:
        cpu = psutil.cpu_percent(interval=1)
        data.append(cpu)

# --- UI Update ---
def update_plot():
    line.set_ydata(data)
    line.set_xdata(range(len(data)))

    ax.relim()
    ax.autoscale_view()

    canvas.draw()

    label.config(text=f"CPU Usage: {data[-1]:.2f}%")

    root.after(500, update_plot)

# --- UI Setup ---
root = tk.Tk()
root.title("CPU Monitor (Better Version)")
root.geometry("800x400")
root.configure(bg="#1e1e1e")

label = tk.Label(root, text="CPU Usage: 0%", fg="white", bg="#1e1e1e", font=("Segoe UI", 16))
label.pack(pady=10)

# --- Matplotlib Figure ---
fig, ax = plt.subplots()
fig.patch.set_facecolor('#1e1e1e')
ax.set_facecolor('#111111')

line, = ax.plot(data)
ax.set_ylim(0, 100)
ax.set_title("Real-time CPU Usage")

# Remove ugly borders
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(colors='white')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill="both", expand=True)

# --- Start Thread ---
threading.Thread(target=cpu_worker, daemon=True).start()

update_plot()

# --- Run ---
try:
    root.mainloop()
finally:
    running = False