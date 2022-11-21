from flask import render_template, redirect

from blog import app, service
from blog.decorators import login_required
from blog.forms import EntryForm, LoginForm


@app.route("/")
def index():
    all_posts = service.filter_entries_by_date(is_published=True)
    return render_template("homepage.html", all_posts=all_posts)


@app.route("/post/", methods=["GET"])
@login_required
def get_new_post_form():
    form = __get_entry_form_object()
    return render_template("entry_form.html", form=form, errors=None)


@app.route("/post/", methods=["POST"])
@login_required
def create_entry():
    service.publish_entry(__get_entry_form_object())
    return redirect("/")


@app.route("/edit-post/<int:entry_id>", methods=["GET"])
@login_required
def get_edit_entry_form(entry_id):
    entry_db = service.get_entry_by_id(entry_id)
    form_for_editing = EntryForm(obj=entry_db)
    return render_template("entry_form.html", form=form_for_editing, errors=None)


@app.route("/edit-post/<int:entry_id>", methods=["POST"])
@login_required
def edit_entry(entry_id):
    entry_db: object = service.get_entry_by_id(entry_id)
    form_for_editing = EntryForm(obj=entry_db)
    service.update_entry(entry_db, form_for_editing)
    return redirect("/")


@app.route("/login/", methods=["GET"])
def get_login_form():
    form = __get_login_form_object()
    return render_template("login_form.html", form=form, errors=None)


@app.route("/login/", methods=["POST"])
def login():
    form = __get_login_form_object()
    service.login(form)
    return redirect("/")


@app.route("/logout/", methods=["POST"])
def logout():
    service.logout()
    return redirect("/")


@app.route("/drafts/", methods=["GET"])
def show_drafts():
    all_drafts = service.filter_entries_by_date(is_published=False)
    return render_template("drafts.html", all_drafts=all_drafts)


@app.route("/delete/<int:entry_id>")
def delete_draft(entry_id):
    entry = service.get_entry_by_id(entry_id)
    service.delete_draft(entry)
    return redirect("/drafts/")


@app.route("/contact/", methods=["GET"])
def get_contact_form():
    return render_template("contact.html")


@app.route("/contact/", methods=["POST"])
def contact():
    service.send_email()
    return redirect("/contact/")


@app.route("/about/")
def about():
    return render_template("about.html")


def __get_entry_form_object():
    return EntryForm()


def __get_login_form_object():
    return LoginForm()
