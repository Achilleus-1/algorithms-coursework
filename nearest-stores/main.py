import csv
import random
import sys
from haversine import haversine


 #Project 2 by , 

# Our "Rand-Select() algorithm" according to how we percieved it from class.
def rand_partition(arr, left, right):

#grabs the first element here.  randomly chooses a pivot with random.randint and partitions the list
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]  # swaps the pivot to the end instead of the start as said... if thats okay.
    pivot = arr[right][0]
    i = left - 1


    for j in range(left, right): # compares based on the distance, aka first element in each group, not againsts two  store objects. so that meets the requirement
        if arr[j][0] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1



def rand_select(arr, left, right, k):
    #uses partition to recursively find the kth smallest distance. Is O(n)
    if left == right:
        return arr[left]
    pivot_index = rand_partition(arr, left, right)  # Uses Rand-Partition here
    order = pivot_index - left + 1  # actual rank of pivot inside subarray
    if k == order:
        return arr[pivot_index]
    elif k < order:
        return rand_select(arr, left, pivot_index - 1, k)
    else:
        return rand_select(arr, pivot_index + 1, right, k - order)



def quickselect(arr, k):
# partitions with Rand-Select
    if k < 1 or k > len(arr):
        return None
    # calls the algo to ensure kth element is in correct spot
    rand_select(arr, 0, len(arr) - 1, k)
    # arr[0:k] now has the smallest k, returns it
    return arr[:k]


#we make sure sorted subset is then output in the required order, like we need. only the top "i" items even though we use pythons builtin sort if thats ok



# code for data reading functions
def read_store_data(filename):
#reads and parses all csv data. skips header.

    stores = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # for header
            for row in reader:
                if len(row) < 7:
                    continue  # skip unused rows
                store = {
                    'id': row[0].strip(),
                    'address': row[1].strip(),
                    'city': row[2].strip(),
                    'state': row[3].strip(),
                    'zip': row[4].strip(),
                    'lat': float(row[5].strip()),
                    'lon': float(row[6].strip())
                }
                stores.append(store)
    except Exception as e:
        print("Error reading {}: {}".format(filename, e), file=sys.stderr)
        sys.exit(1)
    return stores





def read_queries(filename):
#reads and parses queries
    queries = []
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) < 3:
                    continue  # skips unused lines

                try:
                    lat = float(row[0].strip())
                    lon = float(row[1].strip())
                    num_stores = int(row[2].strip())
                    queries.append((lat, lon, num_stores))

                except ValueError:
                    continue  # skip rows with invalid numbers, error fixings
    except Exception as e:
         print("Error reading {}: {}".format(filename, e), file=sys.stderr)
         sys.exit(1)
    return queries




# function for exporting out info PER company
def process_queries_for_company(company_name, store_data, queries):
    #first computes the distances from the query point to each store
    #uses our hopefully working "Rand-Select" to obtain the k closest stores, sorts them closest to furthest
    #company_name formats the header for store name and store num based on typee
    if company_name.lower() == "whataburger":
        header_template = "The {k} closest Stores to ({lat}, {lon}):"
    else:
        header_template = "The {k} closest stores to ({lat}, {lon}):"


    for query in queries:
        query_lat, query_lon, k = query

        # pulls and computes distance per store from query file
        distance_list = []
        for store in store_data:
            d = haversine(query_lat, query_lon, store['lat'], store['lon'])
            distance_list.append((d, store))


        # Uses tge randselect to find the kth smallest here
        closest = quickselect(distance_list, k)
        if closest is None:
            continue

# sorts for distance
        closest_sorted = sorted(closest, key=lambda x: x[0])


        #header printer
        print("{} ".format(company_name) + header_template.format(k=k, lat=query_lat, lon=query_lon))
        for entry in closest_sorted:
            d, store = entry
            print(
                "{} Store #{}. {}, {}, {}, {}. - {:.2f} miles.".format(
                    company_name,
                    store['id'],
                    store['address'],
                    store['city'],
                    store['state'],
                    store['zip'],
                    d
                )
            )
        print()




def main():
    # hardcoded the csv files
    whataburger_file = "WhataburgerData.csv"
    starbucks_file = "StarbucksData.csv"
    queries_file = "Queries.csv"


    # reads said hardcoded csv files
    whataburger_data = read_store_data(whataburger_file)
    starbucks_data = read_store_data(starbucks_file)
    #reads queries file here
    queries = read_queries(queries_file)


    # for every query, process BOTH Whataburger and Starbucks data. instructions didnt specify so we did both to ensure best correctness. open to change if needed.
    for query in queries:
        process_queries_for_company("Whataburger", whataburger_data, [query])
        process_queries_for_company("Starbucks", starbucks_data, [query])


if __name__ == "__main__":
    main()
