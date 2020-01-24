from flask_restful import Resource

list_skills = ['python', 'java', 'html', 'flask']

class skills(Resource):
    def get(self):
        return list_skills