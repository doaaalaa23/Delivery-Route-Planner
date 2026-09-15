# just for testing the delivery route planner, the GUI is taken from AI 
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from delivery_route_planner import delivery_route_planner
from validate_delivery import validate_deliveries


REPORT_PATH = Path("invalid_deliveries_report.txt")


class DeliveryRouteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delivery Route Planner")
        self.root.geometry("900x620")

        self.file_label = ttk.Label(root, text="No CSV file selected")
        self.file_label.pack(anchor="w", padx=16, pady=(16, 4))

        controls = ttk.Frame(root)
        controls.pack(fill="x", padx=16, pady=(0, 12))
        ttk.Button(controls, text="Upload CSV", command=self.upload_file).pack(side="left")
        ttk.Label(controls, text="Max weight (kg):").pack(side="left", padx=(20, 6))
        self.max_weight_input = ttk.Entry(controls, width=10)
        self.max_weight_input.insert(0, "10")
        self.max_weight_input.pack(side="left")
        self.trip_count = ttk.Label(controls, text="Trips: 0")
        self.trip_count.pack(side="left", padx=16)

        content = ttk.PanedWindow(root, orient="horizontal")
        content.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        trips_frame = ttk.Labelframe(content, text="Trips")
        report_frame = ttk.Labelframe(content, text="Invalid delivery report")
        content.add(trips_frame, weight=3)
        content.add(report_frame, weight=2)

        self.trips_output = self._make_output(trips_frame)
        self.report_output = self._make_output(report_frame)

    @staticmethod
    def _make_output(parent):
        output = tk.Text(parent, wrap="word", state="disabled")
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=output.yview)
        output.configure(yscrollcommand=scrollbar.set)
        output.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        return output

    @staticmethod
    def _set_output(output, text):
        output.configure(state="normal")
        output.delete("1.0", tk.END)
        output.insert(tk.END, text)
        output.configure(state="disabled")

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select delivery CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )
        if not file_path:
            return

        try:
            max_weight = float(self.max_weight_input.get())
            if max_weight <= 0:
                raise ValueError("Max weight must be greater than zero.")

            deliveries = validate_deliveries(file_path, max_weight)
            trips = delivery_route_planner(deliveries, file_path, max_weight)
            report = REPORT_PATH.read_text(encoding="utf-8") if REPORT_PATH.exists() else "No invalid deliveries."
        except (KeyError, TypeError, ValueError, OSError) as error:
            messagebox.showerror("Could not process file", str(error))
            return

        self.file_label.configure(text=f"File: {file_path}")
        self.trip_count.configure(text=f"Trips: {len(trips)}")
        self._set_output(self.trips_output, self.format_trips(trips, max_weight))
        self._set_output(self.report_output, report)

    @staticmethod
    def format_trips(trips, max_weight):
        if not trips:
            return "No trips created."

        sections = []
        for number, trip in enumerate(trips, start=1):
            total_weight = sum(delivery.weight for delivery in trip)
            deliveries = ", ".join(str(delivery.ID) for delivery in trip)
            areas = ", ".join(sorted({delivery.area for delivery in trip}))
            sections.append(
                f"Trip {number}\n"
                f"Area: {areas}\n"
                f"Weight: {total_weight:g} / {max_weight:g} kg\n"
                f"Delivery IDs: {deliveries}"
            )
        return "\n\n".join(sections)


if __name__ == "__main__":
    root = tk.Tk()
    DeliveryRouteApp(root)
    root.mainloop()

