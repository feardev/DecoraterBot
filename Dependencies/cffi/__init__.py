# coding=utf-8
__all__ = ['FFI', 'VerificationError', 'VerificationMissing', 'CDefError',
           'FFIError']

# noinspection PyPep8
from .api import FFI, CDefError, FFIError
# noinspection PyPep8
from .ffiplatform import VerificationError, VerificationMissing

__version__ = "1.6.0"
__version_info__ = (1, 6, 0)

# The verifier module file names are based on the CRC32 of a string that
# contains the following version number.  It may be older than __version__
# if nothing is clearly incompatible.
__version_verifier_modules__ = "0.8.6"