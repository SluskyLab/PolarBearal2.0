from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Z6J.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 18+19+20+21+22 & chain A ")


cmd.select("Astrand1", "resi 27+28+29+30+31+32+33+34 & chain A ")


cmd.select("Astrand2", "resi 41+42+43+44+45+46+47+48+49 & chain A ")


cmd.select("Astrand3", "resi 61+62+63+64+65+66+67+68+69 & chain A ")


cmd.select("Astrand4", "resi 74+75+76+77+78+79+80+81+82 & chain A ")


cmd.select("Astrand5", "resi 87+88+89+90+91+92+93+94+95+96+97+98+99 & chain A ")


cmd.select("Astrand6", "resi 106+107+108+109+110+111+112+113+114+115+116+117 & chain A ")


cmd.select("Astrand7", "resi 120+121+122+123+124+125+126+127+128+129+130+131+132 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH29A", pos=[17.607851,16.05868,13.586087])
cmd.pseudoatom ("PseudoH19A", pos=[19.34504,16.67361,11.486045])
cmd.pseudoatom ("PseudoH27A", pos=[21.916874,20.631,15.072395])
cmd.pseudoatom ("PseudoH48A", pos=[18.53915,18.697819,19.147697])
cmd.pseudoatom ("PseudoH28A", pos=[18.117811,19.14703,16.75287])
cmd.pseudoatom ("PseudoH30A", pos=[13.337388,16.302021,14.673726])
cmd.pseudoatom ("PseudoH44A", pos=[7.8954535,16.409777,14.965738])
cmd.pseudoatom ("PseudoH32A", pos=[7.5850887,14.635388,12.703071])
cmd.pseudoatom ("PseudoH42A", pos=[2.2054677,15.769009,11.859947])
cmd.pseudoatom ("PseudoH34A", pos=[1.6783447,13.749669,10.344291])
cmd.pseudoatom ("PseudoH41A", pos=[1.0059594,19.578726,10.201758])
cmd.pseudoatom ("PseudoH67A", pos=[4.023506,19.496223,15.544664])
cmd.pseudoatom ("PseudoH43A", pos=[3.687261,16.98477,15.889706])
cmd.pseudoatom ("PseudoH65A", pos=[8.125697,17.243626,20.426535])
cmd.pseudoatom ("PseudoH45A", pos=[9.672359,15.034489,18.80292])
cmd.pseudoatom ("PseudoH63A", pos=[14.563974,14.888339,22.553753])
cmd.pseudoatom ("PseudoH47A", pos=[16.011509,15.355353,20.7289])
cmd.pseudoatom ("PseudoH61A", pos=[20.675283,15.49294,22.768036])
cmd.pseudoatom ("PseudoH79A", pos=[12.784886,20.424667,24.695206])
cmd.pseudoatom ("PseudoH64A", pos=[12.007723,18.516184,22.40978])
cmd.pseudoatom ("PseudoH77A", pos=[8.145084,22.487574,19.136444])
cmd.pseudoatom ("PseudoH75A", pos=[6.316987,24.129766,12.943644])
cmd.pseudoatom ("PseudoH68A", pos=[5.23282,22.244032,12.193517])
cmd.pseudoatom ("PseudoH74A", pos=[6.94657,26.97294,9.553165])
cmd.pseudoatom ("PseudoH95A", pos=[8.484314,28.123749,16.140676])
cmd.pseudoatom ("PseudoH76A", pos=[7.9617343,26.098331,16.647738])
cmd.pseudoatom ("PseudoH93A", pos=[10.3404,26.222944,22.33814])
cmd.pseudoatom ("PseudoH78A", pos=[10.685041,23.906345,22.473783])
cmd.pseudoatom ("PseudoH91A", pos=[13.339054,24.530972,28.332754])
cmd.pseudoatom ("PseudoH80A", pos=[13.147247,22.20388,28.748293])
cmd.pseudoatom ("PseudoH87A", pos=[19.253378,19.74751,33.252327])
cmd.pseudoatom ("PseudoH90A", pos=[14.144557,26.424047,32.407436])
cmd.pseudoatom ("PseudoH113A", pos=[13.43609,29.829666,26.844666])
cmd.pseudoatom ("PseudoH92A", pos=[13.239293,27.824337,25.391657])
cmd.pseudoatom ("PseudoH111A", pos=[12.098067,31.107056,20.045416])
cmd.pseudoatom ("PseudoH94A", pos=[11.782446,28.864191,18.996902])
cmd.pseudoatom ("PseudoH109A", pos=[12.4525795,30.569403,13.577167])
cmd.pseudoatom ("PseudoH107A", pos=[14.1363535,27.100363,8.244358])
cmd.pseudoatom ("PseudoH98A", pos=[12.589564,26.831463,6.842394])
cmd.pseudoatom ("PseudoH106A", pos=[18.080837,26.208961,6.18123])
cmd.pseudoatom ("PseudoH129A", pos=[17.878485,29.71287,11.56191])
cmd.pseudoatom ("PseudoH108A", pos=[15.761626,30.396006,10.742307])
cmd.pseudoatom ("PseudoH127A", pos=[16.012917,33.59772,16.842806])
cmd.pseudoatom ("PseudoH110A", pos=[13.727742,33.58806,16.814])
cmd.pseudoatom ("PseudoH125A", pos=[13.91237,35.00241,23.465054])
cmd.pseudoatom ("PseudoH112A", pos=[12.5376625,33.173637,24.089674])
cmd.pseudoatom ("PseudoH123A", pos=[12.59914,33.948856,29.795427])
cmd.pseudoatom ("PseudoH114A", pos=[11.839948,31.588665,30.70842])
cmd.pseudoatom ("PseudoH121A", pos=[13.095233,33.58894,36.621685])
cmd.pseudoatom ("PseudoH22A", pos=[21.786999,26.581545,12.66453])
cmd.pseudoatom ("PseudoH130A", pos=[20.387085,26.1171,11.419602])
cmd.pseudoatom ("PseudoH20A", pos=[19.854221,20.886942,9.90917])
cmd.pseudoatom ("PseudoH132A", pos=[19.75471,20.560091,7.601308])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR66A", pos=[7.073125,20.876497,18.276686])
cmd.pseudoatom ("PseudoR93A", pos=[9.550547,27.710995,22.92432])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 18 & chain A & name O", "resi 30 & chain A & name N")
cmd.distance("StrongHBond", "resi 18 & chain A & name N", "resi 30 & chain A & name O")
cmd.distance("StrongHBond", "resi 20 & chain A & name O", "resi 28 & chain A & name N")
cmd.distance("StrongHBond", "resi 20 & chain A & name N", "resi 28 & chain A & name O")
cmd.distance("StrongHBond", "resi 27 & chain A & name O", "resi 49 & chain A & name N")
cmd.distance("StrongHBond", "resi 27 & chain A & name N", "resi 49 & chain A & name O")
cmd.distance("StrongHBond", "resi 29 & chain A & name O", "resi 47 & chain A & name N")
cmd.distance("StrongHBond", "resi 29 & chain A & name N", "resi 47 & chain A & name O")
cmd.distance("StrongHBond", "resi 31 & chain A & name O", "resi 45 & chain A & name N")
cmd.distance("StrongHBond", "resi 31 & chain A & name N", "resi 45 & chain A & name O")
cmd.distance("StrongHBond", "resi 33 & chain A & name O", "resi 43 & chain A & name N")
cmd.distance("StrongHBond", "resi 33 & chain A & name N", "resi 43 & chain A & name O")
cmd.distance("StrongHBond", "resi 42 & chain A & name O", "resi 68 & chain A & name N")
cmd.distance("StrongHBond", "resi 42 & chain A & name N", "resi 68 & chain A & name O")
cmd.distance("StrongHBond", "resi 44 & chain A & name O", "resi 66 & chain A & name N")
cmd.distance("StrongHBond", "resi 44 & chain A & name N", "resi 66 & chain A & name O")
cmd.distance("StrongHBond", "resi 48 & chain A & name O", "resi 62 & chain A & name N")
cmd.distance("StrongHBond", "resi 48 & chain A & name N", "resi 62 & chain A & name O")
cmd.distance("StrongHBond", "resi 65 & chain A & name O", "resi 78 & chain A & name N")
cmd.distance("StrongHBond", "resi 65 & chain A & name N", "resi 78 & chain A & name O")
cmd.distance("StrongHBond", "resi 67 & chain A & name O", "resi 76 & chain A & name N")
cmd.distance("StrongHBond", "resi 67 & chain A & name N", "resi 76 & chain A & name O")
cmd.distance("StrongHBond", "resi 69 & chain A & name O", "resi 74 & chain A & name N")
cmd.distance("StrongHBond", "resi 69 & chain A & name N", "resi 74 & chain A & name O")
cmd.distance("StrongHBond", "resi 75 & chain A & name O", "resi 96 & chain A & name N")
cmd.distance("StrongHBond", "resi 75 & chain A & name N", "resi 96 & chain A & name O")
cmd.distance("StrongHBond", "resi 77 & chain A & name O", "resi 94 & chain A & name N")
cmd.distance("StrongHBond", "resi 77 & chain A & name N", "resi 94 & chain A & name O")
cmd.distance("StrongHBond", "resi 79 & chain A & name O", "resi 92 & chain A & name N")
cmd.distance("StrongHBond", "resi 79 & chain A & name N", "resi 92 & chain A & name O")
cmd.distance("StrongHBond", "resi 91 & chain A & name O", "resi 114 & chain A & name N")
cmd.distance("StrongHBond", "resi 91 & chain A & name N", "resi 114 & chain A & name O")
cmd.distance("StrongHBond", "resi 93 & chain A & name O", "resi 112 & chain A & name N")
cmd.distance("StrongHBond", "resi 93 & chain A & name N", "resi 112 & chain A & name O")
cmd.distance("StrongHBond", "resi 95 & chain A & name O", "resi 110 & chain A & name N")
cmd.distance("StrongHBond", "resi 95 & chain A & name N", "resi 110 & chain A & name O")
cmd.distance("StrongHBond", "resi 97 & chain A & name O", "resi 108 & chain A & name N")
cmd.distance("StrongHBond", "resi 97 & chain A & name N", "resi 108 & chain A & name O")
cmd.distance("StrongHBond", "resi 99 & chain A & name O", "resi 106 & chain A & name N")
cmd.distance("StrongHBond", "resi 99 & chain A & name N", "resi 106 & chain A & name O")
cmd.distance("StrongHBond", "resi 107 & chain A & name O", "resi 130 & chain A & name N")
cmd.distance("StrongHBond", "resi 107 & chain A & name N", "resi 130 & chain A & name O")
cmd.distance("StrongHBond", "resi 109 & chain A & name O", "resi 128 & chain A & name N")
cmd.distance("StrongHBond", "resi 109 & chain A & name N", "resi 128 & chain A & name O")
cmd.distance("StrongHBond", "resi 111 & chain A & name O", "resi 126 & chain A & name N")
cmd.distance("StrongHBond", "resi 111 & chain A & name N", "resi 126 & chain A & name O")
cmd.distance("StrongHBond", "resi 113 & chain A & name O", "resi 124 & chain A & name N")
cmd.distance("StrongHBond", "resi 113 & chain A & name N", "resi 124 & chain A & name O")
cmd.distance("StrongHBond", "resi 115 & chain A & name O", "resi 122 & chain A & name N")
cmd.distance("StrongHBond", "resi 115 & chain A & name N", "resi 122 & chain A & name O")
cmd.distance("StrongHBond", "resi 117 & chain A & name O", "resi 120 & chain A & name N")
cmd.distance("StrongHBond", "resi 117 & chain A & name N", "resi 120 & chain A & name O")
cmd.distance("StrongHBond", "resi 131 & chain A & name O", "resi 21 & chain A & name N")
cmd.distance("StrongHBond", "resi 131 & chain A & name N", "resi 21 & chain A & name O")
cmd.distance("WeakHBond", "resi 18 & chain A & name O", "PseudoH29A")
cmd.distance("WeakHBond", "resi 28 & chain A & name O", "PseudoH19A")
cmd.distance("WeakHBond", "resi 20 & chain A & name O", "PseudoH27A")
cmd.distance("WeakHBond", "resi 27 & chain A & name O", "PseudoH48A")
cmd.distance("WeakHBond", "resi 47 & chain A & name O", "PseudoH28A")
cmd.distance("WeakHBond", "resi 45 & chain A & name O", "PseudoH30A")
cmd.distance("WeakHBond", "resi 31 & chain A & name O", "PseudoH44A")
cmd.distance("WeakHBond", "resi 43 & chain A & name O", "PseudoH32A")
cmd.distance("WeakHBond", "resi 33 & chain A & name O", "PseudoH42A")
cmd.distance("WeakHBond", "resi 41 & chain A & name O", "PseudoH34A")
cmd.distance("WeakHBond", "resi 68 & chain A & name O", "PseudoH41A")
cmd.distance("WeakHBond", "resi 42 & chain A & name O", "PseudoH67A")
cmd.distance("WeakHBond", "resi 66 & chain A & name O", "PseudoH43A")
cmd.distance("WeakHBond", "resi 44 & chain A & name O", "PseudoH65A")
cmd.distance("WeakHBond", "resi 64 & chain A & name O", "PseudoH45A")
cmd.distance("WeakHBond", "resi 46 & chain A & name O", "PseudoH63A")
cmd.distance("WeakHBond", "resi 62 & chain A & name O", "PseudoH47A")
cmd.distance("WeakHBond", "resi 48 & chain A & name O", "PseudoH61A")
cmd.distance("WeakHBond", "resi 63 & chain A & name O", "PseudoH79A")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH64A")
cmd.distance("WeakHBond", "resi 65 & chain A & name O", "PseudoH77A")
cmd.distance("WeakHBond", "resi 67 & chain A & name O", "PseudoH75A")
cmd.distance("WeakHBond", "resi 74 & chain A & name O", "PseudoH68A")
cmd.distance("WeakHBond", "resi 96 & chain A & name O", "PseudoH74A")
cmd.distance("WeakHBond", "resi 75 & chain A & name O", "PseudoH95A")
cmd.distance("WeakHBond", "resi 94 & chain A & name O", "PseudoH76A")
cmd.distance("WeakHBond", "resi 77 & chain A & name O", "PseudoH93A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH78A")
cmd.distance("WeakHBond", "resi 79 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH80A")
cmd.distance("WeakHBond", "resi 81 & chain A & name O", "PseudoH87A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH113A")
cmd.distance("WeakHBond", "resi 112 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH111A")
cmd.distance("WeakHBond", "resi 110 & chain A & name O", "PseudoH94A")
cmd.distance("WeakHBond", "resi 95 & chain A & name O", "PseudoH109A")
cmd.distance("WeakHBond", "resi 97 & chain A & name O", "PseudoH107A")
cmd.distance("WeakHBond", "resi 106 & chain A & name O", "PseudoH98A")
cmd.distance("WeakHBond", "resi 130 & chain A & name O", "PseudoH106A")
cmd.distance("WeakHBond", "resi 107 & chain A & name O", "PseudoH129A")
cmd.distance("WeakHBond", "resi 128 & chain A & name O", "PseudoH108A")
cmd.distance("WeakHBond", "resi 109 & chain A & name O", "PseudoH127A")
cmd.distance("WeakHBond", "resi 126 & chain A & name O", "PseudoH110A")
cmd.distance("WeakHBond", "resi 111 & chain A & name O", "PseudoH125A")
cmd.distance("WeakHBond", "resi 124 & chain A & name O", "PseudoH112A")
cmd.distance("WeakHBond", "resi 113 & chain A & name O", "PseudoH123A")
cmd.distance("WeakHBond", "resi 122 & chain A & name O", "PseudoH114A")
cmd.distance("WeakHBond", "resi 115 & chain A & name O", "PseudoH121A")
cmd.distance("WeakHBond", "resi 129 & chain A & name O", "PseudoH22A")
cmd.distance("WeakHBond", "resi 21 & chain A & name O", "PseudoH130A")
cmd.distance("WeakHBond", "resi 131 & chain A & name O", "PseudoH20A")
cmd.distance("WeakHBond", "resi 19 & chain A & name O", "PseudoH132A")
cmd.distance("NonHBond", "resi 19 & chain A & name CB", "resi 29 & chain A & name CB")
cmd.distance("NonHBond", "resi 21 & chain A & name CB", "resi 27 & chain A & name CB")
cmd.distance("NonHBond", "resi 28 & chain A & name CB", "resi 48 & chain A & name CB")
cmd.distance("NonHBond", "resi 32 & chain A & name CB", "resi 44 & chain A & name CB")
cmd.distance("NonHBond", "resi 34 & chain A & name CB", "resi 42 & chain A & name CB")
cmd.distance("NonHBond", "resi 41 & chain A & name CB", "resi 69 & chain A & name CB")
cmd.distance("NonHBond", "resi 43 & chain A & name CB", "resi 67 & chain A & name CB")
cmd.distance("NonHBond", "resi 45 & chain A & name CB", "resi 65 & chain A & name CB")
cmd.distance("NonHBond", "resi 47 & chain A & name CB", "resi 63 & chain A & name CB")
cmd.distance("NonHBond", "resi 64 & chain A & name CB", "resi 79 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR66A", "resi 77 & chain A & name CB")
cmd.distance("NonHBond", "resi 68 & chain A & name CB", "resi 75 & chain A & name CB")
cmd.distance("NonHBond", "resi 74 & chain A & name CB", "resi 97 & chain A & name CB")
cmd.distance("NonHBond", "resi 76 & chain A & name CB", "resi 95 & chain A & name CB")
cmd.distance("NonHBond", "resi 78 & chain A & name CB", "PseudoR93A")
cmd.distance("NonHBond", "resi 80 & chain A & name CB", "resi 91 & chain A & name CB")
cmd.distance("NonHBond", "resi 82 & chain A & name CB", "resi 87 & chain A & name CB")
cmd.distance("NonHBond", "resi 92 & chain A & name CB", "resi 113 & chain A & name CB")
cmd.distance("NonHBond", "resi 94 & chain A & name CB", "resi 111 & chain A & name CB")
cmd.distance("NonHBond", "resi 98 & chain A & name CB", "resi 107 & chain A & name CB")
cmd.distance("NonHBond", "resi 106 & chain A & name CB", "resi 131 & chain A & name CB")
cmd.distance("NonHBond", "resi 108 & chain A & name CB", "resi 129 & chain A & name CB")
cmd.distance("NonHBond", "resi 110 & chain A & name CB", "resi 127 & chain A & name CB")
cmd.distance("NonHBond", "resi 112 & chain A & name CB", "resi 125 & chain A & name CB")
cmd.distance("NonHBond", "resi 114 & chain A & name CB", "resi 123 & chain A & name CB")
cmd.distance("NonHBond", "resi 116 & chain A & name CB", "resi 121 & chain A & name CB")
cmd.distance("NonHBond", "resi 130 & chain A & name CB", "resi 22 & chain A & name CB")
cmd.distance("NonHBond", "resi 132 & chain A & name CB", "resi 20 & chain A & name CB")
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