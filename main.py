import statistics as stats


def convert_String_into_array(data):
    raw_data = data.split(" ")
    int_data = [int(num) for num in raw_data]
    return int_data


def calculate_arithmetic_mean(data):
    return sum(data) / len(data)


def calculate_harmonic_mean(data):
    return len(data) / sum(1.0 / datum for datum in data)


def calculate_geometric_mean(data):
    product = 1
    for datum in data:
        product *= datum
    return product ** (1 / len(data))


def calculate_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        mid1 = data[n // 2]
        mid2 = data[n // 2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = data[n // 2]
    return median


def find_mode(data):
    return stats.mode(data)


print("Enter Data (Seperated by Spaces): ")
user_data = input().strip()
int_data = convert_String_into_array(user_data)
while True:
    print("1. Arithmetic mean")
    print("2. Harmonic mean")
    print("3. Geometric mean")
    print("4. Median")
    print("5. Mode")
    print("6. Exit Program")
    print("Select Operation: ", end="")
    selection = int(input().strip())
    if selection == 1:
        print("The Arithmetic mean is:", calculate_arithmetic_mean(int_data))
    elif selection == 2:
        print("The Harmonic mean is:", calculate_harmonic_mean(int_data))
    elif selection == 3:
        print("The Geometric mean is:", calculate_geometric_mean(int_data))
    elif selection == 4:
        print("The Median is:", calculate_median(int_data))
    elif selection == 5:
        print("The mode is:", find_mode(int_data))
    elif selection == 6:
        break
    else:
        print("**Invalid Choice**")
