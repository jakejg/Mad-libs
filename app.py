from flask import Flask, request, render_template
import stories

app = Flask(__name__)



def choose_story(num_string):
    for num in range(3):
        if num_string == str(num):
            return stories.stories_list[num]

@app.route('/')
def home_choose_temp():

    return render_template("choose.html", stories_list = stories.stories_list)


@app.route('/form')
def home_form():
    selected_theme = request.args.get("story_id")
    num = -1
    for story in stories.stories_list:
        num += 1
        if story.theme == selected_theme:
            return render_template("form.html", grammar = story.prompts, num = num)
    return "Something went wrong"
   
    

@app.route('/story/<num>')
def display(num):
    curr_story = choose_story(num)
    ans = {word:request.args.get(word) for word in curr_story.prompts}
    text = curr_story.generate(ans)

    return render_template("story.html", text = text)
