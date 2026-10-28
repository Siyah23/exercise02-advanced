x = int(input("enter an integer for x: "))
y = int(input("enter an integer for y: "))
z = int(input("enter an integer for z: "))

is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50
final_condition = is_even and is_positive and is_in_range
print(final_condition)