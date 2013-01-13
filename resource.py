# coding: utf-8
"""
Author: Enrico Tröger
License: GPLv2
"""


###########################################################################
class VzUbcMonResource(object):
    """
    Simple data structure to represent a UBC resource
    """

    #----------------------------------------------------------------------
    def __init__(self, held=None, maxheld=None, barrier=None,
                    limit=None, failcnt=None, resource_seq=None):
        if resource_seq:
            self.held = int(resource_seq[0])
            self.maxheld = int(resource_seq[1])
            self.barrier = int(resource_seq[2])
            self.limit = int(resource_seq[3])
            self.failcnt = int(resource_seq[4])
        else:
            if not isinstance(held, basestring)and not isinstance(held, int):
                raise AttributeError('You must specify either a resource using keyword '
                                     'arguments or a complete resource sequence')
            self.held = int(held)
            self.maxheld = int(maxheld)
            self.barrier = int(barrier)
            self.limit = int(limit)
            self.failcnt = int(failcnt)

    #----------------------------------------------------------------------
    def __repr__(self):
        return '%s:%s (%s)' % (self.barrier, self.limit, self.failcnt)
