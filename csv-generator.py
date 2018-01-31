import csv


def save_dict_to_csv(data, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def create_sample_table(rows=10, columns=10):
    headers = ['header ' + str(n) for n in range(columns)]
    values = [['row %d col %d' % (row, n) for n in range(columns)] for row in range(1, rows)]
    return [headers] + values


if __name__ == "__main__":
    save_dict_to_csv(
        data=create_sample_table(rows=10, columns=1030),
        path='data-files/csv/1030_columns.csv'
    )
