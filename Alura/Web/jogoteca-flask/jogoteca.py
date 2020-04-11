from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from dao import JogoDao, UsuarioDao
from flask_mysqldb import MySQL
from models import Jogo, Usuario
import time
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

#Após configurar a aplicação é necessário importar as Viwes
from views import *
#O código só sera executado se o arquivo jogoteca for iniciado e não importado
if __name__ == '__main__':
    app.run(debug=True)
