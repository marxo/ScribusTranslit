# Version 0.1.0
import scribus

cyrillic_to_latin_map = {
    "Панјелиниз": "Panjeliniz", "Конјуг": "Konjug", "Конјук": "Konjuk", "Конјун": "Konjun", "Анјуг": "Anjug",
    "Поджил": "Podžil", "Поджет": "Podžet", "Поджањ": "Podžanj", "Поджњ": "Podžnj", "Преджет": "Predžet",
    "Преджив": "Predživ", "Подждр": "Podždr", "Подржар": "Podržar", "Поджуп": "Podžup", "Оджал": "Odžal",
    "Оджив": "Odživ", "Оджвал": "Odžval", "Оджељ": "Odželj", "Оджел": "Odžel", "Оджден": "Odžden",
    "Наджир": "Nadžir", "Наджуп": "Nadžup", "Надрждрел": "Nadrždrel", "Наджањ": "Nadžanj", "Наджњ": "Nadžnj",
    "Наджет": "Nadžet", "Наджив": "Nadživ", "Наджн": "Nadžn", "Инјункт": "Injunkt", "Инјек": "Injek",
    "панјелиниз": "panjeliniz", "конјуг": "konjug", "конјук": "konjuk", "конјун": "konjun", "анјуг": "anjug",
    "поджил": "podžil", "поджет": "podžet", "поджањ": "podžanj", "поджњ": "podžnj", "преджет": "predžet",
    "преджив": "predživ", "подждр": "podždr", "подржар": "podržar", "поджуп": "podžup", "оджал": "odžal",
    "оджив": "odživ", "оджвал": "odžval", "оджељ": "odželj", "оджел": "odžel", "оджден": "odžden",
    "наджир": "nadžir", "наджуп": "nadžup", "надрждрел": "nadrždrel", "наджањ": "nadžanj", "наджњ": "nadžnj",
    "наджет": "nadžet", "наджив": "nadživ", "наджн": "nadžn", "инјункт": "injunkt", "инјек": "injek",
    "Њ": "Nj", "Љ": "Lj", "њ": "nj", "љ": "lj", "а": "a", "б": "b", "в": "v", "г": "g", "џ": "dž", "д": "d",
    "ђ": "đ", "е": "e", "ж": "ž", "з": "z", "и": "i", "ј": "j", "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "ћ": "ć", "у": "u", "ф": "f", "х": "h", "ц": "c",
    "ч": "č", "ш": "š", "кс": "x", "иј": "y", "ку": "q", "А": "A", "Б": "B", "В": "V", "Г": "G", "Џ": "Dž",
    "Д": "D", "Ђ": "Đ", "Е": "E", "Ж": "Ž", "З": "Z", "И": "I", "Ј": "J", "К": "K", "Л": "L", "М": "M",
    "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "Ћ": "Ć", "У": "U", "Ф": "F", "Х": "H",
    "Ц": "C", "Ч": "Č", "Ш": "Š", "КС": "X", "ИЈ": "Y", "КУ": "Q"
}


def transliterate_text(text):
    return ''.join(cyrillic_to_latin_map.get(char, char) for char in text)

def transliterate_text_frame(frame_name):
    original_text = scribus.getAllText(frame_name)
    
    transliterated_text = transliterate_text(original_text)
    
    scribus.selectText(0, len(original_text), frame_name)
    scribus.deleteText(frame_name)
    scribus.insertText(transliterated_text, -1, frame_name)
    scribus.layoutTextChain(frame_name)

def main():
    if not scribus.haveDoc():
        scribus.messageBox("Error", "No document open", scribus.ICON_WARNING)
        return

    page_count = scribus.pageCount()
    for page in range(1, page_count + 1):
        scribus.gotoPage(page)  # Go to each page

        # Get all objects on the current page
        frames = scribus.getAllObjects()
        text_frames = [f for f in frames if scribus.getObjectType(f) == "TextFrame"]

        # Transliterate each text frame on the page
        for frame in text_frames:
            transliterate_text_frame(frame)
    
    scribus.messageBox("Info", "Transliteration completed!", scribus.ICON_INFORMATION)

if __name__ == "__main__":
    main()
