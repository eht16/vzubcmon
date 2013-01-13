# coding: utf-8
"""
Author: Enrico Tröger
License: GPLv2
"""

from os.path import exists
from resource import VzUbcMonResource
import sys


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

        return self._bc_version

    #----------------------------------------------------------------------
    def _parse(self):
        """
        Read either from the passed file or from stdin and store the values in the object
        """
        if not exists(self._filename) and self._filename == '-':
            self._parse_input(sys.stdin)
        else:
            ubc_file = open(self._filename, 'r')
            self._parse_input(ubc_file)
            ubc_file.close()

    #----------------------------------------------------------------------
    def _parse_input(self, ubc_file):
        self._resources = {}
        current_ctid = 0
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
                        current_ctid = ctid
                        self._resources[current_ctid] = {}
                    else:
                        # header line
                        continue
                    del values[0]
                resource_name = values[0]
                resource_values = values[1:]  # skip the name
                resource = VzUbcMonResource(resource_seq=resource_values)
                self._resources[current_ctid][resource_name] = resource


if __name__ == '__main__':
    from pprint import pprint
    pprint(VzUbcMonParser('sample_host').get_resources())
