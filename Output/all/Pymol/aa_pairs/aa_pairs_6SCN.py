from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SCN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("astrand0", "resi 276+277+278 & chain a ")


cmd.select("astrand1", "resi 374+375+376 & chain a ")


cmd.select("bstrand2", "resi 276+277+278 & chain b ")


cmd.select("bstrand3", "resi 374+375+376 & chain b ")


cmd.select("cstrand4", "resi 276+277+278 & chain c ")


cmd.select("cstrand5", "resi 374+375+376 & chain c ")


cmd.select("dstrand6", "resi 276+277+278 & chain d ")


cmd.select("dstrand7", "resi 374+375+376 & chain d ")


cmd.select("estrand8", "resi 276+277+278 & chain e ")


cmd.select("estrand9", "resi 374+375+376 & chain e ")


cmd.select("fstrand10", "resi 276+277+278 & chain f ")


cmd.select("fstrand11", "resi 374+375+376 & chain f ")


cmd.select("gstrand12", "resi 276+277+278 & chain g ")


cmd.select("gstrand13", "resi 374+375+376 & chain g ")


cmd.select("Astrand14", "resi 276+277+278 & chain A ")


cmd.select("Astrand15", "resi 374+375+376 & chain A ")


cmd.select("Bstrand16", "resi 276+277+278 & chain B ")


cmd.select("Bstrand17", "resi 374+375+376 & chain B ")


cmd.select("Cstrand18", "resi 276+277+278 & chain C ")


cmd.select("Cstrand19", "resi 374+375+376 & chain C ")


cmd.select("Dstrand20", "resi 276+277+278 & chain D ")


cmd.select("Dstrand21", "resi 374+375+376 & chain D ")


cmd.select("Estrand22", "resi 276+277+278 & chain E ")


cmd.select("Estrand23", "resi 374+375+376 & chain E ")


cmd.select("Fstrand24", "resi 276+277+278 & chain F ")


cmd.select("Fstrand25", "resi 374+375+376 & chain F ")


cmd.select("Gstrand26", "resi 276+277+278 & chain G ")


cmd.select("Gstrand27", "resi 374+375+376 & chain G ")


cmd.select("Hstrand28", "resi 276+277+278 & chain H ")


cmd.select("Hstrand29", "resi 374+375+376 & chain H ")


cmd.select("Istrand30", "resi 276+277+278 & chain I ")


cmd.select("Istrand31", "resi 374+375+376 & chain I ")


cmd.select("Jstrand32", "resi 276+277+278 & chain J ")


cmd.select("Jstrand33", "resi 374+375+376 & chain J ")


cmd.select("Kstrand34", "resi 276+277+278 & chain K ")


cmd.select("Kstrand35", "resi 374+375+376 & chain K ")


cmd.select("Lstrand36", "resi 276+277+278 & chain L ")


cmd.select("Lstrand37", "resi 374+375+376 & chain L ")


cmd.select("Mstrand38", "resi 276+277+278 & chain M ")


cmd.select("Mstrand39", "resi 374+375+376 & chain M ")


cmd.select("Nstrand40", "resi 276+277+278 & chain N ")


cmd.select("Nstrand41", "resi 374+375+376 & chain N ")


cmd.select("Ostrand42", "resi 276+277+278 & chain O ")


cmd.select("Ostrand43", "resi 374+375+376 & chain O ")


cmd.select("Pstrand44", "resi 276+277+278 & chain P ")


cmd.select("Pstrand45", "resi 374+375+376 & chain P ")


cmd.select("Qstrand46", "resi 276+277+278 & chain Q ")


cmd.select("Qstrand47", "resi 374+375+376 & chain Q ")


cmd.select("Rstrand48", "resi 276+277+278 & chain R ")


cmd.select("Rstrand49", "resi 374+375+376 & chain R ")


cmd.select("Sstrand50", "resi 276+277+278 & chain S ")


cmd.select("Sstrand51", "resi 374+375+376 & chain S ")


cmd.select("Tstrand52", "resi 276+277+278 & chain T ")


cmd.select("Tstrand53", "resi 374+375+376 & chain T ")


cmd.select("Ustrand54", "resi 276+277+278 & chain U ")


cmd.select("Ustrand55", "resi 374+375+376 & chain U ")


cmd.select("Vstrand56", "resi 276+277+278 & chain V ")


cmd.select("Vstrand57", "resi 374+375+376 & chain V ")


cmd.select("Wstrand58", "resi 276+277+278 & chain W ")


cmd.select("Wstrand59", "resi 374+375+376 & chain W ")


cmd.select("Xstrand60", "resi 276+277+278 & chain X ")


cmd.select("Xstrand61", "resi 374+375+376 & chain X ")


cmd.select("Ystrand62", "resi 276+277+278 & chain Y ")


cmd.select("Ystrand63", "resi 374+375+376 & chain Y ")


cmd.select("Zstrand64", "resi 276+277+278 & chain Z ")


