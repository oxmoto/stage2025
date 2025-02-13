import json
import logging
from projet1 import main, get_host_number


from dataValidation import checkFileNameIsFull
from files import FileFuncError
from nombre import calcule

logger = logging.getLogger(__name__)

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

def memu(liste_string):
    """
    qu'est-ce que ça fait
    :param liste_string: liste de chaine de caracteres
    :return: la chaine selectioné
    """
    nbr_entry = 0
    chois_int = -1
    if len(liste_string) <= 0:
        return 'exit'
    for entry in liste_string:
        nbr_entry += 1
        print(f'{nbr_entry} - {entry}')
    print('0 - Exit')
    while 0 > chois_int or nbr_entry < chois_int:
        chois_int = int(input("Quel est votre chois?"))
        if 0 > chois_int or nbr_entry < chois_int:
            print(f"Merci de choir une valeur entre 0 et {nbr_entry}!")
    if chois_int==0:
        return 'exit'
    else:
        return liste_string[chois_int-1]



"""
Menu
1- chois1
2- Chois2
3- Chois3
4- chois4
0- exit
Que voulez vous faire?
len(list_chois)
Appel:
list_chois=["chois1","chois2"...]
chois=memu(list_chois)
if chois == "chois1":
    print("chois1")
elif chois == "chois2":
    print("chois2")
elif chois == "chois3":
    print("chois3")
elif chois == "chois4":
    print("chois4")
else:
    print("exit")
    
test={"test1":1,"test2":2}

[test,]
"""
