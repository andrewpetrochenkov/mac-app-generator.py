#!/usr/bin/env python
import os
import mac_app_generator

app_script = os.path.join(os.path.dirname(__file__), ".script.py")
app_path = "/tmp/test_app"
app = mac_app_generator.App(app_script=app_script, app_path=app_path)
app.create_app()
print(app_path)
