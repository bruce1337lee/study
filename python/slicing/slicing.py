# [start:stop:increment]
# slice(start, stop, increment)

# slicing arrays
print("\n")

def get_arr():
     return [0,1,2,3,4,5,6,7,8,9]

arr = get_arr()

print("arr")
print(arr)

print("arr[0:len(arr)]")
print(arr[0:len(arr)])

print("arr[0:len(arr):-1]")
print(arr[len(arr):0:-1])

# slicing tuple
print("\n")

def get_tup():
    return (0,1,2,3,4,5,6,7,8,9)

tup = get_tup()

print("tup")
print(tup)

print("tup[1:3]")
print(tup[1:3])

print("tup[1:2]")
print(tup[1:2])

print("len(tup)")
print(len(tup))

print("tup[1:1]")
print(tup[1:1])


