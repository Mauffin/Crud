from flask_app.config.mysqlconnection import connectToMySQL

class Classroom:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []
    
    @classmethod
    def muestra_salones(cls):
        query = "SELECT * FROM classrooms"
        result = connectToMySQL('esquema_usuarios').query_db(query)
        classrooms = []
        for c in result:
            classrooms.append(cls(c))
        return classrooms
    
    @classmethod
    def muestra_salon(cls, data):
        #data = {"id": "1"}
        query = "SELECT * FROM classrooms WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        # [
        #    {1, Python, 2022-03-10, 2022-03-10}
        # ]
        sal = result[0]
        salon = cls(sal)
        return salon

    @classmethod
    def muestra_salon_2(cls, id):
        data = {"id": id}
        query = "SELECT * FROM classrooms WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        # [
        #    {1, Python, 2022-03-10, 2022-03-10}
        # ]
        sal = result[0]
        salon = cls(sal)
        return salon 