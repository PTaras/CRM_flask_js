from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime
import urllib.request
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from urllib.parse import urlparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logos_all.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Logo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(100), nullable=False, unique=True)
    logo = db.Column(db.String(300), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    delete_button = db.Column(db.String(100), nullable=False)
    download_button = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Logo %r>' % self.id


def loop():
    gui = Tk()
    gui.geometry("400x300")
    gui.wm_attributes("-topmost", 1)
    gui.title("Choose path for save:")

    def getFolderPath():
        folder_selected = filedialog.askdirectory()
        folderPath.set(folder_selected)

    def doStuff():
        folder = folderPath.get()
        return folder

    def close_window():
        gui.destroy()

    folderPath = StringVar()
    E = Entry(gui, textvariable=folderPath)
    E.grid(row=2, column=2)
    E.focus()
    E.focus_set()
    btnFind = ttk.Button(gui, text="Browse Folder", command=getFolderPath)
    btnFind.grid(row=2, column=3)

    c = ttk.Button(gui, text="Save", command=close_window)
    c.grid(row=6, column=2)
    gui.mainloop()
    return doStuff()


@app.route('/logos')
def logos():
    logos_all = Logo.query.order_by(Logo.date_created).all()
    return render_template("logos.html", logos=logos_all)


@app.route('/logos/<int:id>/delete')
def delete_logo(id):
    logo = Logo.query.get_or_404(id)

    try:
        db.session.delete(logo)
        db.session.commit()
        return redirect('/logos')
    except:
        return 'Не удалось удалить запись. Попробуйте, пожалуйста, ещё раз.'


@app.route('/logos/<int:id>/download')
def download_logo(id):
    save_logo = Logo.query.get_or_404(id)

    try:
        path = loop()
        urllib.request.urlretrieve("{}".format(save_logo.logo), "{}.png".format(path + "/" + save_logo.domain))
        return redirect('/logos')
    except:
        return 'Sorry, logo not save. Please, choose path and try, please, again.'


@app.route('/add-logo', methods=['POST', 'GET'])
def add_logo():
    if request.method == 'POST':
        domain = request.form['domain']
        logos_all = Logo.query.order_by(Logo.date_created).all()
        if len(logos_all) > 0:
            for dom in logos_all:
                if domain == dom.domain or urlparse(domain).netloc == dom.domain:
                    return "Logo exist in base!"

        if bool(re.match(r'http.*', domain)) == True:
            logo_url = 'https://logo.clearbit.com/{}'.format(urlparse(domain).netloc)
            domain = urlparse(domain).netloc
        elif bool(re.match(r'http.*', domain)) == False:
            logo_url = 'https://logo.clearbit.com/{}'.format(domain)
        delete_button = 'Delete'
        download_button = 'Download'

        logo = Logo(domain=domain, logo=logo_url, delete_button=delete_button, download_button=download_button)

        try:
            db.session.add(logo)
            db.session.commit()
            return redirect('/logos')
        except:
            return "Logo not added, try once more later."
    else:
        return render_template("add-logo.html")


@app.route('/sorted_domain')
def sort_by_domain():
    domain_sorted = Logo.query.order_by(Logo.domain).all()
    return render_template("sorted.html", logos=domain_sorted)


@app.route('/sorted_id')
def sort_by_id():
    id_sorted = Logo.query.order_by(Logo.id).all()
    return render_template("sorted.html", logos=id_sorted)


@app.route('/sorted_logos')
def sort_by_logos():
    logos_sorted = Logo.query.order_by(Logo.logo).all()
    return render_template("sorted.html", logos=logos_sorted)


@app.route('/sorted_date')
def sort_by_date():
    date_sorted = Logo.query.order_by(desc(Logo.date_created)).all()
    return render_template("sorted.html", logos=date_sorted)


if __name__ == '__main__':
    app.run(debug=True)
