import os
from pathlib import Path
from typing import List

from bilstm_tokenizer import tokenize_sentences_bilstm

from segmentation.models import Intent


def segment(fileName: str):
    file = open("generate/{}/{}.txt".format(fileName, fileName), mode="r", encoding="UTF-8")
    oldList = file.readlines()
    lines: List[str] = [x.strip() for x in oldList]
    file.close()

    sentences = tokenize_sentences_bilstm(lines)

    newFile = open("generate/{}/{}_segment.txt".format(fileName,fileName), mode="w+", encoding="UTF-8")
    for x in sentences:
        newFile.write(x + "\n")
    newFile.close()


def entity(fileName: str):
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

            if word:
                ree = intent.splitEntity(word)
                print("split Entity: " + str(ree))

                if newSentence == "":
                    newSentence = sentence.replace(word, ree)
                else:
                    newSentence = newSentence.replace(word, ree)

            else:
                if newSentence == "":
                    list.append(newSentence)
                    errorList.append(newSentence)
                else:
                    errorList.append(sentence)
            print("newSentence: " + newSentence)

        print("newSentence; " + newSentence)
        list.append(newSentence)

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


def createDir(fileName):
    os.makedirs(os.path.dirname("generate/{}/{}.txt".format(fileName, fileName)), exist_ok=True)


def fileio(fileName, msg):
    # create a file
    createDir(fileName)

    f = open("generate/{}/{}.txt".format(fileName, fileName), 'w+', encoding="utf-8")
    f.write(msg + "\n")
    f.close()


def sentences(fileName, word1, word2, word3, word4, word5):
    # tmp = "\n word1:" + str(word1) + "\n " + "word2:" + str(word2) + "\n " + "word3:" + str(
    #     word3) + "\n " + "word4:" + str(word4) + "\n " + "word5:" + str(
    #     word5) + "\n " + "_______________________________________________"
    #
    # fileio(fileName, tmp)

    for i in range(len(word1)):
        for j in range(len(word2)):
            for k in range(len(word3)):
                for m in range(len(word4)):
                    for r in range(len(word5)):
                        x = "តើ" + word1[i - 1] + word2[j - 1] + word3[k - 1] + word4[m - 1] + word5[r - 1]
                        print(x)
                        myList.append(x)
                        fileio(fileName, x)


myList = []

intentMap = {
    Intent.Person: ["Darot", " ដារូ៉ត ", "Jojo", "ចូចូ", "Lita", "លីតា",
                    "Duoung", "ដួង", "Linda",
                    " លីនដា ", "Sokleap", " សុខលាភ "],
    Intent.Organization: ["CADT", "សាលាសុីអេឌុីធី", "សាលាCADT", "សាកលវិទ្យាល័យCADT", "សាកលវិទ្យាល័យសុីអេឌុីធី",
                          "វិទ្យាល័យCADT",
                          " វិទ្យាល័យសុីអេឌុីធី "]
}

if __name__ == '__main__':
    # sents = ["តើ Darot/B-PER ដឹងថា CADT/B-ORG មានសិស្សសរុបប៉ុន្មាន?",
    #          "តើដារូ៉តមានដឹងសាកលវិទ្យាល័យCADTមាននិស្សិតសុីអេឌុីមានសិស្សសរុបប៉ុន្មានអ្នក?"]
    # res = tokenize_sentences_bilstm(sents)
    # print(res)

    intentMap[Intent.Person] = tokenize_sentences_bilstm(intentMap[Intent.Person])
    intentMap[Intent.Organization] = tokenize_sentences_bilstm(intentMap[Intent.Organization])

    print(intentMap)

    fileName = "FindTotalStudentsV4"

    # Pe edit ah nis edit ah ler pg and brab tv tha ah na intent ah na, kom oy error klang,
    # doch សុខលាភ -> សុខ លាភ since they are first name all, add space between them
    # " សុខលាភ "
    # And dont forget to mer error list pg and recheck everything

    words1 = ["Darot", " ដារូ៉ត ", "Jojo", "ចូចូ", "Lita", "លីតា",
              "Duoung", "ដួង", "Linda",
              " លីនដា ", "Sokleap", " សុខលាភ "]

    words2 = ["ដឹងថា", "មានដឹង"]

    words3 = ["CADT", "សាលាសុីអេឌុីធី", "សាលាCADT", "សាកលវិទ្យាល័យCADT", "សាកលវិទ្យាល័យសុីអេឌុីធី", "វិទ្យាល័យCADT",
              " វិទ្យាល័យសុីអេឌុីធី "]

    words4 = ["មានសិស្សសរុប", "មាននិស្សិតសរុប", "មាននិស្សិត"]

    words5 = ["ប៉ុន្មាន?", "ប៉ុន្មានអ្នក?", "ម៉ាន?", "ម៉ានអត់?", "ម៉ានទេ?",
              "ម៉ានអ្នក?"]

    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5)
    # segment(fileName=fileName)
    entity(fileName=fileName)
