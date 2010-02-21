#!/usr/bin/python
# coding: utf-8
"""
Author: Enrico Tröger
License: GPLv2
"""

from pickle import dump, load
from os.path import exists


###########################################################################
class VzUbcMonDatabase(object):
    """
    Read and write VzUbcMonResources into a pickled file (i.e. the database)
    """

    #----------------------------------------------------------------------
    def __init__(self, filename):
        self._filename = filename

    #----------------------------------------------------------------------
    def read(self):
        """
        Read stored UBC values from the database

        | **return** resources (dict)
        """
        if exists(self._filename):
            database = open(self._filename, 'r')
            resources = load(database)
            database.close()
            return resources
        else:
            return dict()

    #----------------------------------------------------------------------
    def write(self, resources):
        """
        Write passed UBC values into the database

        | **param** resources (dict)
        """
        database = open(self._filename, 'w')
        dump(resources, database)
        database.close()