cmd.select("Zstrand65", "resi 374+375+376 & chain Z ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "astrand* or bstrand* or cstrand* or dstrand* or estrand* or fstrand* or gstrand* or Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand* or Ostrand* or Pstrand* or Qstrand* or Rstrand* or Sstrand* or Tstrand* or Ustrand* or Vstrand* or Wstrand* or Xstrand* or Ystrand* or Zstrand*")
cmd.pseudoatom ("PseudoH276a", pos=[205.74992,232.55905,147.12015])
cmd.pseudoatom ("PseudoH374a", pos=[209.63179,228.61525,143.62062])
cmd.pseudoatom ("PseudoH276b", pos=[215.61761,226.22487,147.14981])
cmd.pseudoatom ("PseudoH374b", pos=[218.69519,221.59473,143.58542])
cmd.pseudoatom ("PseudoH276c", pos=[224.12915,218.14586,147.11768])
cmd.pseudoatom ("PseudoH374c", pos=[226.29765,213.01486,143.61499])
cmd.pseudoatom ("PseudoH276d", pos=[230.97615,208.56554,147.15015])
cmd.pseudoatom ("PseudoH374d", pos=[232.1158,203.12784,143.61453])
cmd.pseudoatom ("PseudoH276e", pos=[235.85355,197.89459,147.16672])
cmd.pseudoatom ("PseudoH374e", pos=[235.96982,192.37929,143.61386])
cmd.pseudoatom ("PseudoH276f", pos=[238.64005,186.51389,147.16313])
cmd.pseudoatom ("PseudoH374f", pos=[237.72884,181.06732,143.62314])
cmd.pseudoatom ("PseudoH276g", pos=[239.28856,174.78107,147.1352])
cmd.pseudoatom ("PseudoH374g", pos=[237.3209,169.56682,143.58923])
cmd.pseudoatom ("PseudoH276A", pos=[237.66379,163.16792,147.13123])
cmd.pseudoatom ("PseudoH374A", pos=[234.70526,158.4335,143.6175])
cmd.pseudoatom ("PseudoH276B", pos=[233.7807,152.07814,147.17929])
cmd.pseudoatom ("PseudoH374B", pos=[230.05269,147.95972,143.6222])
cmd.pseudoatom ("PseudoH276C", pos=[227.95845,141.88567,147.1701])
cmd.pseudoatom ("PseudoH374C", pos=[223.50677,138.53615,143.60997])
cmd.pseudoatom ("PseudoH276D", pos=[220.2629,132.98112,147.16989])
cmd.pseudoatom ("PseudoH374D", pos=[215.31128,130.53848,143.59064])
cmd.pseudoatom ("PseudoH276E", pos=[211.08305,125.621765,147.12148])
cmd.pseudoatom ("PseudoH374E", pos=[205.72519,124.2371,143.62286])
cmd.pseudoatom ("PseudoH276F", pos=[200.6762,120.23299,147.14163])
cmd.pseudoatom ("PseudoH374F", pos=[195.0796,119.915634,143.57965])
cmd.pseudoatom ("PseudoH276G", pos=[189.38835,116.926544,147.12555])
cmd.pseudoatom ("PseudoH374G", pos=[183.87427,117.59799,143.6081])
cmd.pseudoatom ("PseudoH276H", pos=[177.67906,115.746284,147.14389])
cmd.pseudoatom ("PseudoH374H", pos=[172.43875,117.502266,143.60046])
cmd.pseudoatom ("PseudoH276I", pos=[166.00497,116.86758,147.15895])
cmd.pseudoatom ("PseudoH374I", pos=[161.17468,119.55627,143.61879])
cmd.pseudoatom ("PseudoH276J", pos=[154.73824,120.141136,147.12984])
cmd.pseudoatom ("PseudoH374J", pos=[150.48962,123.68737,143.62073])
cmd.pseudoatom ("PseudoH276K", pos=[144.30022,125.4935,147.14128])
cmd.pseudoatom ("PseudoH374K", pos=[140.78465,129.79112,143.596])
cmd.pseudoatom ("PseudoH276L", pos=[135.02663,132.70726,147.12825])
cmd.pseudoatom ("PseudoH374L", pos=[132.42142,137.62305,143.63405])
cmd.pseudoatom ("PseudoH276M", pos=[127.37741,141.60448,147.17574])
cmd.pseudoatom ("PseudoH374M", pos=[125.65168,146.87418,143.6198])
cmd.pseudoatom ("PseudoH276N", pos=[121.44437,151.76003,147.16812])
cmd.pseudoatom ("PseudoH374N", pos=[120.77182,157.23157,143.6017])
cmd.pseudoatom ("PseudoH276O", pos=[117.586914,162.83467,147.16922])
cmd.pseudoatom ("PseudoH374O", pos=[117.94241,168.36374,143.58173])
cmd.pseudoatom ("PseudoH276P", pos=[115.82155,174.4809,147.11937])
cmd.pseudoatom ("PseudoH374P", pos=[117.29685,179.80038,143.63368])
cmd.pseudoatom ("PseudoH276Q", pos=[116.38735,186.18127,147.14832])
cmd.pseudoatom ("PseudoH374Q", pos=[118.85203,191.17395,143.58759])
cmd.pseudoatom ("PseudoH276R", pos=[119.12914,197.5912,147.12419])
cmd.pseudoatom ("PseudoH374R", pos=[122.44169,202.05736,143.6011])
cmd.pseudoatom ("PseudoH276S", pos=[123.99276,208.31177,147.15211])
cmd.pseudoatom ("PseudoH374S", pos=[128.0978,212.01454,143.60088])
cmd.pseudoatom ("PseudoH276T", pos=[130.76514,217.88315,147.15918])
cmd.pseudoatom ("PseudoH374T", pos=[135.5174,220.72392,143.61874])
cmd.pseudoatom ("PseudoH276U", pos=[139.26634,225.99124,147.1485])
cmd.pseudoatom ("PseudoH374U", pos=[144.41681,227.92613,143.62521])
cmd.pseudoatom ("PseudoH276V", pos=[149.09706,232.41953,147.14172])
cmd.pseudoatom ("PseudoH374V", pos=[154.5648,233.27449,143.59283])
cmd.pseudoatom ("PseudoH276W", pos=[159.95877,236.8232,147.12025])
cmd.pseudoatom ("PseudoH374W", pos=[165.53621,236.60043,143.636])
cmd.pseudoatom ("PseudoH276X", pos=[171.51671,238.99489,147.15839])
cmd.pseudoatom ("PseudoH374X", pos=[176.9437,237.82787,143.60573])
cmd.pseudoatom ("PseudoH276Y", pos=[183.25923,239.06068,147.15942])
cmd.pseudoatom ("PseudoH374Y", pos=[188.33186,236.84729,143.60497])
cmd.pseudoatom ("PseudoH276Z", pos=[194.79779,236.85548,147.15564])
cmd.pseudoatom ("PseudoH374Z", pos=[199.39081,233.75703,143.58534])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 277 & chain a & name O", "resi 375 & chain a & name N")
cmd.distance("StrongHBond", "resi 277 & chain a & name N", "resi 375 & chain a & name O")
cmd.distance("StrongHBond", "resi 374 & chain a & name O", "resi 276 & chain b & name N")
cmd.distance("StrongHBond", "resi 374 & chain a & name N", "resi 276 & chain b & name O")
cmd.distance("StrongHBond", "resi 277 & chain b & name O", "resi 375 & chain b & name N")
cmd.distance("StrongHBond", "resi 277 & chain b & name N", "resi 375 & chain b & name O")
cmd.distance("StrongHBond", "resi 374 & chain b & name O", "resi 276 & chain c & name N")
cmd.distance("StrongHBond", "resi 374 & chain b & name N", "resi 276 & chain c & name O")
cmd.distance("StrongHBond", "resi 277 & chain c & name O", "resi 375 & chain c & name N")
cmd.distance("StrongHBond", "resi 277 & chain c & name N", "resi 375 & chain c & name O")
cmd.distance("StrongHBond", "resi 374 & chain c & name O", "resi 276 & chain d & name N")
cmd.distance("StrongHBond", "resi 374 & chain c & name N", "resi 276 & chain d & name O")
cmd.distance("StrongHBond", "resi 277 & chain d & name O", "resi 375 & chain d & name N")
cmd.distance("StrongHBond", "resi 277 & chain d & name N", "resi 375 & chain d & name O")
cmd.distance("StrongHBond", "resi 374 & chain d & name O", "resi 276 & chain e & name N")
cmd.distance("StrongHBond", "resi 374 & chain d & name N", "resi 276 & chain e & name O")
cmd.distance("StrongHBond", "resi 277 & chain e & name O", "resi 375 & chain e & name N")
cmd.distance("StrongHBond", "resi 277 & chain e & name N", "resi 375 & chain e & name O")
cmd.distance("StrongHBond", "resi 374 & chain e & name O", "resi 276 & chain f & name N")
cmd.distance("StrongHBond", "resi 374 & chain e & name N", "resi 276 & chain f & name O")
cmd.distance("StrongHBond", "resi 277 & chain f & name O", "resi 375 & chain f & name N")
cmd.distance("StrongHBond", "resi 277 & chain f & name N", "resi 375 & chain f & name O")
cmd.distance("StrongHBond", "resi 374 & chain f & name O", "resi 276 & chain g & name N")
cmd.distance("StrongHBond", "resi 374 & chain f & name N", "resi 276 & chain g & name O")
cmd.distance("StrongHBond", "resi 277 & chain g & name O", "resi 375 & chain g & name N")
cmd.distance("StrongHBond", "resi 277 & chain g & name N", "resi 375 & chain g & name O")
cmd.distance("StrongHBond", "resi 374 & chain g & name O", "resi 276 & chain A & name N")
cmd.distance("StrongHBond", "resi 374 & chain g & name N", "resi 276 & chain A & name O")
cmd.distance("StrongHBond", "resi 277 & chain A & name O", "resi 375 & chain A & name N")
cmd.distance("StrongHBond", "resi 277 & chain A & name N", "resi 375 & chain A & name O")
cmd.distance("StrongHBond", "resi 374 & chain A & name O", "resi 276 & chain B & name N")
cmd.distance("StrongHBond", "resi 374 & chain A & name N", "resi 276 & chain B & name O")
cmd.distance("StrongHBond", "resi 277 & chain B & name O", "resi 375 & chain B & name N")
cmd.distance("StrongHBond", "resi 277 & chain B & name N", "resi 375 & chain B & name O")
cmd.distance("StrongHBond", "resi 374 & chain B & name O", "resi 276 & chain C & name N")
cmd.distance("StrongHBond", "resi 374 & chain B & name N", "resi 276 & chain C & name O")
cmd.distance("StrongHBond", "resi 277 & chain C & name O", "resi 375 & chain C & name N")
cmd.distance("StrongHBond", "resi 277 & chain C & name N", "resi 375 & chain C & name O")
cmd.distance("StrongHBond", "resi 374 & chain C & name O", "resi 276 & chain D & name N")
cmd.distance("StrongHBond", "resi 374 & chain C & name N", "resi 276 & chain D & name O")
cmd.distance("StrongHBond", "resi 277 & chain D & name O", "resi 375 & chain D & name N")
cmd.distance("StrongHBond", "resi 277 & chain D & name N", "resi 375 & chain D & name O")
cmd.distance("StrongHBond", "resi 374 & chain D & name O", "resi 276 & chain E & name N")
cmd.distance("StrongHBond", "resi 374 & chain D & name N", "resi 276 & chain E & name O")
cmd.distance("StrongHBond", "resi 277 & chain E & name O", "resi 375 & chain E & name N")
cmd.distance("StrongHBond", "resi 277 & chain E & name N", "resi 375 & chain E & name O")
cmd.distance("StrongHBond", "resi 374 & chain E & name O", "resi 276 & chain F & name N")
cmd.distance("StrongHBond", "resi 374 & chain E & name N", "resi 276 & chain F & name O")
cmd.distance("StrongHBond", "resi 277 & chain F & name O", "resi 375 & chain F & name N")
cmd.distance("StrongHBond", "resi 277 & chain F & name N", "resi 375 & chain F & name O")
cmd.distance("StrongHBond", "resi 374 & chain F & name O", "resi 276 & chain G & name N")
cmd.distance("StrongHBond", "resi 374 & chain F & name N", "resi 276 & chain G & name O")
cmd.distance("StrongHBond", "resi 277 & chain G & name O", "resi 375 & chain G & name N")
cmd.distance("StrongHBond", "resi 277 & chain G & name N", "resi 375 & chain G & name O")
cmd.distance("StrongHBond", "resi 374 & chain G & name O", "resi 276 & chain H & name N")
cmd.distance("StrongHBond", "resi 374 & chain G & name N", "resi 276 & chain H & name O")
cmd.distance("StrongHBond", "resi 277 & chain H & name O", "resi 375 & chain H & name N")
cmd.distance("StrongHBond", "resi 277 & chain H & name N", "resi 375 & chain H & name O")
cmd.distance("StrongHBond", "resi 374 & chain H & name O", "resi 276 & chain I & name N")
cmd.distance("StrongHBond", "resi 374 & chain H & name N", "resi 276 & chain I & name O")
cmd.distance("StrongHBond", "resi 277 & chain I & name O", "resi 375 & chain I & name N")
cmd.distance("StrongHBond", "resi 277 & chain I & name N", "resi 375 & chain I & name O")
cmd.distance("StrongHBond", "resi 374 & chain I & name O", "resi 276 & chain J & name N")
cmd.distance("StrongHBond", "resi 374 & chain I & name N", "resi 276 & chain J & name O")
cmd.distance("StrongHBond", "resi 277 & chain J & name O", "resi 375 & chain J & name N")
cmd.distance("StrongHBond", "resi 277 & chain J & name N", "resi 375 & chain J & name O")
cmd.distance("StrongHBond", "resi 374 & chain J & name O", "resi 276 & chain K & name N")
cmd.distance("StrongHBond", "resi 374 & chain J & name N", "resi 276 & chain K & name O")
cmd.distance("StrongHBond", "resi 277 & chain K & name O", "resi 375 & chain K & name N")
cmd.distance("StrongHBond", "resi 277 & chain K & name N", "resi 375 & chain K & name O")
cmd.distance("StrongHBond", "resi 374 & chain K & name O", "resi 276 & chain L & name N")
cmd.distance("StrongHBond", "resi 374 & chain K & name N", "resi 276 & chain L & name O")
cmd.distance("StrongHBond", "resi 277 & chain L & name O", "resi 375 & chain L & name N")
cmd.distance("StrongHBond", "resi 277 & chain L & name N", "resi 375 & chain L & name O")
cmd.distance("StrongHBond", "resi 374 & chain L & name O", "resi 276 & chain M & name N")
cmd.distance("StrongHBond", "resi 374 & chain L & name N", "resi 276 & chain M & name O")
cmd.distance("StrongHBond", "resi 277 & chain M & name O", "resi 375 & chain M & name N")
cmd.distance("StrongHBond", "resi 277 & chain M & name N", "resi 375 & chain M & name O")
cmd.distance("StrongHBond", "resi 374 & chain M & name O", "resi 276 & chain N & name N")
cmd.distance("StrongHBond", "resi 374 & chain M & name N", "resi 276 & chain N & name O")
cmd.distance("StrongHBond", "resi 277 & chain N & name O", "resi 375 & chain N & name N")
cmd.distance("StrongHBond", "resi 277 & chain N & name N", "resi 375 & chain N & name O")
cmd.distance("StrongHBond", "resi 374 & chain N & name O", "resi 276 & chain O & name N")
cmd.distance("StrongHBond", "resi 374 & chain N & name N", "resi 276 & chain O & name O")
cmd.distance("StrongHBond", "resi 277 & chain O & name O", "resi 375 & chain O & name N")
cmd.distance("StrongHBond", "resi 277 & chain O & name N", "resi 375 & chain O & name O")
cmd.distance("StrongHBond", "resi 374 & chain O & name O", "resi 276 & chain P & name N")
cmd.distance("StrongHBond", "resi 374 & chain O & name N", "resi 276 & chain P & name O")
cmd.distance("StrongHBond", "resi 277 & chain P & name O", "resi 375 & chain P & name N")
cmd.distance("StrongHBond", "resi 277 & chain P & name N", "resi 375 & chain P & name O")
cmd.distance("StrongHBond", "resi 374 & chain P & name O", "resi 276 & chain Q & name N")
cmd.distance("StrongHBond", "resi 374 & chain P & name N", "resi 276 & chain Q & name O")
cmd.distance("StrongHBond", "resi 277 & chain Q & name O", "resi 375 & chain Q & name N")
cmd.distance("StrongHBond", "resi 277 & chain Q & name N", "resi 375 & chain Q & name O")
cmd.distance("StrongHBond", "resi 374 & chain Q & name O", "resi 276 & chain R & name N")
cmd.distance("StrongHBond", "resi 374 & chain Q & name N", "resi 276 & chain R & name O")
cmd.distance("StrongHBond", "resi 277 & chain R & name O", "resi 375 & chain R & name N")
cmd.distance("StrongHBond", "resi 277 & chain R & name N", "resi 375 & chain R & name O")
cmd.distance("StrongHBond", "resi 374 & chain R & name O", "resi 276 & chain S & name N")
cmd.distance("StrongHBond", "resi 374 & chain R & name N", "resi 276 & chain S & name O")
cmd.distance("StrongHBond", "resi 277 & chain S & name O", "resi 375 & chain S & name N")
cmd.distance("StrongHBond", "resi 277 & chain S & name N", "resi 375 & chain S & name O")
cmd.distance("StrongHBond", "resi 374 & chain S & name O", "resi 276 & chain T & name N")
cmd.distance("StrongHBond", "resi 374 & chain S & name N", "resi 276 & chain T & name O")
cmd.distance("StrongHBond", "resi 277 & chain T & name O", "resi 375 & chain T & name N")
cmd.distance("StrongHBond", "resi 277 & chain T & name N", "resi 375 & chain T & name O")
cmd.distance("StrongHBond", "resi 374 & chain T & name O", "resi 276 & chain U & name N")
cmd.distance("StrongHBond", "resi 374 & chain T & name N", "resi 276 & chain U & name O")
cmd.distance("StrongHBond", "resi 277 & chain U & name O", "resi 375 & chain U & name N")
cmd.distance("StrongHBond", "resi 277 & chain U & name N", "resi 375 & chain U & name O")
cmd.distance("StrongHBond", "resi 374 & chain U & name O", "resi 276 & chain V & name N")
cmd.distance("StrongHBond", "resi 374 & chain U & name N", "resi 276 & chain V & name O")
cmd.distance("StrongHBond", "resi 277 & chain V & name O", "resi 375 & chain V & name N")
cmd.distance("StrongHBond", "resi 277 & chain V & name N", "resi 375 & chain V & name O")
cmd.distance("StrongHBond", "resi 374 & chain V & name O", "resi 276 & chain W & name N")
cmd.distance("StrongHBond", "resi 374 & chain V & name N", "resi 276 & chain W & name O")
cmd.distance("StrongHBond", "resi 277 & chain W & name O", "resi 375 & chain W & name N")
cmd.distance("StrongHBond", "resi 277 & chain W & name N", "resi 375 & chain W & name O")
cmd.distance("StrongHBond", "resi 374 & chain W & name O", "resi 276 & chain X & name N")
cmd.distance("StrongHBond", "resi 374 & chain W & name N", "resi 276 & chain X & name O")
cmd.distance("StrongHBond", "resi 277 & chain X & name O", "resi 375 & chain X & name N")
cmd.distance("StrongHBond", "resi 277 & chain X & name N", "resi 375 & chain X & name O")
cmd.distance("StrongHBond", "resi 374 & chain X & name O", "resi 276 & chain Y & name N")
cmd.distance("StrongHBond", "resi 374 & chain X & name N", "resi 276 & chain Y & name O")
cmd.distance("StrongHBond", "resi 277 & chain Y & name O", "resi 375 & chain Y & name N")
cmd.distance("StrongHBond", "resi 277 & chain Y & name N", "resi 375 & chain Y & name O")
cmd.distance("StrongHBond", "resi 374 & chain Y & name O", "resi 276 & chain Z & name N")
cmd.distance("StrongHBond", "resi 374 & chain Y & name N", "resi 276 & chain Z & name O")
cmd.distance("StrongHBond", "resi 277 & chain Z & name O", "resi 375 & chain Z & name N")
cmd.distance("StrongHBond", "resi 277 & chain Z & name N", "resi 375 & chain Z & name O")
cmd.distance("StrongHBond", "resi 374 & chain Z & name O", "resi 276 & chain a & name N")
cmd.distance("StrongHBond", "resi 374 & chain Z & name N", "resi 276 & chain a & name O")
cmd.distance("WeakHBond", "resi 375 & chain a & name O", "PseudoH276a")
cmd.distance("WeakHBond", "resi 277 & chain a & name O", "PseudoH374a")
cmd.distance("WeakHBond", "resi 375 & chain b & name O", "PseudoH276b")
cmd.distance("WeakHBond", "resi 277 & chain b & name O", "PseudoH374b")
cmd.distance("WeakHBond", "resi 375 & chain c & name O", "PseudoH276c")
cmd.distance("WeakHBond", "resi 277 & chain c & name O", "PseudoH374c")
cmd.distance("WeakHBond", "resi 375 & chain d & name O", "PseudoH276d")
cmd.distance("WeakHBond", "resi 277 & chain d & name O", "PseudoH374d")
cmd.distance("WeakHBond", "resi 375 & chain e & name O", "PseudoH276e")
cmd.distance("WeakHBond", "resi 277 & chain e & name O", "PseudoH374e")
cmd.distance("WeakHBond", "resi 375 & chain f & name O", "PseudoH276f")
cmd.distance("WeakHBond", "resi 277 & chain f & name O", "PseudoH374f")
cmd.distance("WeakHBond", "resi 375 & chain g & name O", "PseudoH276g")
cmd.distance("WeakHBond", "resi 277 & chain g & name O", "PseudoH374g")
cmd.distance("WeakHBond", "resi 375 & chain A & name O", "PseudoH276A")
cmd.distance("WeakHBond", "resi 277 & chain A & name O", "PseudoH374A")
cmd.distance("WeakHBond", "resi 375 & chain B & name O", "PseudoH276B")
cmd.distance("WeakHBond", "resi 277 & chain B & name O", "PseudoH374B")
cmd.distance("WeakHBond", "resi 375 & chain C & name O", "PseudoH276C")
cmd.distance("WeakHBond", "resi 277 & chain C & name O", "PseudoH374C")
cmd.distance("WeakHBond", "resi 375 & chain D & name O", "PseudoH276D")
cmd.distance("WeakHBond", "resi 277 & chain D & name O", "PseudoH374D")
cmd.distance("WeakHBond", "resi 375 & chain E & name O", "PseudoH276E")
cmd.distance("WeakHBond", "resi 277 & chain E & name O", "PseudoH374E")
cmd.distance("WeakHBond", "resi 375 & chain F & name O", "PseudoH276F")
cmd.distance("WeakHBond", "resi 277 & chain F & name O", "PseudoH374F")
cmd.distance("WeakHBond", "resi 375 & chain G & name O", "PseudoH276G")
cmd.distance("WeakHBond", "resi 277 & chain G & name O", "PseudoH374G")
cmd.distance("WeakHBond", "resi 375 & chain H & name O", "PseudoH276H")
cmd.distance("WeakHBond", "resi 277 & chain H & name O", "PseudoH374H")
cmd.distance("WeakHBond", "resi 375 & chain I & name O", "PseudoH276I")
cmd.distance("WeakHBond", "resi 277 & chain I & name O", "PseudoH374I")
cmd.distance("WeakHBond", "resi 375 & chain J & name O", "PseudoH276J")
cmd.distance("WeakHBond", "resi 277 & chain J & name O", "PseudoH374J")
cmd.distance("WeakHBond", "resi 375 & chain K & name O", "PseudoH276K")
cmd.distance("WeakHBond", "resi 277 & chain K & name O", "PseudoH374K")
cmd.distance("WeakHBond", "resi 375 & chain L & name O", "PseudoH276L")
cmd.distance("WeakHBond", "resi 277 & chain L & name O", "PseudoH374L")
cmd.distance("WeakHBond", "resi 375 & chain M & name O", "PseudoH276M")
cmd.distance("WeakHBond", "resi 277 & chain M & name O", "PseudoH374M")
cmd.distance("WeakHBond", "resi 375 & chain N & name O", "PseudoH276N")
cmd.distance("WeakHBond", "resi 277 & chain N & name O", "PseudoH374N")
cmd.distance("WeakHBond", "resi 375 & chain O & name O", "PseudoH276O")
cmd.distance("WeakHBond", "resi 277 & chain O & name O", "PseudoH374O")
cmd.distance("WeakHBond", "resi 375 & chain P & name O", "PseudoH276P")
cmd.distance("WeakHBond", "resi 277 & chain P & name O", "PseudoH374P")
cmd.distance("WeakHBond", "resi 375 & chain Q & name O", "PseudoH276Q")
cmd.distance("WeakHBond", "resi 277 & chain Q & name O", "PseudoH374Q")
cmd.distance("WeakHBond", "resi 375 & chain R & name O", "PseudoH276R")
cmd.distance("WeakHBond", "resi 277 & chain R & name O", "PseudoH374R")
cmd.distance("WeakHBond", "resi 375 & chain S & name O", "PseudoH276S")
cmd.distance("WeakHBond", "resi 277 & chain S & name O", "PseudoH374S")
cmd.distance("WeakHBond", "resi 375 & chain T & name O", "PseudoH276T")
cmd.distance("WeakHBond", "resi 277 & chain T & name O", "PseudoH374T")
cmd.distance("WeakHBond", "resi 375 & chain U & name O", "PseudoH276U")
cmd.distance("WeakHBond", "resi 277 & chain U & name O", "PseudoH374U")
cmd.distance("WeakHBond", "resi 375 & chain V & name O", "PseudoH276V")
cmd.distance("WeakHBond", "resi 277 & chain V & name O", "PseudoH374V")
cmd.distance("WeakHBond", "resi 375 & chain W & name O", "PseudoH276W")
cmd.distance("WeakHBond", "resi 277 & chain W & name O", "PseudoH374W")
cmd.distance("WeakHBond", "resi 375 & chain X & name O", "PseudoH276X")
cmd.distance("WeakHBond", "resi 277 & chain X & name O", "PseudoH374X")
cmd.distance("WeakHBond", "resi 375 & chain Y & name O", "PseudoH276Y")
cmd.distance("WeakHBond", "resi 277 & chain Y & name O", "PseudoH374Y")
cmd.distance("WeakHBond", "resi 375 & chain Z & name O", "PseudoH276Z")
cmd.distance("WeakHBond", "resi 277 & chain Z & name O", "PseudoH374Z")
cmd.distance("NonHBond", "resi 276 & chain a & name CB", "resi 376 & chain a & name CB")
cmd.distance("NonHBond", "resi 278 & chain a & name CB", "resi 374 & chain a & name CB")
cmd.distance("NonHBond", "resi 276 & chain b & name CB", "resi 376 & chain b & name CB")
cmd.distance("NonHBond", "resi 278 & chain b & name CB", "resi 374 & chain b & name CB")
cmd.distance("NonHBond", "resi 276 & chain c & name CB", "resi 376 & chain c & name CB")
cmd.distance("NonHBond", "resi 278 & chain c & name CB", "resi 374 & chain c & name CB")
cmd.distance("NonHBond", "resi 276 & chain d & name CB", "resi 376 & chain d & name CB")
cmd.distance("NonHBond", "resi 278 & chain d & name CB", "resi 374 & chain d & name CB")
cmd.distance("NonHBond", "resi 276 & chain e & name CB", "resi 376 & chain e & name CB")
cmd.distance("NonHBond", "resi 278 & chain e & name CB", "resi 374 & chain e & name CB")
cmd.distance("NonHBond", "resi 276 & chain f & name CB", "resi 376 & chain f & name CB")
cmd.distance("NonHBond", "resi 278 & chain f & name CB", "resi 374 & chain f & name CB")
cmd.distance("NonHBond", "resi 276 & chain g & name CB", "resi 376 & chain g & name CB")
cmd.distance("NonHBond", "resi 278 & chain g & name CB", "resi 374 & chain g & name CB")
cmd.distance("NonHBond", "resi 276 & chain A & name CB", "resi 376 & chain A & name CB")
cmd.distance("NonHBond", "resi 278 & chain A & name CB", "resi 374 & chain A & name CB")
cmd.distance("NonHBond", "resi 276 & chain B & name CB", "resi 376 & chain B & name CB")
cmd.distance("NonHBond", "resi 278 & chain B & name CB", "resi 374 & chain B & name CB")
cmd.distance("NonHBond", "resi 276 & chain C & name CB", "resi 376 & chain C & name CB")
cmd.distance("NonHBond", "resi 278 & chain C & name CB", "resi 374 & chain C & name CB")
cmd.distance("NonHBond", "resi 276 & chain D & name CB", "resi 376 & chain D & name CB")
cmd.distance("NonHBond", "resi 278 & chain D & name CB", "resi 374 & chain D & name CB")
cmd.distance("NonHBond", "resi 276 & chain E & name CB", "resi 376 & chain E & name CB")
cmd.distance("NonHBond", "resi 278 & chain E & name CB", "resi 374 & chain E & name CB")
cmd.distance("NonHBond", "resi 276 & chain F & name CB", "resi 376 & chain F & name CB")
cmd.distance("NonHBond", "resi 278 & chain F & name CB", "resi 374 & chain F & name CB")
cmd.distance("NonHBond", "resi 276 & chain G & name CB", "resi 376 & chain G & name CB")
cmd.distance("NonHBond", "resi 278 & chain G & name CB", "resi 374 & chain G & name CB")
cmd.distance("NonHBond", "resi 276 & chain H & name CB", "resi 376 & chain H & name CB")
cmd.distance("NonHBond", "resi 278 & chain H & name CB", "resi 374 & chain H & name CB")
cmd.distance("NonHBond", "resi 276 & chain I & name CB", "resi 376 & chain I & name CB")
cmd.distance("NonHBond", "resi 278 & chain I & name CB", "resi 374 & chain I & name CB")
cmd.distance("NonHBond", "resi 276 & chain J & name CB", "resi 376 & chain J & name CB")
cmd.distance("NonHBond", "resi 278 & chain J & name CB", "resi 374 & chain J & name CB")
cmd.distance("NonHBond", "resi 276 & chain K & name CB", "resi 376 & chain K & name CB")
cmd.distance("NonHBond", "resi 278 & chain K & name CB", "resi 374 & chain K & name CB")
cmd.distance("NonHBond", "resi 276 & chain L & name CB", "resi 376 & chain L & name CB")
cmd.distance("NonHBond", "resi 278 & chain L & name CB", "resi 374 & chain L & name CB")
cmd.distance("NonHBond", "resi 276 & chain M & name CB", "resi 376 & chain M & name CB")
cmd.distance("NonHBond", "resi 278 & chain M & name CB", "resi 374 & chain M & name CB")
cmd.distance("NonHBond", "resi 276 & chain N & name CB", "resi 376 & chain N & name CB")
cmd.distance("NonHBond", "resi 278 & chain N & name CB", "resi 374 & chain N & name CB")
cmd.distance("NonHBond", "resi 276 & chain O & name CB", "resi 376 & chain O & name CB")
cmd.distance("NonHBond", "resi 278 & chain O & name CB", "resi 374 & chain O & name CB")
cmd.distance("NonHBond", "resi 276 & chain P & name CB", "resi 376 & chain P & name CB")
cmd.distance("NonHBond", "resi 278 & chain P & name CB", "resi 374 & chain P & name CB")
cmd.distance("NonHBond", "resi 276 & chain Q & name CB", "resi 376 & chain Q & name CB")
cmd.distance("NonHBond", "resi 278 & chain Q & name CB", "resi 374 & chain Q & name CB")
cmd.distance("NonHBond", "resi 276 & chain R & name CB", "resi 376 & chain R & name CB")
cmd.distance("NonHBond", "resi 278 & chain R & name CB", "resi 374 & chain R & name CB")
cmd.distance("NonHBond", "resi 276 & chain S & name CB", "resi 376 & chain S & name CB")
cmd.distance("NonHBond", "resi 278 & chain S & name CB", "resi 374 & chain S & name CB")
cmd.distance("NonHBond", "resi 276 & chain T & name CB", "resi 376 & chain T & name CB")
cmd.distance("NonHBond", "resi 278 & chain T & name CB", "resi 374 & chain T & name CB")
cmd.distance("NonHBond", "resi 276 & chain U & name CB", "resi 376 & chain U & name CB")
cmd.distance("NonHBond", "resi 278 & chain U & name CB", "resi 374 & chain U & name CB")
cmd.distance("NonHBond", "resi 276 & chain V & name CB", "resi 376 & chain V & name CB")
cmd.distance("NonHBond", "resi 278 & chain V & name CB", "resi 374 & chain V & name CB")
cmd.distance("NonHBond", "resi 276 & chain W & name CB", "resi 376 & chain W & name CB")
cmd.distance("NonHBond", "resi 278 & chain W & name CB", "resi 374 & chain W & name CB")
cmd.distance("NonHBond", "resi 276 & chain X & name CB", "resi 376 & chain X & name CB")
cmd.distance("NonHBond", "resi 278 & chain X & name CB", "resi 374 & chain X & name CB")
cmd.distance("NonHBond", "resi 276 & chain Y & name CB", "resi 376 & chain Y & name CB")
cmd.distance("NonHBond", "resi 278 & chain Y & name CB", "resi 374 & chain Y & name CB")
cmd.distance("NonHBond", "resi 276 & chain Z & name CB", "resi 376 & chain Z & name CB")
cmd.distance("NonHBond", "resi 278 & chain Z & name CB", "resi 374 & chain Z & name CB")
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
