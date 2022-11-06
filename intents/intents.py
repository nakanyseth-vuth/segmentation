import os

from models import Intent
from stores.process import pos
from test import sentences, segment, entity, convertToCSV


def findCurrentTime():
    fileName = "IsLibraryExist"

    words1 = ["អ្នក", "Danith", "ដាណីត", "Lita", "លីតា", "You", "យូរ", "Mey", "មីរ", "នៅសាលាCADT", "អាគារនេះជាន់នេះ"]
    words2 = ["មានដែរដឹងទេថា", "មានដែរឆ្ថល់ទេថា", "មានដែរចាប់អារម្មណ៍ទេថា"]
    words3 = ["សាលាយើង", "អាគារអុីនូវេសិនសែនធឺរ", "សាលាសុីអេឌីធី", "អាគារIDT", "អាគារអាយឌីធី"]
    words4 = ["មានបន្ទប់បណ្ណាល័យ"]
    words5 = ["ដែរឬទេ?"]

    intentMap = {
        Intent.Person: ["Mey", "មីរ", "ដាណីត", "Danith", "Lita", "លីតា"],
        Intent.Organization: ["សាលាCADT", "សាលាសុីអេឌីធី"],
        Intent.Building: ["អាគារ អុីនូវេសិនសែនធឺរ", "អាគារ IDT", "អាគារ អាយឌីធី"],
        # Intent.CountryCity: ["ប្រទេសFrance", "ប្រទេសបារាំង", "ប្រទេសCambodia", "ប្រទេសកម្ពុជា", "ប្រទេសអាឡីម៉ង់",
        #                      "ប្រទេសGermany"]
        Intent.Room: ["បន្ទប់ បណ្ណាល័យ"]
    }

    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5,
    #           initialWord=False)
    # segment(fileName=fileName)
    # entity(fileName=fileName, intentMap=intentMap)
    # pos(fileName=fileName)
    convertToCSV(fileName)


def AskHowToComplain():
    fileName = "AskHowToComplain"

    # words1 = ["ខ្ញំុ", "គាត់", "នាង", "ពួកយើង", "ថ្នាក់ពួកខ្ញំុ", "Vitou", "វីទូ", "Rathana", "រដ្ឋាណា",
    #           "សុខលាភនិងសាមឌី", "លីតានិងដាណីត"]
    # words2 = ["គួរតែ", "អាច", "ចង់", ]
    # words3 = ["Complain", "ដាក់លិខិតជំទាស់", "Report", "រាយការ", "រីភាត់"]
    # words4 = ["ទៅសាលា", "ទៅសាលាCADT", "ទៅសាលាសុីអេឌីធី", "ទៅលើអាគារInnovation Center", "ទៅលើអាគារ អុីនូវេសិនសែនធឺរ",
    #           "ទៅលើអាគារ IDT", "ទៅលើអាគារ អាយឌីធី"]
    # words5 = ["តាមរយះណាខ្លះ?", "បានយ៉ាងមិចខ្លះ?", ]

    words1 = ["ខ្ញំុ", "គាត់", "នាង", "ពួកយើង", "ថ្នាក់ពួកខ្ញំុ", "Vitou", "វីទូ", "Rathana", "រដ្ឋាណា",
              "សុខលាភនិងសាមឌី", "លីតានិងដាណីត"]
    words2 = ["មិនយល់ស្របទៅនឹងរបៀបធ្វើ", "ជំទាស់ទៅនឹងការដាក់ពន្ទុ", "អត់ពេញចិត្តទៅលើការធ្វើ", ]
    words3 = ["របស់សាលាទេ", "នៅនឹងសាលាCADT", "នៅនឹងសាលាសុីអេឌីធី", "នៅអាគារInnovation Center",
              "ទៅលើអាគារអុីនូវេសិនសែនធឺរ",
              "នៅអាគារ IDT", "ទៅអាគារអាយឌីធី", "របស់អ្នកគ្រូ", "របស់លោកគ្រូ", ]
    words4 = ["តើ"]
    words5 = ["គួរធ្វើដូចម្តេចទៅ?", "គួរធ្វើយ៉ាងមិចទៅ?", "គួរReportយ៉ាងមិចទៅ?"]

    intentMap = {
        Intent.Person: ["សុខលាភ", "សាមឌី", "ដាណីត", "Rathana", "រដ្ឋាណា", "លីតា", "វីទូ", "Vitou"],
        Intent.Organization: ["សាលា CADT", "សាលា សុីអេឌីធី"],
        Intent.Building: ["អាគារ អុីនូវេសិន សែនធឺរ", "អាគារ IDT", "អាគារ អាយឌីធី", "អាគារInnovation Center"],
        # Intent.CountryCity: ["ប្រទេសFrance", "ប្រទេសបារាំង", "ប្រទេសCambodia", "ប្រទេសកម្ពុជា", "ប្រទេសអាឡីម៉ង់",
        #                      "ប្រទេសGermany"]
        # Intent.Room: ["បន្ទប់ បណ្ណាល័យ"]
    }

    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5,
    #           initialWord=False)
    # segment(fileName=fileName)
    # entity(fileName=fileName, intentMap=intentMap)
    # pos(fileName=fileName)
    convertToCSV(fileName)


