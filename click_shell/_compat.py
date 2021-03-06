"""
click_shell._compat

Compatibility things for python 2.6
"""

# pylint: disable=unused-import, wrong-import-position

import sys
import types

PY2 = sys.version_info[0] == 2

try:
    from logging import NullHandler
except ImportError:
    import logging

    class NullHandler(logging.Handler):
        """
        Backported from python 2.7
        """
        def handle(self, record):
            pass

        def emit(self, record):
            pass

        def createLock(self):
            self.lock = None


def get_method_type(func, obj):
    if PY2:
        return types.MethodType(func, obj, type(obj))
    else:
        return types.MethodType(func, obj)
