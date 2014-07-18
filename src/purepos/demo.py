#!/usr/bin/env python3

"""
Copyright (C) György Orosz
Author: György Orosz <oroszgy@itk.ppke.hu>
URL: <http://github.com/ppke-nlpg/purepos>
For license information, see LICENSE.TXT
"""

from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division

import os
import sys

_base_dir = os.path.dirname( os.path.abspath( __file__) )
sys.path.append(_base_dir)

from .purepos import PurePosTagger, PurePosTrainer
from .util import parse_text
from pprint import pprint

train_text = """Egyéves#egyéves#[MN][NOM] előkészítő#előkészít#[IGE][_OKEP][NOM] munka#munka#[FN][NOM] és#és#[KOT] féléves#féléves#[MN][NOM] kísérleti#kísérleti#[MN][NOM] szakasz#szakasz#[FN][NOM] után#után#[NU] november#november#[FN][NOM] elején#eleje#[FN][PSe3][SUP] kezdte#kezd#[IGE][TMe3] meg#meg#[IK] nyilvános#nyilvános#[MN][NOM] szolgáltatását#szolgáltatás#[FN][PSe3][ACC] egy#egy#[DET] új#új#[MN][NOM] internetes#internetes#[MN][NOM] portál#portál#[FN][NOM] .#.#[PUNCT]
A#a#[DET] hírügynökség#hírügynökség#[FN][NOM] munkatársai#munkatárs#[FN][PSe3i][NOM] az#az#[DET] interneten#internet#[FN][SUP] publikált#publikál#[IGE][_MIB][NOM] napilapokat#napilap#[FN][PL][ACC] ,#,#[PUNCT] hetilapokat#hetilap#[FN][PL][ACC] ,#,#[PUNCT] folyóiratokat#folyóirat#[FN][PL][ACC] és#és#[KOT] honlapokat#honlap#[FN][PL][ACC] figyelik#figyel#[IGE][Tt3] ,#,#[PUNCT] az#az#[DET] ott#ott#[HA|NM] talált#talál#[IGE][_MIB][NOM] érdekes#érdekes#[MN][NOM] cikkekből#cikk#[FN][PL][ELA] készítenek#készít#[IGE][t3] összefoglalót#összefoglaló#[FN][ACC] .#.#[PUNCT]
Így#így#[KOT] a#a#[DET] weboldalon#weboldal#[FN][SUP] csupán#csupán#[HA] a#a#[DET] cikkek#cikk#[FN][PL][NOM] összefoglalói#összefoglaló#[FN][PSe3i][NOM] tekinthetők#tekinthető#[MN][PL][NOM] meg#meg#[IK] ,#,#[PUNCT] ugyanakkor#ugyanakkor#[HA|NM] elérhetők#elérhető#[MN][PL][NOM] az#az#[DET] eredeti#eredeti#[MN][NOM] cikkek#cikk#[FN][PL][NOM] is#is#[HA] .#.#[PUNCT]
"""

def main(model_path="./_test.model"):
    # Training the tagger
    print("==Training the tagger (verbose)==")
    pt = PurePosTrainer(model_path, verbose=True)
    pt.train(parse_text(train_text), finalize=True)
    
    # Tagging with multiple output
    print("\n==Tagging with multiple output==")
    tagger = PurePosTagger(model_path, multi_tag=5)
    pprint(tagger.tag("A jó munka érdekes .".split()))
    
    # Tagging by providing analyses and scores
    print("\n==Tagging with analyses==")
    tagger = PurePosTagger(model_path)
    print(tagger.tag([("Józsi", [("Józsi", "[FN][NOM]")]), 
                      ("ütött", [("üt", "[IGE][Me3]", -0.001), ("üt", "[IGE][_MIB][NOM]", -99)]), 
                      "."]
                     ))
    del tagger
    os.remove(model_path)
    
if __name__ == "__main__":
    model = "./test.model"
    main(model)
    os.remove(model)