from functools import wraps

from flask import current_app, flash, request, redirect, url_for
from flask_login import config, current_user

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS or current_app.config.get("LOGIN_DISABLED"):
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_admin:
            flash('Эта страница доступна только админам')
            return redirect(location=url_for(endpoint='magazine.index'))
        return func(*args, **kwargs)
    return decorated_view
