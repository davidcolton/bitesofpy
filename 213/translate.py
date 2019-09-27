import re
from bs4 import BeautifulSoup


def _replace_tag_contents(tag, soup_en, soup_2nd, trans_text):

    # Extract the english tags first
    code_en_dict = dict()
    code_en = soup_en.find_all(tag)
    for idx_en, code_en_str in enumerate(code_en):
        code_en_dict[idx_en] = code_en_str

    # Now get the 2nd language <code> and replace with english
    code_2nd = soup_2nd.find_all(tag)
    for idx, code in enumerate(code_2nd):
        trans_text = trans_text.replace(str(code), str(code_en_dict[idx]))

    return trans_text


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    soup_en = BeautifulSoup(org_text, "html.parser")
    soup_2nd = BeautifulSoup(trans_text, "html.parser")

    trans_text = _replace_tag_contents("pre", soup_en, soup_2nd, trans_text)
    trans_text = _replace_tag_contents("code", soup_en, soup_2nd, trans_text)

    return trans_text
