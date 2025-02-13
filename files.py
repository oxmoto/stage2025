# -*- coding: utf-8 -*-
"""
Tools for files manipulation

"""

# imports
import json
import logging
import os
import pickle



# vars
SECRET_PATH_ENV = "SECRET_PATH"

logger = logging.getLogger(__name__)

# functions old and deprecated
# def initLogs(logSecret: str, name: str, logLevel: str) -> (logging.Logger, str):
#     """"""
#     # get log file path
#     logsPathsSecret = None
#     log = str()
#     logLevelDict = {
#         'debug': logging.DEBUG,
#         'info':  logging.INFO,
#         'warn':  logging.WARNING,
#         'err':   logging.ERROR,
#         'crit':  logging.CRITICAL,
#     }
#     if logLevel not in logLevelDict.keys():
#         raise ValueError(f'initLogs fail: logLevel need to be in {logLevelDict.keys()}!')
#     try:
#         logsPathsSecret, initLog = loadSecretFromFile('logsSecrets', True)
#         assert isinstance(logsPathsSecret, dict)
#         logFilePath = logsPathsSecret['basePath'] + logsPathsSecret[logSecret]
#     except EnvVarError as eVE:
#         log += f'Cant find secret with log path:{initLog}\n'
#         log += str(eVE)
#         log += f"Using {os.environ['HOME']}/ as path for logs!\n"
#         logFilePath = f"{os.environ['HOME']}/"
#     except FileFuncError as fFE:
#         log += 'Cant read the file with log secrets!'
#         log += str(fFE)
#         log += f"Using {os.environ['HOME']}/ as path for logs!\n"
#         logFilePath = f"{os.environ['HOME']}/"
#     except AssertionError as aE:
#         log += f'secret is not a dict! secret: {logsPathsSecret}, type: {logsPathsSecret}'
#         log += str(aE)
#         log += f"Using {os.environ['HOME']}/ as path for logs!\n"
#         logFilePath = f"{os.environ['HOME']}/"
#     log += f'Log file for {name} is {logFilePath}.\n'
#     logger = logging.getLogger(name)
#     logger.setLevel(logLevel)
#     ch = logging.FileHandler(filename=logFilePath, mode='a', encoding=None)
#     ch.setLevel(logLevel)
#     formatter = logging.Formatter(logsPathsSecret['logFormat'])
#     ch.setFormatter(formatter)
#     logger.addHandler(ch)
#     log = 'Log init successfully'
#     return logger, log


def loadBinaryObject(fileName: str) -> object:
    """
    Load a binary object from file
    :param fileName: the file to read
    :return: Object read and logs or empty string
    """
    logger.info("[loadBinaryObject] Start\n")
    fullFileName = checkFileNameIsFull(fileName)
    logger.debug("[loadBinaryObject] File Full name: %s.\n" % fullFileName)
    try:
        with open(fullFileName, "rb") as fileToRead:
            objectFromFile = pickle.load(fileToRead)
        assert fileToRead.closed
        logger.info("[loadBinaryObject] file %s read successfully!\n" % fullFileName)
        logger.info("[loadBinaryObject] End.\n")
        return objectFromFile
    except IOError as returnedError:
        logger.fatal("Read error: \n %s" % returnedError)
        raise FileFuncError("loadBinaryObject", "Read error!", returnedError)
    except Exception as returnedError:
        logger.fatal("Unexpected error: \n %s" % returnedError)
        raise FileFuncError("loadBinaryObject", "Unexpected error", returnedError)


def loadJsonFile(fileName: str) -> dict:
    """
    This function is used to load a json file
    :param fileName: the file name containing the json
    :return: a tuple with a dict and log or empty strings
    """
    logger.info("[loadJsonFile] Start\n")
    fullFileName = checkFileNameIsFull(fileName)
    logger.debug("[loadJsonFile] File Full name: %s.\n" % fullFileName)
    try:
        with open(fullFileName, "r") as fileToRead:
            brutData = json.load(fileToRead)
        assert fileToRead.closed
        logger.debug("[loadJsonFile] file %s readed successfully!\n" % fullFileName)
        logger.info("[loadJsonFile] End.\n")
        return brutData
    except IOError as returnedError:
        logger.fatal("Read error: %s" % returnedError)
        raise FileFuncError("loadJsonFile", "Read error!", returnedError)
    except Exception as returnedError:
        logger.fatal("Unexpected error: %s" % returnedError)
        raise FileFuncError("loadJsonFile", "Unexpected error", returnedError)


def loadSecretFromFile(secretFile: str, secretPathEnv: str = SECRET_PATH_ENV) -> dict:
    """
    This function load a secret from a file name located in folder stored in env VAR.
    Default SECRET_PATH_ENV is set at begining of this file.
    :param secretFile: the secret file name
    :param secretPathEnv: the env variable. set to ECRET_PATH_ENV by default
    :return: The secret dict and log or empty str
    """
    secretPath = os.getenv(secretPathEnv)
    if (secretPath is None) or (secretPath == ""):
        logger.fatal('Cant find Environment Var %s!' % secretPathEnv)
        raise EnvVarError('main', f'Cant find Environment Var %s!' % secretPathEnv)
    secretFqn = secretPath + secretFile
    secret = loadJsonFile(secretFqn)
    return secret


