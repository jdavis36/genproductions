import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            '25:onMode = off', # Turn off all H decays
            '25:oneChannel = 1 1 100 24 -24', # H->W+ W-
            '25:onIfMatch = 24 -24',
            '35:onMode = off',
            '35:oneChannel = 1 1 100 5 -5',  # Y->b b~
            '35:onIfMatch = 5 -5',
            '15:onMode = on', # allow all tau decays. Leptonic and Hadronic
            '24:mMin = 0.05', # the lower limit of the allowed mass range generated by the Breit-Wigner (in GeV)
            '24:onMode = off', # Turn off all W decays
            '24:onIfAny = 11 13 15', # Add W->enu, W->munu, W->taunu. Add W->qq decays
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent  = on', #on: treat all three neutrino flavours as equivalent
            'ResonanceDecayFilter:udscAsEquivalent  = on',  #on: treat udsc quarks as equivalent
            'ResonanceDecayFilter:mothers = 35,25,24', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 5,5,11,12,11,12', # qq,lnu,lnu
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters')
    )
)
