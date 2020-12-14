from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JIW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Istrand0", "resi 13+14+15+16+17+18+19 & chain I ")


cmd.select("Istrand1", "resi 25+26+27+28+29+30+31+32+33+34+35 & chain I ")


cmd.select("Istrand2", "resi 40+41+42+43+44+45 & chain I ")


cmd.select("Istrand3", "resi 60+61+62+63+64 & chain I ")


cmd.select("Istrand4", "resi 67+68+69+70+71 & chain I ")


cmd.select("Istrand5", "resi 77+78+79+80+81+82+83+84+85 & chain I ")


cmd.select("Istrand6", "resi 88+89+90+91+92 & chain I ")


cmd.select("Istrand7", "resi 98+99+100+101+102+103 & chain I ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Istrand*")
cmd.pseudoatom ("PseudoH29I", pos=[49.402576,56.891293,-36.2308])
cmd.pseudoatom ("PseudoH14I", pos=[47.931873,56.39373,-38.46059])
cmd.pseudoatom ("PseudoH27I", pos=[42.672974,56.58182,-34.636196])
cmd.pseudoatom ("PseudoH16I", pos=[42.525394,54.03427,-35.066113])
cmd.pseudoatom ("PseudoH25I", pos=[37.506763,53.41185,-31.424152])
cmd.pseudoatom ("PseudoH28I", pos=[46.54817,57.302868,-32.75426])
cmd.pseudoatom ("PseudoH43I", pos=[52.793716,56.140205,-31.621613])
cmd.pseudoatom ("PseudoH41I", pos=[59.808067,54.268295,-30.875845])
cmd.pseudoatom ("PseudoH34I", pos=[62.307053,54.54062,-31.565886])
cmd.pseudoatom ("PseudoH60I", pos=[55.404278,54.901978,-28.15693])
cmd.pseudoatom ("PseudoH70I", pos=[51.88513,50.321667,-27.196476])
cmd.pseudoatom ("PseudoH61I", pos=[54.328396,50.472084,-28.189249])
cmd.pseudoatom ("PseudoH68I", pos=[52.806908,45.20351,-31.72025])
cmd.pseudoatom ("PseudoH63I", pos=[55.040073,45.36043,-32.98818])
cmd.pseudoatom ("PseudoH67I", pos=[50.560696,41.361923,-33.317516])
cmd.pseudoatom ("PseudoH80I", pos=[49.847267,44.122673,-27.087374])
cmd.pseudoatom ("PseudoH69I", pos=[51.451805,45.79152,-27.629002])
cmd.pseudoatom ("PseudoH77I", pos=[53.367043,47.250393,-22.860907])
cmd.pseudoatom ("PseudoH81I", pos=[46.245537,42.97441,-29.408123])
cmd.pseudoatom ("PseudoH89I", pos=[45.725666,42.135403,-34.8248])
cmd.pseudoatom ("PseudoH83I", pos=[47.60262,40.694763,-35.466457])
cmd.pseudoatom ("PseudoH88I", pos=[43.90377,44.1913,-38.326344])
cmd.pseudoatom ("PseudoH100I", pos=[41.009792,45.038128,-33.171284])
cmd.pseudoatom ("PseudoH90I", pos=[42.684116,43.43757,-31.999397])
cmd.pseudoatom ("PseudoH98I", pos=[37.810486,42.65819,-27.994865])
cmd.pseudoatom ("PseudoH19I", pos=[36.290195,47.57023,-29.767742])
cmd.pseudoatom ("PseudoH99I", pos=[38.53078,46.592213,-29.995995])
cmd.pseudoatom ("PseudoH17I", pos=[41.540264,50.16289,-33.065414])
cmd.pseudoatom ("PseudoH101I", pos=[42.998577,48.81595,-34.624504])
cmd.pseudoatom ("PseudoH15I", pos=[45.29408,52.815315,-38.439674])
cmd.pseudoatom ("PseudoH103I", pos=[45.735607,51.40357,-40.11203])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR67I", pos=[50.96196,41.308125,-31.641617])
cmd.pseudoatom ("PseudoR82I", pos=[47.234447,38.987072,-31.118145])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 13 & chain I & name O", "resi 30 & chain I & name N")
cmd.distance("StrongHBond", "resi 13 & chain I & name N", "resi 30 & chain I & name O")
cmd.distance("StrongHBond", "resi 15 & chain I & name O", "resi 28 & chain I & name N")
cmd.distance("StrongHBond", "resi 15 & chain I & name N", "resi 28 & chain I & name O")
cmd.distance("StrongHBond", "resi 17 & chain I & name O", "resi 26 & chain I & name N")
cmd.distance("StrongHBond", "resi 17 & chain I & name N", "resi 26 & chain I & name O")
cmd.distance("StrongHBond", "resi 29 & chain I & name O", "resi 44 & chain I & name N")
cmd.distance("StrongHBond", "resi 29 & chain I & name N", "resi 44 & chain I & name O")
cmd.distance("StrongHBond", "resi 35 & chain I & name O", "resi 40 & chain I & name N")
cmd.distance("StrongHBond", "resi 35 & chain I & name N", "resi 40 & chain I & name O")
cmd.distance("StrongHBond", "resi 41 & chain I & name O", "resi 61 & chain I & name N")
cmd.distance("StrongHBond", "resi 41 & chain I & name N", "resi 61 & chain I & name O")
cmd.distance("StrongHBond", "resi 62 & chain I & name O", "resi 69 & chain I & name N")
cmd.distance("StrongHBond", "resi 62 & chain I & name N", "resi 69 & chain I & name O")
cmd.distance("StrongHBond", "resi 64 & chain I & name O", "resi 67 & chain I & name N")
cmd.distance("StrongHBond", "resi 64 & chain I & name N", "resi 67 & chain I & name O")
cmd.distance("StrongHBond", "resi 68 & chain I & name O", "resi 81 & chain I & name N")
cmd.distance("StrongHBond", "resi 68 & chain I & name N", "resi 81 & chain I & name O")
cmd.distance("StrongHBond", "resi 70 & chain I & name O", "resi 79 & chain I & name N")
cmd.distance("StrongHBond", "resi 70 & chain I & name N", "resi 79 & chain I & name O")
cmd.distance("StrongHBond", "resi 82 & chain I & name O", "resi 90 & chain I & name N")
cmd.distance("StrongHBond", "resi 82 & chain I & name N", "resi 90 & chain I & name O")
cmd.distance("StrongHBond", "resi 85 & chain I & name O", "resi 88 & chain I & name N")
cmd.distance("StrongHBond", "resi 85 & chain I & name N", "resi 88 & chain I & name O")
cmd.distance("StrongHBond", "resi 89 & chain I & name O", "resi 101 & chain I & name N")
cmd.distance("StrongHBond", "resi 89 & chain I & name N", "resi 101 & chain I & name O")
cmd.distance("StrongHBond", "resi 91 & chain I & name O", "resi 99 & chain I & name N")
cmd.distance("StrongHBond", "resi 91 & chain I & name N", "resi 99 & chain I & name O")
cmd.distance("StrongHBond", "resi 100 & chain I & name O", "resi 18 & chain I & name N")
cmd.distance("StrongHBond", "resi 100 & chain I & name N", "resi 18 & chain I & name O")
cmd.distance("StrongHBond", "resi 102 & chain I & name O", "resi 16 & chain I & name N")
cmd.distance("StrongHBond", "resi 102 & chain I & name N", "resi 16 & chain I & name O")
cmd.distance("WeakHBond", "resi 13 & chain I & name O", "PseudoH29I")
cmd.distance("WeakHBond", "resi 28 & chain I & name O", "PseudoH14I")
cmd.distance("WeakHBond", "resi 15 & chain I & name O", "PseudoH27I")
cmd.distance("WeakHBond", "resi 26 & chain I & name O", "PseudoH16I")
cmd.distance("WeakHBond", "resi 17 & chain I & name O", "PseudoH25I")
cmd.distance("WeakHBond", "resi 44 & chain I & name O", "PseudoH28I")
cmd.distance("WeakHBond", "resi 29 & chain I & name O", "PseudoH43I")
cmd.distance("WeakHBond", "resi 33 & chain I & name O", "PseudoH41I")
cmd.distance("WeakHBond", "resi 40 & chain I & name O", "PseudoH34I")
cmd.distance("WeakHBond", "resi 41 & chain I & name O", "PseudoH60I")
cmd.distance("WeakHBond", "resi 60 & chain I & name O", "PseudoH70I")
cmd.distance("WeakHBond", "resi 69 & chain I & name O", "PseudoH61I")
cmd.distance("WeakHBond", "resi 62 & chain I & name O", "PseudoH68I")
cmd.distance("WeakHBond", "resi 67 & chain I & name O", "PseudoH63I")
cmd.distance("WeakHBond", "resi 81 & chain I & name O", "PseudoH67I")
cmd.distance("WeakHBond", "resi 68 & chain I & name O", "PseudoH80I")
cmd.distance("WeakHBond", "resi 79 & chain I & name O", "PseudoH69I")
cmd.distance("WeakHBond", "resi 70 & chain I & name O", "PseudoH77I")
cmd.distance("WeakHBond", "resi 90 & chain I & name O", "PseudoH81I")
cmd.distance("WeakHBond", "resi 82 & chain I & name O", "PseudoH89I")
cmd.distance("WeakHBond", "resi 88 & chain I & name O", "PseudoH83I")
cmd.distance("WeakHBond", "resi 101 & chain I & name O", "PseudoH88I")
cmd.distance("WeakHBond", "resi 89 & chain I & name O", "PseudoH100I")
cmd.distance("WeakHBond", "resi 99 & chain I & name O", "PseudoH90I")
cmd.distance("WeakHBond", "resi 91 & chain I & name O", "PseudoH98I")
cmd.distance("WeakHBond", "resi 98 & chain I & name O", "PseudoH19I")
cmd.distance("WeakHBond", "resi 18 & chain I & name O", "PseudoH99I")
cmd.distance("WeakHBond", "resi 100 & chain I & name O", "PseudoH17I")
cmd.distance("WeakHBond", "resi 16 & chain I & name O", "PseudoH101I")
cmd.distance("WeakHBond", "resi 102 & chain I & name O", "PseudoH15I")
cmd.distance("WeakHBond", "resi 14 & chain I & name O", "PseudoH103I")
cmd.distance("NonHBond", "resi 14 & chain I & name CB", "resi 29 & chain I & name CB")
cmd.distance("NonHBond", "resi 16 & chain I & name CB", "resi 27 & chain I & name CB")
cmd.distance("NonHBond", "resi 18 & chain I & name CB", "resi 25 & chain I & name CB")
cmd.distance("NonHBond", "resi 30 & chain I & name CB", "resi 43 & chain I & name CB")
cmd.distance("NonHBond", "resi 34 & chain I & name CB", "resi 41 & chain I & name CB")
cmd.distance("NonHBond", "resi 42 & chain I & name CB", "resi 60 & chain I & name CB")
cmd.distance("NonHBond", "resi 61 & chain I & name CB", "resi 70 & chain I & name CB")
cmd.distance("NonHBond", "resi 63 & chain I & name CB", "resi 68 & chain I & name CB")
cmd.distance("NonHBond", "PseudoR67I", "PseudoR82I")
cmd.distance("NonHBond", "resi 69 & chain I & name CB", "resi 80 & chain I & name CB")
cmd.distance("NonHBond", "resi 71 & chain I & name CB", "resi 77 & chain I & name CB")
cmd.distance("NonHBond", "resi 83 & chain I & name CB", "resi 89 & chain I & name CB")
cmd.distance("NonHBond", "resi 90 & chain I & name CB", "resi 100 & chain I & name CB")
cmd.distance("NonHBond", "resi 92 & chain I & name CB", "resi 98 & chain I & name CB")
cmd.distance("NonHBond", "resi 99 & chain I & name CB", "resi 19 & chain I & name CB")
cmd.distance("NonHBond", "resi 101 & chain I & name CB", "resi 17 & chain I & name CB")
cmd.distance("NonHBond", "resi 103 & chain I & name CB", "resi 15 & chain I & name CB")
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