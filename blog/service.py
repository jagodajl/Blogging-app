from flask import flash, session

from blog import db
from blog.func import new_entry
from blog.models import Entry


def filter_entries_by_date(is_published):
    return Entry.query.filter_by(is_published=is_published).order_by(Entry.pub_date.desc())


def get_entry_by_id(entry_id):
    return Entry.query.filter_by(id=entry_id).first_or_404()


def publish_entry(form):
    if form.is_published.data:
        new_entry(form)
        flash("Your Post has been published!", "success")
    else:
        new_entry(form)
        flash("Post created and saved in Drafts", "info")


def update_entry(entry, form):
    if form.validate_on_submit():
        form.populate_obj(entry)
        db.session.commit()
        flash("Your Post has been updated!", "info")


def login(form):
    if form.validate_on_submit():
        session["logged_in"] = True
        session.permanent = True  # Use cookie to store session.
        flash("You are now logged in.", "success")
