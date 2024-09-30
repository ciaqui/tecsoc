import secrets
from flask import url_for, redirect
from . import app #, db
from flask import render_template, url_for, request, redirect, flash

#################################
#                               #
#           Site Stuff          #
#                               #
#################################

# when '/home' or '/index' are typed in the URL or redirected, it will the redirect to the url without anything after the /
@app.route("/index")
@app.route("/home")
@app.route("/b", strict_slashes=False) # from: https://stackoverflow.com/questions/33241050/trailing-slash-triggers-404-in-flask-path-rule
def home_redirect():
    return redirect(url_for('index'))

@app.route("/")
def index():
    from .data.projects import projects # to be removed when DB is connected
    # from .data.team import team_members, testimonials # to be removed when DB is connected
    from .data.events import events # to be removed when DB is connected
    # from .data.blogs import blogs # to be removed when DB is connected
   
    return render_template(
        'index.html',
        title = 'Home',
        projects = projects,
        events = events #,
        # past_events = past_events
    )

@app.route("/about")
def about():
    from .data.team import team_members, testimonials # to be removed when DB is connected

    return render_template(
        'about.html',
        title = 'About Us',
        team_members = team_members,
        testimonials = testimonials
    )

@app.route("/contact")
def contact():
    return render_template(
        'contact.html',
        title = 'Contact Us'
    )


#################################
#                               #
#           event Stuff         #
#                               #
#################################

@app.route("/events")
def events():
    from .data.events import events # to be removed when DB is connected
    from .data.past_events import past_events # to be removed when DB is connected

    return render_template(
        'event/events.html',
        title = 'Events',
        events = events,
        past_events = past_events
    )


#################################
#                               #
#           project Stuff       #
#                               #
#################################

@app.route("/projects")
def projects():
    from .data.projects import projects

    return render_template(
        'project/projects.html',
        title = 'Projects',
        projects = projects
    )


#################################
#                               #
#           blog Stuff          #
#                               #
#################################

@app.route("/b/<blog_id>")
def short_blogs(blog_id):
    if blog_id.lower() == "tecsu":
        return redirect("https://www.cardiffstudents.com/activities/society/etsoc/")
    if blog_id.lower() == "cybersu":
        return redirect("https://www.cardiffstudents.com/activities/society/cybersoc/")
        
    return redirect(url_for('single_blog', blog_id=blog_id))

@app.route("/blogs/<blog_id>")
def single_blog(blog_id):
    return render_template(
        'blog/blog_single_page.html',
        title = f'blog: {blog_id}'
    )

@app.route("/blogs")
def blogs():
    from .data.blogs import blogs # to be removed when DB is connected
    
    return render_template(
        'blog/blogs.html',
        title = 'blogs',
        blogs = blogs
    )


#################################
#                               #
#           Error Stuff         #
#                               #
#################################

# Reference: https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template(
        '404.html', 
        title = 'Page Not Found'
        ), 404
