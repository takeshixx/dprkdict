import re
import urllib.parse

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Definition

RE_HANGUL = re.compile(r'[(]*[\uAC00-\uD7AF]+[\uAC00-\uD7AF (),;]*', re.IGNORECASE)


def index(request):
    definitions = Definition.objects.all()
    limit = request.GET.get('limit')
    try:
        limit = int(limit)
    except (ValueError, TypeError):
        limit = 15
    paginator = Paginator(definitions, limit)
    page = request.GET.get('page')
    try:
        show_lines = paginator.page(page)
    except PageNotAnInteger:
        show_lines = paginator.page(1)
    except EmptyPage:
        show_lines = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'definitions': definitions,
                                          'lines': show_lines})


def fix_definition_format(definition):
    definition = definition.replace('{I}', '<i>') \
                           .replace('{/I}', '</i>') \
                        .replace('{B}', '<b>') \
                        .replace('{/B}', '</b>') \
                        .replace('{Pr}', '[') \
                        .replace('{/Pr}', ']') \
                        .replace('{H}', '') \
                        .replace('{/H}', '') \
                        .replace('{E}', '') \
                        .replace('{/E}', '') \
                        .replace('{J}', '') \
                        .replace('{/J}', '') \
                        .replace('{S}', '') \
                        .replace('{/S}', '') \
                        .replace('{U}', '') \
                        .replace('{-}', '- ')
    if definition.startswith('&'):
        definition = definition[1:]
    word, _definition = definition.split('\n', 1)
    definition = '<h4>' + word + '</h4>\n'
    definition += _definition
    return definition


def generate_translate_tag(word):
    out = '<a href="https://translate.google.de/#ko/en/{word_url}" '
    out += 'title="Translate with Google Translate" target="'
    out += '_blank">{word}</a>'
    out = out.format(word_url=urllib.parse.quote_plus(word.group(0)),
                    word=word.group(0))
    return out


def get_definitions(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        definitions = Definition.objects.filter(word__icontains=q) \
                                        .values_list('word', flat=True)[:25]
        data = list(definitions)
    else:
        data = []
    return JsonResponse(data, safe=False)


def get_definition(request, id):
    definition = get_object_or_404(Definition, id=id)
    data = fix_definition_format(definition.definition)
    data = RE_HANGUL.sub(generate_translate_tag, data)
    return HttpResponse(data)


def get_definition_word(request, word):
    definition = get_object_or_404(Definition, word=word)
    data = fix_definition_format(definition.definition)
    data = RE_HANGUL.sub(generate_translate_tag, data)
    return HttpResponse(data)