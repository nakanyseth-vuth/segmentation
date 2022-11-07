from models import Intent
from stores.process import sentences, segment, entity, pos, convertToCSV, getAllFile
import os
import shutil


if __name__ == '__main__':
    """
    FindEnrollmentLocation, AskaboutRegisterDate, AskaboutMotocycleParkingFee, AskaboutFemaleDressCode, AskaboutMaleDressCode, IsExistDoorExit, WhyshouldchooseCADT, SchoolMission
    """
    # fileName, words1, words2, words3, words4, words5,words6, intentMap = askWhereHRRoomIs()

    # sentences(fileName=fileName, word1=words1, word2=words2,
    #           word3=words3, word4=words4, word5=words5, word6=words6, initialWord=False)
    # segment(fileName=fileName)
    # entity(fileName=fileName, intentMap=intentMap)
    # pos(fileName=fileName)
    # convertToCSV(fileName=fileName)
    shutil.copyfile("generate/ListEvent/ListEvent.txt", "rise/ListEvent.txt")

    # getAllFile()