def FindTSC():
    filename = "FindTSC"
    # តើបន្ទប់TSCនៅទីណាទៅ?
    # ខ្ញំុកំពុងរកបន្ទប់TSC តើអាចប្រាប់ខ្ញំុបន្តិចបានទេ?
    # ខ្ញំុមានរៀងមួយចំនួនដែលត្រូវការជំនួយពីTSC តើអាចប្រាប់ទីតាំងTSCបានទេ?

    words1 = ["ខ្ញំុ", "រុន ចំរើន",
              "រុន ណាលិ",
              "រុន ធុល",
              "រុន សារិន",
              "រុន សារឿង",
              "លី កែវធីតា",
              "លី គីមគី",
              "លី គឹមលាង",
              "លី ជរ",
              "លី ជុងថេង",
              "លី ដាលីន",
              "លី ឌី",
              "លី ណាំ",
              "លី តារា",
              "លី ទឹង",
              "លី ប៉េងហ៊ាង",
              "លី ប៊ិច",
              "លី ប៊ុនទូច",
              "លី ប៊ុនរិទ្ធ",
              "លី មុនីពៅ",
              "លី ម៉ារ៉ុង",
              "លី ម៉េង",
              "លី រ៉ា",
              "លី ល័ក្ខនីតា",
              "លី វណ្ណដ្ឋា",
              "លី វណ្ណស៊ី",
              "លី សាន",
              "លី សាមិ",
              "លី សារុន",
              "លី សារ៉ន",
              "លី សារ៉េត",
              "លី សាលឿម",
              "លី សុខខេម",
              "លី សុខគីម",
              "លី សុខលាភ",
              "លី សុខា",
              "លី ស៊ីណា",
              "លី ស៊ីថា",
              "លី ស៊ីវម៉ី",
              "លី ស៊ុគ្រី",
              "លី ស៊ូវ៉ាន", ]
    words2 = ["កំពុងតែមានផលវិបាកក្នុងការរកបន្ទប់TSC", "កំពុងតែមានផលវិបាកក្នុងការរកបន្ទប់ធីអែសសុី"]
    words3 = ["តើអាចជួយប្រាប់"]
    words4 = ["បន្តិចពីទីតាំងរបស់បន្ទប់នឹង", "ថាជាន់ណាបានមានបន្ទប់TSC", "ថាជាន់ណាបានមានបន្ទប់ធីអែសសុី",
              "ថានៅអាគារណាបានមានបន្ទប់ធីអែសសុី", "ថានៅអាគារណាបានមានបន្ទប់TSC"]
    words5 = ["បានដែររឺទេ?"]

    intentMap = {
        Intent.Person: ["រុន ចំរើន",
                        "រុន ណាលិ",
                        "រុន ធុល",
                        "រុន សារិន",
                        "រុន សារឿង",
                        "លី កែវធីតា",
                        "លី គីមគី",
                        "លី គឹមលាង",
                        "លី ជរ",
                        "លី ជុងថេង",
                        "លី ដាលីន",
                        "លី ឌី",
                        "លី ណាំ",
                        "លី តារា",
                        "លី ទឹង",
                        "លី ប៉េងហ៊ាង",
                        "លី ប៊ិច",
                        "លី ប៊ុនទូច",
                        "លី ប៊ុនរិទ្ធ",
                        "លី មុនីពៅ",
                        "លី ម៉ារ៉ុង",
                        "លី ម៉េង",
                        "លី រ៉ា",
                        "លី ល័ក្ខនីតា",
                        "លី វណ្ណដ្ឋា",
                        "លី វណ្ណស៊ី",
                        "លី សាន",
                        "លី សាមិ",
                        "លី សារុន",
                        "លី សារ៉ន",
                        "លី សារ៉េត",
                        "លី សាលឿម",
                        "លី សុខខេម",
                        "លី សុខគីម",
                        "លី សុខលាភ",
                        "លី សុខា",
                        "លី ស៊ីណា",
                        "លី ស៊ីថា",
                        "លី ស៊ីវម៉ី",
                        "លី ស៊ុគ្រី",
                        "លី ស៊ូវ៉ាន", ],
        # Intent.Organization: ["សាលា CADT", "សាលា សុីអេឌីធី"],
        # Intent.Building: ["អាគារ អុីនូវេសិន សែនធឺរ", "អាគារ IDT", "អាគារ អាយឌីធី", "អាគារInnovation Center"],
        # Intent.CountryCity: ["ប្រទេសFrance", "ប្រទេសបារាំង", "ប្រទេសCambodia", "ប្រទេសកម្ពុជា", "ប្រទេសអាឡីម៉ង់",
        #                      "ប្រទេសGermany"]
        Intent.Room: ["បន្ទប់ ធីអែសសុី", "បន្ទប់ TSC"]
    }
    # sentences(fileName=filename, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5,
    #           initialWord=False)
    # segment(fileName=filename)
    # entity(fileName=filename, intentMap=intentMap)
    # pos(fileName=filename)
    convertToCSV(fileName=filename)


