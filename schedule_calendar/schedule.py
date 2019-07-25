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
        schedule_key = "2469d3563444d6fbd6ecd75255587c3e46ed187b"

        url = "https://calendarific.com/api/v2/holidays?api_key=" + schedule_key

        results_template = jinja_env.get_template('/schedule.html')
        self.response.write(results_template.render())

    def post(self):
        # description = self.request.get('zip_code')
        schedule_key = "2469d3563444d6fbd6ecd75255587c3e46ed187b"

        url = "https://calendarific.com/api/v2/holidays?api_key=" + schedule_key


        print(url)

        response = urlfetch.fetch(url)
        content = response.content
        as_json = json.loads(content)
        #
        self.response.write(response)



app = webapp2.WSGIApplication([
    ("/", MainHandler),
], debug=True)
