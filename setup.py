import setuptools

setuptools.setup(
    name='mac-app-generator',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/mac-app-generator']
)
