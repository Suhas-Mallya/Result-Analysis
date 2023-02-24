from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

def analyze_total_marks(data, code, category="TM"):
    from matplotlib import pyplot as plt
    fig_name = "total_marks.png"
    tm = data[code + str(" - TOTAL MARKS")]

    stat = {
        "F": 0,
        "E": 0,
        "D": 0,
        "C": 0,
        "B": 0,
        "A": 0,
        "S": 0
    }

    for i in range(len(data)):
        if tm[i] < 40:
            stat["F"] += 1
        elif tm[i] < 45:
            stat["E"] += 1
        elif tm[i] < 60:
            stat["D"] += 1
        elif tm[i] < 70:
            stat["C"] += 1
        elif tm[i] < 80:
            stat["B"] += 1
        elif tm[i] < 90:
            stat["A"] += 1
        else:
            stat["S"] += 1

    # print(stat)
    # x = ["F (m<40)", "E (40<=m<45)", "D (45<=m<60)",
    #     "C (60<=m<70)", "B (70<=m<80)", "A (80<=m<90)", "S (m>=90)"]
    x = ['F', 'E', 'D', 'C', 'B', 'A', 'S']
    y = []
    for k, v in stat.items():
        y.append(v)

    plt.switch_backend('agg')
    plt.barh(x, y, color=['red', 'orange', 'blue', 'green', 'yellow'])

    for i, v in enumerate(y):
        plt.text(v+0.25, i, str(v), color='blue', fontweight='bold')

    plt.title(code + " - TOTAL MARKS")
    plt.autoscale()
    plt.ylabel("grades")
    plt.xlabel("no of students")
    # plt.xticks(rotation=30, ha='right')
    # plt.show()
    plt.axis("tight")

    plt.savefig('static/'+fig_name)
    plt.close()

def analyze_internal_marks(data, code):
    from matplotlib import pyplot as plt
    fig_name = "internal_marks.png"
    im = data[code + str(" - INTERNAL MARKS")]

    stat = {
        ">40": 0,
        "36-40": 0,
        "31-35": 0,
        "26-30": 0,
        "20-25": 0,
        "<=20": 0
    }

    for i in range(len(data)):
        if im[i] <= 20:
            stat["<=20"] += 1
        elif im[i] <= 25:
            stat["20-25"] += 1
        elif im[i] <= 30:
            stat["26-30"] += 1
        elif im[i] <= 35:
            stat["31-35"] += 1
        elif im[i] <= 40:
            stat["36-40"] += 1
        else:
            stat[">40"] += 1

    x = ['>40', '36-40', '31-35', '26-30', '20-25', '<=20']
    y = []
    for k, v in stat.items():
        y.append(v)

    plt.switch_backend('agg')
    plt.barh(x, y, color=(0.2, 0.4, 0.6, 0.6))

    for i, v in enumerate(y):
        plt.text(v+0.25, i, str(v), color='blue', fontweight='bold')

    plt.title(code + " - INTERNAL MARKS")
    plt.autoscale()
    plt.ylabel("internal marks")
    plt.xlabel("no of students")
    # plt.xticks(rotation=30, ha='right')
    # plt.show()
    plt.axis("tight")

    plt.savefig('static/'+fig_name)
    plt.close()

def analyze_external_marks(data, code):
    from matplotlib import pyplot as plt
    fig_name = "external_marks.png"
    em = data[code + str(" - EXTERNAL MARKS")]

    stat = {
        ">50": 0,
        "41-50": 0,
        "31-40": 0,
        "21-30": 0,
        "11-20": 0,
        "<=10": 0
    }

    for i in range(len(data)):
        if em[i] > 50:
            stat[">50"] += 1
        elif em[i] > 40:
            stat["41-50"] += 1
        elif em[i] > 30:
            stat["31-40"] += 1
        elif em[i] > 20:
            stat["21-30"] += 1
        elif em[i] > 10:
            stat["11-20"] += 1
        else:
            stat["<=10"] += 1

    x = ['>50', '41-50', '31-40', '21-30', '11-20', '<=10']
    y = []
    for k, v in stat.items():
        y.append(v)

    plt.switch_backend('agg')
    plt.barh(x, y, color=(0.2, 0.4, 0.6, 0.6))

    for i, v in enumerate(y):
        plt.text(v+0.25, i, str(v), color='blue', fontweight='bold')

    plt.title(code + " - EXTERNAL MARKS")
    plt.autoscale()
    plt.ylabel("external marks")
    plt.xlabel("no of students")
    # plt.xticks(rotation=30, ha='right')
    # plt.show()
    plt.axis("tight")

    plt.savefig('static/'+fig_name)
    plt.close()

