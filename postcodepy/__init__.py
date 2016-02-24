"""
 _____         _             _             
|  _  |___ ___| |_ ___ ___ _| |___ ___ _ _ 
|   __| . |_ -|  _|  _| . | . | -_| . | | |
|__|  |___|___|_| |___|___|___|___|  _|_  |
                                  |_| |___|

"""
__title__ = "Postcode API Wrapperi for the REST API of Postcode.nl"
__version__ = "1.0.0"
__author__ = "Feite Brekeveld"
__license__ = "MIT"
__copyright__ = "Copyright 2014-2016 Feite Brekeveld"

# Version synonym
VERSION = __version__

from .postcodepy import API, PostcodeError    # flake8: noqa
