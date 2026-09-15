from read_data import read_deliveries
from delivery_class import Delivery

def validate_deliveries(file_path: str, max_weight: float = 10) -> list[Delivery]:
    valid_deliveries=[]
    invalid_deliveries=[]
    reasons=[]
    deliveries = read_deliveries(file_path)
    for delivery in deliveries:
      if delivery.weight > max_weight:
        invalid_deliveries.append(delivery)
        reason = f"Delivery ID {delivery.ID} exceeds weight limit: {delivery.weight} kg"
        reasons.append(reason)
      else:
        valid_deliveries.append(delivery)
    if invalid_deliveries:
      make_report(invalid_deliveries, reasons, max_weight)

    return valid_deliveries


def make_report(invalid_deliveries, reasons, max_weight=10):
    with open("invalid_deliveries_report.txt", "w") as report_file:
        for delivery, reason in zip(invalid_deliveries, reasons):
            report_file.write(f"========================================\nINVALID DELIVERY REPORT\n========================================\nVehicle capacity: {max_weight:g} kg\nInvalid deliveries:{len(invalid_deliveries)}\n\n")
            report_file.write(f"Delivery ID: {delivery.ID}, Area: {delivery.area}, Priority: {delivery.priority}, Weight: {delivery.weight} kg\n\n")
            report_file.write(f"The Reason for invalidation: {reason}\n")
            report_file.write("========================================\n\n")
    print("Report generated: invalid_deliveries_report.txt")