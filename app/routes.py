from app import app
from flask import render_template, request, redirect
from models import providers_list
import random

@app.route('/')
@app.route('/index')
def index():
    # return "Hello Flask!"
    return render_template('index.html', title="Welcome")

@app.route('/providers')
def providers():
    return render_template('providers/providers-list.html', title="Vehicle Control", providers=providers_list)

def build_provider_object(request, id):
            return {
                    "id": id,
                    "owname": request.form['owname'],
                    "mowner": request.form['mowner'],
                    "carmodel": request.form['carmodel'],
                    "color": request.form['color']
                    }

def getProviderIndex(id,providers_list):
    for i in range(0, len(providers_list)):
        if providers_list[i]['id']==int(id):
            return i
    return None

# add
@app.route('/providers/add-provider', methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        id = random.randint(100000,999999)
        provider = build_provider_object(request,id)
        providers_list.append(provider)
        return redirect('/providers')

    return render_template('providers/provider-add-form.html', title="Add Owner", 
    providers=providers_list)

# edit
@app.route('/providers/edit/<id>', methods=["GET", "POST"])
def edit(id):
    provider = None
    index = getProviderIndex(id,providers_list)
    if request.method == 'POST':
        provider = build_provider_object(request, int(id))
        if index is not None:
            providers_list[index]=provider
        return redirect('/providers')
    if index is not None:
        provider = providers_list[index]

    return render_template('providers/provider-edit-form.html', title="Update Owner", 
    provider=provider, id=id)

# delete
@app.route('/providers/delete/<id>')
def delete(id):
    index = getProviderIndex(id,providers_list)
    if index is not None:
        del providers_list[index]
    return redirect('/providers')