def ListEvent():
    fileName = "ListEventV2"

    # តើមានដឹងថាសាលាយើងមានEventអ្វីខ្លះអត់?
    # Xបានចាប់អារម្មណ៍ទៅលើeventសាលាយើងមានអ្វីខ្លះអត់?

    words1 = ["គាត់", "នាង", "ពួកយើង", "Vitou", "វីទូ", "Rathana", "រដ្ឋាណា",
              "កង់ ហាន់",
              "កង ញ៉ុង",
              "កង ឌីណាត",
              "កង ណី",
              "កង ប៊ន",
              "កង លាច",
              "កង លីណា",
              "កង វន្ថា",
              "កង វិគុណ",
              "កង សាមឌី",
              "កង សារី",
              "កង សាវ៉ន",
              ]
    words2 = ["ដែល"]
    words3 = ["បានចាប់អារម្មណ៏", "បានដឹងអត់"]
    words4 = ["ថា", "ទៅលើ"]
    words5 = ["Eventសាលា", "EventសាលាCADT", "សាលា សុីអេឌីធី", "ព្រឹត្តិការណ៍សាលា", "EventនៅអាគារInnovation Center",
              "Eventនៅអាគារអុីនូវេសិនសែនធឺរ", "ព្រឹត្តិការណ៍នៅអាគារអុីនូវេសិនសែនធឺរ", "Eventនៅអាគារអាយឌីធី",
              "ព្រឹត្តិការណ៍នៅអាគារអាយឌីធី", "EventនៅអាគារIDT"]
    words6 = ["យើងមានអ្វីខ្លះអត់?", "មានប៉ុន្មានខ្លះ?"]

    intentMap = {
        Intent.Person: ["Vitou", "វីទូ", "Rathana", "រដ្ឋាណា",
                        "កង់ ហាន់",
                        "កង ញ៉ុង",
                        "កង ឌីណាត",
                        "កង ណី",
                        "កង ប៊ន",
                        "កង លាច",
                        "កង លីណា",
                        "កង វន្ថា",
                        "កង វិគុណ",
                        "កង សាមឌី",
                        "កង សារី",
                        "កង សាវ៉ន"],
        Intent.Organization: ["សាលា CADT", "សាលា សុីអេឌីធី"],
        Intent.Building: ["អាគារ អុីនូវេសិន សែនធឺរ", "អាគារ IDT", "អាគារ អាយឌីធី", "អាគារInnovation Center"],
        # Intent.CountryCity: ["ប្រទេសFrance", "ប្រទេសបារាំង", "ប្រទេសCambodia", "ប្រទេសកម្ពុជា", "ប្រទេសអាឡីម៉ង់",
        #                      "ប្រទេសGermany"]
        # Intent.Room: ["បន្ទប់ បណ្ណាល័យ"]
    }

    sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5, word6=words6,
              initialWord=False)
    # segment(fileName=fileName)
    # entity(fileName=fileName, intentMap=intentMap)
    # pos(fileName=fileName)
    # convertToCSV(fileName=fileName)


