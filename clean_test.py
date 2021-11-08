import re
import unittest
import clean

class TestCase(unittest.TestCase):

    def test_clean_hashtags(self):
        result = clean.text_delete_hashtags("#12CovidBitsin istiyoruz #covid")
        self.assertNotRegex("(#\S+)", result)

    def test_clean_numbers(self):
        result = clean.text_delete_words_that_contain_numbers("Bu 12ii buradan gidecek")
        self.assertNotRegex("\w*\d\w*", result)


    def test_delete_punctuation(self):
        result = clean.text_delete_punctuation("Oku, baban gibi esek olma")
        self.assertNotRegex("[%s]", result)
    
    def test_delete_quotation_marks(self):
        result = clean.text_delete_quotation_marks('"Cevaplari olan degil sorulari olan insanlari dinleyin." - Albert Einstein')
        self.assertNotRegex("[?????]", result)

    def test_delete_enter_character(self):
        result = clean.text_delete_enter_character('Bir \n iki \n uc \n')
        self.assertNotRegex("\n", result)

    def test_clean_at_characters(self):
        result = clean.text_delete_at_character("Sayin @drfahrettinkoca")
        self.assertNotRegex("(@\S+)", result)

    def test_delete_rt_word(self):
        result = clean.text_delete_rt_word("rt aacanli livehalt kart rte rte")
        self.assertNotRegex("(\s+rt\s+)|(^rt\s+)", result)

    def test_delete_double_or_more_spaces(self):
        result = clean.text_delete_double_or_more_spaces("Merhaba     birden   cok bosluklu bir   string  bunu duzeltmesi gerekiyor")
        self.assertNotRegex('\s\s+', result)

    def test_clean_text(self):
        result = clean.text_clean("rt #aacanli @aacanli @anadoluajansi 21/12/2022 \" boyle dedim \" - @drfahrettinkoca drfahrettinkoca. okuyum, olmasin \n alt satira gecilsin")
        self.assertEqual(result, "boyle dedim drfahrettinkoca okuyum olmasin alt satira gecilsin")

    if __name__ == '__main__':
        unittest.main()
