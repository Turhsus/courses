from system.core.model import Model

class Course(Model):
	def __init__(self):
		super(Course, self).__init__()

	def add_course(self, course):
		query = "INSERT INTO courses (name, description, created_at, updated_at) VALUES (:name, :description, NOW(), NOW())"
		data = {
			'name': course['name'],
			'description': course['description']
		}
		print "Just before query"
		return self.db.query_db(query, data)

	def get_all_courses(self):
		return self.db.query_db("SELECT * FROM courses")

	def get_course(self, id):
		query = "SELECT * FROM courses WHERE id = :id"
		data = {
			'id': id
		}
		return self.db.query_db(query, data)

	def delete_course(self, id):
		query = "DELETE FROM courses WHERE id = :id"
		data = {
			'id': id
		}
		return self.db.query_db(query, data)