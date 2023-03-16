from django.db import models


MAPPINGS = {
            "hospitals": ["Hospital", "Sick"],
            "default": ["DeliveryReport"],
            "companies": ["Company", "Employee"]
           }


class HospRouter:
    def db_for_read(self, model: models.Model, **hints):
        if model._meta.model_name.title() in MAPPINGS["hospitals"]:
            return "hospitals"
        if model._meta.model_name.title() in MAPPINGS["default"]:
            return "default"
    
    def db_for_write(self, model: models.Model, **hints):
        if model._meta.model_name.title() in MAPPINGS["hospitals"]:
            return "hospitals"
        if model._meta.model_name.title() in MAPPINGS["default"]:
            return "default"
        
    def allow_relations(self, obj1: models.Model, obj2: models.Model, **hints):
        if obj1._state.db == obj2._state.db:
            return True
        return False
    
    def allow_migrations(self, db, app_label, model_name=None, **hints):
        if model_name in MAPPINGS["default"]:
            return "default"
        if model_name in MAPPINGS["hospitals"]:
            return "hospitals"


class CompRouter:
    def db_for_read(self, model: models.Model, **hints):
        if model._meta.model_name.title() in MAPPINGS["companies"]:
            return "companies"
        if model._meta.model_name.title() in MAPPINGS["default"]:
            return "default"
    
    def db_for_write(self, model: models.Model, **hints):
        if model._meta.model_name.title() in MAPPINGS["companies"]:
            return "companies"
        if model._meta.model_name.title() in MAPPINGS["default"]:
            return "default"
        
    def allow_relations(self, obj1: models.Model, obj2: models.Model, **hints):
        if obj1._state.db == obj2._state.db:
            return True
        return False
    
    def allow_migrations(self, db, app_label, model_name=None, **hints):
        if model_name in MAPPINGS["default"]:
            return "default"
        if model_name in MAPPINGS["companies"]:
            return "companies"
