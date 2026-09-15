from delivery_route_planner import delivery_route_planner
from validate_delivery import validate_deliveries

if __name__ == "__main__":
    try:
        file_path=input("Enter the path to the CSV file: ")
        max_weight=float(input("Enter the maximum weight limit (kg): "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()

    deliveries = validate_deliveries(file_path, max_weight=max_weight)
    trips = delivery_route_planner(deliveries, file_path, max_weight=max_weight)

    if trips:
        print(f"Total trips: {len(trips)}")
        for i, trip in enumerate(trips, start=1):
            total_weight = sum(delivery.weight for delivery in trip)
            delivery_ids = ", ".join(str(delivery.ID) for delivery in trip)
            areas = ", ".join(sorted({delivery.area for delivery in trip}))
            print(f"Trip {i}: Area: {areas}, Weight: {total_weight:g} / {max_weight:g} kg, Delivery IDs: {delivery_ids}")
    else:
        print("No valid trips could be planned.")
   
