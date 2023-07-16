#!/usr/bin/env python

parameters = (
  ("ghz1=1,0", "", "pTjetcut=0", "0PM"),
  ("ghz1=0,0 ghz2=0,0", "","pTjetcut=0","0PH"),
  ("ghz1=0,0 ghz4=1,0", "","pTjetcut=0", "0M"),
  ("ghz1=0,0 ghz1_prime2=-12100.42,0", "","pTjetcut=0", "0L1"),
  ("ghz1=0,0 ghzgs2=0.0477547", "", "pTjetcut=1","0PHZy"),
  ("ghz1=0,0 ghzgs4=0.0529487", "", "pTjetcut=1","0MZy"),
  ("ghz1=0,0 ghgsgs2=0.0530640", "", "pTjetcut=1", "0PHyy"),
  ("ghz1=0,0 ghgsgs4=0.0536022", "", "pTjetcut=1", "0Myy"),
  ("ghz1=0,0 ghzgs2=0.0477547", "MPhotonCutoff=4", "", "0PHZyDec"),
  ("ghz1=0,0 ghzgs4=0.0529487", "MPhotonCutoff=4",  "", "0MZyDec"),
  ("ghz1=0,0 ghgsgs2=0.0530640", "MPhotonCutoff=4", "", "0PHyyDec"),
  ("ghz1=0,0 ghgsgs4=0.0536022", "MPhotonCutoff=4",  "", "0MyyDec"),
  ("ghz1=1,0 ghz2=0,0", "","pTjetcut=0", "0PHf05ph0"),
  ("ghz1=1,0 ghz4=1,0", "","pTjetcut=0", "0Mf05ph0"),
  ("ghz1=1,0 ghz1_prime2=-12100.42,0","", "pTjetcut=0", "0L1f05ph0"),
  ("ghz1=1,0 ghzgs2=0.0477547", "", "pTjetcut=1", "0PHZyf05ph0"),
  ("ghz1=1,0 ghzgs4=0.0529487", "", "pTjetcut=1",  "0MZyf05ph0"),
  ("ghz1=1,0 ghgsgs2=0.0530640", "", "pTjetcut=1", "0PHyyf05ph0"),
  ("ghz1=1,0 ghgsgs4=0.0536022", "", "pTjetcut=1", "0Myyf05ph0"),
  ("ghz1=1,0 ghzgs2=0.0477547", "MPhotonCutoff=4", "", "0PHZyf05ph0Dec"),
  ("ghz1=1,0 ghzgs4=0.0529487", "MPhotonCutoff=4", "",  "0MZyf05ph0Dec"),
  ("ghz1=1,0 ghgsgs2=0.0530640", "MPhotonCutoff=4", "",  "0PHyyf05ph0Dec"),
  ("ghz1=1,0 ghgsgs4=0.0536022", "MPhotonCutoff=4", "",  "0Myyf05ph0Dec"),
 )

with open("JHUGen_Template.input") as f:
  template = f.read()

dct = {}

for dct["COUPLING_STRING"], dct["Q2_CUT"], dct["Pt_JetCut"], dct["Hypothesis"] in parameters:
  print(dct)
  with open("JHUGen_{}.input".format(dct["Hypothesis"]), "w") as f:
    f.write(template.format(**dct))
