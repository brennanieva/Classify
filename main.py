import webapp2
# import twilio

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import os
from datastore_stuff import ToDoList
from seed_data import seed_datas
import sched
import time

# from twilio.rest import Client
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

class CalendarHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/calendar.html")
        self.response.write(results_template.render())

class WeatherHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/weather.html")
        self.response.write(results_template.render())

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
        print("post")
        print("Hidden is: "+ hidden)
        seed_datas(hidden)

        output = ""
        todolist_query = ToDoList.query().fetch(1)
        todolist_query_1 = todolist_query[0]
        print("To do list queried from datastore: " + str(todolist_query_1))
        new_list = todolist_query_1.user_input
        for thing in new_list:
            output = output + str(thing) + "\n"
        print("Should be user tasks from to do list: " + output)
        print("hi")
        template_vars = {"todolist": output}
        self.response.write(results_template.render(template_vars))


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
    # def post(self):
    #     results_template = jinja_current_directory.get_template("/templates/settings.html")
    #     number = self.request.get("number")
    #     minute = self.request.get("minute")
    #
    #     Settings = {"number" : number,
    #     "minute" : minute,}






class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/about_us.html")
        self.response.write(results_template.render())
    def post(self):
        results_template = jinja_current_directory.get_template("/templates/about_us.html")
        self.response.write(results_template.render())

class NoUserHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("/templates/nouser.html")
        self.response.write(results_template.render())
            # [START user_details]
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                nickname, logout_url)
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
        # [END user_details]
        self.response.write(
            '<html><body>{}</body></html>'.format(greeting))



class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_datas()


app = webapp2.WSGIApplication([
("/", RedirectHandler),
("/index.html", MainHandler),
("/calendar.html",CalendarHandler),
("/weather.html", WeatherHandler),
("/todolist.html", ToDoListHandler),
("/health.html", HealthHandler),
("/settings.html", SettingsHandler),
("/about_us.html", AboutUsHandler),
("/nouser", NoUserHandler),
("/seed-data", LoadDataHandler),
], debug=True)
