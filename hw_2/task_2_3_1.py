import csv
from flask import Flask

app = Flask(__name__)

@app.route('/mean/')

def file_open():
    with open('hw.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #headers = next(spamreader, None)
        #print(headers)

        for index, row in enumerate(spamreader):
            w = []  # weight
            h = []  # height

            if index == 0:
                continue
            if row:
                str_lst = row
                #замена Weight(Pounds) для расчета - данные всех записей csv
                new_row = w.append(int(float(row[2]) // 1 * 0.453592))

                print(w)


                #замена Height(Inches) для расчета - данные всех записей csv
                new_row2 = h.append((int(float(str_lst[1].replace(',', '')) // 1 * 2.54)))
                #h = ''.join(new_row2)

                print(h)

                #print(row)

        return 'OK'


if __name__ == "__main__":
    app.run(port=5092)
