#Lingualizer

A collection of ~~Django~~ Flask and SQLAlchemy data models and web-based tools for representing
poems as highly detailed and coherent linguistic data-sets.

More Info: http://github.com/mitchsmith/Lingualizer/wiki/

##Requirements

Lingualizer is currently being developed and tested using:

Python==3.4.0
Flask==0.10.1
SQLAlchemy==0.9.4
WTForms==2.0

(see requirements.txt)

Additionally, to use MySQL in place of sqlite3 will also require:

PyMySQL==0.6.2

and eventually, the REST api will probably need PyYAML to make up for deficient unicode support in json and simplejson.  

NOTE: At some point, this project will depend on nltk. Depending on when that happens (this is very much a hobby project), it may, or may not be necessary to dial back these requirements to run under Python 2.7.

##Installation

Gosh, but isn't virtualenvwrapper handy! (http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

With virtualenvwrapper installed:

Either add the following line your virtualenv and virtualenv wrapper environment setup in .bashrc:

```bash
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
```

or, if you prefer to leave you default virtualenv with a 2.x interpreter, use the -p virtualenv option:

```bash
mkproject -p /usr/bin/python3 <projectname>
```

then:

```bash
workon <projectname>
git clone https://github.com/mitchsmith/Lingualizer.git ./
pip install -r reqirements.txt
```
(If your default virtualenv uses 2.7, you may need to use pip3 explicitly when installing requirements.)

##Notes to Self


