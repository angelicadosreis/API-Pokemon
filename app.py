from flask import Flask, request, render_template, make_response
import json
import requests


app = Flask(__name__)

@app.route('/')
def display_gui():
    return render_template('index.html')

@app.route('/consultar', methods=['POST'])
def check():
    pokemon = request.form['pokemon']
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon)
    info = requests.request('GET',url)
    info = info.json()
    abilities = info['abilities']

    lista=[]
    lista2=[]

    for i in range(len(abilities)):
        ability = abilities[i]['ability']
        lista.append(ability)
    for i in range(len(lista)):
        habilidade = lista[i]['name']
        lista2.append(habilidade)
    return render_template('index.html', lista=lista2)

if __name__ == '__main__':
    app.run(debug=True)
