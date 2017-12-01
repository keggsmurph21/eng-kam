#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, codecs, copy
import xml.etree.ElementTree as ET

def main():
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    src = { 'name':'Kikamba', 'iso':'kam' }
    tar = { 'name':'English', 'iso':'eng' }

    src_xml = ET.parse( src['iso'] + '.dix' ).getroot()
    tar_xml = ET.parse( tar['iso'] + '.dix' ).getroot()
    bil_xml = ET.parse( src['iso'] + '-' + tar['iso'] + '.dix' ).getroot()

    src_sdefs = [ sdef.attrib['n'] for sdef in list(src_xml.find('sdefs')) ]
    src_pardefs = [ pardef.attrib['n'] for pardef in list(src_xml.find('pardefs')) ]
    src_lemmas = [ e.attrib['lm'] for e in list(src_xml.find('section')) ]

    tar_sdefs = [ sdef.attrib['n'] for sdef in list(tar_xml.find('sdefs')) ]
    tar_pardefs = [ pardef.attrib['n'] for pardef in list(tar_xml.find('pardefs')) ]
    tar_lemmas = [ e.attrib['lm'] for e in list(tar_xml.find('section')) ]

    bil_sdefs = src_sdefs + tar_sdefs

if __name__ == '__main__':
    main()
