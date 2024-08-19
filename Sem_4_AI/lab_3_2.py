import pandas as pd

myData = {
    'Subjects': ['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 'Chemistry'],
    'Book_Authors': ['RD Sharma', 'DC Pandey', 'OP Tandon', 'SL Loney', 'HC Verma', 'MS Chouhan'],
    'No_of_Books': [20, 5, 4, 3, 14, 17]
}

IIITG_Library = pd.DataFrame(myData)
print("IIITG_Library")
print(IIITG_Library)
print("-----------------------------------------------------------------------------------------")
print("Number of books for each subject:")
books_per_subject = IIITG_Library.groupby('Subjects')['No_of_Books'].sum()
print(books_per_subject)