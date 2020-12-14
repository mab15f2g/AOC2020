# 1
with open("map", 'r') as f:
    lines=f.readlines()

current_x = 0

pos_x = 3
pos_y=1

counter = 0
for curr_y, each_line in enumerate(lines):
    if each_line[current_x] == "#":
        counter+=1
    current_x = (current_x + pos_x) % len(each_line[:-1])
print(f"Star1 1:{trees}")

#2
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
mult_trees=1
for slope in slopes:
    print("Slope: ", slope)
    pos_x, pos_y=slope
    counter = 0
    current_x = 0
    for curr_y, each_line in enumerate(lines):
        if curr_y%pos_y == 0:
            if each_line[current_x] == "#":
                counter+=1
            current_x = (current_x + pos_x) % len(each_line[:-1])
    print("Trees: ", counter)
    mult_trees*=counter
print("Star2: ", mult_trees)