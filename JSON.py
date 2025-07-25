#json stands for java script object notation
import json
student = { 
    "name": "Nisha",
    "age": 20,
    "subjects": ["Math", "Science", "English"],
    "grades": { "algebra": 90, "biology": 85, "history": 88 }
}
y=json.dumps(student)
print(y)