# -*- coding: utf-8 -*-

# se n'ai pas moi qui les fait c'est mon tuteur de stage qui la fait

"""
All fonction to validate data
"""
# import
from files import FileFuncError
import logging
import os
import re
import unicodedata

# variable
acceptedChars = r'[^a-zA-Z0-9_ .-]'
badFileNameRe = r"[/@#&é\"\'\\(§è!çà)êëîï$\*`£ù%+=:;,\?]"
dateTimePatern = r"""
    ^
    (202[1-9])\-
    (0[1-9]|1[0-2]|[1-9])\-
    ([1-9]|0[1-9]|[1-2][0-9]|3[0-1])\_
    ([0-9]|0[0-9]|1[0-2])\:
    ([0-9]|[0-5][0-9])
    $
    """
goodHexWordReg = '^0x([0-9a-fA-F]{2}){1,}$'
ipPatern = r"""
    ^                                                   #Start
    ((25[0-5]|2[0-4][0-9]|1([0-9]){2}|[0-9]{1,2})\.){3} #0 to 255 with . 3 time
    (25[0-5]|2[0-4][0-9]|1([0-9]){2}|[0-9]{1,2})        #0 to 255 1 time
    $                                                   #end
    """

logger = logging.getLogger(__name__)


# Functions
def cleanStr(aString: str) -> str:
    """
    This function remove special char from a string.
    Special char removed are stored in acceptedChars define at beginig of this file
    :param aString: a string to clean
    :return: a string without accent and without bad char
    """
    aStringWithoutAccents = stripAccents(aString)
    rx = re.compile(acceptedChars)
    cleanedString = rx.sub('_', aStringWithoutAccents).strip()
    logger.debug("Input string: %s, output string: %s" % aString, cleanedString)
    return cleanedString


def checkFileName(fileName:str)->bool:
    """
    Check if file name does not contain bad char
    :param fileName: the file name to test
    :return: True if filename does not contain special forbiden char.
    """
    return re.match(badFileNameRe, fileName) is None


def checkFileNameIsFull(fileName: str, rwFolder: bool = False) -> str:
    """
    Check if it's a full file name and convert it if not. If no path is provided, we use home folder of the current
    user. We also clean the file name to avoid special char or accents.
    :param fileName:
    :param rwFolder:
    :return: return complete file name
    """
    logger.info("[checkFileNameIsFull] Start.\n")
    if fileName.find('/') == -1:
        # This is a simple file name. Set fullFileName in home directory
        logger.info("[checkFileNameIsFull] No path provided, using home directory.\n")
        path =  f"{os.environ['HOME']}/"
        goodFileName = cleanStr(fileName)
    elif (fileName.endswith('/')) or (os.path.isdir(fileName)):
        logger.fatal("A folder have been provided as full file name!\n")
        raise DataFuncError("checkFileNameIsFull", "A folder have been provided as full file name!\n")
    else:
        goodFileName = cleanStr(fileName.split('/')[-1])
        path = "/".join(fileName.split('/')[0:-1]) + '/'
    if not checkFileName(goodFileName):
        message = f"bad File name %s! Please remove special char.\n" % goodFileName
        logger.fatal(message)
        raise DataFuncError("checkFileNameIsFull", message)
    try:
        path = checkPath(path, rwFolder)
    except FileFuncError as fFE:
        logger.fatal("Bad Path: %s" % fFE)
        raise DataFuncError("checkFileNameIsFull", "Bad Path!", fFE)
    logger.info("[checkFileNameIsFull] End.\n")
    return path + goodFileName


def checkIfIp(IPv4:str)->bool:
    """
    If ipAddress is a correct IPv4
    :param IPv4: a string containing IPv4
    :return: True if IP is correct
    """
    return checkPatern(ipPatern, IPv4)


def checkPatern(pattern:str, toCheck:str)->bool:
    """
    compare tochek with regex pattern and return true if match
    :param pattern: the regex pattern
    :param toCheck: the string to check
    :return: True if match
    """
    return re.match(pattern, toCheck, re.VERBOSE) is not None


def checkPath(path: str, rwFolder: bool = False) -> str:
    """
    Check a file path. if path is not clear, return home directory.
    :param path: the path to check
    :param rwFolder: if set to True, check if path is writable
    :return: return the path
    """
    # check path format and correct it
    if path.find('/') == -1:
        if path == "":
            goodPath = os.getcwd() + '/'
        elif path.find('\\') == -1:
            goodPath = os.getcwd() + '/' + path + '/'
        else:
            goodPath = path.replace('\\', '/')
            if not goodPath.endswith('/'):
                goodPath += '/'
    else:
        goodPath = path
        if not path.endswith('/'):
            goodPath += '/'
    # check path exist
    if not os.path.isdir(goodPath):
        message = f"Path {goodPath} Does not exist!"
        logger.fatal(message)
        raise DataFuncError("checkPath", message)
    # Check if path is RW
    if (not os.access(goodPath, os.W_OK)) and rwFolder:
        message = f"No write permission for Path {goodPath}!"
        logger.fatal(message)
        raise DataFuncError("checkPath", message)
    return goodPath


def stripAccents(str2Clean: str) -> str:
    """
    Remove accent from a string
    :param str2Clean: the string to clean
    :return: a clean string
    """
    return ''.join(c for c in unicodedata.normalize('NFD', str2Clean) if unicodedata.category(c) != 'Mn')


# Error management
class DataFuncError(Exception):
    def __init__(self, funcName, message, origineMessage=None):
        Exception.__init__(self, message)
        self.funcName = funcName
        self.message = message
        self.origineMessage = origineMessage

    def __str__(self):
        return f'\n\tFunc:\t{self.funcName}\n\tError:\t{self.message}\n\tSource:\t{self.origineMessage}'
