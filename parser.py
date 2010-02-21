# coding: utf-8
"""
Author: Enrico Tröger
License: GPLv2
"""

from resource import VzUbcMonResource


###########################################################################
class VzUbcMonParser(object):
    """
    Parser to read /proc/user_beancounters and hold the values
    in a sequence of VzUbcMonResource
    """

    #----------------------------------------------------------------------
    def __init__(self, filename):
        self._filename = filename
        self._bc_version = None
        self._container_id = None
        self._resources = None

    #----------------------------------------------------------------------
    def get_resources(self):
        """
        Parse and return the current UBC values for the system

        | **return** resources (dict)
        """
        if self._resources is None:
            self._parse()

        return self._resources

    #----------------------------------------------------------------------
    def get_information(self):
        """
        Return the version field of the parsed bean counters file and the container ID

        | **return** beancounter_version, container_id (tuple)
        """
        if self._resources is None:
            self._parse()

        return (self._bc_version, self._container_id)

    #----------------------------------------------------------------------
    def _parse(self):
        """
        Parse /proc/user_beancounters and store the values in the object
        """
        # TODO adjust the code to also parse more than one container so that we
        # could also run on a container node
        ubc_file = open(self._filename, 'r')
        self._resources = {}
        for line in ubc_file:
            values = line.strip().split()
            values_len = len(values)
            if values_len == 2:
                self._bc_version = values[1]
            elif values_len >= 6:
                if values_len == 7:
                    ctid = values[0][:-1]
                    if ctid.isdigit():
                        # we got the container id
                        self._container_id = ctid
                    else:
                        # header line
                        continue
                    del values[0]
                resource_name = values[0]
                resource_values = values[1:] # skip the name
                self._resources[resource_name] = VzUbcMonResource(resource_seq=resource_values)

        ubc_file.close()