def askAboutCompetition():
    fileName = "askAboutCompetition"

    # words1 = ["សាលាCADT", "សាលាស៊ីអេឌីធី", "បណ្ឌិតសភាបច្ចេកវិទ្យាឌីជីថលកម្ពុជា", "CADT"]
    #
    # words2 = ["មាន", "បាន"]
    #
    # words3 = ["បង្កើតនូវកម្មវិធី", "hostនូវកម្មវិធី", "បានប្រកាស់ថាមាន"]
    #
    # words4 = ["Competition", "ការប្រកួតប្រជែង"]
    #
    # words5 = ["អ្វីខ្លះ?"]

    # words1 = ["Vitou", "វិទូ", "លោកគ្រូវិទូ", "លោកគ្រូច័ន្ទត្រា", "teacher Chantra", "ច័ន្ទត្រា"]
    # words2 = ["អាចប្រាប់ខ្ញំុថា"]
    #
    # words3 = ["សាលាCADT", "សាលាស៊ីអេឌីធី", "បណ្ឌិតសភាបច្ចេកវិទ្យាឌីជីថលកម្ពុជា", "CADT"]
    #
    # words4 = ["យើងមានCompetition", "របស់ពួកយើងមានបានបង្កើតEvent Competition", "របស់ពួកយើងមានបានបង្កើតកម្មវិធីប្រកួតប្រជែង"]
    #
    # words5 = ["អ្វីខ្លះ?"]

    words1 = ["នៅអាគារinnovation center", "នៅអាគារអុីនូវេសិនសែនធឺរ"]
    words2 = ["និង"]
    words3 = ["អាគារIDT", "អាគារអាយដីធី"]
    words4 = ["នឹង", "ដែលខ្ញំុរៀននឹង", "ដែលខ្មំុកំពុងនៅនឹង"]
    words5 = ["គេមានបានបង្កើតកម្មវីធីប្រកួតប្រជែងអ្វីខ្លះ?", "គេមានបានHostកម្មវីធីប្រកួតប្រជែងអ្វីខ្លះ?"]

    intentMap = {
        Intent.Person: ["Vitou", "វិទូ", "លោកគ្រូវិទូ", "លោកគ្រូច័ន្ទត្រា", "teacher Chantra", "ច័ន្ទត្រា"],
        Intent.Organization: ["សាលាCADT", "សាលាស៊ីអេឌីធី", "បណ្ឌិតសភាបច្ចេកវិទ្យាឌីជីថលកម្ពុជា", "CADT"],
        Intent.Building: ["នៅអាគារinnovation center", "នៅអាគារអុីនូវេសិនសែនធឺរ"]
    }

    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5)
    # segment(fileName=fileName)
    entity(fileName=fileName, intentMap=intentMap)
    pos(fileName=fileName)


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


def findCurrentTime():
    fileName = "FindCurrentTimeV2"
    # នៅពេលនេះម៉ោងប៉ុន្មានហើយ?
    # words1 = ["ខ្ញំុចង់សួរថា", "ខ្ញំុឆ្ងល់ថា", "ហើយចុះ", "មិត្តខ្ញំុឆ្ងល់ថា", "គាត់ចង់ដឹង", "នាងចង់ដឹង",
    #           "អាចប្រាប់មិត្តភក្តិខ្ញំុថា", "ប្រាប់Rathanaតិចមើល ", "ប្រាប់រតនាតិចមើល ", "ប្រាប់Panhaតិចមើល",
    #           "ប្រាប់បញ្ញាតិចមើល", "Panhaដែលជាមិត្តខ្ញំុនេះ", "Rathanaដែលជាមិត្តខ្ញំុនេះ", "រតនាដែលជាមិត្តខ្ញំុនេះ"]
    # words11 = ["ក្នុងប្រទេសកម្ពុជានេះ", "ក្នុងប្រទេសCambodia", "ក្នុងប្រទេសFrance", "ក្នុងប្រទេសបារាំង",
    #           "ក្នុងប្រទេសអាឡីម៉ង់", "ក្នុងប្រទេសGermany"]

    # words2 = ["នាទី", "ម៉ោង", "នៅ", "ឥឡូវ", "ក្នុងពិភពលោក", ]
    # # words3 = ["នេះ","ក្នុងប្រទេសនេះ", "ក្នុងសាលារៀននេះ", "ក្នុងវិទ្យាល័យនេះ", "ក្រោមមេឃលើដីនេះ"]
    # # words3 = ["ក្នុងវិទ្យាល័យCADTនេះ", "ក្នុងវិទ្យាល័យសុីអេដីឌីនេះ", "ក្នុងសាលារៀនសុីអេដីឌីនេះ"]
    # words3 = ["នេះ"]
    # words31 = ["នេះ"]
    # words4 = ["ម៉ោងប៉ុន្មាន", "ពេលវេលាដើរដល់ណា", "ត្រនិចនាឡិការវិលដល់ណា"]
    # words5 = ["ហើយ?"]

    words1 = ["ម៉ោងដើរដល់ណាហើយ"]
    words2 = ["នាទី", "ម៉ោង", "នៅ", "ឥឡូវ", "ក្នុងពិភពលោក", ]
    words3 = ["នេះ"]
    words4 = ["ម៉ោងប៉ុន្មាន", "ពេលវេលាដើរដល់ណា", "ត្រនិចនាឡិការវិលដល់ណា"]
    words5 = ["ហើយ?"]

    intentMap = {
        Intent.Person: ["Rathana", "រតនា", "Panha", "បញ្ញា"],
        Intent.Organization: ["សាលាCADT", "សាលារៀនសុីអេដីឌី", "វិទ្យាល័យសុីអេដីឌី", "CADT", "វិទ្យាល័យCADT"],
        # Intent.Building: ["នៅអាគារinnovation center", "នៅអាគារអុីនូវេសិនសែនធឺរ"],
        Intent.CountryCity: ["ប្រទេសFrance", "ប្រទេសបារាំង", "ប្រទេសCambodia", "ប្រទេសកម្ពុជា", "ប្រទេសអាឡីម៉ង់",
                             "ប្រទេសGermany"]
    }

    sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5,
              initialWord=False)
    # segment(fileName=fileName)
    entity(fileName=fileName, intentMap=intentMap)
    # pos(fileName=fileName)


