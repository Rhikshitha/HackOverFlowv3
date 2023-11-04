from django.contrib import admin
from django.apps import apps

# Get a list of all models in your app
app_name = 'route_scheduler'  
app_models = apps.get_app_config(app_name).get_models()

# Register each model in the admin
for model in app_models:
    admin.site.register(model)