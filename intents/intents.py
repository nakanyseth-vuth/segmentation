from models import Intent
from stores.process import pos
from test import sentences, segment, entity


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

def askWhereHRRoom():
    # ka ri ya lie HR
    # ka ri ya lie បុក្គលិក
    # room hr
    # បណ្តោះបណ្តាល
    # kang បុក្គលិក nv na del?
    #

    fileName = "AskWhereHRRoom"
    words1 = ["អ្នកអាចប្រាប់", "លោកអាចប្រាប់", "បងអាចប្រាប់", "លោកអ៊ំុអាចប្រាប់", "អ្នកមឹងអាចប្រាប់"]

    # words2 = ["សាលាCADT", "សាលាស៊ីអេឌីធី", "បណ្ឌិតសភាបច្ចេកវិទ្យាឌីជីថល", "CADT"]

    # words2 = ["បងChanto", "បងចាន់តូ", "បងរិទ្ធ", "bongrith", "ដារា", "Dara"]
    words2 = ["ខ្ញំុ", "ញំុ", "me"]
    words3 = ["ថាកន្លែងណាជា", "ថាទៅផ្លូវណាបានទៅដល់", "ថាទៅជាន់ណាបានដល់", "ថាទៅអាគារណាបានដល់"]
    words4 = ["បន្ទប់HR", "បន្ទប់បុក្គលិក", "បន្ទប់ធនធានមនុស្", "Department HR", "នាយកដ្ឋានធនធានមនុស្ស", "ដេប៉ាទីម៉ង់HR", "ដេប៉ាទីម៉ង់ធនធានមនុស្ស"]
    words5 = ["ទៅ?", "ដែរ?"]

    intentMap = {
        Intent.Room: words4,
        Intent.Person: ["បងChanto", "បងចាន់តូ", "បងរិទ្ធ", "bongrith", "ដារា", "Dara"],

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
        Intent.CountryCity: ["ប្រទេសFrance","ប្រទេសបារាំង", "ប្រទេសCambodia","ប្រទេសកម្ពុជា", "ប្រទេសអាឡីម៉ង់","ប្រទេសGermany"]
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