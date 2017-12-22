eng-kam
===============================================================================

This is an Apertium bilingual language package for English-Kikamba. What
you can use this language package for:

* Morphological analysis of English/Kikamba
* Morphological generation of English/Kikamba
* Translation between English and Kikamba, currently supports translations of noun phrases the following form:
  - {DetPrN/PossPrN}{Adj}{Noun} <-> {Noun}{Adj}{DetPrN/PossPrN}


Requirements
===============================================================================

You will need the following software installed:

* `lttoolbox` (>= 3.3.0)
* `apertium` (>= 3.3.0)

If this does not make any sense, we recommend you look at: www.apertium.org

Compiling
===============================================================================

Given the requirements being installed, you should be able to just run:

`$ ./translate.sh --build`

`$ sudo chmod +x translate.sh`

Testing
===============================================================================

If you are in the source directory after building, the following
commands should work:

`$  ./translate.sh`
- Translate Kikamba NPs into English NPs

`$ ./translate.sh -e`
- Translate English NPs into Kikamba NPs

`$ ./translate.sh --help`
- For help with arguments

Currently supported arguments:
* `0`:    force a one-time translation in the opposite direction
* `1`:    show morphological analysis
* `2`:    show morphological analysis and pretagging
* `3`:    show morphological analysis, pretagging, and disambiguation
* `4`:    show transferred but ungenerated morphemes

Files and data
===============================================================================

* `eng.dix`
  - Monolingual English dictionary
* `eng-kam.t1x`
  - English -> Kikamba structural transfer rules
* `kam.dix`
  - Monolingual Kikamba dictionary
* `kam-eng.dix`
  - Bilingual Kikamba & English dictionary
* `kam-eng.t1x`
  - Kikamba -> English structural transfer rules
* `nc-morphology.pdf`
  - Morphology paper on which this tool is based
* `pretagger.py`
  - Pretagger helper tool
* `tagger.awk`
  - Tagging disambiguation tool
* `translate.sh`
  - Executable file for translations

Kikamba lemmas
===============================================================================
* mũndũ
* mwaki
* mũte
* mũaĩo
* mũalyũlo
* mũamba
* mũandĩko
* mwaki
* mwaka
* ĩamũko
* ĩana
* ĩandasi
* ĩandĩko
* ĩandi
* ĩandiko
* ĩandiko
* ĩanga
* ĩangi
* ĩelo
* ĩema
* ĩembe
* ĩembe
* ĩeyo
* ĩia
* ĩia
* ĩia
* ĩika
* ĩiko
* ĩiko
* ĩiko
* ĩima
* ĩindi
* ĩindi
* ĩiu
* ĩkalatasi
* ĩkalatya
* ĩkalĩ
* ĩkalũ
* ĩkanda
* ĩkanga
* ĩkanisia
* ĩkanya
* ĩkaya
* ĩkeleko
* ĩkenge
* ĩkenge
* ĩkesa
* ĩkooa
* ĩlovoto
* ĩsembo
* ĩseso
* ĩsindano
* ĩsindano ma wanake
* ĩsomo
* ĩtema
* ĩthaa
* ĩthaũ
* ĩthaũ
* ĩtialyo
* ĩtukũ
* ĩtumbe
* ĩuta
* ĩvia
* ĩvive
* ĩwa
* yaka
* yanga
* thayũ
* kĩala
* kĩamata
* kĩamũko
* kĩkoyo
* kĩvĩla
* kĩtuo
* kĩwũ
* mũnĩnĩ
* mũnene
* mũseo
* ũyũ
* aya
* ũũ
* ũsu
* wakwa
* witũ
* waku
* wenyu
* wake
* woo

English lemmas
===============================================================================
* person
* builder
* tree
* weaning
* interpretation
* Baobab tree
* handwriting
* fire
* year
* good morning
* hundred
* bun
* writing
* stiffness
* section
* letter
* footprint
* arrow
* fee
* tent
* hoe
* mango
* tooth
* lake
* milk
* weed
* age group
* kitchen
* fireplace
* stove
* hole
* ditch
* corncob
* banana
* paper
* roughly ground grain
* brick
* temple
* rope
* full moon
* church
* eggshell
* outcry
* dreg
* bird trap
* ostrich egg
* chisel
* cough
* droplet
* track meet
* honeycomb
* competition
* beauty pageant
* lesson
* liver
* decoration
* sport
* banter
* leftover
* day
* egg
* butter
* pus
* decoration
* honeycomb
* branch
* cassava
* soul
* rafter
* burdock
* epiphany
* leopard
* chair
* shoulder
* water
* small
* big
* good
* this
* that
* these
* those
* my
* our
* your
* your
* his
* her
* its
* their

For more information
===============================================================================

* http://wiki.apertium.org/wiki/Installation
* http://wiki.apertium.org/wiki/apertium-kik
* http://wiki.apertium.org/wiki/Using_an_lttoolbox_dictionary

Help and support
===============================================================================

If you need help using this language pair or data, you can contact:

* Developers: [Irene](mailto:itang1@swarthmore.edu) & [Kevin](mailto:kmurphy4@swarthmore.edu)
* Mailing list: [apertium-stuff@lists.sourceforge.net](mailto:apertium-stuff@lists.sourceforge.net)
* IRC: #apertium on [irc.freenode.net](freenode.net)
