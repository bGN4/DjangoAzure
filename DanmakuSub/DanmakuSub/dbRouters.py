# -*- coding: utf-8 -*- 
from django.conf import settings

DATABASE_APPS_MAPPING = {
}

class DBRouter(object):
    def db_for_read(self, model, **hints):
        return DATABASE_APPS_MAPPING.get(model._meta.app_label, 'default')
  
    def db_for_write(self, model, **hints):
        return DATABASE_APPS_MAPPING.get(model._meta.app_label, 'default')

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db in DATABASE_APPS_MAPPING.values():
            return DATABASE_APPS_MAPPING.get(app_label) == db
        elif app_label in DATABASE_APPS_MAPPING:
            return False
        return None

