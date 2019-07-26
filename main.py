import webapp2
from google.appengine.api import users
import jinja2
import os
# from twilio.rest import Client
# import time

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




        logout_url = users.create_logout_url("/index.html")
        self.response.write("Hello " + '! <a href = "' + logout_url + '">Logout here</a>')

    def post(self):
        index_template = jinja_current_directory.get_template("/templates/index.html")
        health_template = jinja_current_directory.get_template("/templates/health.html")
        username = self.request.get("first-name")
        birthday = self.request.get("month"+"day")
        timeZone = self.request.get("time_zone")
        bedTime = self.request.get("bed_time")
        health = self.request.get("health_priority")
        mood = self.request.get("mood")
        number = self.request.get("number")

        Settings = {
        "name" : username,
        "birthday" : birthday,
        "timeZone" : timeZone,
        "bedTime" : bedTime,
        "health" : health,
        "mood" : mood,
        "number" : number,
        }
        Settings.put()

        def post(self):
            # def sendSMS():
            #     account_sid = "AC3d7a4655023c4eef9f7147fdc4310b1a"
            #     auth_token = "917aabd65c59dd238a49ce37b7876254"
            #     client = Client(account_sid, auth_token)
            #
            #
            #     message = client.messages.create(
            #                                   from_='+12055256928',
            #                                   body='Take a Break! Get up, stretch, drink water!',
            #                                   to='+1'+ number,
            #                               )
            #
            #     print(message.sid)
            #     pass
            #     time.sleep(14400) #4hours
            #
            # while True:
            #     sendSMS()
            self.response.write(index_template.render(Settings))
            self.response.write(health_template.render(Settings))



class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("about_us.html")
        self.response.write(results_template.render())

class NoUserHandler(webapp2.RequestHandler):
    def get(self):
        login_url = users.create_login_url("/index.html")
        self.response.write('You are not logged in! Login here: <a href="' + login_url + '">click here</a>')

        
class WeatherHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_directory.get_template("weather/weather.html")
        self.response.write(results_template.render())

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
("/weather", WeatherHandler),
# ("/receiver", ReceiverHandler),
], debug=True)