# def AskAboutCurrentProject():
#     fileName = "AskCurrentProject"
#
#     words1 = ['Team Research', 'បងៗ', 'គ្រូៗនៅResearch', 'លោកគ្រូ', 'គេនៅTeam-Research',
#               'គាត់ក្នុង Team-Research', 'ពួកគាត់ក្នុងក្រុមស្រាវជ្រាវ', 'Teacher', 'Researcher']
#     words2 = ['នៅក្រុមជាមួយលោកគ្រូ']
#     words3 = ['លីហៀង', 'Lyheang', 'ចាន់ទោ', 'Chanto',
#               'វឌ្ឍនា', 'Vathna', 'ថៃហេង', 'Thayheng']
#     words4 = ['សិក្សាស្រាវជ្រាវលើគំរោង', 'កំពុងធ្វើការលើគំរោង',
#               'សិក្សាគំរោង', 'កំពុងresearch លើគំរោង', 'ធ្ចើការរៀនលើប្រធានបទ']
#     words5 = ['អីដែរ?', 'អីដែរនឹង?', 'អ្វីដែរ?', 'អីគេទៅ?',
#               'អីគេ?', 'អ្វីនឹង?', 'មួយណាដែរ?', 'អីគេដែរ?']
#
#     intentMap = {
#         Intent.Person: ['លីហៀង', 'Lyheang', 'ចាន់ទោ', 'Chanto',
#               'វឌ្ឍនា', 'Vathna', 'ថៃហេង', 'Thayheng', ]
#     }
#     sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5)
#     segment(fileName=fileName)
#     entity(fileName=fileName, intentMap=intentMap)
#     pos(fileName)


def AskAboutCurrentProject():
    fileName = "AskCurrentProject"

    words1 = ['Team Research', 'បងៗ', 'គ្រូៗនៅResearch', 'លោកគ្រូ', 'គេនៅTeam-Research',
              'គាត់ក្នុង Team-Research', 'ពួកគាត់ក្នុងក្រុមស្រាវជ្រាវ', 'Teacher', 'Researcher']
    words2 = ['នៅក្រុមជាមួយលោកគ្រូ']
    words3 = ['លីហៀង', 'Lyheang', 'ចាន់ទោ', 'Chanto',
              'វឌ្ឍនា', 'Vathna', 'ថៃហេង', 'Thayheng']
    words4 = ['សិក្សាស្រាវជ្រាវលើគំរោង', 'កំពុងធ្វើការលើគំរោង',
              'សិក្សាគំរោង', 'កំពុងresearch លើគំរោង', 'ធ្ចើការរៀនលើប្រធានបទ']
    words5 = ['អីដែរ?', 'អីដែរនឹង?', 'អ្វីដែរ?', 'អីគេទៅ?',
              'អីគេ?', 'អ្វីនឹង?', 'មួយណាដែរ?', 'អីគេដែរ?']

    intentMap = {
        Intent.Person: ["លោកគ្រូលីហៀង", 'លោកគ្រូ Lyheang', 'លោកគ្រូវឌ្ឍនា', 'លោកគ្រូ Chanto', 'លោកគ្រូច ាន់ ទោ',
                        'លោកគ្រូ Vathna', "លោកគ្រូ Thayheng", 'លោកគ្រូ ថៃហេង'],
    }
    entity(fileName=fileName, intentMap=intentMap)