def extract_from_headers(header):
    l = []
    for code in header:
        if code == "NAME" or code == "USN" or code == "CGPA" or code == "SGPA":
            continue
        l.append(code.split(" ")[0])

    codes = []
    for x in l:
        if x not in codes:
            codes.append(x)
    return codes

def get_class_result(dataset,code):
    data = [0,0]
    for i in range(len(dataset)):
        if dataset.iloc[i, dataset.columns.get_loc(code+" - RESULT")] == 'PASS':
            data[0] += 1
        else:
            data[1] += 1
    return data

def get_grades(data, code):
    from matplotlib import pyplot as plt
    fig_name = "grades.png"
    grade = data[code + str(" - GRADE")]

    stat = {
        "F": 0,
        "E": 0,
        "D": 0,
        "C": 0,
        "B": 0,
        "A": 0,
        "S": 0
    }

    for i in range(len(data)):
        if grade[i] == 'F':
            stat["F"] += 1
        elif grade[i] == 'E':
            stat["E"] += 1
        elif grade[i] == 'D':
            stat["D"] += 1
        elif grade[i] == 'C':
            stat["C"] += 1
        elif grade[i] == 'B':
            stat["B"] += 1
        elif grade[i] == 'A':
            stat["A"] += 1
        elif grade[i] == 'S':
            stat["S"] += 1

    x = ['F', 'E', 'D', 'C', 'B', 'A', 'S']
    y = []
    for k, v in stat.items():
        y.append(v)

    plt.switch_backend('agg')
    plt.barh(x, y, color=['red', 'orange', 'blue', 'green', 'yellow'])

    for i, v in enumerate(y):
        plt.text(v+0.25, i, str(v), color='blue', fontweight='bold')

    plt.title(code + " - GRADES")
    plt.autoscale()
    plt.ylabel("grades")
    plt.xlabel("no of students")
    # plt.xticks(rotation=30, ha='right')
    # plt.show()
    plt.axis("tight")

    plt.savefig('static/'+fig_name)
    plt.close()
    return stat
    
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/marks')
def marks():
    return render_template("home.html")
    
@app.route('/grades')
def grades():
    return render_template("home2.html")


@app.route('/grade')
def grade():
    args = request.args
    code = args.get('code')
    sub_codes = extract_from_headers(data.columns)
    stat = get_grades(data,code)
    class_res = [0,0]
    for k, v in stat.items():
        if k == 'F':
            class_res[1] = v
        else:
            class_res[0] += v

    sorted_data_sgpa = data.sort_values("SGPA", ascending=False)
    sorted_data_cgpa = data.sort_values("CGPA", ascending=False)

    top_sgpa = sorted_data_sgpa.head(5)
    bottom_sgpa = sorted_data_sgpa.tail(5)
    
    top_cgpa = sorted_data_cgpa.head(5)
    bottom_cgpa = sorted_data_cgpa.tail(5)

    return render_template("home2.html", cur_code=code, codes=sub_codes, res=class_res, top_cgpa=top_cgpa, top_sgpa=top_sgpa, bottom_cgpa=bottom_cgpa, bottom_sgpa=bottom_sgpa)

@app.route('/result')
def result():
    args = request.args
    code = args.get('code')
    sub_codes = extract_from_headers(data.columns)

    analyze_total_marks(data, code)
    analyze_internal_marks(data, code)
    analyze_external_marks(data, code)
    class_res = get_class_result(data,code)

    sorted_data = data.sort_values(code + " - TOTAL MARKS", ascending=False)
    top = sorted_data.head(5)
    bottom = sorted_data.tail(5)
    return render_template("home.html", cur_code=code, codes=sub_codes, res=class_res, top=top, bottom=bottom)

@app.route('/postgrade', methods=['POST'])
def postgrade():
    if request.method == 'POST':
        f = request.files['file']
        global data
        data = pd.read_excel(f)
        sub_codes = extract_from_headers(data.columns)        
        return render_template("home2.html", codes=sub_codes)

@app.route('/postmarks', methods=['POST'])
def postmarks():
    if request.method == 'POST':
        f = request.files['file']
        global data
        data = pd.read_excel(f)
        sub_codes = extract_from_headers(data.columns)        
        return render_template("home.html", codes=sub_codes)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
