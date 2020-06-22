import csv
from flask import Flask
#from statistics import median

app = Flask(__name__)

@app.route('/mean/')

def file_open():
    with open('hw.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        w = []  # weight
        h = []  # height

        for index, row in enumerate(spamreader):

            if index == 0:
                continue
            if row:
                str_lst = row
                #замена Weight(Pounds) для расчета - данные всех записей csv
                w.append(int(float(row[2]) // 1 * 0.453592))

                #замена Height(Inches) для расчета - данные всех записей csv
                h.append((int(float(str_lst[1].replace(',', '')) // 1 * 2.54)))

    av_h = sum(h) / len(h)
    #min_h = min(h)
    #max_h = max(h)
    #median_h = median(h)

    av_w = sum(w) / len(w)
    #min_w = min(w)
    #max_w = max(w)
    #median_w = median(w)
    return f'height av: {av_h}; weight av: {av_w}'



if __name__ == "__main__":
    app.run(port=5092)