def AskaboutCarParkingFee():
    fileName = "AskAboutCarParkingFee"

    words1 = ['សួរមួយមើល', 'មានដឹងអត់ថា', 'ដឹងថា', 'តើ', 'អត់ទោស']
    words2 = ['នៅសាលានេះ', 'នៅសាលាស៊ីអេឌីធី', 'នៅសាលាCADTនឹង', 'នៅអាគារអាយឌីធី', 'នៅអាគារអុីនូវេសិនសែនធឺរ',
              'នៅអាគារអាយឌីអរអាយ', 'នៅអាគារIDRI', 'នៅអាគារInnovation Center']
    words3 = ['គេ', 'ពួកយើងត្រូវ', 'គ្រូៗ', 'បុគ្គលិក', 'ភ្ញៀវ']
    words4 = ['បង់ប្រាប់ចំនួនប៉ុន្មាន', 'ផាក១ដងប៉ុន្មាន', 'ទុក១ដងប៉ុន្មានទៅ', 'បង់ប៉ុន្មានរយ', 'ផ្ញើអស់ម៉ានរយ',
              'អោយប៉ុន្មាន', 'ចំណាយអស់ប៉ុន្មាន']
    words5 = ['សំរាប់ការផ្ញើឡាន']
    words6 = ['?']
    intentMap = {
        Intent.Organization: ["សាលាCADT", "សាលាស៊ីអេឌីធី"],
        Intent.Building: ["អាគារ innovation center", "អាគារ អុីនូវេសិនសែនធឺរ", 'អាគារ អាយឌីអរអាយ', 'អាគារ IDT',
                          'អាគារ អាយឌីធី', 'អាគារ IDRI']
    }
    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5, word6=words6, initialWord=False)
    # segment(fileName=fileName)
    # entity(fileName=fileName, intentMap=intentMap)
    # pos(fileName=fileName)\
    convertToCSV(fileName=fileName)


