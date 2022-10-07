from segmentation.models import Intent
from segmentation.stores.process import pos
from segmentation.test import sentences, segment, entity


def busInfo():
    fileName = "BusInfo"
    words1 = ["ដឹងទេថា", "មានដឹងថា"]

    words2 = ["សាលាCADT", "សាលាស៊ីអេឌីធី", "បណ្ឌិតសភាបច្ចេកវិទ្យាឌីជីថល", "CADT"]

    words3 = ["មានឡានក្រុង", "មានឡានដឹកសិស្ស", "មានរថយន្តដឹកសិស្ស"]

    words4 = ["ដើម្បីដឹកសិស្ស", "សម្រួលការធ្វើដំណើររបស់សិស្ស"]

    words5 = ["អត់?", "ដែរទេ?", "ចំនួនប៉ុន្មាន?"]

    sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5)
    segment(fileName=fileName)
    entity(fileName=fileName, intentMap={})

def socialMediaExist():
    fileName = "SocialMediaExist"

    words1 = ["Manuth", "ម៉ាន៉ុត", " Rithiya", "រិទ្ធិយ៉ា", "Chhunheang", "ឈុនហ៊ាង",
              "Kimhong", "គីមហុង", "Nary",
              "ណារី", " Nao ", "ណោ"]

    words2 = ["មានដឹង", "ដឹងថា"]
    words3 = ["សាលាមាន"]
    words4 = [' Facebook page ', " ហ្វេសបុកភេច", " social media page ", " សូសលមីឌិរភេច ", " page ",
              "ភេច",
              " instagram page ", "អុីនស្តាក្រាម ភេច", " Twitter ", "ថ្វីតធឺរ", " TikTok ",
              "តិកតុក"]

    words5 = ["អត់?", "ទេ?"]

    intentMap = {
        Intent.Person: words1,
        Intent.Organization: words4,
        # Intent.Building: ["អន្តេរវាសិកដ្ឋាន", "Dorm", "កន្លែងស្នាក់"],
        # Intent.Room: ["ផ្ទះបាយ", "បន្ទប់ទឹក"],
    }

    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5)
    # segment(fileName=fileName)
    entity(fileName=fileName, intentMap=intentMap)


def findTotalStudent():
    fileName = "FindTotalStudentV5"

    # words1 = ["Darot", "ដារូ៉ត", "Jojo", "ចូចូ", "Lita", "លីតា",
    #           "Duoung", "ដួង", "Linda",
    #           "លីនដា", "Sokleap", "សុខលាភ"]
    #
    # words2 = ["ដែលដឹងថា", "", ]
    #
    # words3 = ["CADT", "សាលាសុីអេឌុីធី", "សាលាCADT", "សាកលវិទ្យាល័យCADT", "សាកលវិទ្យាល័យសុីអេឌុីធី", "វិទ្យាល័យCADT",
    #           "វិទ្យាល័យសុីអេឌុីធី"]
    #
    # words4 = ["មានសិស្សសរុប", "មាននិស្សិតសរុប", "មាននិស្សិត"]
    #
    # words5 = ["ប៉ុន្មាន?", ]
    words1 = ["នៅCADT", "នៅសាលាសុីអេឌុីធី", "នៅសាលាCADT", "នៅសាកលវិទ្យាល័យCADT", "នៅសាកលវិទ្យាល័យសុីអេឌុីធី",
              "នៅវិទ្យាល័យCADT",
              "នៅវិទ្យាល័យសុីអេឌុីធី"]

    words2 = ["Darot", "ដារូ៉ត", "Jojo", "ចូចូ", "Lita", "លីតា",
              "Duoung", "ដួង", "Linda",
              "លីនដា", "Sokleap", "សុខលាភ"]

    words3 = ["ដឹងទេថា", "ដែលដឹងថា", ]

    words4 = ["មានសិស្សសរុប", "មានstudent", "មាននិស្សិត"]

    words5 = ["ប៉ុន្មាន?"]

    intentMap = {
        Intent.Organization: words1,
        Intent.Person: words2,
        # Intent.Building: ["អន្តេរវាសិកដ្ឋាន", "Dorm", "កន្លែងស្នាក់"],
        # Intent.Room: ["ផ្ទះបាយ", "បន្ទប់ទឹក"],
    }
    #
    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5)
    # segment(fileName=fileName)
    # entity(fileName=fileName, intentMap=intentMap)
    pos(fileName=fileName)


def schoolMajor():
    fileName = "AskAboutSchoolMajors"

    # words1 = ["Darot", "ដារូ៉ត", "teacher Dara", "លោកគ្រូដារា", "Teacher Lita", "អ្នកគ្រូលីតា",
    #           "Sokleap", "សុខលាភ"]
    #
    # words2 = ["ដឹងថា", "អាចប្រាប់ខ្ញុំថា", "អាចជួយប្រាប់ខ្ញំុថា", "មានលទ្ធភាពបា្រប់ខ្ញំុថា"]
    #
    # words3 = ["CADT", "សាលាសុីអេឌុីធី", "សាលាCADT", "សាកលវិទ្យាល័យCADT", "សាកលវិទ្យាល័យសុីអេឌុីធី", "វិទ្យាល័យCADT",
    #           "វិទ្យាល័យសុីអេឌុីធី"]
    #
    # words4 = ["មានmajor", "មានវគ្កសិក្សា", "មានមហាវិទ្យាល័យ"]
    #
    # words5 = ["អ្វីខ្លះ?"]

    # "សាលានឹងមានរៀនអ្វីខ្លះ?"
    # "CADTមានមហាវិទ្យាល័យ"
    words1 = ["សាលាសុីអេឌុីធី", "សាលាCADT", "សាកលវិទ្យាល័យCADT", "សាកលវិទ្យាល័យសុីអេឌុីធី", "វិទ្យាល័យCADT",
              "វិទ្យាល័យសុីអេឌុីធី"]

    words2 = ["នឹង", "រប់សយើងនេះ", "របស់ខ្ញំុនេះ", "ដែលខ្ញំុរកំពុងតែរៀន", "ដែលយើងកំពុងតែរៀន"]

    words3 = ["មាន", ]

    words4 = ["រៀន", "វគ្កសិក្សា", "មហាវិទ្យាល័យ", "Major", "មេច័រ", "វគ្គបង្រៀន"]

    words5 = ["អ្វីខ្លះ?"]

    intentMap = {
        Intent.Person: ["Darot", "ដារូ៉ត", "teacher Dara", "លោកគ្រូដារា", "Teacher Lita", "អ្នកគ្រូលីតា",
                        "Sokleap", "សុខ លាភ", "វិទ្យាល័យ សុីអេឌុីធី"],
        Intent.Organization: ["សាលាសុីអេឌុីធី", "សាលាCADT", "សាកលវិទ្យាល័យCADT",
                              "វិទ្យាល័យCADT",
                              "វិទ្យាល័យសុីអេឌុីធី", "CADT",
                              "សាកលវិទ្យាល័យសុីអេឌុីធី"
                              ],
        # Intent.Building: ["អន្តេរវាសិកដ្ឋាន", "Dorm", "កន្លែងស្នាក់"],
        # Intent.Room: ["ផ្ទះបាយ", "បន្ទប់ទឹក"],
    }

    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5)
    # segment(fileName=fileName)
    # entity(fileName=fileName, intentMap=intentMap)
    pos(fileName=fileName)
