from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

rutas = Blueprint('rutas', __name__)

@rutas.route("/")
def home():
    contacts = Contact.query.all()
    return render_template("index.html",contacts=contacts)

@rutas.route("/new", methods=["POST"])
def add_contact():
    fullname    =request.form['fullname']
    email       =request.form['email']
    phone       =request.form['phone']
    
    new_contact = Contact(fullname,email,phone)
    db.session.add(new_contact)
    db.session.commit()
    
    flash("Contact added successfully")
    return redirect(url_for('rutas.home'))

@rutas.route("/update/<id>", methods=["POST","GET"])
def update(id):
    contact         = Contact.query.get(id)
    if request.method == "POST":
        contact.fullname    = request.form['fullname']
        contact.email       = request.form['email']
        contact.phone       = request.form['phone']
        db.session.commit()        
        return redirect(url_for('rutas.home'))

    return render_template("update.html",id=id,contacts=contact)

@rutas.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    
    return redirect(url_for('rutas.home'))