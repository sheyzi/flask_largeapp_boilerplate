from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, request, flash


class AuthUserView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))

    can_delete = False
    can_export = True
    column_exclude_list = ['password', ]
    edit_modal = True
    create_modal = True
    column_filters = ['active', 'is_admin']
    column_searchable_list = ['user_name', 'first_name', 'last_name', 'phone_number']
    form_excluded_columns = ['password']
    form_args = {
        'user_name': {
            'label': 'Username',
        }
    }


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash("You aren't allowed to visit that page", 'danger')
        return redirect(url_for('core.home', next=request.url))