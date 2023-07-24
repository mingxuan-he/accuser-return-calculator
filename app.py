from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    r_t = None
    r_f = None
    p_cfp = None
    p_ctp = None
    alpha = None

    if request.method == 'POST':
        p_ctp = int(request.form.get('p_ctp')) 
        p_cfp = int(request.form.get('p_cfp'))
        alpha = float(request.form.get('alpha'))

        if not p_ctp or not p_cfp or not alpha:
            return render_template("home.html", error="Please enter all values")

        r_t = round(100*((alpha/10 + 1) * p_ctp/100 - 1), 1)
        r_f = round(100*((alpha/10 + 1) * p_cfp/100 - 1), 1)
        alpha_scaled = alpha/10
    return render_template('home.html', r_t=r_t, r_f=r_f, p_ctp=p_ctp, p_cfp=p_cfp, alpha=alpha)

    
if __name__ == '__main__':
    app.run(debug=True)