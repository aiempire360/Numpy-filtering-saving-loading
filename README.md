# NumPy Filtering, Saving, and Loading Arrays

This project demonstrates how to filter NumPy arrays using conditions and how to save and load arrays from files.

## Topics Covered

### Array Filtering

Filter data using comparison operators and Boolean indexing.

```python
marks[marks > 50]
marks[marks < 50]
```

### Grade Classification

Select students based on score ranges.

#### C Grade Students

```python
marks[(marks >= 50) & (marks < 60)]
```

#### B Grade Students

```python
marks[(marks >= 70) & (marks < 80)]
```

#### A Grade Students

```python
marks[(marks >= 80) & (marks < 100)]
```

### Boolean Indexing

Use logical conditions to extract specific values from arrays.

```python
marks[marks > 50]
```

### Saving Multiple Arrays

Store multiple NumPy arrays in a single file using `.npz` format.

```python
np.savez('multiplemarks', marks1, marks2)
```

### Loading Saved Arrays

Load previously saved arrays from disk.

```python
array = np.load("multiplemarks.npz")
```

### Accessing Saved Arrays

Retrieve arrays stored inside an `.npz` file.

```python
array["arr_0"]
array["arr_1"]
```

### Loading Single Arrays

Load arrays stored in `.npy` format.

```python
np.load("marks.npy")
```

## Learning Objectives

By completing this project, you will learn:

* How Boolean filtering works in NumPy
* How to apply multiple conditions using logical operators
* How to categorize data using filtering rules
* How to save arrays to files
* How to load arrays from files
* How `.npy` and `.npz` file formats work
* How to access multiple arrays stored in a single file

## Technologies Used

* Python
* NumPy

## Skills Practiced

* Data filtering
* Boolean indexing
* Conditional selection
* File handling with NumPy
* Data persistence
* Array storage and retrieval

## Example Use Cases

* Student result analysis
* Grade classification systems
* Data preprocessing
* Saving machine learning datasets
* Working with large numerical datasets

This project is designed for beginners learning NumPy and demonstrates practical techniques for filtering, storing, and retrieving numerical data efficiently.
