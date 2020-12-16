# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from model.Role import Role
from model.User import User
from model.Category import Category
from model.Device import Device
from model.Register import Register

from admin.Views import UserView, HomeView, RoleView, CategoryView, DeviceView, RegisterView

def start_views(app, db):
    admin = Admin(app, name='Meu Estoque', base_template='admin/base.html', template_mode='bootstrap3', index_view=HomeView())

    admin.add_view(RoleView(Role, db.session, "Funções", category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(CategoryView(Category, db.session, 'Categorias',category="Dipositivos"))
    admin.add_view(DeviceView(Device, db.session, "Dispositivos", category="Dispositivos"))
    admin.add_view(RegisterView(Register, db.session, "Dispositivos", category="Dispositivos"))
    
    admin.add_link(MenuLink(name='Logout', url='/logout'))