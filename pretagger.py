#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, codecs, copy
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

form = ''
tag = ''
tags = []
lemma = ''
reading = ''

def pop_tags(tags, out):
    if len(tags) < 1:
        return out
    out = tags.pop() + out
    return pop_tags(tags, out)

def pull_tags(tags, out):
    for tag in tags:
        out = out + tag
    return out

for char in sys.stdin.read().decode('utf-8'):
    if char == '^':
        sys.stdout.write(char)
        reading = 'form'
        continue

    if char == '/':
        reading = 'lemma'

        if len(form) < 1 and len(lemma) > 1:
            sys.stdout.write(lemma + pop_tags(tags, ''))
            lemma = ''
            tags = []

        sys.stdout.write(form)
        sys.stdout.write(char)
        form = ''
        continue

    if char == '#':
        reading = 'pass'

        if len(form) < 1 and len(lemma) > 1:
            sys.stdout.write(lemma + pop_tags(tags, ''))
            form = ''
            lemma = ''
            tags = []

        sys.stdout.write(char)
        continue

    if char == "+":
        reading = 'pass'

        if len(form) < 1 and len(lemma) > 1:
            sys.stdout.write(lemma + pull_tags(tags, ''))
            form = ''
            lemma = ''
            tags = []

        sys.stdout.write(char)
        continue

    if char == '<' and reading is not 'pass':
        tag = ''
        reading = 'tag'

    if char == '>' and reading is not 'pass':
        tag = tag + char
        tags.append(tag)
        reading = 'lemma'
        continue

    if char == '$':
        if len(form) < 1 and len(lemma) > 1:
            sys.stdout.write(lemma + pop_tags(tags, ''))
            reading = 'lemma'

        tags = []
        form = ''
        lemma = ''
        sys.stdout.write(char)
        reading = 'pass'
        continue

    if reading == 'form':
        form = form + char
        continue

    if reading == 'lemma':
        lemma = lemma + char
        continue

    if reading == 'tag':
        tag = tag + char
        continue

    if reading == 'pass':
        sys.stdout.write(char)
        continue
