from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
# Constants


def calculate():
    try:
        a = int(request.form['C'])
        b = int (request.form['H'])
        c = int (request.form['N'])
        d = int (request.form['O'])
        hof = float (request.form['delta_H_c'])
        dens = float(request.form['dens'])

        CW = 12.011
        HW = 1.00794
        NW = 14.00674
        OW = 15.9994
        # Calculate molecular weight (MW)
        MW = (a * CW) + (b * HW) + (c * NW) + (d * OW)

        # Determine the value of j
        if d >= (2 * a) + (b / 2):
            j = 1
        elif d >= (b / 2):
            j = 2
        else:
            j = 3

        # Perform calculations based on the value of j
        if j == 1:
            N = (b + 2 * d + 2 * c) / (4 * MW)
            M = (4 * MW) / (b + 2 * d + 2 * c)
            Q = ((28.9 * b) + (94.05 * a) + (0.239 * hof)) * 1000 / MW
            det = (1.01 * ((N * (M ** -0.31) * (Q ** 0.7)) ** 0.26) * (1 + (1.3 * dens)) * 1000) * 2.5787 - 1487.8
            P = -7.225763889 * ((d * OW) / MW) + 1.073014648 * (
            (1.558 * (dens ** 2) * N * (M ** 0.5) * (Q ** 0.5))) + 0.874638096
        elif j == 2:
            N = (b + 2 * d + 2 * c) / (4 * MW)
            M = ((56 * c) + (88 * d) - (8 * b)) / (b + 2 * d + 2 * c)
            Q = ((28.9 * b) + (94.05 * ((d / 2) - (b / 4))) + (0.239 * hof)) * 1000 / MW
            det = (1.01 * ((N * (M ** -0.31) * (Q ** 0.7)) ** 0.26) * (1 + (1.3 * dens)) * 1000) * 2.5787 - 1487.8
            P = -7.225763889 * ((d * OW) / MW) + 1.073014648 * (
            (1.558 * (dens ** 2) * N * (M ** 0.5) * (Q ** 0.5))) + 0.874638096
        elif j == 3:
            if d > 0:
                N = (b + c) / (2 * MW)
                M = ((2 * b) + (28 * c) + (32 * d)) / (b + c)
                Q = ((49 * d) + (4 * a) + (6 * c) + (0.239 * hof)) * 1000 / MW
                det = ((1.01 * ((N * (M ** 0.5) * (Q ** 0.5)) ** 0.5) * (1 + (1.3 * dens)) * 1000)) * 0.897 + 1121.1
                Q = ((57.8 * d) + (0.239 * hof)) * 1000 / MW
                P = ((1.558 * (dens ** 2) * N * (M ** 0.5) * (Q ** 0.5))) * 0.951658083 + 7.459693403 * (
                            (c * NW) / MW) - 2.323132420
            else:
                N = (b + c) / (2 * MW)
                M = ((2 * b) + (28 * c) + (32 * d)) / (b + c)
                Q = ((38 * a) + (13 * b) + (2 * c) + (0.239 * hof)) * 1000 / MW
                det = (1.01 * ((N * (M ** 0.5) * (Q ** 0.5)) ** 0.5) * (1 + (1.3 * dens)) * 1000) * 1.4756 - 4790.6
                det = -11.720125876 * a + 5.214484019 * b + 7.929257396 * c - 1021.430356125 * (
                            a * CW / MW) + 1416.751937871 * (b * HW / MW) + 1062.019268865 * (
                                  c * NW / MW) + 0.124474682 * hof + 1671.064704905 * dens + 0.681165087 * det - 882.755600027
                Q = ((57.8 * d) + (0.239 * hof)) * 1000 / MW
                P = 18.763928137 * dens - 3.597483720 * (
                            ((a * 6) + (b * 1) + (c * 7) + (d * 8)) / (a + b + c + d)) + 0.830623881 * (
                    (1.558 * (dens ** 2) * N * (M ** 0.5) * (Q ** 0.5))) - 5.140535928

        return render_template('result.html', D=det, P=P, C=a, H=b, N=c, O=d, delta_H_c=hof, dens=dens)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
