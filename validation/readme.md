### Validation 

We use `validate_no_meta.py` to check the consistency of annotation according to the UDv2.5 scheme. 
This is a standard validate.py script by https://universaldependencies.org/release_checklist.html#validation
but sentence meta data are not checked. 

==============================
validate_no_meta.py
==============================

Reads a CoNLL-U file and verifies that it complies with the UD specification. It must be run with the language
code and there must exist corresponding lists of treebank-specific features and dependency relations in order
to check that they are valid, too.

The script runs under Python 3 and needs the third-party module "regex". If you do not have the "regex" module,
install it using "pip install --user regex". NOTE: Depending on the configuration of your system, it is possible
that both Python 2 and 3 are installed; then you may have to run "python3" instead of "python", and "pip3"
instead of "pip".

```
  cat file.conllu | python validate_no_meta.py --lang ru --max-err=0
```

Other useful options:

* check the consistency of conllu format (LF end of line, 10 columns, empty line between sentences, tokens enumerated corrrectly:

```
  cat file.conllu | python validate_no_meta.py --lang ru --level 1
```   

You can run "python validate.py --help" for a list of available options.


