### ADD THIS TO YOUR .gitignore FILE ###

# Given title for application.  Anything you choose
APPLICATION_TITLE = '<title>'

# DJango Secret key can be generated using this tool: https://www.miniwebtool.com/django-secret-key-generator/
secret_key = '<django secret key>'

# OAUTH Consumer Credentials---you must register a consumer as outlined here:
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


