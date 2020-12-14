from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain A ")


cmd.select("Bstrand1", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain B ")


cmd.select("Bstrand2", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain B ")


cmd.select("Astrand3", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain A ")


cmd.select("Astrand4", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain A ")


cmd.select("Cstrand5", "resi 315+316+317+318+319+320+321+322+323+324+325 & chain C ")


cmd.select("Cstrand6", "resi 292+293+294+295+296+297+298+299+300+301+302+303 & chain C ")


cmd.select("Cstrand7", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117 & chain C ")


cmd.select("Bstrand8", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain B ")


cmd.select("Cstrand9", "resi 81+82+83+84+85+86+87+88+89+90+91+92+93+94+95 & chain C ")


cmd.select("Bstrand10", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118 & chain B ")


cmd.select("Astrand11", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.pseudoatom ("PseudoH324B", pos=[-89.85529,-67.767395,-47.807407])
cmd.pseudoatom ("PseudoH85A", pos=[-89.07595,-69.68167,-47.07555])
cmd.pseudoatom ("PseudoH322B", pos=[-90.05714,-71.97538,-52.87644])
cmd.pseudoatom ("PseudoH87A", pos=[-89.72173,-74.0001,-52.00321])
cmd.pseudoatom ("PseudoH320B", pos=[-87.94697,-75.181946,-57.99027])
cmd.pseudoatom ("PseudoH89A", pos=[-86.98473,-77.49873,-57.576923])
cmd.pseudoatom ("PseudoH318B", pos=[-86.72127,-78.95771,-63.506493])
cmd.pseudoatom ("PseudoH316B", pos=[-83.19661,-81.932205,-68.75326])
cmd.pseudoatom ("PseudoH93A", pos=[-81.96006,-84.5085,-67.59341])
cmd.pseudoatom ("PseudoH315B", pos=[-81.93054,-81.39265,-73.029655])
cmd.pseudoatom ("PseudoH299B", pos=[-85.52436,-76.45731,-69.70191])
cmd.pseudoatom ("PseudoH317B", pos=[-85.34358,-78.1063,-67.66136])
cmd.pseudoatom ("PseudoH297B", pos=[-87.40338,-73.59653,-63.591866])
cmd.pseudoatom ("PseudoH319B", pos=[-88.63646,-75.020905,-62.27826])
cmd.pseudoatom ("PseudoH295B", pos=[-90.97439,-70.838844,-58.803715])
cmd.pseudoatom ("PseudoH321B", pos=[-91.50195,-72.280075,-57.084183])
cmd.pseudoatom ("PseudoH293B", pos=[-93.63069,-67.61928,-53.21048])
cmd.pseudoatom ("PseudoH323B", pos=[-92.38769,-68.508446,-51.28075])
cmd.pseudoatom ("PseudoH323A", pos=[-64.72058,-63.327038,-44.563595])
cmd.pseudoatom ("PseudoH293A", pos=[-66.07247,-62.548,-42.71795])
cmd.pseudoatom ("PseudoH321A", pos=[-69.27279,-68.2582,-42.054897])
cmd.pseudoatom ("PseudoH295A", pos=[-71.23254,-67.140305,-41.7482])
cmd.pseudoatom ("PseudoH319A", pos=[-74.2241,-72.33462,-41.460556])
cmd.pseudoatom ("PseudoH297A", pos=[-76.21972,-71.36668,-41.73753])
cmd.pseudoatom ("PseudoH317A", pos=[-79.44804,-76.93527,-40.866302])
cmd.pseudoatom ("PseudoH299A", pos=[-81.41442,-75.69915,-39.75575])
cmd.pseudoatom ("PseudoH315A", pos=[-84.57414,-81.77257,-39.96215])
cmd.pseudoatom ("PseudoH315C", pos=[-54.953465,-76.38324,-54.55641])
cmd.pseudoatom ("PseudoH299C", pos=[-57.53781,-71.327866,-58.373516])
cmd.pseudoatom ("PseudoH317C", pos=[-58.83795,-73.16466,-59.53623])
cmd.pseudoatom ("PseudoH297C", pos=[-62.56419,-68.86537,-62.513943])
cmd.pseudoatom ("PseudoH319C", pos=[-63.057293,-70.205956,-64.18298])
cmd.pseudoatom ("PseudoH295C", pos=[-66.04881,-66.03864,-67.38665])
cmd.pseudoatom ("PseudoH321C", pos=[-67.06822,-67.69479,-68.69063])
cmd.pseudoatom ("PseudoH293C", pos=[-70.51929,-63.33858,-71.8351])
cmd.pseudoatom ("PseudoH323C", pos=[-72.6029,-64.74831,-71.92297])
cmd.pseudoatom ("PseudoH117C", pos=[-67.62112,-59.68058,-68.166084])
cmd.pseudoatom ("PseudoH294C", pos=[-67.69338,-62.058464,-68.77949])
cmd.pseudoatom ("PseudoH296C", pos=[-65.002174,-65.06128,-63.227737])
cmd.pseudoatom ("PseudoH113C", pos=[-61.983032,-66.14552,-57.577595])
cmd.pseudoatom ("PseudoH298C", pos=[-60.95971,-68.51302,-58.30471])
cmd.pseudoatom ("PseudoH109C", pos=[-61.647285,-73.89447,-50.599075])
cmd.pseudoatom ("PseudoH302C", pos=[-61.241188,-76.21492,-51.39095])
cmd.pseudoatom ("PseudoH107C", pos=[-65.62248,-78.95778,-48.172527])
cmd.pseudoatom ("PseudoH94A", pos=[-78.147194,-86.34111,-66.26096])
cmd.pseudoatom ("PseudoH102A", pos=[-80.69034,-87.2773,-67.12835])
cmd.pseudoatom ("PseudoH92A", pos=[-84.76056,-84.927185,-64.391594])
cmd.pseudoatom ("PseudoH104A", pos=[-85.84855,-86.6226,-62.794212])
cmd.pseudoatom ("PseudoH90A", pos=[-87.515175,-81.68643,-58.933655])
cmd.pseudoatom ("PseudoH106A", pos=[-87.01537,-83.004944,-56.875282])
cmd.pseudoatom ("PseudoH88A", pos=[-88.00137,-78.11335,-53.27813])
cmd.pseudoatom ("PseudoH108A", pos=[-88.08257,-79.37845,-51.23586])
cmd.pseudoatom ("PseudoH86A", pos=[-89.74044,-74.23206,-47.69671])
cmd.pseudoatom ("PseudoH110A", pos=[-88.62593,-75.052345,-45.68431])
cmd.pseudoatom ("PseudoH84A", pos=[-87.34622,-69.06442,-43.011677])
cmd.pseudoatom ("PseudoH112A", pos=[-85.66869,-70.00617,-41.7405])
cmd.pseudoatom ("PseudoH82A", pos=[-82.59746,-65.28225,-40.457893])
cmd.pseudoatom ("PseudoH114A", pos=[-80.53887,-65.9782,-41.23103])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR320B", pos=[-87.18379,-73.67714,-58.43489])
cmd.pseudoatom ("PseudoR91A", pos=[-85.89385,-81.0268,-63.029682])
cmd.pseudoatom ("PseudoR93A", pos=[-81.36778,-83.1846,-66.63748])
cmd.pseudoatom ("PseudoR297B", pos=[-88.26625,-72.71369,-64.85196])
cmd.pseudoatom ("PseudoR297A", pos=[-77.194336,-70.51407,-40.57068])
cmd.pseudoatom ("PseudoR297C", pos=[-61.38337,-67.54228,-62.51058])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 84 & chain A & name O", "resi 325 & chain B & name N")
cmd.distance("StrongHBond", "resi 84 & chain A & name N", "resi 325 & chain B & name O")
cmd.distance("StrongHBond", "resi 86 & chain A & name O", "resi 323 & chain B & name N")
cmd.distance("StrongHBond", "resi 86 & chain A & name N", "resi 323 & chain B & name O")
cmd.distance("StrongHBond", "resi 88 & chain A & name O", "resi 321 & chain B & name N")
cmd.distance("StrongHBond", "resi 88 & chain A & name N", "resi 321 & chain B & name O")
cmd.distance("StrongHBond", "resi 90 & chain A & name O", "resi 319 & chain B & name N")
cmd.distance("StrongHBond", "resi 90 & chain A & name N", "resi 319 & chain B & name O")
cmd.distance("StrongHBond", "resi 92 & chain A & name O", "resi 317 & chain B & name N")
cmd.distance("StrongHBond", "resi 92 & chain A & name N", "resi 317 & chain B & name O")
cmd.distance("StrongHBond", "resi 316 & chain B & name O", "resi 300 & chain B & name N")
cmd.distance("StrongHBond", "resi 316 & chain B & name N", "resi 300 & chain B & name O")
cmd.distance("StrongHBond", "resi 318 & chain B & name O", "resi 298 & chain B & name N")
cmd.distance("StrongHBond", "resi 318 & chain B & name N", "resi 298 & chain B & name O")
cmd.distance("StrongHBond", "resi 320 & chain B & name O", "resi 296 & chain B & name N")
cmd.distance("StrongHBond", "resi 320 & chain B & name N", "resi 296 & chain B & name O")
cmd.distance("StrongHBond", "resi 322 & chain B & name O", "resi 294 & chain B & name N")
cmd.distance("StrongHBond", "resi 322 & chain B & name N", "resi 294 & chain B & name O")
cmd.distance("StrongHBond", "resi 324 & chain B & name O", "resi 292 & chain B & name N")
cmd.distance("StrongHBond", "resi 324 & chain B & name N", "resi 292 & chain B & name O")
cmd.distance("StrongHBond", "resi 292 & chain A & name O", "resi 324 & chain A & name N")
cmd.distance("StrongHBond", "resi 292 & chain A & name N", "resi 324 & chain A & name O")
cmd.distance("StrongHBond", "resi 294 & chain A & name O", "resi 322 & chain A & name N")
cmd.distance("StrongHBond", "resi 294 & chain A & name N", "resi 322 & chain A & name O")
cmd.distance("StrongHBond", "resi 296 & chain A & name O", "resi 320 & chain A & name N")
cmd.distance("StrongHBond", "resi 296 & chain A & name N", "resi 320 & chain A & name O")
cmd.distance("StrongHBond", "resi 298 & chain A & name O", "resi 318 & chain A & name N")
cmd.distance("StrongHBond", "resi 298 & chain A & name N", "resi 318 & chain A & name O")
cmd.distance("StrongHBond", "resi 300 & chain A & name O", "resi 316 & chain A & name N")
cmd.distance("StrongHBond", "resi 300 & chain A & name N", "resi 316 & chain A & name O")
cmd.distance("StrongHBond", "resi 316 & chain C & name O", "resi 300 & chain C & name N")
cmd.distance("StrongHBond", "resi 316 & chain C & name N", "resi 300 & chain C & name O")
cmd.distance("StrongHBond", "resi 318 & chain C & name O", "resi 298 & chain C & name N")
cmd.distance("StrongHBond", "resi 318 & chain C & name N", "resi 298 & chain C & name O")
cmd.distance("StrongHBond", "resi 320 & chain C & name O", "resi 296 & chain C & name N")
cmd.distance("StrongHBond", "resi 320 & chain C & name N", "resi 296 & chain C & name O")
cmd.distance("StrongHBond", "resi 322 & chain C & name O", "resi 294 & chain C & name N")
cmd.distance("StrongHBond", "resi 322 & chain C & name N", "resi 294 & chain C & name O")
cmd.distance("StrongHBond", "resi 324 & chain C & name O", "resi 292 & chain C & name N")
cmd.distance("StrongHBond", "resi 324 & chain C & name N", "resi 292 & chain C & name O")
cmd.distance("StrongHBond", "resi 295 & chain C & name O", "resi 116 & chain C & name N")
cmd.distance("StrongHBond", "resi 295 & chain C & name N", "resi 116 & chain C & name O")
cmd.distance("StrongHBond", "resi 297 & chain C & name O", "resi 114 & chain C & name N")
cmd.distance("StrongHBond", "resi 297 & chain C & name N", "resi 114 & chain C & name O")
cmd.distance("StrongHBond", "resi 299 & chain C & name O", "resi 112 & chain C & name N")
cmd.distance("StrongHBond", "resi 299 & chain C & name N", "resi 112 & chain C & name O")
cmd.distance("StrongHBond", "resi 301 & chain C & name O", "resi 110 & chain C & name N")
cmd.distance("StrongHBond", "resi 301 & chain C & name N", "resi 110 & chain C & name O")
cmd.distance("StrongHBond", "resi 303 & chain C & name O", "resi 108 & chain C & name N")
cmd.distance("StrongHBond", "resi 303 & chain C & name N", "resi 108 & chain C & name O")
cmd.distance("StrongHBond", "resi 99 & chain A & name O", "resi 95 & chain A & name N")
cmd.distance("StrongHBond", "resi 99 & chain A & name N", "resi 95 & chain A & name O")
cmd.distance("StrongHBond", "resi 103 & chain A & name O", "resi 93 & chain A & name N")
cmd.distance("StrongHBond", "resi 103 & chain A & name N", "resi 93 & chain A & name O")
cmd.distance("StrongHBond", "resi 105 & chain A & name O", "resi 91 & chain A & name N")
cmd.distance("StrongHBond", "resi 105 & chain A & name N", "resi 91 & chain A & name O")
cmd.distance("StrongHBond", "resi 107 & chain A & name O", "resi 89 & chain A & name N")
cmd.distance("StrongHBond", "resi 107 & chain A & name N", "resi 89 & chain A & name O")
cmd.distance("StrongHBond", "resi 109 & chain A & name O", "resi 87 & chain A & name N")
cmd.distance("StrongHBond", "resi 109 & chain A & name N", "resi 87 & chain A & name O")
cmd.distance("StrongHBond", "resi 111 & chain A & name O", "resi 85 & chain A & name N")
cmd.distance("StrongHBond", "resi 111 & chain A & name N", "resi 85 & chain A & name O")
cmd.distance("StrongHBond", "resi 113 & chain A & name O", "resi 83 & chain A & name N")
cmd.distance("StrongHBond", "resi 113 & chain A & name N", "resi 83 & chain A & name O")
cmd.distance("StrongHBond", "resi 115 & chain A & name O", "resi 81 & chain A & name N")
cmd.distance("StrongHBond", "resi 115 & chain A & name N", "resi 81 & chain A & name O")
cmd.distance("WeakHBond", "resi 84 & chain A & name O", "PseudoH324B")
cmd.distance("WeakHBond", "resi 323 & chain B & name O", "PseudoH85A")
cmd.distance("WeakHBond", "resi 86 & chain A & name O", "PseudoH322B")
cmd.distance("WeakHBond", "resi 321 & chain B & name O", "PseudoH87A")
cmd.distance("WeakHBond", "resi 88 & chain A & name O", "PseudoH320B")
cmd.distance("WeakHBond", "resi 319 & chain B & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH318B")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH316B")
cmd.distance("WeakHBond", "resi 315 & chain B & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 300 & chain B & name O", "PseudoH315B")
cmd.distance("WeakHBond", "resi 316 & chain B & name O", "PseudoH299B")
cmd.distance("WeakHBond", "resi 298 & chain B & name O", "PseudoH317B")
cmd.distance("WeakHBond", "resi 318 & chain B & name O", "PseudoH297B")
cmd.distance("WeakHBond", "resi 296 & chain B & name O", "PseudoH319B")
cmd.distance("WeakHBond", "resi 320 & chain B & name O", "PseudoH295B")
cmd.distance("WeakHBond", "resi 294 & chain B & name O", "PseudoH321B")
cmd.distance("WeakHBond", "resi 322 & chain B & name O", "PseudoH293B")
cmd.distance("WeakHBond", "resi 292 & chain B & name O", "PseudoH323B")
cmd.distance("WeakHBond", "resi 292 & chain A & name O", "PseudoH323A")
cmd.distance("WeakHBond", "resi 322 & chain A & name O", "PseudoH293A")
cmd.distance("WeakHBond", "resi 294 & chain A & name O", "PseudoH321A")
cmd.distance("WeakHBond", "resi 320 & chain A & name O", "PseudoH295A")
cmd.distance("WeakHBond", "resi 296 & chain A & name O", "PseudoH319A")
cmd.distance("WeakHBond", "resi 318 & chain A & name O", "PseudoH297A")
cmd.distance("WeakHBond", "resi 298 & chain A & name O", "PseudoH317A")
cmd.distance("WeakHBond", "resi 316 & chain A & name O", "PseudoH299A")
cmd.distance("WeakHBond", "resi 300 & chain A & name O", "PseudoH315A")
cmd.distance("WeakHBond", "resi 300 & chain C & name O", "PseudoH315C")
cmd.distance("WeakHBond", "resi 316 & chain C & name O", "PseudoH299C")
cmd.distance("WeakHBond", "resi 298 & chain C & name O", "PseudoH317C")
cmd.distance("WeakHBond", "resi 318 & chain C & name O", "PseudoH297C")
cmd.distance("WeakHBond", "resi 296 & chain C & name O", "PseudoH319C")
cmd.distance("WeakHBond", "resi 320 & chain C & name O", "PseudoH295C")
cmd.distance("WeakHBond", "resi 294 & chain C & name O", "PseudoH321C")
cmd.distance("WeakHBond", "resi 322 & chain C & name O", "PseudoH293C")
cmd.distance("WeakHBond", "resi 292 & chain C & name O", "PseudoH323C")
cmd.distance("WeakHBond", "resi 293 & chain C & name O", "PseudoH117C")
cmd.distance("WeakHBond", "resi 116 & chain C & name O", "PseudoH294C")
cmd.distance("WeakHBond", "resi 114 & chain C & name O", "PseudoH296C")
cmd.distance("WeakHBond", "resi 297 & chain C & name O", "PseudoH113C")
cmd.distance("WeakHBond", "resi 112 & chain C & name O", "PseudoH298C")
cmd.distance("WeakHBond", "resi 301 & chain C & name O", "PseudoH109C")
cmd.distance("WeakHBond", "resi 108 & chain C & name O", "PseudoH302C")
cmd.distance("WeakHBond", "resi 303 & chain C & name O", "PseudoH107C")
cmd.distance("WeakHBond", "resi 101 & chain A & name O", "PseudoH94A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH102A")
cmd.distance("WeakHBond", "resi 103 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH104A")
cmd.distance("WeakHBond", "resi 105 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH106A")
cmd.distance("WeakHBond", "resi 107 & chain A & name O", "PseudoH88A")
cmd.distance("WeakHBond", "resi 87 & chain A & name O", "PseudoH108A")
cmd.distance("WeakHBond", "resi 109 & chain A & name O", "PseudoH86A")
cmd.distance("WeakHBond", "resi 85 & chain A & name O", "PseudoH110A")
cmd.distance("WeakHBond", "resi 111 & chain A & name O", "PseudoH84A")
cmd.distance("WeakHBond", "resi 83 & chain A & name O", "PseudoH112A")
cmd.distance("WeakHBond", "resi 113 & chain A & name O", "PseudoH82A")
cmd.distance("WeakHBond", "resi 81 & chain A & name O", "PseudoH114A")
cmd.distance("NonHBond", "resi 85 & chain A & name CB", "resi 324 & chain B & name CB")
cmd.distance("NonHBond", "resi 87 & chain A & name CB", "resi 322 & chain B & name CB")
cmd.distance("NonHBond", "resi 89 & chain A & name CB", "PseudoR320B")
cmd.distance("NonHBond", "PseudoR91A", "resi 318 & chain B & name CB")
cmd.distance("NonHBond", "PseudoR93A", "resi 316 & chain B & name CB")
cmd.distance("NonHBond", "resi 315 & chain B & name CB", "resi 301 & chain B & name CB")
cmd.distance("NonHBond", "resi 317 & chain B & name CB", "resi 299 & chain B & name CB")
cmd.distance("NonHBond", "resi 319 & chain B & name CB", "PseudoR297B")
cmd.distance("NonHBond", "resi 321 & chain B & name CB", "resi 295 & chain B & name CB")
cmd.distance("NonHBond", "resi 323 & chain B & name CB", "resi 293 & chain B & name CB")
cmd.distance("NonHBond", "resi 293 & chain A & name CB", "resi 323 & chain A & name CB")
cmd.distance("NonHBond", "resi 295 & chain A & name CB", "resi 321 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR297A", "resi 319 & chain A & name CB")
cmd.distance("NonHBond", "resi 299 & chain A & name CB", "resi 317 & chain A & name CB")
cmd.distance("NonHBond", "resi 301 & chain A & name CB", "resi 315 & chain A & name CB")
cmd.distance("NonHBond", "resi 315 & chain C & name CB", "resi 301 & chain C & name CB")
cmd.distance("NonHBond", "resi 317 & chain C & name CB", "resi 299 & chain C & name CB")
cmd.distance("NonHBond", "resi 319 & chain C & name CB", "PseudoR297C")
cmd.distance("NonHBond", "resi 321 & chain C & name CB", "resi 295 & chain C & name CB")
cmd.distance("NonHBond", "resi 323 & chain C & name CB", "resi 293 & chain C & name CB")
cmd.distance("NonHBond", "resi 294 & chain C & name CB", "resi 117 & chain C & name CB")
cmd.distance("NonHBond", "resi 296 & chain C & name CB", "resi 115 & chain C & name CB")
cmd.distance("NonHBond", "resi 298 & chain C & name CB", "resi 113 & chain C & name CB")
cmd.distance("NonHBond", "resi 302 & chain C & name CB", "resi 109 & chain C & name CB")
cmd.distance("NonHBond", "resi 102 & chain A & name CB", "PseudoR93A")
cmd.distance("NonHBond", "resi 102 & chain A & name CB", "resi 94 & chain A & name CB")
cmd.distance("NonHBond", "resi 104 & chain A & name CB", "resi 92 & chain A & name CB")
cmd.distance("NonHBond", "resi 106 & chain A & name CB", "resi 90 & chain A & name CB")
cmd.distance("NonHBond", "resi 108 & chain A & name CB", "resi 88 & chain A & name CB")
cmd.distance("NonHBond", "resi 110 & chain A & name CB", "resi 86 & chain A & name CB")
cmd.distance("NonHBond", "resi 112 & chain A & name CB", "resi 84 & chain A & name CB")
cmd.distance("NonHBond", "resi 114 & chain A & name CB", "resi 82 & chain A & name CB")
cmd.show("stick", "barrel")
cmd.color("red","StrongHBond")
cmd.color("green","WeakHBond")
cmd.color("purpleblue","NonHBond")
cmd.color("magenta","PseudoR*")
cmd.color("green","name CA & barrel")
cmd.color("red","name O & barrel")
cmd.color("blue","name N & barrel")
cmd.hide("labels")
cmd.zoom("barrel")