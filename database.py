#!/usr/bin/python
# coding: utf-8
"""
Author: Enrico Tröger
License: GPLv2
"""

from pickle import dump, load
from os.path import dirname, exists
from os import makedirs


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
        try:
            database = open(self._filename, 'r')
            resources = load(database)
            database.close()
            return resources
        except IOError:
            return dict()

    #----------------------------------------------------------------------
    def _check_database_directory(self):
        """
        Check whether the directory into which the database file should be
        saved already exists and if not, create it
        """
        database_directory = dirname(self._filename)
        if not exists(database_directory):
            makedirs(database_directory, 0700)

    #----------------------------------------------------------------------
    def _check_database_file_permissions(self):
        """
        Check that the database file only has the necessary file permissions set
        """
        # TODO implement me

    #----------------------------------------------------------------------
    def write(self, resources):
        """
        Write passed UBC values into the database

        | **param** resources (dict)
        """
        self._check_database_directory()
        # write the data
        database = open(self._filename, 'w')
        dump(resources, database)
        database.close()
        # check file permissions
        self._check_database_file_permissions()
