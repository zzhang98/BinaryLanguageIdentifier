import codecs

from numpy.core import unicode

'''
Block                                   Range       Comment
CJK Unified Ideographs                  4E00-9FFF   Common
CJK Unified Ideographs Extension A      3400-4DBF   Rare
CJK Unified Ideographs Extension B      20000-2A6DF Rare, historic
CJK Unified Ideographs Extension C      2A700–2B73F Rare, historic
CJK Unified Ideographs Extension D      2B740–2B81F Uncommon, some in current use
CJK Unified Ideographs Extension E      2B820–2CEAF Rare, historic
CJK Compatibility Ideographs            F900-FAFF   Duplicates, unifiable variants, corporate characters
CJK Compatibility Ideographs Supplement 2F800-2FA1F Unifiable variants
Ref:stackoverflow
'''
def checkchinese(val):
    if val > 0x4E00 and val < 0x9FFF:
        return True
    elif val > 0x3400 and val < 0x4DBF:
        return True
    elif val > 0x20000 and val < 0x2A6DF:
        return True
    elif val > 0x2A700 and val < 0x2B73F:
        return True
    elif val > 0x2B740 and val < 0x2B81F:
        return True
    elif val > 0x2B820 and val < 0x2CEAF:
        return True
    elif val > 0xF900 and val < 0xFAFF:
        return True
    elif val > 0x2F800 and val < 0x2FA1F:
        return True
    return False

'''
Hiragana
Unicode code points regex: [\x3041-\x3096]

Katakana (Full Width)
Unicode code points regex: [\x30A0-\x30FF]

Kanji Radicals
Unicode code points regex: [\x2E80-\x2FD5]     # same with Chinese

Katakana and Punctuation (Half Width)
Unicode code points regex: [\xFF5F-\xFF9F]

Japanese Symbols and Punctuation
Unicode code points regex: [\x3000-\x303F]

Miscellaneous Japanese Symbols and Characters
Unicode code points regex: [\x31F0-\x31FF\x3220-\x3243\x3280-\x337F]

Alphanumeric and Punctuation (Full Width)
Unicode code points regex: [\xFF01-\xFF5E]

Ref:http://www.localizingjapan.com/blog/2012/01/20/regular-expressions-for-japanese-text/
'''
def checkjapanese(val):
    lower = [0x3041, 0x30A0, 0x2E80, 0xFF5F, 0x3000, 0x31F0, 0x3220, 0x3280, 0xFF01]
    upper = [0x3096, 0x30FF, 0x2FD5, 0xFF9F, 0x303F, 0x31FF, 0x3243, 0x337F, 0xFF3E]
    for i in range(len(lower)):
        if val > lower[i] and val < upper[i]:
            return True
    return False

'''
This block ranges from U+0080 to U+00FF, contains 128 characters and includes the C1 controls, 
Latin-1 punctuation and symbols, 30 pairs of majuscule and minuscule accented Latin characters
and 2 mathematical operators.
Ref:Wikipedia>Latin-1 Supplement (Unicode block)
'''
def checkspanish(val):
    if val > 0x0080 and val < 0x00FF:
        return True

'''
Range: U+0900..U+097F (128 code points), including Devanagari (122 char.) Common (2 char.) Inherited (4 char.)
Ref:Wikipedia>Devanagari (Unicode block)
'''
def checkhindi(val):
    if val > 0x0900 and val < 0x097F:
        return True

'''
Cyrillic: U+0400–U+04FF, 256 characters
Cyrillic Supplement: U+0500–U+052F, 48 characters
Cyrillic Extended-A: U+2DE0–U+2DFF, 32 characters
Cyrillic Extended-B: U+A640–U+A69F, 96 characters
Cyrillic Extended-C: U+1C80–U+1C8F, 9 characters
Phonetic Extensions: U+1D2B, U+1D78, 2 Cyrillic characters
Combining Half Marks: U+FE2E–U+FE2F, 2 Cyrillic characters
Ref:Wikipedia>Cyrillic script in Unicode
'''
def checkrussian(val):
    lower = [0x0400, 0x0500, 0x2DE0, 0xA640, 0x1C80, 0x1D2B, 0xFE2E]
    upper = [0x04FF, 0x052F, 0x2DFF, 0xA69F, 0x1C8F, 0x1D78, 0xFE2F]
    for i in range(len(lower)):
        if val > lower[i] and val < upper[i]:
            return True
    return False

'''
U+1100..U+11FF
Ref:Wikipedia>Hangul Jamo (Unicode block)
'''
def checkkorean(val):
    if val > 0x1100 and val < 0x11FF:
        return True

'''
U+0600..U+06FF (256 code points)
Ref:Wikipedia>Arabic (Unicode block)
'''
def checkarabic(val):
    if val > 0x0600 and val < 0x06FF:
        return True

def getlanguagefile(filename):
    f = codecs.open(filename, "r", encoding='utf-8')
    for line in f:
        for b in line:
            # print(ord(b))    # integer representation of unicode
            val = ord(b)

            # Chinese
            if (checkchinese(val)):
                return 'Chinese'

            # Spanish
            if (checkspanish(val)):
                return 'Spanish'

            # Hindi
            if (checkhindi(val)):
                return 'Hindi'

            # Japanese
            if (checkjapanese(val)):
                return 'Japanese'

            # Russian
            if (checkrussian(val)):
                return 'Russian'

            # Korean
            if (checkkorean(val)):
                return 'Korean'

            # Arabic
            if (checkarabic(val)):
                return 'Arabic'

            # todo: 1.french 2.cantoese 3.hanji in japanese


    f.close()

def getlanguageline(b):
    unicode_str = unicode(b, encoding='utf-8')    # decoding bytes to numpy_str
    for b in unicode_str:
        print(b)

#getlanguageline(b'helloo')
print(getlanguagefile('test1 - Copy'))
