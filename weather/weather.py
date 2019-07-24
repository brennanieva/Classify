import webapp2
from google.appengine.api import urlfetch
import json
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        weather_key = "fc1a305754d1452dbe1175203192307"

        results_template = jinja_env.get_template('/weather.html')
        self.response.write(results_template.render())

    def post(self):
        zip_code = 98230;
        # description = self.request.get('zip_code')
        weather_key = "fc1a305754d1452dbe1175203192307"
        url_day = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weather_key + "&q=" + zip_code + "&num_of_days=1&tp=3&format=xml"
        url_week = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weather_key + "&q=" + zip_code + "&num_of_days=7&tp=3&format=xml"

        print(url)

        response = urlfetch.fetch(url)
        content = response.content
        as_json = json.loads(content)
        #
        self.response.write(response)



app = webapp2.WSGIApplication([
    ("/", MainHandler),
], debug=True)
