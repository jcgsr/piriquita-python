# 22.10.2019 terminado 26.10.2019
# meu primeiro webapp!!
# na Internet pela primeira vez em 28.10.2019

from flask import Flask, request


app = Flask(__name__)

def calcular(d, p, c):

    return d*p/c

@app.route('/', methods=['GET', 'POST'])
def calc():

    if request.method == 'GET': #cria as entradas
        return '''
         <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta charset="utf-8">
    <title>Piriquita WebApp</title>
    <style type="text/css">
      body {
        background-color: #FFC0CB;
      }

    </style>
    </head>
    <body>
        <h1>WebApp de Jhunya Francine</h1>
        <h2>Graduanda em Veterinária pela UFS</h2>
        <p> Informe a dose, o peso <br />e a concentração nos campos abaixo respectivamente:</p>
            <form method="post">
                <input type="text" name="d" />
                <input type="text" name="p" />
                <input type="text" name="c" />
                <input type="submit" value="calcular" />

            </form>
            </body>
            </html>
        '''
    if request.method == 'POST': #salva as variáveis informadas
        dR = float(request.form.get('d'))
        pR = float(request.form.get('p'))
        cR = float(request.form.get('c'))

        res = calcular(dR, pR, cR)
        return '''
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Resultado</title>
        <style>
        body{
        background-color: #FFC0CB

        }
        </style>
            <h1>A dosagem é: <b>%.1f</b></h1>''' % res





if __name__ == '__main__':
    app.run(debug=True)

