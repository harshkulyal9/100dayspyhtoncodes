student={
    "names":"harsh",
    "SAP":590024485,
    "subjects":{
      'physics':7,
      "AEM-1" : 8,
      "c programing":7,
      "problem solving":10

    }
}
print(f"{student}")
print(f"{student['subjects']}")
student["names"]="tanmay"
student["subjects"]
print(f"{student}")

print(f"{student.keys()}")
print(f"{student.items()}")
print(f"{student.values()}")
print(f"{student['subjects'].values()}")