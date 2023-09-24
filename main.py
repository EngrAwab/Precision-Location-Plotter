import tkinter as tk
from tkinter import messagebox
import folium

# Create a list to store points
points = []

# Function to handle the "Plot" button click
def plot_button_click():
    lat_str = entry1.get()
    lon_str = entry2.get()

    try:
        if lat_str and lon_str:
            lat = float(lat_str)
            lon = float(lon_str)
            points.append((lat, lon))
            update_map()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid latitude and longitude.")

# Function to update the map with all stored points
def update_map():
    map_object = folium.Map(location=[points[0][0], points[0][1]], zoom_start=10)

    for lat, lon in points:
        folium.Marker([lat, lon], tooltip="Location").add_to(map_object)

    map_object.save("map.html")
    messagebox.showinfo("Info", "Map updated successfully! Check 'map.html'.")

# Create the main application window
root = tk.Tk()
root.title("Map Display")

# Create two input bars
input_frame = tk.Frame(root)
input_frame.pack(side="top", pady=10)
label1 = tk.Label(input_frame, text="Latitude:")
label1.pack(side="left")
entry1 = tk.Entry(input_frame)
entry1.pack(side="left", padx=10)
label2 = tk.Label(input_frame, text="Longitude:")
label2.pack(side="left")
entry2 = tk.Entry(input_frame)
entry2.pack(side="left")

# Create a button to trigger the map plot
plot_button = tk.Button(root, text="Plot", command=plot_button_click)
plot_button.pack()

# Start the GUI main loop
root.mainloop()
