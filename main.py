import webapp2
from google.appengine.api import users
import jinja2
import os

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    undefined=jinja2.StrictUndefined,
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("index.html")
        self.response.write(results_template.render())
        # user = users.get_current_user()
    #     if user:
    #         # results_template = jinja_current_directory.get_template("templates/index.html")
    #         # self.response.write(results_template.render())
    #     else:
    #         self.redirect("/nouser")
    #
    # def post(self):
    #     pass

# class ReceiverHandler(webapp2.RequestHandler):
#     def post(self):
#         results_template = jinja_current_directory.get_template("templates/things.html")
#         users_name = self.request.get("username")
#         template_vars = {"name": users_name}
#         user = users.get_current_user()
#         nickname = user.nickname()
#
#         logout_url = users.create_logout_url("/")
#         self.response.write("Hello " + nickname + '. <a href = "' + logout_url + '">Logout here</a>')
#         self.response.write(results_template.render(template_vars))

# class ToDoListHandler(webapp2.RequestHandler):
#     def post(self):
#         results_template = jinja_current_directory.get_template("templates/todolist.html")
#         self.response.write(results_template.render())

# class HealthHandler(webapp2.RequestHandler):
#     def get(self):
#         results_template = jinja_current_directory.get_template("templates/health.html")
#         self.response.write(results_template.render())

# class NoUserHandler(webapp2.RequestHandler):
#     def get(self):
#         login_url = users.create_login_url("/")
#         self.response.write('You are not logged in! Login here: <a href="' + login_url + '">click here</a>')


app = webapp2.WSGIApplication([
("/", MainHandler),
# ("/receiver", ReceiverHandler),
# ("/nouser", NoUserHandler),
# ("/todolist" ToDoListHandler),
], debug=True)
