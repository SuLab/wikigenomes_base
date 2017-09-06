# wikigenomes_base
A configurable codebase for launching organism specific WikiGenomes spinoff applications (e.g. LactoBase.org)

This is a web application framework for creating a model organism database leveraging the taxonomic, genetic and functional data that has been loaded to Wikidata.org by the [Gene Wiki Project](https://github.com/SuLab/GeneWikiCentral).

To create your own instance:

You will need to run a virtual environment with python 3.4 or higher.
You will also need to install the current version of MongoDB and make sure it is running before proceeding.

1. create a wikigenomes_conf.py file and populate with the proper configurations using wikigenomes_conf.py.template in the root (wikigenomes_setup) directory 

wikigenomes_conf.py.template
```
### ADD THIS TO YOUR .gitignore FILE ###

# Given title for application.  Anything you choose
APPLICATION_TITLE = '<title>'

# DJango Secret key can be generated using this tool: https://www.miniwebtool.com/django-secret-key-generator/
secret_key = '<django secret key>'

# OAUTH Consumer Credentials---to gain consumer credentials from MediaWiki.org you must register a consumer as outlined here:
# https://www.mediawiki.org/wiki/OAuth/For_Developers#Registration
consumer_key = '<wikimedia oauth consumer key>'
consumer_secret = '<wikimedia oauth consumer secret>'

# Configurations for django settings.py
# ALLOWED_HOSTS add IP or domain name to list.
allowed_hosts = ['title.org', 'localhost', 'aws IP', 'etc']
# TIME_ZONE
wg_timezone = 'America/Los_Angeles'


#  Application customization ##
"""
 Taxids of the organisms that will included in the instance
 Currently available genomes include the 120 bacterial reference genomes:
 https://www.ncbi.nlm.nih.gov/genome/browse/reference/ that currently populate WikiGenomes
 You may also provide a  list of taxids from the list of representative species at NCBI RefSeq at the same url
       - to get the desired taxids into Wikidata for use in your WikiGenomes instance, create an issue at:
           https://github.com/SuLab/scheduled-bots
         providing the list of taxids, the name and a brief description of your application.
         You will then be notified through GitHub when the genomes,
         their genes an proteins have been loaded to Wikidata
"""
# a list of taxids
taxids = []
```

2. run setup.sh

3. point your browser at the host name you specified in 'allowed_hosts'