#!/usr/bin/env python

parameters = (
  ("ghz1=1,0", "", "0PM"),
  ("ghz1=0,0 ghz2=0,0", "", "0PH"),
  ("ghz1=0,0 ghz4=1,0", "", "0M"),
  ("ghz1=0,0 ghz1_prime2=-12100.42,0", "", "0M"),
  ("ghz1=0,0 ghzgs2=0.0477547", "MPhotonCutoff=4", "0PHZy"),
  ("ghz1=0,0 ghzgs4=0.0529487", "MPhotonCutoff=4", "0MZy"),
  ("ghz1=0,0 ghgsgs2=0.0530640", "MPhotonCutoff=4", "0PHyy"),
  ("ghz1=0,0 ghgsgs4=0.0536022", "MPhotonCutoff=4", "0Myy"),
  ("ghz1=1,0 ghz2=0,0", "", "0PHf05ph0"),
  ("ghz1=1,0 ghz4=1,0", "", "0Mf05ph0"),
  ("ghz1=1,0 ghz1_prime2=-12100.42,0", "", "0Mf05ph0"),
  ("ghz1=1,0 ghzgs2=0.0477547", "MPhotonCutoff=4", "0PHZyf05ph0"),
  ("ghz1=1,0 ghzgs4=0.0529487", "MPhotonCutoff=4", "0MZyf05ph0"),
  ("ghz1=1,0 ghgsgs2=0.0530640", "MPhotonCutoff=4", "0PHyyf05ph0"),
  ("ghz1=1,0 ghgsgs4=0.0536022", "MPhotonCutoff=4", "0Myyf05ph0"),
 )

with open("JHUGen_Template.input") as f:
  template = f.read()

dct = {}

for dct["COUPLING_STRING"], dct["Q2_CUT"], dct["Hypothesis"]in parameters:
  print(dct)
  with open("JHUGen_{}.input".format(dct["Hypothesis"]), "w") as f:
    f.write(template.format(**dct))
