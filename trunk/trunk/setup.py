#!/usr/bin/python

from distutils.core import setup
#from setuptools import setup,find_packages

NAME = "rhcpdl"
VERSION = "0.1"
SHORT_DESC = "wget-esque utility for downloading files from Red Hat's Customer Portal"
LONG_DESC = """
A simple cli tool that allows you to cleanly and easily download files from the
Red Hat Customer Portal due to the 2011 changes that made it a multi-step process.
"""


if __name__ == "__main__":
 
        #manpath    = "share/man/man1/"
        setup(
                name = NAME,
                version = VERSION,
                author = "Greg Swift",
                author_email = "gregswift@gmail.com",
                url = "https://%s.googlecode.com/" % NAME,
                license = "LICENSE",
                scripts = ["scripts/%s" % NAME],
                description = SHORT_DESC,
                long_description = LONG_DESC
        )
#                package_dir = {NAME: NAME},
#                packages = [NAME],
#                data_files = [(manpath,  ["docs/%s.1.gz" % NAME])],

