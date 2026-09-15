# Delivery Route Planner

## Requirements

* Python 3.9 or newer
* No external packages are needed.

## Input Format

The program reads a CSV file with this header:

```text
ID,area,priority,weight
```

Each delivery has an ID, area, priority, and weight.

A smaller priority number means the delivery is more important.

The sample input file is `test.csv`.

## How To Run

Run the program with:

```text
python main.py
```

The program asks for the CSV file path and the vehicle capacity.

For the assignment, enter `10` kg.

The program then shows the trips and their delivery IDs, areas, and total weight.

## Solution Approach

First, the program reads the CSV file and creates a `Delivery` object for each row.

Then, it checks the weight of each delivery. Deliveries that are heavier than the capacity are not added to the trips.

The valid deliveries are sorted by priority. Lower priority numbers are handled first.

After that, the program creates the trips. It tries to put deliveries from the same area together while making sure the total weight does not go over the capacity.

Each delivery is removed after it is added to a trip, so a delivery cannot be added twice.

## Edge Cases

* **No deliveries:** The program does not create any trips.
* **Package heavier than capacity:** The package is not added to a trip.
* **Same priority:** The deliveries are handled in their input order, with lighter packages first.
* **Package does not fit:** It is saved for another trip.
* **Many packages in the same area:** They are divided into different trips if they do not fit together.

## Difficult Part

The difficult part was handling the priority, weight, and area at the same time.

I had to make sure that urgent deliveries are handled first, packages do not exceed the capacity, and deliveries from the same area are grouped when possible.

## Algorithm Limitations

The program uses a greedy algorithm. It makes a choice at each step instead of checking all possible combinations.

Because of this, it may not always find the minimum number of trips.

## Large Inputs

For a very large number of deliveries, the program may use a lot of memory.

Sorting the deliveries also takes more time.

## Extension

I added two extensions to the basic problem:

1. **Invalid delivery report:**
   Deliveries that are heavier than the capacity are saved in `invalid_deliveries_report.txt` instead of being ignored.

2. **User-selected capacity:**
   The user can enter the vehicle capacity instead of always using 10 kg.

## Possible Improvement

A possible improvement would be to change the problem into a **graph problem**.

The deliveries could be represented as nodes, and the connections between them could represent things like the same area, priority, or weight.

Then, optimization algorithms could be used to find better routes and possibly reduce the number of trips.
