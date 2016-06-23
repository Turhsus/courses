"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses = courses)

    def add(self):
        if (len(request.form['name']) > 15):
            newCourse = {}
            newCourse['name'] = request.form['name']
            newCourse['description'] = request.form['description']
            self.models['Course'].add_course(newCourse)
        else:
            flash("Course name too short or nonexistant!!")
        return redirect('/')

    def destroy(self, id):
        course = self.models['Course'].get_course(id)
        session['id'] = id
        return self.load_view('verify.html', course=course)

    def dont_delete(self):
        return redirect('/')

    def delete(self):
        self.models['Course'].delete_course(session['id'])
        session.clear()
        return redirect('/')

