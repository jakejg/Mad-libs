from flask import Flask, request, render_template
import stories

app = Flask(__name__)



def choose_story(num_string):
    for num in range(3):
        if num_string == str(num):
            return stories.stories_list[num]

@app.route('/')
def home_choose_temp():
    temp = stories.story0.template
    temp1 = stories.story1.template
    temp2 = stories.story2.template

    return render_template("choose.html", temp = temp, temp1 = temp1, temp2 = temp2)


@app.route('/form/<num>')
def home_form(num):
    s = choose_story(num).prompts
    return render_template("form.html", grammar = s, num = num)
    

@app.route('/story/<num>')
def display(num):
    curr_story = choose_story(num)
    ans = {word:request.args.get(word) for word in curr_story.prompts}
    text = curr_story.generate(ans)

    return render_template("story.html", text = text)
