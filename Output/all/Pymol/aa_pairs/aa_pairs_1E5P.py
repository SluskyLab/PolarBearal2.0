from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1E5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Bstrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19 & chain B ")


cmd.select("Bstrand1", "resi 44+45+46+47+48+49+50+51+52+53 & chain B ")


cmd.select("Bstrand2", "resi 35+36+37+38+39 & chain B ")


cmd.select("Bstrand3", "resi 56+57+58+59+60+61+62+63+64+65+66+67 & chain B ")


cmd.select("Bstrand4", "resi 71+72+73+74+75+76 & chain B ")


cmd.select("Bstrand5", "resi 79+80+81+82+83 & chain B ")


cmd.select("Bstrand6", "resi 91+92+93+94+95+96+97+98+99+100 & chain B ")


cmd.select("Bstrand7", "resi 105+106+107+108+109+110+111+112+113 & chain B ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Bstrand*")
cmd.pseudoatom ("PseudoH38B", pos=[-47.364307,52.370777,12.058073])
cmd.pseudoatom ("PseudoH45B", pos=[-47.423782,54.607323,13.449494])
cmd.pseudoatom ("PseudoH36B", pos=[-46.058784,51.757046,18.321697])
cmd.pseudoatom ("PseudoH47B", pos=[-47.08716,53.700882,19.78231])
cmd.pseudoatom ("PseudoH64B", pos=[-47.78214,61.548454,15.239614])
cmd.pseudoatom ("PseudoH72B", pos=[-43.794422,62.65772,11.665726])
cmd.pseudoatom ("PseudoH66B", pos=[-44.253315,61.385956,9.519692])
cmd.pseudoatom ("PseudoH71B", pos=[-39.342567,62.766262,11.263312])
cmd.pseudoatom ("PseudoH81B", pos=[-42.07736,66.06822,15.512665])
cmd.pseudoatom ("PseudoH73B", pos=[-44.642033,65.50973,15.010231])
cmd.pseudoatom ("PseudoH79B", pos=[-46.784195,69.035194,19.686617])
cmd.pseudoatom ("PseudoH98B", pos=[-41.67035,68.80708,21.477911])
cmd.pseudoatom ("PseudoH80B", pos=[-42.66408,67.57032,19.704464])
cmd.pseudoatom ("PseudoH96B", pos=[-38.091946,64.27178,18.631851])
cmd.pseudoatom ("PseudoH82B", pos=[-38.707153,63.581284,16.72185])
cmd.pseudoatom ("PseudoH94B", pos=[-35.175064,58.166443,17.462582])
cmd.pseudoatom ("PseudoH91B", pos=[-33.934437,48.730026,20.640333])
cmd.pseudoatom ("PseudoH111B", pos=[-33.768776,54.598408,22.320097])
cmd.pseudoatom ("PseudoH93B", pos=[-32.986347,55.4295,20.055954])
cmd.pseudoatom ("PseudoH109B", pos=[-33.65912,61.15937,21.811913])
cmd.pseudoatom ("PseudoH95B", pos=[-34.33883,62.10511,19.629944])
cmd.pseudoatom ("PseudoH107B", pos=[-35.091106,68.137054,21.981611])
cmd.pseudoatom ("PseudoH97B", pos=[-37.42423,68.225464,20.732376])
cmd.pseudoatom ("PseudoH105B", pos=[-39.170197,73.29413,23.305561])
cmd.pseudoatom ("PseudoH17B", pos=[-33.10721,65.62936,26.400023])
cmd.pseudoatom ("PseudoH108B", pos=[-33.77849,64.84332,24.514133])
cmd.pseudoatom ("PseudoH15B", pos=[-34.40623,58.88811,26.924574])
cmd.pseudoatom ("PseudoH110B", pos=[-34.98168,58.12444,24.691668])
cmd.pseudoatom ("PseudoH12B", pos=[-37.89256,52.95147,26.248499])
cmd.pseudoatom ("PseudoH112B", pos=[-36.923275,51.97244,24.048391])
cmd.pseudoatom ("PseudoH10B", pos=[-40.097374,47.378468,22.89039])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR64B", pos=[-46.668427,60.13239,15.250206])
cmd.pseudoatom ("PseudoR113B", pos=[-34.771484,48.210167,24.0585])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 44 & chain B & name O", "resi 39 & chain B & name N")
cmd.distance("StrongHBond", "resi 44 & chain B & name N", "resi 39 & chain B & name O")
cmd.distance("StrongHBond", "resi 46 & chain B & name O", "resi 37 & chain B & name N")
cmd.distance("StrongHBond", "resi 46 & chain B & name N", "resi 37 & chain B & name O")
cmd.distance("StrongHBond", "resi 48 & chain B & name O", "resi 35 & chain B & name N")
cmd.distance("StrongHBond", "resi 48 & chain B & name N", "resi 35 & chain B & name O")
cmd.distance("StrongHBond", "resi 65 & chain B & name O", "resi 73 & chain B & name N")
cmd.distance("StrongHBond", "resi 65 & chain B & name N", "resi 73 & chain B & name O")
cmd.distance("StrongHBond", "resi 72 & chain B & name O", "resi 82 & chain B & name N")
cmd.distance("StrongHBond", "resi 72 & chain B & name N", "resi 82 & chain B & name O")
cmd.distance("StrongHBond", "resi 74 & chain B & name O", "resi 80 & chain B & name N")
cmd.distance("StrongHBond", "resi 74 & chain B & name N", "resi 80 & chain B & name O")
cmd.distance("StrongHBond", "resi 79 & chain B & name O", "resi 99 & chain B & name N")
cmd.distance("StrongHBond", "resi 79 & chain B & name N", "resi 99 & chain B & name O")
cmd.distance("StrongHBond", "resi 81 & chain B & name O", "resi 97 & chain B & name N")
cmd.distance("StrongHBond", "resi 81 & chain B & name N", "resi 97 & chain B & name O")
cmd.distance("StrongHBond", "resi 83 & chain B & name O", "resi 95 & chain B & name N")
cmd.distance("StrongHBond", "resi 83 & chain B & name N", "resi 95 & chain B & name O")
cmd.distance("StrongHBond", "resi 92 & chain B & name O", "resi 112 & chain B & name N")
cmd.distance("StrongHBond", "resi 92 & chain B & name N", "resi 112 & chain B & name O")
cmd.distance("StrongHBond", "resi 94 & chain B & name O", "resi 110 & chain B & name N")
cmd.distance("StrongHBond", "resi 94 & chain B & name N", "resi 110 & chain B & name O")
cmd.distance("StrongHBond", "resi 96 & chain B & name O", "resi 108 & chain B & name N")
cmd.distance("StrongHBond", "resi 96 & chain B & name N", "resi 108 & chain B & name O")
cmd.distance("StrongHBond", "resi 98 & chain B & name O", "resi 106 & chain B & name N")
cmd.distance("StrongHBond", "resi 98 & chain B & name N", "resi 106 & chain B & name O")
cmd.distance("StrongHBond", "resi 109 & chain B & name O", "resi 16 & chain B & name N")
cmd.distance("StrongHBond", "resi 109 & chain B & name N", "resi 16 & chain B & name O")
cmd.distance("StrongHBond", "resi 111 & chain B & name O", "resi 14 & chain B & name N")
cmd.distance("StrongHBond", "resi 111 & chain B & name N", "resi 14 & chain B & name O")
cmd.distance("StrongHBond", "resi 113 & chain B & name O", "resi 11 & chain B & name N")
cmd.distance("StrongHBond", "resi 113 & chain B & name N", "resi 11 & chain B & name O")
cmd.distance("WeakHBond", "resi 44 & chain B & name O", "PseudoH38B")
cmd.distance("WeakHBond", "resi 37 & chain B & name O", "PseudoH45B")
cmd.distance("WeakHBond", "resi 46 & chain B & name O", "PseudoH36B")
cmd.distance("WeakHBond", "resi 35 & chain B & name O", "PseudoH47B")
cmd.distance("WeakHBond", "resi 73 & chain B & name O", "PseudoH64B")
cmd.distance("WeakHBond", "resi 65 & chain B & name O", "PseudoH72B")
cmd.distance("WeakHBond", "resi 71 & chain B & name O", "PseudoH66B")
cmd.distance("WeakHBond", "resi 82 & chain B & name O", "PseudoH71B")
cmd.distance("WeakHBond", "resi 72 & chain B & name O", "PseudoH81B")
cmd.distance("WeakHBond", "resi 80 & chain B & name O", "PseudoH73B")
cmd.distance("WeakHBond", "resi 74 & chain B & name O", "PseudoH79B")
cmd.distance("WeakHBond", "resi 79 & chain B & name O", "PseudoH98B")
cmd.distance("WeakHBond", "resi 97 & chain B & name O", "PseudoH80B")
cmd.distance("WeakHBond", "resi 81 & chain B & name O", "PseudoH96B")
cmd.distance("WeakHBond", "resi 95 & chain B & name O", "PseudoH82B")
cmd.distance("WeakHBond", "resi 83 & chain B & name O", "PseudoH94B")
cmd.distance("WeakHBond", "resi 112 & chain B & name O", "PseudoH91B")
cmd.distance("WeakHBond", "resi 92 & chain B & name O", "PseudoH111B")
cmd.distance("WeakHBond", "resi 110 & chain B & name O", "PseudoH93B")
cmd.distance("WeakHBond", "resi 94 & chain B & name O", "PseudoH109B")
cmd.distance("WeakHBond", "resi 108 & chain B & name O", "PseudoH95B")
cmd.distance("WeakHBond", "resi 96 & chain B & name O", "PseudoH107B")
cmd.distance("WeakHBond", "resi 106 & chain B & name O", "PseudoH97B")
cmd.distance("WeakHBond", "resi 98 & chain B & name O", "PseudoH105B")
cmd.distance("WeakHBond", "resi 107 & chain B & name O", "PseudoH17B")
cmd.distance("WeakHBond", "resi 16 & chain B & name O", "PseudoH108B")
cmd.distance("WeakHBond", "resi 109 & chain B & name O", "PseudoH15B")
cmd.distance("WeakHBond", "resi 14 & chain B & name O", "PseudoH110B")
cmd.distance("WeakHBond", "resi 111 & chain B & name O", "PseudoH12B")
cmd.distance("WeakHBond", "resi 11 & chain B & name O", "PseudoH112B")
cmd.distance("WeakHBond", "resi 113 & chain B & name O", "PseudoH10B")
cmd.distance("NonHBond", "resi 45 & chain B & name CB", "resi 38 & chain B & name CB")
cmd.distance("NonHBond", "resi 47 & chain B & name CB", "resi 36 & chain B & name CB")
cmd.distance("NonHBond", "PseudoR64B", "resi 74 & chain B & name CB")
cmd.distance("NonHBond", "resi 66 & chain B & name CB", "resi 72 & chain B & name CB")
cmd.distance("NonHBond", "resi 73 & chain B & name CB", "resi 81 & chain B & name CB")
cmd.distance("NonHBond", "resi 75 & chain B & name CB", "resi 79 & chain B & name CB")
cmd.distance("NonHBond", "resi 80 & chain B & name CB", "resi 98 & chain B & name CB")
cmd.distance("NonHBond", "resi 82 & chain B & name CB", "resi 96 & chain B & name CB")
cmd.distance("NonHBond", "resi 91 & chain B & name CB", "PseudoR113B")
cmd.distance("NonHBond", "resi 93 & chain B & name CB", "resi 111 & chain B & name CB")
cmd.distance("NonHBond", "resi 95 & chain B & name CB", "resi 109 & chain B & name CB")
cmd.distance("NonHBond", "resi 97 & chain B & name CB", "resi 107 & chain B & name CB")
cmd.distance("NonHBond", "resi 99 & chain B & name CB", "resi 105 & chain B & name CB")
cmd.distance("NonHBond", "resi 108 & chain B & name CB", "resi 17 & chain B & name CB")
cmd.distance("NonHBond", "resi 110 & chain B & name CB", "resi 15 & chain B & name CB")
cmd.distance("NonHBond", "resi 112 & chain B & name CB", "resi 12 & chain B & name CB")
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
