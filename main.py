import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())
class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/new_post.html')
        self.response.write(template.render())
    def post(self):
            title_var = self.request.get('title')
            content_var = self.request.get('content')
            name_var = self.request.get('name')
            print(title_var)
            print(content_var)
            print(name_var)
            template = jinja_env.get_template('index.html')
            self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/new_post', BlogHandler),
], debug=True)
