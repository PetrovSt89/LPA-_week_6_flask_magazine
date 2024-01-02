from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user
from webapp.user.decorators import admin_required


blueprint = Blueprint(name='admin', import_name=__name__, url_prefix='/admin')

@blueprint.route("/")
@admin_required
def admin_index():
    page_title = 'Админка'
    text_message = f'Привет {current_user.username}'

    return render_template('admin/admin.html',
                    page_title=page_title, text_message=text_message)
