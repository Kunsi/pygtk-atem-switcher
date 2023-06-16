from setuptools import find_packages, setup


setup(
    name = "pygtk-atem-switcher",
    version = "0.0.1",
    author = "Franziska Kunsmann",
    author_email = "hi@kunsmann.eu",
    description = (""),
    license = "",
    keywords = "atem blackmagic gtk a/v",
    url = "github.com/kunsi/pygtk-atem-switcher/",
    packages=find_packages(),
    install_requires=['PyATEMMax', 'pycairo', 'PyGObject', 'rtoml'],
    long_description="",
    entry_points={
        'gui_scripts': [
            'pygtk-atem-switcher=pygtk_atem_switcher:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
    ],
)
