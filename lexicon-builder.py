#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, codecs, copy
import xml.etree.ElementTree as ET

def main():
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

    src = { 'name':'Kikamba', 'iso':'kam', 'prefix':True, 'chars':[ ('U','ũ'), ('I','ĩ')] }
    tar = { 'name':'English', 'iso':'eng', 'prefix':False,'chars':[] }

    src_xml = ET.parse( src['iso'] + '.dix' ).getroot()
    tar_xml = ET.parse( tar['iso'] + '.dix' ).getroot()
    bil_xml = ET.parse( src['iso'] + '-' + tar['iso'] + '.dix' ).getroot()

    src_sdefs = [ sdef.attrib['n'] for sdef in list(src_xml.find('sdefs')) ]
    src_pars = [ pardef.attrib['n'] for pardef in list(src_xml.find('pardefs')) ]
    src_entries = [ e.attrib['lm'] for e in list(src_xml.find('section')) ]

    tar_sdefs = [ sdef.attrib['n'] for sdef in list(tar_xml.find('sdefs')) ]
    tar_pars = [ pardef.attrib['n'] for pardef in list(tar_xml.find('pardefs')) ]
    tar_entries = [ e.attrib['lm'] for e in list(tar_xml.find('section')) ]

    bil_sdefs = src_sdefs + tar_sdefs

    new_src_sdefs = []
    new_src_pars = []
    new_src_es = []
    new_tar_sdefs = []
    new_tar_pars = []
    new_tar_es = []
    new_bil_sdefs = []
    new_bil_es = []

    # get the new lemma
    src_token = raw_input( '  Enter a word in ' + src['name'] + ': ' ).decode('utf-8')
    for char in src['chars']:
        src_token = src_token.replace(char[0].decode('utf-8'), char[1].decode('utf-8'))
    token_duplicate = ''
    while (src_token in src_entries and src_token != token_duplicate) or len(src_token) < 1:
        print "\n      Note: entry for <%s> already exists in <%s.dix>." % (src_token, src['iso'])
        print "        Type it again if you're sure.\n"
        token_duplicate = src_token
        src_token = raw_input( '  Enter a word in ' + src['name'] + ': ' ).decode('utf-8')
        for char in src['chars']:
            src_token = src_token.replace(char[0].decode('utf-8'), char[1].decode('utf-8'))
    src_token = src_token.lower()

    # get the lemma's root
    src_root = raw_input( '    <' + src_token + '> has root: ' )
    for char in src['chars']:
        src_root = src_root.replace(char[0].decode('utf-8'), char[1].decode('utf-8'))
    src_root = src_root.lower()

    # get the paradigm
    src_par = raw_input( '    <' + src_token + '> belongs to paradigm: ' )
    par_duplicate = ''
    while src_par not in src_pars and src_par != par_duplicate:
        print "\n      Note: there is no paradigm <%s> defined in <%s.dix>." % (src_par, src['iso'])
        print "        To define a new paradigm, type <%s> again.\n" % src_par
        par_duplicate = src_par
        src_par = raw_input( '    <' + src_token + '> belongs to paradigm: ' )
        if src_par == par_duplicate:

            # define new paradigm
            print '\n    >> Begin definition for paradigm: "%s" <<' % src_par

            par_entries = raw_input('         number of lines: ')
            while type(par_entries) == str:
                try:
                    par_entries = int(par_entries)
                    if par_entries < 1:
                        par_entries = raw_input('         number of lines: ')
                except:
                    par_entries = raw_input('         number of lines: ')

            for e in range(par_entries):
                left_root = raw_input('\n         LEFT root: ')
                right_root= raw_input('         RIGHT root: ')
                raw_tags = raw_input('         tags (comma sep.): ').split(',')

                tags = []
                for tag in raw_tags:
                    tag_duplicate = ''
                    while tag not in src_sdefs and tag not in new_src_sdefs and tag != tag_duplicate:
                        print "\n         Note: there is no <%s> tag defined in <%s.dix>." % (tag, src['iso'])
                        print "           To define a new tag, type <%s> again.\n" % tag
                        tag_duplicate = tag
                        tag = raw_input('         confirm tag: ')
                        if tag == tag_duplicate:
                            new_src_sdefs.append(tag)
                            if tag not in new_bil_sdefs:
                                new_bil_sdefs.append(tag)
                    tags.append(tag)

                if src['prefix']:
                    s = '<e><p> <l>' + left_root + '</l> <r>'
                    for tag in tags:
                        s = s + '<s n="' + tag + '">'
                    s = s + right_root + ' </r></p></e>'
                else:
                    s = '<e><p> <l>' + left_root + '</l> <r>'
                    s = s + right_root + '</r> </p></e>'
                    for tag in tags:
                        s = s + '<s n="' + tag + '">'

                print s

            print '\n    >> End definition for paradigm: "%s" <<' % src_par

    print new_src_sdefs, new_src_pars, new_src_es
    print new_tar_sdefs, new_tar_pars, new_tar_pars
    print new_bil_sdefs, new_bil_es

if __name__ == '__main__':
    main()
