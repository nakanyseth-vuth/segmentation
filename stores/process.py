import os
from typing import List, Dict, Union

from segmentation.bilstm_tokenizer import tokenize_sentences_bilstm_pos, tokenize_sentences_bilstm
from segmentation.models import Intent


myList = []

def pos(fileName: str):
    file = open("generate/{}/{}_segment.txt".format(fileName, fileName), mode="r", encoding="UTF-8")
    oldList = file.readlines()
    lines: List[str] = [x.strip() for x in oldList]
    file.close()

    list = tokenize_sentences_bilstm_pos(lines)

    f = open("generate/{}/{}_pos.txt".format(fileName, fileName), mode="w+", encoding="UTF-8")
    for intent in list:
        f.write(intent + "\n")
    f.close()


def segment(fileName: str):
    file = open("generate/{}/{}.txt".format(fileName, fileName), mode="r", encoding="UTF-8")
    oldList = file.readlines()
    lines: List[str] = [x.strip() for x in oldList]
    file.close()

    sentences = tokenize_sentences_bilstm(lines)

    createDir(fileName, fileName2=fileName + "_segment")
    newFile = open("generate/{}/{}_segment.txt".format(fileName, fileName), mode="w+", encoding="UTF-8")
    for x in sentences:
        newFile.write(x + "\n")
    newFile.close()


def entity(fileName: str, intentMap: Dict[Intent, Union[List[str], List[str]]]):
    for x in intentMap:
        intentMap[x] = tokenize_sentences_bilstm(intentMap[x])
    print(intentMap)

    file = open("generate/{}/{}_segment.txt".format(fileName, fileName), mode="r", encoding="UTF-8")
    oldList = file.readlines()
    lines: List[str] = [x.strip() for x in oldList]
    file.close()

    list = []
    errorList = []

    for sentence in lines:
        newSentence = ""
        print("sentence: " + sentence)

        for intent in intentMap:
            length = 0
            word: str = ""

            for index in range(len(intentMap[intent])):
                if sentence.lower().strip().__contains__(intentMap[intent][index].strip().lower()) and length < len(
                        intentMap[intent][index]):
                    length = len(intentMap[intent][index])
                    word = intentMap[intent][index].strip()
                else:
                    errorIndex = index

            if word != "":
                ree = intent.splitEntity(word)
                print("split Entity: " + str(ree))

                if newSentence == "":
                    newSentence = sentence.replace(word, ree)
                else:
                    newSentence = newSentence.replace(word, ree)

        # lastSentence = re.sub(r"/[A-Z]-[A-Z]{3,7}", "", list[-1])
        if newSentence == "" and sentence != "":
            print("ERROR SENTENCE: " + sentence)
            list.append(sentence)
            errorList.append(sentence)

        print("newSentence; " + newSentence)
        list.append(newSentence)

    createDir(fileName, fileName2=fileName + "_entity")
    f = open("generate/{}/{}_entity.txt".format(fileName, fileName), mode="w+", encoding="UTF-8")
    for intent in list:
        if intent:
            f.write(intent + "\n")
    f.close()

    print("passeddddddd")
    print("Error List: ")
    for x in errorList:
        if x != "":
            print(x)


def createDir(fileName, fileName2):
    os.makedirs(os.path.dirname("generate/{}/{}.txt".format(fileName, fileName2)), exist_ok=True)


def fileio(fileName, msg, mode: str = "a+"):
    # create a file
    createDir(fileName, fileName2=fileName)

    f = open("generate/{}/{}.txt".format(fileName, fileName), mode=mode, encoding="utf-8")
    f.write(msg + "\n")
    f.close()


def sentences(fileName, word1, word2, word3, word4, word5):
    # tmp = "\n word1:" + str(word1) + "\n " + "word2:" + str(word2) + "\n " + "word3:" + str(
    #     word3) + "\n " + "word4:" + str(word4) + "\n " + "word5:" + str(
    #     word5) + "\n " + "_______________________________________________"
    #
    # fileio(fileName, tmp)
    fileio(fileName, "", mode="a+")
    for i in range(len(word1)):
        for j in range(len(word2)):
            for k in range(len(word3)):
                for m in range(len(word4)):
                    for r in range(len(word5)):
                        x = "តើ" + word1[i - 1] + word2[j - 1] + word3[k - 1] + word4[m - 1] + word5[r - 1]
                        print(x)
                        myList.append(x)
                        fileio(fileName, x)

