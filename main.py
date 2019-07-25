import webapp2
from google.appengine.api import users
import jinja2
import os

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    undefined=jinja2.StrictUndefined,
    autoescape=True)

class RedirectHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/index.html")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            results_template = jinja_current_directory.get_template("/templates/index.html")
            user = users.get_current_user()
            nickname = user.nickname()
            template_vars = {"username": nickname}
            self.response.write(results_template.render(template_vars))
        else:
            self.redirect("/nouser")

class ToDoListHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/todolist.html")
        self.response.write(results_template.render())

class HealthHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/health.html")
        self.response.write(results_template.render())

class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/settings.html")
        self.response.write(results_template.render())

        username = self.request.get("first-name")
        birthday = self.request.get("month"+"day")
        timeZone = self.request.get("time_zone")
        bedTime = self.request.get("bed_time")
        health = self.request.get("health_priority")
        mood = self.request.get("mood")
        
        logout_url = users.create_logout_url("/index.html")
        self.response.write("Hello " + '! <a href = "' + logout_url + '">Logout here</a>')

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/about_us.html")
        self.response.write(results_template.render())

class NoUserHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url("/index.html")
        self.response.write('You are not logged in! Login here: <a href="' + login_url + '">click here</a>')

# class ReceiverHandler(webapp2.RequestHandler):
#     def get(self):
#         self.redirect("/index.html")
#         # results_template = jinja_current_directory.get_template("templates/things.html")
#         # users_name = self.request.get("username")
#         # template_vars = {"name": users_name}
#         # user = users.get_current_user()
#         # nickname = user.nickname()
#         #
#         # logout_url = users.create_logout_url("/")
#         # self.response.write("Hello " + nickname + '. <a href = "' + logout_url + '">Logout here</a>')
#         # self.response.write(results_template.render(template_vars))

app = webapp2.WSGIApplication([
("/", RedirectHandler),
("/index.html", MainHandler),
("/todolist.html", ToDoListHandler),
("/health.html", HealthHandler),
("/settings.html", SettingsHandler),
("/about_us.html", AboutUsHandler),
("/nouser", NoUserHandler),
# ("/receiver", ReceiverHandler),
], debug=True)
