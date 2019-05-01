from flask import Flask, render_template, request

app = Flask(__name__)

postai1 = [
    {
        'autorius': 'Tomas',
        'pavadinimas': 'Blogas NR1',
        'turinys': 'Pirmo blogo turinys',
        'paskelbimo_data': '2019.04.02'
    },
    {
        'autorius': 'Petras',
        'pavadinimas': 'Blogas NR2',
        'turinys': 'Antro blogo turinys',
        'paskelbimo_data': '2019.04.03'
    }
]


@app.route('/')
@app.route('/home') #falibuti pora route bet ji vistiek paleis ta pacia funkcija
def index():
    return render_template('home.html', postai2 = postai1)
    
@app.route('/about')

def about():
    return render_template('about.html', title='Apie mane')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        return render_template('contact.html', title='Kontaktai')
    elif request.method == "POST":
        asmens_vardas = request.form.get('asmens-vardas')
        asmens_pastas = request.form.get('asmens-pastas')
        asmens_zinute = request.form.get('asmens-zinute')

        print(asmens_vardas)
        print(asmens_pastas)
        print(asmens_zinute)
        return render_template('success.html')






if __name__ == '__main__':
    app.run(debug = True)