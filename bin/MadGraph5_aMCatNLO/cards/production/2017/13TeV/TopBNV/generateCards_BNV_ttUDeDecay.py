import os
import random

#see Eq.2 in https://arxiv.org/pdf/1107.3805.pdf

#S-ch = tDUE
#T-ch = tEUD

MG = [
['generate  p p > t t~ BNV=0 /h a z ,  (t > u~ d~ e+) @0','add process  p p > t t~ BNV=0 /h a z , (t~ > u d e-)@1'],
['generate  p p > t t~ BNV=0 /h a z ,  (t > c~ d~ e+) @0','add process  p p > t t~ BNV=0 /h a z , (t~ > c d e-)@1'],
['generate  p p > t t~ BNV=0 /h a z ,  (t > u~ s~ e+) @0','add process  p p > t t~ BNV=0 /h a z , (t~ > u s e-)@1'],
['generate  p p > t t~ BNV=0 /h a z ,  (t > c~ s~ e+) @0','add process  p p > t t~ BNV=0 /h a z , (t~ > c s e-)@1'],
['generate  p p > t t~ BNV=0 /h a z ,  (t > u~ b~ e+) @0','add process  p p > t t~ BNV=0 /h a z , (t~ > u b e-)@1'],
['generate  p p > t t~ BNV=0 /h a z ,  (t > c~ b~ e+) @0','add process  p p > t t~ BNV=0 /h a z , (t~ > c b e-)@1'],
]

processName=[
'TDUE',
'TDCE',
'TSUE',
'TSCE',
'TBUE',
'TBCE',
]

couplingsName = [
['cS','cT'],
['cS','cT'],
['cS','cT'],
['cS','cT'],
['cS','cT'],
['cS','cT']
]


couplings =[
[['aaa3x1','bbb3x1','ccc1x1','ddd1x1'],['aaaprime3x1','bbbprime3x1','cccprime1x1','dddprime1x1']],
[['aaa3x1','bbb3x1','ccc2x1','ddd2x1'],['aaaprime3x1','bbbprime3x1','cccprime2x1','dddprime2x1']],
[['aaa3x2','bbb3x2','ccc1x1','ddd1x1'],['aaaprime3x1','bbbprime3x1','cccprime1x2','dddprime1x2']],
[['aaa3x2','bbb3x2','ccc2x1','ddd2x1'],['aaaprime3x1','bbbprime3x1','cccprime2x2','dddprime2x2']],
[['aaa3x3','bbb3x3','ccc1x1','ddd1x1'],['aaaprime3x1','bbbprime3x1','cccprime1x3','dddprime1x3']],
[['aaa3x3','bbb3x3','ccc2x1','ddd2x1'],['aaaprime3x1','bbbprime3x1','cccprime2x3','dddprime2x3']]
]

scanValues = 20

for num, name in enumerate(processName):
    os.system('rm -rf BNV_TT_' + name)
    os.system('mkdir BNV_TT_' + name)
    customizecards = ''
    customizecards = customizecards + 'set param_card mass   6  172.5\n'
    customizecards = customizecards + 'set param_card yukawa 6  172.5\n'
    customizecards = customizecards + 'set param_card mass   25 125.0\n'
    customizecards = customizecards + 'set dynamical_scale_choice 3\n'
    for gWC in couplings[num]:
        for WC in gWC:
            customizecards = customizecards + 'set param_card '+WC+ ' ' + str(1) + '\n'     
    open('BNV_TT_' + name + '/BNV_TT_' + name + '_customizecards.dat', 'wt').write(customizecards)
    n=-1
    rwgtCards = ''
    rwgtCards = rwgtCards + 'change rwgt_dir rwgt'+ '\n'+ '\n'
    for v in range(scanValues):
        randomWC = []
        for WC1 in couplingsName[num]:
            r = random.uniform(0,10)
            randomWC.append(round(r,2))
        n  = n+1
        rwgtCards = rwgtCards + '\n'
        rwgtCards = rwgtCards + 'launch --rwgt_name=EFTrwgt' + str(n) + '_'
        for WC1 in couplingsName[num]:
            rwgtCards = rwgtCards + WC1 + '_' + str(randomWC[couplingsName[num].index(WC1)]) + '_'
        rwgtCards = rwgtCards[:-1]
        rwgtCards = rwgtCards + '\n'
        for WC1 in couplingsName[num]:
            for wcIndex in couplings[num][couplingsName[num].index(WC1)]:
                rwgtCards = rwgtCards +'    set param_card ' + wcIndex + ' ' + str(randomWC[couplingsName[num].index(WC1)])  + '\n'
    open('BNV_TT_' + name + '/BNV_TT_' + name + '_reweight_card.dat', 'wt').write(rwgtCards)
    
    process = ''
    process = process + 'import model bnv_mediator_ufo' + '\n'
    process = process + 'define p = g u c d s u~ c~ d~ s~' + '\n'
    process = process + MG[num][0] + '\n'
    process = process + MG[num][1] + '\n'
    process = process + 'output BNV_TT_' + name + ' -f -nojpeg'
    open('BNV_TT_' + name + '/BNV_TT_' + name + '_proc_card.dat', 'wt').write(process)
    os.system('cp BNV_run_card.dat BNV_TT_' + name + '/BNV_TT_' + name + '_run_card.dat')

