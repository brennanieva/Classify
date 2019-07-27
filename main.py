import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import os
from datastore_stuff import ToDoList
from seed_data import seed_datas
# from google.cloud import datastore
# from datastore import ToDoList
# Retrieve Datastore
# client = datastore.Client()
# product_key = client.key('Product', 123)
# print(client.get(product_key))

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    undefined=jinja2.StrictUndefined,
    autoescape=True)

# Page handlers
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
    def post(self):
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

    def post(self):
        results_template = jinja_current_directory.get_template("/templates/todolist.html")
        hidden = self.request.get("hidden")
        seed_datas(hidden)
        self.response.write(results_template.render())

class HealthHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/health.html")
        self.response.write(results_template.render())

class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/settings.html")
        self.response.write(results_template.render())
        logout_url = users.create_logout_url("/index.html")
        self.response.write('! <a href = "' + logout_url + '">Logout here</a>')

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("about_us.html")
        self.response.write(results_template.render())
    def post(self):
        results_template = jinja_current_directory.get_template("about_us.html")
        self.response.write(results_template.render())

class NoUserHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url("/index.html")
        self.response.write('You are not logged in! Login here: <a href="' + login_url + '">click here</a>')

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_datas()


app = webapp2.WSGIApplication([
("/", RedirectHandler),
("/index.html", MainHandler),
("/todolist.html", ToDoListHandler),
("/health.html", HealthHandler),
("/settings.html", SettingsHandler),
("/about_us.html", AboutUsHandler),
("/nouser", NoUserHandler),
("/seed-data", LoadDataHandler),
], debug=True)
