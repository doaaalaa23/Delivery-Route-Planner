import csv

from delivery_class import Delivery


def read_deliveries(file_path: str) -> list[Delivery]:
    try:
        with open(file_path, newline="", encoding="utf-8") as csv_file:
            rows = csv.DictReader(csv_file)
            return [
                Delivery(
                    ID=int(row["ID"]),
                    area=row["area"],
                    priority=int(row["priority"]),
                    weight=float(row["weight"]),
                )
                for row in rows
            ]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error reading deliveries from {file_path}: {e}")
        return []
