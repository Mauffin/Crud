#classe y querys
from pickle import FALSE
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
import re #importamos expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class User:

    def __init__(self,data):
        self.id = data['id']
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.email =data['email']
        self.password =data['password']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def save(cls,data):
        query='INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)'
        result = connectToMySQL('registro').query_db(query,data)
        return result 

    @staticmethod
    def valida_usuario(user):
        
        es_valido = True
        #validar mi nombre sea mayor a 3 caracteres
        if len(user['first_name']) < 3:
            flash('nombre debe de tener almenos 3 caracteres','register')
            es_valido = False

        if len(user['last_name']) < 3:
            flash('apellido debe de tener almenos 3 caracteres','register')
            es_valido = False
        
        if not EMAIL_REGEX.match(user['email']):
            flash('email invalido')
            es_valido = False

        if len(user['password']) < 6:
            flash('contrasena debe tener almenos 6 caracteres','register')
            es_valido = False
        
        if user['password'] != user['confirm']:
            flash('contrasena no coinciden','register')
            es_valido = False

        query = "select * from  users WHERE email = %(email)s"
        result = connectToMySQL('registro').query_db(query,user)
        if len(result) >= 1:
            flash('email registrado previamente')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('registro'). query_db(query,data)
        usr = result[0]
        user = cls(usr)
        return user

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('registro'). query_db(query,data)
        if len(result) < 1:
            return False
        else:
            usr = result[0]
            user = cls(usr)
            return user
