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

###Segments and Phonemes
http://linguistics.byu.edu/faculty/eddingtond/223/distinctive%20features%20chart.pdf
http://www.sfs.uni-tuebingen.de/~cebert/teaching/10PhonPhon/handout06.pdf

In this schema, the basic element to be instantiated and stored is a `segment`,
representing a particular expression of a given phoneme in a given text. For
example, analysis of a single sonnet will yield as many as five or six hundred
new segment records. This might seem excessively redundant, but it is necessary
in order to allow the user to make fine adjustments to the phonetic realization
of a poem, and is intended to generate a more supple data set on which to train
an nltk nerual net based phonological AI than could be genreated procedurally.

segment_prototypes:
    The set of attested speech sounds indexed by IPA symbol, IPA generic classi-
    fication, and distinctive feature bundle. A segment prototype serves a dual
    function:
 
    First, it is used to instantiate a new phoneme object using a representative
    IPA symbol and it's associated characterization by manner and major place of
    articulation, as well as its base set of distinctive featues, upon which a
    language-specific transformation is applied by an initialization routine, in
    order to map the selected phonemeic symbol to its allowable set of phonetic
    realizations.

    Second, the segment_prototypes table as a whole provides a means by which a
    segment instance can look up it's phonetic realization as a function of its
    context and a set of rules given by its parent phoneme. See example 1 below.

phonemes:
    This table contains rows corresponding to the phonemic inventory for a given
    language. Each phoneme consists of a reference to a prototypical segment or
    "phone" (in other words, a row in the segment_prototypes table), a language
    key specifying the inventory to which it belongs, and a set of rules which,
    when applied to a feature bundle in a given context, yields a foreign key to
    a sement_prototype representing its phonetic realization in that context.

segments:
   

Example 1.

Given the string "pet spaniel":
1. split the string into words "pet" and "spaniel"
2. look up the phonemic transcription of each to yield "pɛt" and "spæn.jəl"
3. instantiate new segment objects for each element in ["p","ə","t"] and
   ["s", "p", "æ", "n", ".", "j", "ə", "l"]
   a) Look up "p" in phonemes where language is English to retrieve the phoneme
      represented by the first element in ["p","ə","t"] to create a new intance
      of /p/:
          {
              "p": {
                  "prototype" : segment_prototype.get("p"),
                  "init_params": ("/p/ --> [pʰ]","[etc...]"),
                  "rules": ("/p/ --> [pʰ] /#__/", "/p/ --> [p] /v__V/", "etc...")
              }
          }
      then apply this template to instantiate and initialize each occurance of
      the symbol `p` in the text as a new segment represneting /p/.
   b) To obtain the phonetic realization of a given segment, retrieve it's
      prototype. Since each segment instance is addressable by it's own position
      within the text, it can determine it's context and apply the appropriate
      transfromation rule, in this case yielding [pʰ] and [p] respectively.

      IMPLEMENTATION NOTE:
      For the sake of legibility, the transormation rules for /p/ are expressed,
      in the example, using conventional phonological notation. In practice, the
      rules are specified as bitwise and/or matrix operations on a twenty-one
      place binary vector representing a feature bundle.

