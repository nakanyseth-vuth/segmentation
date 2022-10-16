from models import Intent
from stores.process import sentences, segment, entity, pos


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

    # words1 = ["ម៉ោងដើរដល់ណាហើយ"]
    # words2 = ["នាទី", "ម៉ោង", "នៅ", "ឥឡូវ", "ក្នុងពិភពលោក", ]
    # words3 = ["នេះ"]
    # words4 = ["ម៉ោងប៉ុន្មាន", "ពេលវេលាដើរដល់ណា", "ត្រនិចនាឡិការវិលដល់ណា"]
    # words5 = ["ហើយ?"]

    intentMap = {
        Intent.Person: ["Rathana", "រតនា", "Panha", "បញ្ញា"],
        Intent.Organization: ["សាលាCADT", "សាលារៀនសុីអេដីឌី", "វិទ្យាល័យសុីអេដីឌី", "CADT", "វិទ្យាល័យCADT"],
        # Intent.Building: ["នៅអាគារinnovation center", "នៅអាគារអុីនូវេសិនសែនធឺរ"],
        Intent.CountryCity: ["ប្រទេសFrance","ប្រទេសបារាំង", "ប្រទេសCambodia","ប្រទេសកម្ពុជា", "ប្រទេសអាឡីម៉ង់","ប្រទេសGermany"]
    }

    # sentences(fileName=fileName, word1=words1, word2=words2, word3=words3, word4=words4, word5=words5,
    #           initialWord=False)
    # segment(fileName=fileName)
    entity(fileName=fileName, intentMap=intentMap)
    # pos(fileName=fileName)


if __name__ == '__main__':
    # fileName = "Bus"
    findCurrentTime()
    # Pe edit ah nis edit ah ler pg and brab tv tha ah na intent ah na, kom oy error klang,
    # doch សុខលាភ -> សុខ លាភ since they are first name all, add space between them
    # " សុខលាភ "
    # And dont forget to mer error list pg and recheck everything
