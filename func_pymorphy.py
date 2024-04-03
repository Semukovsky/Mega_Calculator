import pymorphy2


def pymorphy2_311_hotfix():
    from inspect import getfullargspec
    from pymorphy2.units.base import BaseAnalyzerUnit

    def _get_param_names_311(klass):
        if klass.__init__ is object.__init__:
            return []
        args = getfullargspec(klass.__init__).args
        return sorted(args[1:])

    setattr(BaseAnalyzerUnit, '_get_param_names', _get_param_names_311)


def get_normal_form(word):
    pymorphy2_311_hotfix()
    morph = pymorphy2.MorphAnalyzer()
    parse_result = morph.parse(word)
    return parse_result[0].normal_form


def get_accs(word):
    pymorphy2_311_hotfix()
    morph = pymorphy2.MorphAnalyzer()
    parse_result = morph.parse(word)[0]
    parse_result = parse_result.inflect({"nomn"})
    return parse_result.word