def FindEnrollmentLocation():
    fileName = "FindEnrollmentLocation"

    words1 = ['ឯណាទៅ', 'នៅទីណា', 'នៅទីណាទៅ', 'នៅទីតាំងមួយណាទៅ', 'នៅម្ដំណាទៅ',
              'នៅណា', 'នៅបន្ទប់ណាទៅ', 'អាចប្រាប់តិចមើលណានៅ', 'សួរមួយមើល!តើទីណា', 'នៅណាហូវ']
    words2 = ["កន្លែង"]
    words3 = ['ដាក់ពាក្យចូលរៀន', 'ទិញពាក្យចូលរៀន',
              'ចុះឈ្មោះចូលរៀន', 'ដាក់ដឺម៉ង់']
    words4 = ['នៅ']
    words5 = ["សាលានេះ", "សាលាCADT", "សាលាសុីអេឌីធី"]
    words6 = ["?"]

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា សុីអេឌីធី"],
        Intent.Building: ["អាគារ innovation center", "អាគារ អុីនូវេសិនសែនធឺរ"],
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def AskaboutRegisterDate():
    fileName = "AskAboutRegisterDate"

    words1 = ['នៅពេលណា', 'ថ្ងៃណា', 'ពេលណាបាន', 'ស្មាណា']
    words2 = ['គេ']
    words3 = ['ដាក់ពាក្យចូលរៀន', 'ទិញពាក្យចូលរៀន',
              'ចុះឈ្មោះចូលរៀន', 'ដាក់ដឺម៉ង់', 'ចាប់បើកទទួលពាក្យចុះឈ្មោះ']
    words4 = ['នៅ']
    words5 = ['សាលានេះ', "សាលាស៊ីអេឌីធី", "សាលាCADTនឹង"]
    words6 = ["?"]

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា ស៊ីអេឌីធី"],
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def AskaboutMotocycleParkingFee():
    fileName = "AskAboutMotocycleParkingFee"

    words1 = ['សួរមួយមើល', 'មានដឹងអត់ថា', 'ដឹងថា', 'តើ', 'អត់ទោស']
    words2 = ['នៅសាលានេះ', 'នៅសាលាស៊ីអេឌីធី', 'នៅសាលាCADTនឹង', 'នៅអាគារអាយឌីធី', 'នៅអាគារអុីនូវេសិនសែនធឺរ',
              'នៅអាគារអាយឌីអរអាយ', 'នៅអាគារIDT', 'នៅអាគារIDRI', 'នៅអាគារInnovation Center']
    words3 = ['គេ', 'ពួកយើងត្រូវ', 'គ្រូៗ', 'បុគ្គលិក', 'ភ្ញៀវ']
    words4 = ['បង់ប្រាប់ចំនួនប៉ុន្មាន', 'ផាក១ដងប៉ុន្មាន', 'ទុក១ដងប៉ុន្មានទៅ',
              'បង់ប៉ុន្មានរយ', 'ផ្ញើអស់ម៉ានរយ', 'អោយប៉ុន្មាន', 'ចំណាយអស់ប៉ុន្មាន']
    words5 = ['សំរាប់ការផ្ញើម៉ូតូ']
    words6 = ['?']

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា ស៊ីអេឌីធី"],
        Intent.Building: ["អាគារ Innovation Center", "អាគារ អុីនូវេសិនសែនធឺរ",
                          'អាគារ អាយឌីអរអាយ', 'អាគារ IDT', 'អាគារ អាយឌីធី', 'អាគារ IDRI']
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def AskaboutFemaleDressCode():
    fileName = "AskaboutFemaleDressCode"

    words1 = ['សួរមួយមើល', 'មានដឹងអត់ថា', 'ដឹងថា', 'តើ', 'អត់ទោស']
    words2 = ['នៅសាលានេះ', 'នៅសាលាស៊ីអេឌីធី', 'នៅសាលាCADTនឹង']
    words3 = ['និស្សិតស្រី', 'សិស្សស្រី', 'ក្មេងស្រី']
    words4 = ['គួរស្លៀកពាក់', 'ត្រូវពាក់ខោអាវ', 'រៀបចំសំលៀកបំពាក់',
              'រៀបចំតុមតែងខ្លួន', 'ផ្ញើអស់ម៉ានរយ', 'អោយប៉ុន្មាន', 'ចំណាយអស់ប៉ុន្មាន']
    words5 = ['បែបណាដែរទើបសមរម្យ''យ៉ាងណាបានល្អទៅ']
    words6 = ['?']

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា ស៊ីអេឌីធី"]
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def AskaboutMaleDressCode():
    fileName = "AskaboutMaleDressCode"

    words1 = ['សួរមួយមើល', 'មានដឹងអត់ថា', 'ដឹងថា', 'តើ', 'អត់ទោស']
    words2 = ['នៅសាលានេះ', 'នៅសាលាស៊ីអេឌីធី', 'នៅសាលាCADTនឹង']
    words3 = ['និស្សិតប្រុស', 'សិស្សប្រុស', 'ក្មេងប្រុស']
    words4 = ['គួរស្លៀកពាក់', 'ត្រូវពាក់ខោអាវ', 'រៀបចំសំលៀកបំពាក់',
              'រៀបចំតុមតែងខ្លួន', 'ផ្ញើអស់ម៉ានរយ', 'អោយប៉ុន្មាន', 'ចំណាយអស់ប៉ុន្មាន']
    words5 = ['បែបណាដែរទើបសមរម្យ''យ៉ាងណាបានល្អទៅ']
    words6 = ['?']

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា សុីអេឌីធី"],
        Intent.Building: ["អាគារ innovation center", "អាគារ អុីនូវេសិនសែនធឺរ"],
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def IsExistDoorExit():
    fileName = "IsExistDoorExit"

    words1 = ['សួរមួយមើល', 'មានដឹងអត់ថា', 'ដឹងថា', 'តើ', 'អត់ទោស']
    words2 = ['នៅសាលានេះ', 'នៅសាលាស៊ីអេឌីធី', 'នៅសាលាCADTនឹង', 'នៅអាគារអាយឌីធី', 'នៅអាគារអុីនូវេសិនសែនធឺរ',
              'នៅអាគារអាយឌីអរអាយ', 'នៅអាគារIDT', 'នៅអាគារIDRI', 'នៅអាគារinnovation center']
    words3 = ['ជាន់ទី១', 'ជាន់ទី២', 'ជាន់ទី៣', 'ជាន់លើគេបង្អស់',
              'ជាន់ធ្វើការរបស់បុគ្គលិក', 'ជាន់ផ្ទាល់ដី', 'ជាន់ក្រោម', 'ជាន់ក្រោមគេបង្អស់']
    words4 = ['មាន']
    words5 = ['ជណ្ដើរអាសន្ន''ជណ្ដើរគេចគ្រោះថ្នាក់',
              'ជណ្ដើរពេលមានអគ្គិភ័យ', 'ជណ្ដើរអ៊ិចស៊ីស', 'ជណ្ដើរexist']
    words6 = ['ដែរឬទេ?']

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា ស៊ីអេឌីធី"],
        Intent.Building: ['អាគារ អាយឌីធី', 'អាគារ អុីនូវេសិនសែនធឺរ',
                          'អាគារ អាយឌីអរអាយ', 'អាគារ IDT', 'អាគារ IDRI', 'អាគារ Innovation Center'],
        Intent.Floor: ['ជាន់ទី១', 'ជាន់ទី២', 'ជាន់ទី៣']
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def WhyshouldchooseCADT():
    fileName = "WhyShouldChooseCADT"

    words1 = ['ហេតុអ្វី''ហេតុផលអ្វីខ្លះដែល', 'ចំណុចល្អអ្វីខ្លះ', 'មានលក្ខណៈពិសេសអ្វីខ្លះ']
    words2 = ['ដែល']
    words3 = ['យើងគូរតែ', 'សិស្សជនិស្សិតជ្រើសរើសយក', ]
    words4 = ['ជ្រើសយក', 'មករៀននៅ', 'ឆាប់ជំនាញនៅ']
    words5 = ['សាលានេះ', 'សាលាស៊ីអេឌីធី', 'សាលាCADTនឹង']
    words6 = ['សំរាប់បន្ដការសិក្សាថ្នាក់បរិញ្ញាប័ត្រ?']

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា ស៊ីអេឌីធី"],
        Intent.Building: ['អាគារ អាយឌីធី', 'អាគារ អុីនូវេសិនសែនធឺរ',
                          'អាគារ អាយឌីអរអាយ', 'អាគារ IDT', 'អាគារ IDRI', 'អាគារ Innovation Center'],
        Intent.Floor: ['ជាន់ទី១', 'ជាន់ទី២', 'ជាន់ទី៣']
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def WhenLaunchIDRI():
    fileName = "WhenLaunchIDRI"

    words1 = ['នៅពេលណា', 'ពេលណាបាន', 'ស្មាណា']
    words2 = ['គេ']
    words3 = ['ដាក់សម្ភោធអោយប្រើប្រាស់', 'បើកអោយប្រើប្រាស់']
    words4 = ['នៅអាគារអាយឌីអរអាយ', 'នៅអាគារIDT', 'នៅអាគារIDRI', ]
    words5 = ['ដែរទៅ']
    words6 = ['?']

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា ស៊ីអេឌីធី"],
        Intent.Building: ['អាគារ អាយឌីធី', 'អាគារ អុីនូវេសិនសែនធឺរ',
                          'អាគារ អាយឌីអរអាយ', 'អាគារ IDT', 'អាគារ IDRI', 'អាគារ Innovation Center'],
    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def SchoolMission():
    fileName = "SchoolMission"

    words1 = ['ម៉ីសសិន', 'បេសកម្ម', 'mission']
    words2 = ['របស់', 'នៅ']
    words3 = ['សាលានេះ', 'សាលាស៊ីអេឌីធី', 'សាលាCADTនឹង', 'អាគារអាយឌីធី', 'អាគារអុីនូវេសិនសែនធឺរ',
              'អាគារអាយឌីអរអាយ', 'អាគារIDT', 'អាគារIDRI', 'អាគារinnovation center']
    words4 = ['មាន']
    words5 = ['អ្វីខ្លះ']
    words6 = ['?']

    intentMap = {
        Intent.Organization: ["សាលា CADT", "សាលា ស៊ីអេឌីធី"],
        Intent.Building: ['អាគារ អាយឌីធី', 'អាគារ អុីនូវេសិនសែនធឺរ',
                          'អាគារ អាយឌីអរអាយ', 'អាគារ IDT', 'អាគារ IDRI', 'អាគារ Innovation Center'],

    }
    return fileName, words1, words2, words3, words4, words5, words6, intentMap


