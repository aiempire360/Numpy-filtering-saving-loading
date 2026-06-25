import numpy as np
#filtering
marks = np.array ( [[44, 27, 89, 30, 55],[92,77,44, 23, 56,]])

passStudents = marks [marks > 50]
print(passStudents)

failStudents = marks [marks < 50]
print(failStudents)
cGrade = marks [(marks >= 50) & (marks < 60)]
print(cGrade)
bGrade = marks [(marks >= 70) & (marks < 80)]
print(bGrade)
aGrade = marks [(marks >= 80) & (marks < 100)]
print(aGrade)

# saving & loading arrays

marks1 = np.array ( [[44, 27, 89, 30, 55],
                     [92,77,44, 23, 56,]])
marks2 = np.array ( [[42, 12, 39, 30, 95],
                     [12,27,84, 93, 36,]])

np.savez('multiplemarks', marks1, marks)

np.savez('multiplemarks_compressed', marks1, marks)

print("saving marks.....")
array = np.load("multiplemarks_compressed.npz")

newMarks = array["arr_0"]
newMarks2 = array["arr_1"]

print(newMarks)
print(newMarks2)


array = np.load('C:\\PythonProject\\marks.npy')
print(array)