def loadTextFile(fileName: str) -> str:
    """
    This function is used to load a text file in a string
    :param fileName: The text file to load
    :return: a string
    """
    logger.info("[loadTextFile] Start\n")
    fullFileName, checkLog = checkFileNameIsFull(fileName, True)
    logger.debug("[loadTextFile] File Full name: %s.\n" % fullFileName)
    try:
        with open(fullFileName, "r") as fileToRead:
            brutData = fileToRead.read()
        assert fileToRead.closed
        logger.debug("[loadTextFile] file %s readed successfully!\n" % fullFileName)
        logger.debug("[loadTextFile] End.\n")
        return brutData
    except IOError as returnedError:
        logger.fatal("Read error: %s" % returnedError)
        raise FileFuncError("loadTextFile", "Read error!", returnedError)
    except Exception as returnedError:
        logger.fatal("Unexpected error: %s" % returnedError)
        raise FileFuncError("loadTextFile", "Unexpected error", returnedError)


def writeFileJson(listOfDict: list, fileName: str) -> None:
    """
    Write a string list in a file.
    :param listOfDict: list of dict objects
    :param fileName: the file to write
    :return: logs or empty string
    """
    logger.info("[writeFileJson] Start.\n")
    try:
        fullFileName, checkLog = checkFileNameIsFull(fileName, True)
    except FileFuncError as fFE:
        logger.fatal("file name error")
        raise FileFuncError("writeFileCvs", "file name error", fFE)
    logger.debug("[writeFileJson] File Full name: %s.\n" % fullFileName)
    try:
        with open(fullFileName, "w") as fileToWrite:
            json.dump(listOfDict, fileToWrite, sort_keys=True, indent=4)
        assert fileToWrite.closed
        logger.debug("[writeFileJson] file %s writen successfully!\n" % fullFileName)
        logger.info("[writeFileJson] End.\n")
    except IOError as returnedError:
        logger.fatal("Write error: %s" % returnedError)
        raise FileFuncError("writeFileJson", "Write error!", returnedError)
    except Exception as returnedError:
        logger.fatal("Unexpected error: %s" % returnedError)
        raise FileFuncError("writeFileJson", "Unexpected error", returnedError)


def writeLineInFile(stringLine: str, fileName: str, newFile: bool = False) -> None:
    """
    Write a line in a file.
    :param stringLine: a string to add
    :param fileName: the file to write
    :param newFile: True if we want to create the file
    :return: logs or empty string
    """
    logger.info("[writeLineInFile] Start.\n")
    fullPathFile = checkFileNameIsFull(fileName)
    if newFile:
        openMode = 'w'
    else:
        openMode = 'a'
    try:
        with open(fullPathFile, openMode) as fileToWrite:
            fileToWrite.write(stringLine)
        assert fileToWrite.closed
        logger.debug("[writeLineInFile] Line added in %s file.\n" % fullPathFile)
        logger.info("[writeLineInFile] End.\n")
    except IOError as returnedError:
        logger.fatal("File write error: %s" % returnedError)
        raise FileFuncError("writeLineInFile", "File write error.", returnedError)
    except AssertionError as returnedError:
        logger.fatal("Unexpected error: %s" % returnedError)
        raise FileFuncError("writeLineInFile", "Unexpected error.", returnedError)


def writeObjectInFile(myObjectList: list, fileName: str) -> None:
    """
    Write an object list in a binary file.
    :param myObjectList: the object list to write
    :param fileName: the file to write
    :return: logs or empty string
    """
    logger.info("[writeObjectInFile] Start\n")
    fullFileName = checkFileNameIsFull(fileName)
    logger.debug("[writeObjectInFile] File Full name: %s.\n" % fullFileName)
    try:
        with open(fullFileName, "wb") as fileToWrite:
            pickle.dump(myObjectList, fileToWrite)
        assert fileToWrite.closed
        logger.debug("[writeObjectInFile] file %s writen successfully!\n" % fullFileName)
        logger.info(f"[writeObjectInFile] End.\n")
    except IOError as returnedError:
        logger.fatal("Write error: %s" % returnedError)
        raise FileFuncError("writeObjectInFile", "Write error!", returnedError)
    except Exception as returnedError:
        logger.fatal("Unexpected error: %s" % returnedError)
        raise FileFuncError("writeObjectInFile", "Unexpected error", returnedError)


def writeTextInFile(string2Write: list, fileName: str) -> None:
    """
    Write a string list in a text file.
    :param string2Write: a list of objets
    :param fileName: the file to write
    :return: logs or empty string
    """
    logger.info("[writeTextInFile] Start\n")
    fullFileName, checkLog = checkFileNameIsFull(fileName, True)
    logger.debug("[writeTextInFile] File Full name: %s.\n" % fullFileName)
    try:
        with open(fullFileName, "w") as fileToWrite:
            fileToWrite.write('\n'.join(string2Write))
        assert fileToWrite.closed
        logger.debug("[writeTextInFile] file %s writen successfully!\n" % fullFileName)
        logger.info(f"[writeTextInFile] End.\n")
    except IOError as returnedError:
        logger.fatal("Write error: %s" % returnedError)
        raise FileFuncError("writeTextInFile", "Write error!", returnedError)
    except Exception as returnedError:
        logger.fatal("Unexpected error: %s" % returnedError)
        raise FileFuncError("writeTextInFile", "Unexpected error", returnedError)


# Error management
class EnvVarError(Exception):
    def __init__(self, funcName, message, origineMessage=None):
        Exception.__init__(self, message)
        self.funcName = funcName
        self.message = message
        self.origineMessage = origineMessage

    def __str__(self):
        return f'\n\tFunc:\t{self.funcName}\n\tError:\t{self.message}\n\tSource:\t{self.origineMessage}'


class FileFuncError(Exception):
    def __init__(self, funcName, message, origineMessage=None):
        Exception.__init__(self, message)
        self.funcName = funcName
        self.message = message
        self.origineMessage = origineMessage

    def __str__(self):
        return f'\n\tFunc:\t{self.funcName}\n\tError:\t{self.message}\n\tSource:\t{self.origineMessage}'