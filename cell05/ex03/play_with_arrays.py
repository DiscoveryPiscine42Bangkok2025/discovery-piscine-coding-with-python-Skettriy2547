original_array = [2, 8, 9, 48, 8, 22, -12, 2]

processed_array = []

print(original_array)

for number in original_array:
    if number > 5:
        processed_array.append(number + 2)

unique_array = list(set(processed_array))

print(unique_array)