def askWhereHRRoomIs():
    fileName = "AskWhereHRRoomIs"
    words1 = ["អ្នកអាចប្រាប់", "លោកអាចប្រាប់", "បងអាចប្រាប់", "លោកអ៊ំុអាចប្រាប់", "អ្នកមឹងអាចប្រាប់"]

    # words2 = ["សាលាCADT", "សាលាស៊ីអេឌីធី", "បណ្ឌិតសភាបច្ចេកវិទ្យាឌីជីថល", "CADT"]

    words2 = ["បងChanto", "បងចាន់តូ", "បងរិទ្ធ", "bongrith", "ដារា", "Dara"]
    # words2 = ["ខ្ញំុ", "ញំុ", "me"]
    words3 = ["ថាកន្លែងណាជា", "ថាទៅផ្លូវណាបានទៅដល់", "ថាទៅជាន់ណាបានដល់", "ថាទៅអាគារណាបានដល់"]
    words4 = ["បន្ទប់HR", "បន្ទប់បុក្គលិក", "បន្ទប់ធនធានមនុស្ស", "Department HR", "នាយកដ្ឋានធនធានមនុស្ស",
              "ដេប៉ាទីម៉ង់HR", "ដេប៉ាទីម៉ង់ធនធានមនុស្ស"]
    words5 = ["ទៅ", "ដែរ"]
    words6 = ["?"]

    intentMap = {
        Intent.Room: ["ដេប៉ាទីម៉ង់ HR", "បន្ទប់ HR", "បន្ទប់បុក្គលិក", "បន្ទប់ធនធានមនុស្ស", "Department HR",
                      "នាយកដ្ឋានធនធានមនុស្ស"],
        Intent.Person: ["បង Chanto", "បង ចាន់តូ", "បង រិទ្ធ", "bong rith", "ដារា", "Dara"],
        Intent.Organization: ["សាលាCADT", "សាលាស៊ីអេឌីធី", "បណ្ឌិតសភាបច្ចេកវិទ្យាឌីជីថល", "CADT"]
    }

    return fileName, words1, words2, words3, words4, words5, words6, intentMap
