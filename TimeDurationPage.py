# Time Duration Page

# Pandas table and Matplotlib line plot

# Comparing time durations of the Hash/Salt functions insertion and deletion using the hashlib python library in chart
# form.  These numbers will be compared to similar numbers with previous projects concerning arrays and linked lists.
# The time durations of a hundred, thousand, ten-thousand, and hundred-thousand random numbers will be compared.

# Main reference for the Matplotlip plot on this page:
# https://matplotlib.org/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py

# Other references:
# https://matplotlib.org/api/table_api.html?highlight=table#module-matplotlib.table
# https://matplotlib.org/gallery/index.html
# https://matplotlib.org/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py

import numpy as np
import xlrd
import pandas as pd
import matplotlib.pyplot as plt


# Creating a variable for data being pulled from the TimeDurationComparison.xlsx file and placed into array format
book = xlrd.open_workbook('TimeDurationComparison.xlsx')
sheets = book.sheets()
for sheet in sheets:
    data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

# Creating a variable for data to be transformed into excel file format
timeduration_df = pd.read_excel(book, index_col=None,
                                na_values=['NA'])

class Regression():
    def _showTable_(self):

        # Showing the data that was pulled from TimeDurationComparison.xlsx in array form
        print("\n\nData pulled from the excel file:\n\n", data, "\n\n")

        # Obtaining the shape of the data
        print("Data shape: ", data.shape, "\n\n")
        # Data shape:  (9, 4)

        # Showing the data that was pulled from TimeDurationComparison.xlsx in excel form
        print("Data put into excel format:\n\n", timeduration_df, "\n\n")

    # Reference for plot:
    # https: // matplotlib.org / gallery / lines_bars_and_markers / categorical_variables.html  # sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
    def _showPlot_(self):

        # Attempting to create a table and plot chart of the dataframe TimeDurationComparison.xlsx
        # using iloc (row and column slicing) for python, references:
        # https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
        # https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/
        # Rows 0-7 (0:8), and columns 1-3 (to take out column 0, shows as 1:4 in iloc) to show the main data in the
        # dataframe
        ###data = timeduration_df.iloc[0:8, 1:4]
        print("------- Splitting the dataframe into sections -------\n\nThe data of the dataframe:\n\n", data, "\n")

        # 1st data column, the Array column
        arrayVectorData = timeduration_df.iloc[:, 1]
        print("Array column: \n", arrayVectorData, "\n")

        # 2nd data column, the DoublyLinkedList column
        DblData = timeduration_df.iloc[:, 2]
        print("Doubly Linked List column: \n", DblData, "\n")

        # 3rd data column, the Binary Tree column
        BinData = timeduration_df.iloc[:, 3]
        print("Binary Tree column: \n", BinData, "\n")

        # 4th data column, the Hash/Salt column
        HashData = timeduration_df.iloc[:, 4]
        print("Hash/Salt column: \n", HashData, "\n")


        # This is the iloc to show the entire first column, the row labels, of the dataframe, for the label column
        rowLabels_ForData = timeduration_df.iloc[:, 0]
        print("The column of the dataframe:\n\n", rowLabels_ForData, "\n")

        # This is to pull the top label for the data only, with the variable set to call the index 0.
        # You can change the index to show more rows.
        columnLabels = data[0]
        print("Showing the header labels only:\n\n", columnLabels, "\n\n")


        # saving value creation for future reference
        # Creating values for the graph
        # Creating the values variable as increments 0.125 apart, between 0 and 1.625, so that the top level value
        # shows as 1.5
        # using np.arange(bottom level #, just above top level #, increment)
        # reference: https://appdividend.com/2019/01/31/numpy-arange-tutorial-with-example-python-numpy-functions/

        fig, ax = plt.subplots()

        ax.plot(rowLabels_ForData, arrayVectorData, label="Array")
        ax.plot(rowLabels_ForData, DblData, label="DblLinked")
        ax.plot(rowLabels_ForData, BinData, label="BST")
        ax.plot(rowLabels_ForData, HashData, label="Hash/Salt")
        ax.legend()
        # x and y axis labels
        plt.xlabel("Insertions and Deletions by Random Number\n")
        plt.ylabel("Amount of Time Duration in Seconds\n")
        # The top title (suptitle) and title descriptor(title)
        plt.suptitle("Duration in Seconds of Insertion and Deletion Functionality in Python")
        plt.title("\nArrays, Doubly Linked Lists, Binary Search Trees, and Hash/Salt Tables")

        plt.show()

        # Reference for plot:
        # https: // matplotlib.org / gallery / lines_bars_and_markers / categorical_variables.html  # sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py

Regression()

show = Regression()

# Calling methods
show._showTable_()
show._showPlot_()