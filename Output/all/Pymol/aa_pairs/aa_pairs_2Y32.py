from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y32.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8 & chain A ")


cmd.select("Astrand1", "resi 45+46+47+48+49+50+51+52+53 & chain A ")


cmd.select("Astrand2", "resi 102+103+104+105+106+107+108+109+110+111+112+113 & chain A ")


cmd.select("Astrand3", "resi 58+59+60+61+62+63+64+65+66 & chain A ")


cmd.select("Astrand4", "resi 85+86+87+88+89+90+91+92+93 & chain A ")


cmd.select("Astrand5", "resi 71+72+73+74+75+76+77+78 & chain A ")


cmd.select("Astrand6", "resi 26+27+28+29+30+31+32 & chain A ")


cmd.select("Astrand7", "resi 14+15+16+17+18+19+20 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH85A", pos=[34.877457,4.6084332,52.09576])
cmd.pseudoatom ("PseudoH87A", pos=[40.423634,1.6150274,51.31777])
cmd.pseudoatom ("PseudoH75A", pos=[44.216652,-1.4460157,52.16808])
cmd.pseudoatom ("PseudoH89A", pos=[45.279255,-1.8254358,50.054623])
cmd.pseudoatom ("PseudoH73A", pos=[47.869873,-7.3573165,51.547863])
cmd.pseudoatom ("PseudoH91A", pos=[48.814735,-7.672945,49.65484])
cmd.pseudoatom ("PseudoH71A", pos=[51.224976,-13.388529,50.86064])
cmd.pseudoatom ("PseudoH20A", pos=[37.639435,-2.0891447,68.43173])
cmd.pseudoatom ("PseudoH27A", pos=[39.104748,-3.2073917,66.644806])
cmd.pseudoatom ("PseudoH17A", pos=[35.57044,-6.7342844,62.843605])
cmd.pseudoatom ("PseudoH15A", pos=[35.501118,-8.157592,56.757812])
cmd.pseudoatom ("PseudoH31A", pos=[36.7072,-10.342354,56.243507])
cmd.pseudoatom ("PseudoH14A", pos=[32.45479,-8.341281,53.40432])
cmd.pseudoatom ("PseudoH6A", pos=[31.14131,-5.6629376,58.76727])
cmd.pseudoatom ("PseudoH16A", pos=[32.382763,-7.314268,59.784523])
cmd.pseudoatom ("PseudoH2A", pos=[32.716797,-6.1455846,70.69137])
cmd.pseudoatom ("PseudoH18A", pos=[32.621906,-7.245887,65.90957])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 88 & chain A & name O", "resi 76 & chain A & name N")
cmd.distance("StrongHBond", "resi 88 & chain A & name N", "resi 76 & chain A & name O")
cmd.distance("StrongHBond", "resi 90 & chain A & name O", "resi 74 & chain A & name N")
cmd.distance("StrongHBond", "resi 90 & chain A & name N", "resi 74 & chain A & name O")
cmd.distance("StrongHBond", "resi 92 & chain A & name O", "resi 72 & chain A & name N")
cmd.distance("StrongHBond", "resi 92 & chain A & name N", "resi 72 & chain A & name O")
cmd.distance("StrongHBond", "resi 28 & chain A & name O", "resi 19 & chain A & name N")
cmd.distance("StrongHBond", "resi 28 & chain A & name N", "resi 19 & chain A & name O")
cmd.distance("StrongHBond", "resi 30 & chain A & name O", "resi 16 & chain A & name N")
cmd.distance("StrongHBond", "resi 30 & chain A & name N", "resi 16 & chain A & name O")
cmd.distance("StrongHBond", "resi 32 & chain A & name O", "resi 14 & chain A & name N")
cmd.distance("StrongHBond", "resi 32 & chain A & name N", "resi 14 & chain A & name O")
cmd.distance("StrongHBond", "resi 15 & chain A & name O", "resi 7 & chain A & name N")
cmd.distance("StrongHBond", "resi 15 & chain A & name N", "resi 7 & chain A & name O")
cmd.distance("StrongHBond", "resi 17 & chain A & name O", "resi 5 & chain A & name N")
cmd.distance("StrongHBond", "resi 17 & chain A & name N", "resi 5 & chain A & name O")
cmd.distance("WeakHBond", "resi 78 & chain A & name O", "PseudoH85A")
cmd.distance("WeakHBond", "resi 76 & chain A & name O", "PseudoH87A")
cmd.distance("WeakHBond", "resi 88 & chain A & name O", "PseudoH75A")
cmd.distance("WeakHBond", "resi 74 & chain A & name O", "PseudoH89A")
cmd.distance("WeakHBond", "resi 90 & chain A & name O", "PseudoH73A")
cmd.distance("WeakHBond", "resi 72 & chain A & name O", "PseudoH91A")
cmd.distance("WeakHBond", "resi 92 & chain A & name O", "PseudoH71A")
cmd.distance("WeakHBond", "resi 26 & chain A & name O", "PseudoH20A")
cmd.distance("WeakHBond", "resi 19 & chain A & name O", "PseudoH27A")
cmd.distance("WeakHBond", "resi 28 & chain A & name O", "PseudoH17A")
cmd.distance("WeakHBond", "resi 30 & chain A & name O", "PseudoH15A")
cmd.distance("WeakHBond", "resi 14 & chain A & name O", "PseudoH31A")
cmd.distance("WeakHBond", "resi 7 & chain A & name O", "PseudoH14A")
cmd.distance("WeakHBond", "resi 15 & chain A & name O", "PseudoH6A")
cmd.distance("WeakHBond", "resi 5 & chain A & name O", "PseudoH16A")
cmd.distance("WeakHBond", "resi 18 & chain A & name O", "PseudoH2A")
cmd.distance("WeakHBond", "resi 3 & chain A & name O", "PseudoH18A")
cmd.distance("NonHBond", "resi 89 & chain A & name CB", "resi 75 & chain A & name CB")
cmd.distance("NonHBond", "resi 91 & chain A & name CB", "resi 73 & chain A & name CB")
cmd.distance("NonHBond", "resi 93 & chain A & name CB", "resi 71 & chain A & name CB")
cmd.distance("NonHBond", "resi 27 & chain A & name CB", "resi 20 & chain A & name CB")
cmd.distance("NonHBond", "resi 31 & chain A & name CB", "resi 15 & chain A & name CB")
cmd.distance("NonHBond", "resi 14 & chain A & name CB", "resi 8 & chain A & name CB")
cmd.distance("NonHBond", "resi 16 & chain A & name CB", "resi 6 & chain A & name CB")
cmd.distance("NonHBond", "resi 19 & chain A & name CB", "resi 2 & chain A & name CB")
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