from flask import session, redirect, url_for, request
import functools


def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        if session.get("logged_in"):
            return view_func(*args, **kwargs)
        return redirect(url_for("login", next=request.path))

    return check_permissions
