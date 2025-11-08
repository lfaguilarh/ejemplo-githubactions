from flask import Blueprint, request, render_template, redirect, url_for, flash

from models.notas.notas import Notas
from utils.db import db

notas = Blueprint('notas',__name__,template_folder='templates')

@notas.route('/notas', methods=['GET'])
def ver_notas():
    notas = Notas.query.all()
    return render_template('notas/notas.html', notas=notas)

@notas.route('/crear_nota', methods=['GET','POST'])
def crear_nota():
    error = None
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        if not titulo:
            error = 'Debes ingresar un titulo'
        elif not descripcion:
            error = 'Debes ingresar una descripción'
        else:
            nota = Notas(titulo,descripcion)
            db.session.add(nota)
            db.session.commit()
            return redirect(url_for('notas.ver_notas'))
    return render_template('notas/crear.html', error = error)

@notas.route('/actualizar_nota/<id>', methods=['GET','POST'])
def actualizar_nota(id):
    nota = Notas.query.get(id)
    if request.method == 'POST':
        nota.titulo = request.form.get('titulo')
        nota.descripcion = request.form.get('descripcion')
        db.session.commit()
        return redirect(url_for('notas.ver_notas'))
        
    return render_template('notas/actualizar.html', nota = nota)

@notas.route('/borrar_nota/<id>', methods=['GET','POST'])
def borrar_nota(id):
    nota = Notas.query.get(id)
    db.session.delete(nota)
    db.session.commit()
    return redirect(url_for('notas.ver_notas'))


    