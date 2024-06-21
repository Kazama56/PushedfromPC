# get()
# update()
# keys()
# values()
# items()
# pop()
 
student = {"name": "Jane", "age": 12, "address": "KTM"}
# roll = student["roll"]  # KeyError
# print(roll)  #
 
 
# get()
roll = student.get("roll")
print(roll)  # None
 
name = student.get("name", "Ram")
print(name)  # Jane
 
 
# update()
student = {"name": "Jane", "age": 12, "address": "KTM"}
student.update(name="Jon")
print(student)
 
student.update({"age": 30, "roll": 3})
print(student)  # {"name": "Jon", "age": 30, "address": "KTM", "roll": 3}
 
 
# keys
student = {"name": "Jane", "age": 12, "address": "KTM"}
print(student.keys())  # dict_keys(["name", "age", "address"])
keys = student.keys()
print(keys) # dict_keys(["name", "age", "address"])
# k = keys[0]  # This raises error because this is not list/tuple/string
 
 
keys = list(student.keys())
print(keys)  # ["name", "age", "address"]
 
k = keys[0]
print(k)  # "name"
 
 
# values
student = {"name": "Jane", "age": 12, "address": "KTM"}
values = student.values()
print(values)  # dict_values(["Jane", 12, "KTM"])
 
values = list(values)
print(values)  # ["Jane", 12, "KTM"]
 
 
# # items()
# student = {"name": "Jane", "age": 12, "address": "KTM"}
# items = student.items()
# print(items) #dict_items([('name', 'Jane'), ('age', 12), ('address', 'KTM')])
# a = items[2][1]
# print(a)


student = {"name": "Jane", "age": 12, "address": "KTM"}
data = student.pop("name")
print(student)


students = {
    "student1":{"name": "Jon", "age": 30, "address": "KTM"},
    "student2":{"name": "Jane", "age": 30, "address": "BKT"},
    "student3":{"name": "Alex", "age": 21, "address": "LTP"},
    }

students.pop("student2")
print(students)

x = students.get("student2")
u = x.pop("address")
print(u)