<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-app-generator.svg?maxAge=3600)](https://pypi.org/project/mac-app-generator/)
[![](https://img.shields.io/npm/v/mac-app-generator.svg?maxAge=3600)](https://www.npmjs.com/package/mac-app-generator)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-app-generator.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-app-generator.py/actions)

### Installation
```bash
$ [sudo] pip install mac-app-generator
```

```bash
$ [sudo] npm i -g mac-app-generator
```

#### Features
shell (mini) and python (full) versions

#### Examples
create app from shell script
```bash
$ mac-app-generator script.sh name.app
$ mac-app-generator script.sh name.app Icon.png
```

create app from python script
```python
>>> mac_app.App(app_script="file.py", app_path="name.app").create_app()
```

create app from a python class
```python
import mac_app_generator
class MyApp(mac_app_generator.App):
    def run(self):
        pass

if __name__ == "__main__":
    MyApp().run()
```

```python
>>> MyApp().create_app()
```

#### Related
+   [`commands-generator` - shell commands generator](https://pypi.org/project/commands-generator/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`readme-generator` - `README.md` generator](https://pypi.org/project/readme-generator/)
+   [`setupcfg-generator` - `setup.cfg` generator](https://pypi.org/project/setupcfg-generator/)
+   [`travis-generator` - `.travis.yml` generator](https://pypi.org/project/travis-generator/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
