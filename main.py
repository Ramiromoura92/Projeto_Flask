from flask import Flask, request_started, render_template, request
import mysql.connector
import pandas as pd


app = Flask(__name__)

@app.route("/cadastro/", methods = ['POST'])
def cadastro():

    #dados = request_started.get_json() 
    nome = request.form['nome']
    sexo = request.form['sexo']
    altura = request.form['altura']
    nacionalidade = request.form['nacionalidade']
    
    con =  mysql.connector.connect(host = 'localhost', database = 'cadastro',user = 'root', password = 'ramiro1992')
    conexao = "INSERT INTO pessoas (nome, sexo, altura, nacionalidade) VALUES (%s,%s,%s,%s)"
    inp = (nome, sexo, altura, nacionalidade)
    cursor = con.cursor()
    cursor.execute(conexao,inp)
    con.commit()
    
    return "Registro inserido na tabela"

@app.route("/cadastro_get", methods = ['GET'])
def cadastro_get():

    

    
    con =  mysql.connector.connect(host = 'localhost', database = 'cadastro',user = 'root', password = 'ramiro1992')
    conexao = "SELECT * FROM cadastro.pessoas"
    cursor = con.cursor()
    cursor.execute(conexao)
    dados=[]
    for x in cursor:
        dados.append({
            'id':'{}'.format(x[0]),
            'nome':'{}'.format(x[1]),
            'nascimento':'{}'.format(x[2]),
            'sexo':'{}'.format(x[3]),
            'peso':'{}'.format(x[4]),
            'altura':'{}'.format(x[5]),
            'nacionalidade':'{}'.format(x[6]),
        })
    
        
    return render_template('return.html', the_result = dados)


@app.route('/')
def entry_page():
    return render_template('entry.html', the_title = 'Form Mysql')

app.run(debug = True)
