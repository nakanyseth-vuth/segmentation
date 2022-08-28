from bilstm_tokenizer import tokenize_sentences_bilstm

sents=["គាត់កំពុងឆ្លើយតបទៅនឹងការអត្ថាធិប្បាយរបស់វាគ្មិន", "ញញ្ញត្តិរបស់ក្រុមបុគ្គលិកត្រូវបានតំណាងក្រសួងការងារទទួលយកប៉ុន្តែនៅមិនទាន់សម្រេចបែបណានៅឡើយទេ"]
res = tokenize_sentences_bilstm(sents)

print(res)