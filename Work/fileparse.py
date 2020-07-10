# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            # Read the file headers
            headers = next(rows)
        else:
            headers = []
        # If a column selector was given, find indices of the specified columns.
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if select:
                row = [ row[index] for index in indices ]
            # Apply type conversion to the row
            if types:
                row = [func(val) for func, val in zip(types, row) ]

            # Make a dictionary or a tuple depending on headers
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
                
            records.append(record)

    return records