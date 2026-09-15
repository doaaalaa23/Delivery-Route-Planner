
def order_deliveries(deliveries):
    return sorted(deliveries, key=lambda d: (d.priority, d.weight))


def search_by_area(deliveries, area, delivery_weight, max_weight=10):
    deliveries_by_area = []
    total_weight = delivery_weight

    for delivery in deliveries:
        if delivery.area == area:
            if delivery.weight + total_weight <= max_weight:
                deliveries_by_area.append(delivery)
                total_weight += delivery.weight

    return deliveries_by_area


def search_by_weight(deliveries, max_weight=10, current_weight=0):
    deliveries_by_weight = []

    for delivery in deliveries:
        if current_weight + delivery.weight <= max_weight:
            deliveries_by_weight.append(delivery)
            current_weight += delivery.weight

    return deliveries_by_weight


def make_trips(deliveries, max_weight=10):
    trips = []
    remaining_deliveries = deliveries.copy()

    while remaining_deliveries:

        current_trip = []
        current_weight = 0

        delivery = remaining_deliveries.pop(0)

        current_trip.append(delivery)
        current_weight += delivery.weight

        area = delivery.area

      
        deliveries_by_area = search_by_area(
            remaining_deliveries,
            area,
            current_weight,
            max_weight
        )

       
        for delivery in deliveries_by_area:
            current_trip.append(delivery)
            current_weight += delivery.weight
            remaining_deliveries.remove(delivery)

        
        deliveries_by_weight = search_by_weight(
            remaining_deliveries,
            max_weight,
            current_weight
        )

        
        for delivery in deliveries_by_weight:
            current_trip.append(delivery)
            current_weight += delivery.weight
            remaining_deliveries.remove(delivery)

       
        trips.append(current_trip)

    return trips

def delivery_route_planner(deliveries, path, max_weight=10):
    ordered_deliveries = order_deliveries(deliveries)
    trips = make_trips(ordered_deliveries, max_weight=max_weight)
    return trips