#!/bin/bash

# define colors
GREEN='\033[1;32m'
NC='\033[0m'
GREY='\033[1;34m'

# build stuff if we need it
if [[ $* == *-b* ]]; then

  echo -e "${GREEN} >> building monolingual dict tools...${NC}"
  lt-comp lr kam.dix bin/kam-eng.morf
  lt-comp rl kam.dix bin/eng-kam.gen
  lt-comp lr eng.dix bin/eng-kam.morf
  lt-comp rl eng.dix bin/kam-eng.gen

  echo -e "${GREEN} >> building bilingual dict tools...${NC}"
  lt-comp lr kam-eng.dix bin/kam-eng.bil
  lt-comp rl kam-eng.dix bin/eng-kam.bil

  echo -e "${GREEN} >> building transfer tools...${NC}"
  apertium-preprocess-transfer kam-eng.t1x bin/kam-eng.t1x
  apertium-preprocess-transfer eng-kam.t1x bin/eng-kam.t1x

  echo -e "${GREEN} >> all tools built...${NC}"

  if [[ $* == *--build* ]]; then
    exit
  fi
fi

# show some help stuff
if [[ $* == *-h* ]]; then

  echo -e "\nAvailable execution flags:${GREEN}"
  echo -e "\t-b, --build\tForce a compile of all dictionary tools"
  echo -e "\t-e\t\tUse English->Kikamba translations"
  echo -e "\t-h, --help\tShow this help page${NC}"

  echo -e "\nSpecial line characters:${GREEN}"
  echo -e "\t0\t\tForce a one-time translation in the opposite direction"
  echo -e "\t1\t\tShow morphological analysis"
  echo -e "\t2\t\tShow morph. analysis and pretagging"
  echo -e "\t3\t\tShow morph. analysis, pretagging, and disambiguation"
  echo -e "\t4\t\tShow transferred but ungenerated morphemes${NC}"

  if [[ $* == *--help* ]]; then
    exit
  fi
fi

# set the correct translation direction
NAME="Kikamba"
SRC="kam-eng"
TAR="eng-kam"
if [[ $* == *-e* ]]; then
  NAME="English"
  SRC="eng-kam"
  TAR="kam-eng"
fi

# get SOURCE tokens
echo -e "\nPlease enter a $NAME token\t${GREY}[to quit, type 'quit()']${NC}"
read -p ' > ' TOKEN

while true; do

  # replace U with ũ and I with ĩ
  TOKEN=${TOKEN//I/ĩ}
  TOKEN=${TOKEN//U/ũ}

  # allow one-line translations going the other way
  DIR=$SRC
  if [[ $TOKEN == *"0"* ]]; then
    DIR=$TAR
  fi

  # analyze it (in SOURCE) and optionally generate it (into TARGET)
  if [[ $TOKEN == 'quit()' ]]; then
    exit
  fi
  if [[ $TOKEN == *"1"* ]]; then
    echo $TOKEN | lt-proc bin/$DIR.morf
  elif [[ $TOKEN == *"2"* ]]; then
    echo $TOKEN | lt-proc bin/$DIR.morf | \
      python pretagger.py
  elif [[ $TOKEN == *"3"* ]]; then
    echo $TOKEN | lt-proc bin/$DIR.morf | \
      python pretagger.py | \
      ./tagger.awk
  elif [[ $TOKEN == *"4"* ]]; then
    echo $TOKEN | lt-proc bin/$DIR.morf | \
      python pretagger.py | \
      ./tagger.awk | \
      apertium-transfer $DIR.t1x bin/$DIR.t1x bin/$DIR.bil
  else
    echo $TOKEN | lt-proc bin/$DIR.morf | \
      python pretagger.py | \
      ./tagger.awk | \
      apertium-transfer $DIR.t1x bin/$DIR.t1x bin/$DIR.bil | \
      lt-proc -g bin/$DIR.gen
  fi

  # get more SOURCE tokens
  echo -e "\n"
  read -p ' > ' TOKEN

done
