from flask import Blueprint, render_template, request
#from flask_ckeditor import CKEditorField, CKEditor
import openai  #new
import os.path

example_blueprint = Blueprint('example_blueprint', __name__)
#second = Blueprint('example_blueprint', __name__, template_folder='templates')
openai.api_key = "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" #new

myprompt = """make a 4 paragraph blog about Flights to 

start every new paragraph with '#'
separate the questions on its own line
make an introduction about

"""

@example_blueprint.route('/mypost/')
def mypost():
    if request.method == 'POST':
       # title = request.form['title']
      #  content = request.form['content']
        #name = request.form['name']
        return render_template("cool.html",myprompt=myprompt)
    return render_template("cool.html",myprompt=myprompt)
@example_blueprint.route('/mypostt/', methods=['GET', 'POST'])
def myypost():
    #first = request.args.get('content')
    first = request.form['content']  
    return render_template("cool.html", first=first)

@example_blueprint.route('/gpt3/', methods=['GET', 'POST'])
def gpt3():
    first = request.form['content']
    response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens=2000,
            prompt=first,
            temperature=0.6)
    first=first + response.choices[0].text    
    return render_template("cool.html", first=first)






blog ="""
\n{% extends "base.html" %}
\n{% block h1 %}{% block title %}TTT{% endblock %}{% endblock %}
\n{% block travel %}  {% include "mexico-flights/mexico-base.html" %}{% endblock travel%}
\n{% block flag %}<img class="bodyphoto visainfodiv" src="/static/mexicoflag.png">{% endblock flag%}
\n{% block travelphoto %} <img class="bodyphoto" src="/static/nice view of mexico.png">{% endblock %}


\n{% block widget %}
\n<div id="widget-holder"></div>
\n<script 
\ndata-affilid="apophis51saltlaketobogota" 
\ndata-from="LAX" 
\ndata-to="bogota_co" 
\ndata-transport-types="FLIGHT" 
\nsrc="https://widgets.kiwi.com/scripts/widget-search-iframe.js">
\n</script>
\n{% endblock widget%}


\n<div class = "white">
\n{% block visa %} <p class= "smallfont">Get Current Visa Information From <a href="https://www.visahq.com/mexico/"
        rel="sponsored">VisaHQ</a></p>
\n {% endblock %}

\n{% block content %}
\n ###

\n<em>
\n    <strong>Before booking your trip, make sure to compare flights and prices to get the most out of your experience. To
        get started, check out FlightTicketFinder.com flight tracker for the best deals and discounts on <a
            href="/mexico-flights/">flights to Mexico.</a></strong>
\n</em>
\n</div>
\n{% endblock %}
"""



@example_blueprint.route('/print/', methods=['GET', 'POST'])
def printt():
    content = request.form['content'] 
    
    title = request.form['title']
    route = title.replace(" ","-")
    url = title.replace(" " , "-") + ".html"
    urlwithouthtml = title.replace(" ", "-")
    method = title.replace(' ', '')
    print(title)
    print(url)
    print(method)

    navigation = f"""
    \n\n<li>
     \n <a href = "/mexico-flights/{urlwithouthtml}/">{title}</a>
   \n </li>
   \n
    """
    #writes everything here instead of individual files
    #text = open(f"{url}","a")
    #text.writelines(blog.replace("TTT",title).replace("###",content))
    #text = open('example_blueprint.py', 'a')
    #text.writelines(f'\n@mexico_blueprint.route("/{route}/") #ai-generated')
    #text.writelines(f'\ndef {method}(): #ai-generated')
    #text.writelines(f'\n\treturn render_template("/mexico-flights/{url}") #ai-generated')
    #text.writelines(navigation)
    #return render_template("cool.html", first=content)

    save_path = r"C:\Users\malco\Bussinflights.com\templates\mexico-flights" 
    filelocation = f"{url}"
    completeName = os.path.join(save_path, filelocation)
    text = open(completeName,"a")
    text.writelines(blog.replace("TTT",title).replace("###",content))

    text = open('mexico_blueprint.py', 'a')
    text.writelines(f'\n@mexico_blueprint.route("/{route}/") #ai-generated')
    text.writelines(f'\ndef {method}(): #ai-generated')
    text.writelines(f'\n\treturn render_template("/mexico-flights/{url}") #ai-generated')

    filelocation = "mexico-base.html"
    completeName = os.path.join(save_path, filelocation)


    text = open(completeName,"r")
    data = text.readlines()
   # data = data[len(data)-2]+ navigation
    data[len(data)-4] = navigation
    text = open(completeName,"w")
    text.writelines(data)
    #text.writelines(navigation)
    #data[-1] = navigation
    

    return render_template("cool.html", first=content)

 
    