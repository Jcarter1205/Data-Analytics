import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3,10)
pi = math.pi

# Calculations using the sample of 75 numbers

sample_sum = sum(vals_sample)

sample_average = statistics.mean(vals_sample)

sample_median = statistics.median(vals_sample)

# Calculations using the 200 randomly selected numbers

choices_average = statistics.mean(vals_choices)

choices_median = statistics.median(vals_choices)

choices_mode = statistics.mode(vals_choices)

choices_stdev = statistics.stdev(vals_choices)

choices_variance = statistics.variance(vals_choices)

# Calculate the area of a circle

circle_area = pi * radius ** 2

area_rounded_up = math.ceil(circle_area)

area_rounded_down = math.floor(circle_area)

# Display the sample statistics
print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_average}")
print(f"Median of 75 sample values: {sample_median}")

print('\n')

# Display the statistics for 200 values
print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {choices_average}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")

print('\n')

# Display the circle calculations
print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_rounded_up} (rounded up)")
print(f"Radius = {radius}, area = {area_rounded_down} (rounded down)")