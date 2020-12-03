from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1MDC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13 & chain A ")


cmd.select("Astrand1", "resi 112+113+114+115+116+117 & chain A ")


cmd.select("Astrand2", "resi 37+38+39+40+41+42+43 & chain A ")


cmd.select("Astrand3", "resi 100+101+102+103+104+105+106+107 & chain A ")


cmd.select("Astrand4", "resi 48+49+50+51+52+53 & chain A ")


cmd.select("Astrand5", "resi 58+59+60+61+62+63 & chain A ")


cmd.select("Astrand6", "resi 77+78+79+80+81+82+83+84+85 & chain A ")


cmd.select("Astrand7", "resi 68+69+70+71+72 & chain A ")


cmd.select("Astrand8", "resi 90+91+92+93+94+95 & chain A ")


cmd.select("Astrand9", "resi 124+125+126+127+128+129+130 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH62A", pos=[24.647053,29.088968,2.0600138])
cmd.pseudoatom ("PseudoH49A", pos=[23.265358,29.767618,3.6069615])
cmd.pseudoatom ("PseudoH60A", pos=[24.218134,26.324892,8.089875])
cmd.pseudoatom ("PseudoH51A", pos=[22.241985,26.265554,9.171595])
cmd.pseudoatom ("PseudoH58A", pos=[23.059372,21.674866,13.304336])
cmd.pseudoatom ("PseudoH72A", pos=[24.732782,14.973819,1.9283932])
cmd.pseudoatom ("PseudoH78A", pos=[25.512508,13.0379,0.11937645])
cmd.pseudoatom ("PseudoH70A", pos=[26.752718,17.594807,-4.3293777])
cmd.pseudoatom ("PseudoH80A", pos=[24.221493,17.422,-5.2717657])
cmd.pseudoatom ("PseudoH68A", pos=[22.819263,22.593884,-7.5877004])
cmd.pseudoatom ("PseudoH125A", pos=[3.8904233,13.47081,3.267182])
cmd.pseudoatom ("PseudoH12A", pos=[4.4258347,16.654348,9.1037855])
cmd.pseudoatom ("PseudoH127A", pos=[6.023032,18.242065,8.206038])
cmd.pseudoatom ("PseudoH9A", pos=[8.718403,21.644188,12.457252])
cmd.pseudoatom ("PseudoH129A", pos=[7.220095,23.520725,11.974133])
cmd.pseudoatom ("PseudoH7A", pos=[10.5455065,28.014273,12.943502])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 48 & chain A & name O", "resi 63 & chain A & name N")
cmd.distance("StrongHBond", "resi 48 & chain A & name N", "resi 63 & chain A & name O")
cmd.distance("StrongHBond", "resi 50 & chain A & name O", "resi 61 & chain A & name N")
cmd.distance("StrongHBond", "resi 50 & chain A & name N", "resi 61 & chain A & name O")
cmd.distance("StrongHBond", "resi 52 & chain A & name O", "resi 59 & chain A & name N")
cmd.distance("StrongHBond", "resi 52 & chain A & name N", "resi 59 & chain A & name O")
cmd.distance("StrongHBond", "resi 79 & chain A & name O", "resi 71 & chain A & name N")
cmd.distance("StrongHBond", "resi 79 & chain A & name N", "resi 71 & chain A & name O")
cmd.distance("StrongHBond", "resi 81 & chain A & name O", "resi 69 & chain A & name N")
cmd.distance("StrongHBond", "resi 81 & chain A & name N", "resi 69 & chain A & name O")
cmd.distance("StrongHBond", "resi 126 & chain A & name O", "resi 13 & chain A & name N")
cmd.distance("StrongHBond", "resi 126 & chain A & name N", "resi 13 & chain A & name O")
cmd.distance("StrongHBond", "resi 128 & chain A & name O", "resi 11 & chain A & name N")
cmd.distance("StrongHBond", "resi 128 & chain A & name N", "resi 11 & chain A & name O")
cmd.distance("StrongHBond", "resi 130 & chain A & name O", "resi 8 & chain A & name N")
cmd.distance("StrongHBond", "resi 130 & chain A & name N", "resi 8 & chain A & name O")
cmd.distance("WeakHBond", "resi 48 & chain A & name O", "PseudoH62A")
cmd.distance("WeakHBond", "resi 61 & chain A & name O", "PseudoH49A")
cmd.distance("WeakHBond", "resi 50 & chain A & name O", "PseudoH60A")
cmd.distance("WeakHBond", "resi 59 & chain A & name O", "PseudoH51A")
cmd.distance("WeakHBond", "resi 52 & chain A & name O", "PseudoH58A")
cmd.distance("WeakHBond", "resi 77 & chain A & name O", "PseudoH72A")
cmd.distance("WeakHBond", "resi 71 & chain A & name O", "PseudoH78A")
cmd.distance("WeakHBond", "resi 79 & chain A & name O", "PseudoH70A")
cmd.distance("WeakHBond", "resi 69 & chain A & name O", "PseudoH80A")
cmd.distance("WeakHBond", "resi 81 & chain A & name O", "PseudoH68A")
cmd.distance("WeakHBond", "resi 13 & chain A & name O", "PseudoH125A")
cmd.distance("WeakHBond", "resi 126 & chain A & name O", "PseudoH12A")
cmd.distance("WeakHBond", "resi 11 & chain A & name O", "PseudoH127A")
cmd.distance("WeakHBond", "resi 128 & chain A & name O", "PseudoH9A")
cmd.distance("WeakHBond", "resi 8 & chain A & name O", "PseudoH129A")
cmd.distance("WeakHBond", "resi 130 & chain A & name O", "PseudoH7A")
cmd.distance("NonHBond", "resi 49 & chain A & name CB", "resi 62 & chain A & name CB")
cmd.distance("NonHBond", "resi 51 & chain A & name CB", "resi 60 & chain A & name CB")
cmd.distance("NonHBond", "resi 53 & chain A & name CB", "resi 58 & chain A & name CB")
cmd.distance("NonHBond", "resi 78 & chain A & name CB", "resi 72 & chain A & name CB")
cmd.distance("NonHBond", "resi 80 & chain A & name CB", "resi 70 & chain A & name CB")
cmd.distance("NonHBond", "resi 82 & chain A & name CB", "resi 68 & chain A & name CB")
cmd.distance("NonHBond", "resi 127 & chain A & name CB", "resi 12 & chain A & name CB")
cmd.distance("NonHBond", "resi 129 & chain A & name CB", "resi 9 & chain A & name CB")
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
