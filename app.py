from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def pick_story():
    """ Prompts user to pick a story prompt to use """



@app.get('/silly_stories')
def build_form():
    """ Uses input silly story prompt to render our form """
    required_words = silly_story.prompts

    return render_template("questions.html",
                           word_fields=required_words)

@app.get("/results")
def post_results():
    """ Calling get_result_text of story instance to create our story and
        rendering it to the results html """

    story = silly_story.get_result_text(request.args)

    return render_template(
        "results.html",
        story_text = story
    )
