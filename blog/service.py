from flask import flash, redirect

from blog.func import new_entry
from blog.models import Entry


def filter_entries_by_date(is_published):
    return Entry.query.filter_by(is_published=is_published).order_by(Entry.pub_date.desc())


def publish_entry(form):
    if form.is_published.data:
        new_entry(form)
        flash("Your Post has been published!", "success")
    else:
        new_entry(form)
        flash("Post created and saved in Drafts", "info")
