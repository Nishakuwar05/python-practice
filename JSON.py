#json stands for java script object notation
import json
student = { 
    "name": "Nisha",
    "age": 20,
    "subjects": ["Math", "Science", "English"],
    "grades": { "algebra": 90, "biology": 85, "history": 88 }
}
y=json.dumps(student,indent=4,sort_keys=True)#convert python object to json string
print(y) #indent is used to make the json string more readable
z='{"name": "Nisha","age": 20, "subjects": ["Math", "Science", "English"], "grades": {"algebra": 90, "biology": 85, "history": 88}}'
x=json.loads(z)#covert json string to python object
print(x)