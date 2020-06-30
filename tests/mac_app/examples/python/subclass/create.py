#!/usr/bin/env python
import os
import sys
import app_class


sys.path.append(os.path.dirname(__file__))
app_image = os.path.join(os.path.dirname(__file__), "image.png")

app = app_class.AppName()
app.create_app()
print(app.app_path)

app_class.AppName(app_name="app-with-image", app_image=app_image).create_app()
