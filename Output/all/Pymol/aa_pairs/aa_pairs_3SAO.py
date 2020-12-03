from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SAO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 10+11+12+13+14+15+16+17+18 & chain A ")


cmd.select("Astrand1", "resi 34+35+36+37+38+39+40+41 & chain A ")


cmd.select("Astrand2", "resi 45+46+47+48+49+50+51+52 & chain A ")


cmd.select("Astrand3", "resi 82+83+84+85+86+87+88+89 & chain A ")


cmd.select("Astrand4", "resi 74+75+76+77 & chain A ")


cmd.select("Astrand5", "resi 94+95+96+97+98+99+100+101+102+103 & chain A ")


cmd.select("Astrand6", "resi 59+60+61+62+63+64+65+66 & chain A ")


cmd.select("Astrand7", "resi 106+107+108+109+110+111+112+113+114+115 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH37A", pos=[-18.641962,5.737878,-9.420382])
cmd.pseudoatom ("PseudoH11A", pos=[-19.8522,3.7782965,-8.376662])
cmd.pseudoatom ("PseudoH35A", pos=[-14.737694,0.06211126,-9.479407])
cmd.pseudoatom ("PseudoH13A", pos=[-16.084856,-1.0057603,-11.389964])
cmd.pseudoatom ("PseudoH34A", pos=[-10.526987,-0.99084514,-10.541094])
cmd.pseudoatom ("PseudoH50A", pos=[-12.196074,4.9035244,-10.289721])
cmd.pseudoatom ("PseudoH36A", pos=[-14.46403,4.388704,-10.289378])
cmd.pseudoatom ("PseudoH48A", pos=[-16.152287,9.394545,-12.632913])
cmd.pseudoatom ("PseudoH38A", pos=[-18.719894,9.179507,-12.233651])
cmd.pseudoatom ("PseudoH46A", pos=[-19.799372,14.60321,-14.822832])
cmd.pseudoatom ("PseudoH40A", pos=[-22.000902,14.538154,-13.957817])
cmd.pseudoatom ("PseudoH76A", pos=[-13.226164,13.5431385,-24.473927])
cmd.pseudoatom ("PseudoH83A", pos=[-12.60447,11.564549,-25.701998])
cmd.pseudoatom ("PseudoH74A", pos=[-18.428505,10.258236,-27.078312])
cmd.pseudoatom ("PseudoH110A", pos=[-8.5137205,-0.36263853,-25.862146])
cmd.pseudoatom ("PseudoH17A", pos=[-11.327483,-3.6246393,-21.519882])
cmd.pseudoatom ("PseudoH112A", pos=[-13.051233,-1.9030224,-21.27114])
cmd.pseudoatom ("PseudoH14A", pos=[-15.425569,-1.8101295,-15.764782])
cmd.pseudoatom ("PseudoH114A", pos=[-17.730991,-1.1290559,-16.43966])
cmd.pseudoatom ("PseudoH12A", pos=[-20.39858,0.37892443,-11.305622])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 10 & chain A & name O", "resi 38 & chain A & name N")
cmd.distance("StrongHBond", "resi 10 & chain A & name N", "resi 38 & chain A & name O")
cmd.distance("StrongHBond", "resi 12 & chain A & name O", "resi 36 & chain A & name N")
cmd.distance("StrongHBond", "resi 12 & chain A & name N", "resi 36 & chain A & name O")
cmd.distance("StrongHBond", "resi 14 & chain A & name O", "resi 34 & chain A & name N")
cmd.distance("StrongHBond", "resi 14 & chain A & name N", "resi 34 & chain A & name O")
cmd.distance("StrongHBond", "resi 35 & chain A & name O", "resi 51 & chain A & name N")
cmd.distance("StrongHBond", "resi 35 & chain A & name N", "resi 51 & chain A & name O")
cmd.distance("StrongHBond", "resi 37 & chain A & name O", "resi 49 & chain A & name N")
cmd.distance("StrongHBond", "resi 37 & chain A & name N", "resi 49 & chain A & name O")
cmd.distance("StrongHBond", "resi 39 & chain A & name O", "resi 47 & chain A & name N")
cmd.distance("StrongHBond", "resi 39 & chain A & name N", "resi 47 & chain A & name O")
cmd.distance("StrongHBond", "resi 41 & chain A & name O", "resi 45 & chain A & name N")
cmd.distance("StrongHBond", "resi 41 & chain A & name N", "resi 45 & chain A & name O")
cmd.distance("StrongHBond", "resi 82 & chain A & name O", "resi 77 & chain A & name N")
cmd.distance("StrongHBond", "resi 82 & chain A & name N", "resi 77 & chain A & name O")
cmd.distance("StrongHBond", "resi 84 & chain A & name O", "resi 75 & chain A & name N")
cmd.distance("StrongHBond", "resi 84 & chain A & name N", "resi 75 & chain A & name O")
cmd.distance("StrongHBond", "resi 111 & chain A & name O", "resi 18 & chain A & name N")
cmd.distance("StrongHBond", "resi 111 & chain A & name N", "resi 18 & chain A & name O")
cmd.distance("StrongHBond", "resi 115 & chain A & name O", "resi 13 & chain A & name N")
cmd.distance("StrongHBond", "resi 115 & chain A & name N", "resi 13 & chain A & name O")
cmd.distance("WeakHBond", "resi 10 & chain A & name O", "PseudoH37A")
cmd.distance("WeakHBond", "resi 36 & chain A & name O", "PseudoH11A")
cmd.distance("WeakHBond", "resi 12 & chain A & name O", "PseudoH35A")
cmd.distance("WeakHBond", "resi 34 & chain A & name O", "PseudoH13A")
cmd.distance("WeakHBond", "resi 51 & chain A & name O", "PseudoH34A")
cmd.distance("WeakHBond", "resi 35 & chain A & name O", "PseudoH50A")
cmd.distance("WeakHBond", "resi 49 & chain A & name O", "PseudoH36A")
cmd.distance("WeakHBond", "resi 37 & chain A & name O", "PseudoH48A")
cmd.distance("WeakHBond", "resi 47 & chain A & name O", "PseudoH38A")
cmd.distance("WeakHBond", "resi 39 & chain A & name O", "PseudoH46A")
cmd.distance("WeakHBond", "resi 45 & chain A & name O", "PseudoH40A")
cmd.distance("WeakHBond", "resi 82 & chain A & name O", "PseudoH76A")
cmd.distance("WeakHBond", "resi 75 & chain A & name O", "PseudoH83A")
cmd.distance("WeakHBond", "resi 84 & chain A & name O", "PseudoH74A")
cmd.distance("WeakHBond", "resi 18 & chain A & name O", "PseudoH110A")
cmd.distance("WeakHBond", "resi 111 & chain A & name O", "PseudoH17A")
cmd.distance("WeakHBond", "resi 16 & chain A & name O", "PseudoH112A")
cmd.distance("WeakHBond", "resi 113 & chain A & name O", "PseudoH14A")
cmd.distance("WeakHBond", "resi 13 & chain A & name O", "PseudoH114A")
cmd.distance("WeakHBond", "resi 115 & chain A & name O", "PseudoH12A")
cmd.distance("NonHBond", "resi 11 & chain A & name CB", "resi 37 & chain A & name CB")
cmd.distance("NonHBond", "resi 13 & chain A & name CB", "resi 35 & chain A & name CB")
cmd.distance("NonHBond", "resi 34 & chain A & name CB", "resi 52 & chain A & name CB")
cmd.distance("NonHBond", "resi 36 & chain A & name CB", "resi 50 & chain A & name CB")
cmd.distance("NonHBond", "resi 38 & chain A & name CB", "resi 48 & chain A & name CB")
cmd.distance("NonHBond", "resi 40 & chain A & name CB", "resi 46 & chain A & name CB")
cmd.distance("NonHBond", "resi 83 & chain A & name CB", "resi 76 & chain A & name CB")
cmd.distance("NonHBond", "resi 85 & chain A & name CB", "resi 74 & chain A & name CB")
cmd.distance("NonHBond", "resi 112 & chain A & name CB", "resi 17 & chain A & name CB")
cmd.distance("NonHBond", "resi 114 & chain A & name CB", "resi 14 & chain A & name CB")
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
