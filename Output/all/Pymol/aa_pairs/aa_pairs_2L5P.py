from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2L5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 51+52+53+54+55+56+57+58+59+60 & chain A ")


cmd.select("Astrand1", "resi 86+87+88+89+90+91+92+93+94 & chain A ")


cmd.select("Astrand2", "resi 75+76+77+78+79+80 & chain A ")


cmd.select("Astrand3", "resi 97+98+99+100+101+102+103+104+105+106+107 & chain A ")


cmd.select("Astrand4", "resi 113+114+115+116 & chain A ")


cmd.select("Astrand5", "resi 128+129+130+131+132+133+134+135+136 & chain A ")


cmd.select("Astrand6", "resi 140+141+142+143+144+145+146+147+148 & chain A ")


cmd.select("Astrand7", "resi 153+154+155+156+157+158+159+160+161 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH86A", pos=[-4.3970537,-10.58451,-4.8094673])
cmd.pseudoatom ("PseudoH78A", pos=[-0.14461234,-8.905054,-4.714461])
cmd.pseudoatom ("PseudoH88A", pos=[0.45564985,-8.682439,-2.1100988])
cmd.pseudoatom ("PseudoH76A", pos=[5.337029,-6.1906734,-1.8938262])
cmd.pseudoatom ("PseudoH90A", pos=[5.956642,-6.8547087,-0.22836643])
cmd.pseudoatom ("PseudoH116A", pos=[-6.624235,-8.69563,3.7587912])
cmd.pseudoatom ("PseudoH105A", pos=[-6.933449,-8.718192,1.3035529])
cmd.pseudoatom ("PseudoH114A", pos=[-11.305275,-5.74951,-0.35638434])
cmd.pseudoatom ("PseudoH107A", pos=[-12.088776,-6.7864747,-2.2474923])
cmd.pseudoatom ("PseudoH113A", pos=[-11.789022,-1.5101175,-1.5517907])
cmd.pseudoatom ("PseudoH129A", pos=[-9.518312,-3.1804438,4.532412])
cmd.pseudoatom ("PseudoH115A", pos=[-9.387318,-5.2984796,3.8092256])
cmd.pseudoatom ("PseudoH128A", pos=[-7.0372667,-3.1270685,8.140619])
cmd.pseudoatom ("PseudoH145A", pos=[-6.071448,0.51937276,3.5312927])
cmd.pseudoatom ("PseudoH130A", pos=[-6.707232,-1.0535077,1.844482])
cmd.pseudoatom ("PseudoH143A", pos=[-4.714958,2.1734176,-2.8820145])
cmd.pseudoatom ("PseudoH132A", pos=[-6.4137554,1.5573351,-4.1474967])
cmd.pseudoatom ("PseudoH141A", pos=[-2.0193121,2.9547963,-8.582701])
cmd.pseudoatom ("PseudoH135A", pos=[-3.4258924,2.7995021,-9.633508])
cmd.pseudoatom ("PseudoH140A", pos=[2.3318207,3.266529,-10.06737])
cmd.pseudoatom ("PseudoH159A", pos=[0.95454466,5.1948385,-3.7663913])
cmd.pseudoatom ("PseudoH157A", pos=[-2.5221145,4.801143,2.1217241])
cmd.pseudoatom ("PseudoH155A", pos=[-5.6483135,4.50075,8.00016])
cmd.pseudoatom ("PseudoH146A", pos=[-6.1331596,2.0577602,7.707225])
cmd.pseudoatom ("PseudoH153A", pos=[-7.572395,1.2856988,13.409786])
cmd.pseudoatom ("PseudoH60A", pos=[-0.45685202,6.502371,7.8325367])
cmd.pseudoatom ("PseudoH156A", pos=[-1.5929232,5.312768,6.4333415])
cmd.pseudoatom ("PseudoH58A", pos=[3.2924166,5.226073,2.3547676])
cmd.pseudoatom ("PseudoH158A", pos=[1.5851195,4.35589,0.5472257])
cmd.pseudoatom ("PseudoH55A", pos=[5.432725,1.7867529,-2.8892105])
cmd.pseudoatom ("PseudoH160A", pos=[3.8569357,2.0476248,-4.830895])
cmd.pseudoatom ("PseudoH53A", pos=[4.777349,-2.1992056,-7.9598427])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR161A", pos=[5.5834255,3.14899,-8.695803])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 87 & chain A & name O", "resi 79 & chain A & name N")
cmd.distance("StrongHBond", "resi 87 & chain A & name N", "resi 79 & chain A & name O")
cmd.distance("StrongHBond", "resi 89 & chain A & name O", "resi 77 & chain A & name N")
cmd.distance("StrongHBond", "resi 89 & chain A & name N", "resi 77 & chain A & name O")
cmd.distance("StrongHBond", "resi 91 & chain A & name O", "resi 75 & chain A & name N")
cmd.distance("StrongHBond", "resi 91 & chain A & name N", "resi 75 & chain A & name O")
cmd.distance("StrongHBond", "resi 106 & chain A & name O", "resi 115 & chain A & name N")
cmd.distance("StrongHBond", "resi 106 & chain A & name N", "resi 115 & chain A & name O")
cmd.distance("StrongHBond", "resi 114 & chain A & name O", "resi 130 & chain A & name N")
cmd.distance("StrongHBond", "resi 114 & chain A & name N", "resi 130 & chain A & name O")
cmd.distance("StrongHBond", "resi 129 & chain A & name O", "resi 146 & chain A & name N")
cmd.distance("StrongHBond", "resi 129 & chain A & name N", "resi 146 & chain A & name O")
cmd.distance("StrongHBond", "resi 131 & chain A & name O", "resi 144 & chain A & name N")
cmd.distance("StrongHBond", "resi 131 & chain A & name N", "resi 144 & chain A & name O")
cmd.distance("StrongHBond", "resi 134 & chain A & name O", "resi 142 & chain A & name N")
cmd.distance("StrongHBond", "resi 134 & chain A & name N", "resi 142 & chain A & name O")
cmd.distance("StrongHBond", "resi 136 & chain A & name O", "resi 140 & chain A & name N")
cmd.distance("StrongHBond", "resi 136 & chain A & name N", "resi 140 & chain A & name O")
cmd.distance("StrongHBond", "resi 141 & chain A & name O", "resi 160 & chain A & name N")
cmd.distance("StrongHBond", "resi 141 & chain A & name N", "resi 160 & chain A & name O")
cmd.distance("StrongHBond", "resi 143 & chain A & name O", "resi 158 & chain A & name N")
cmd.distance("StrongHBond", "resi 143 & chain A & name N", "resi 158 & chain A & name O")
cmd.distance("StrongHBond", "resi 145 & chain A & name O", "resi 156 & chain A & name N")
cmd.distance("StrongHBond", "resi 145 & chain A & name N", "resi 156 & chain A & name O")
cmd.distance("StrongHBond", "resi 147 & chain A & name O", "resi 154 & chain A & name N")
cmd.distance("StrongHBond", "resi 147 & chain A & name N", "resi 154 & chain A & name O")
cmd.distance("StrongHBond", "resi 157 & chain A & name O", "resi 59 & chain A & name N")
cmd.distance("StrongHBond", "resi 157 & chain A & name N", "resi 59 & chain A & name O")
cmd.distance("StrongHBond", "resi 159 & chain A & name O", "resi 57 & chain A & name N")
cmd.distance("StrongHBond", "resi 159 & chain A & name N", "resi 57 & chain A & name O")
cmd.distance("StrongHBond", "resi 161 & chain A & name O", "resi 54 & chain A & name N")
cmd.distance("StrongHBond", "resi 161 & chain A & name N", "resi 54 & chain A & name O")
cmd.distance("WeakHBond", "resi 79 & chain A & name O", "PseudoH86A")
cmd.distance("WeakHBond", "resi 87 & chain A & name O", "PseudoH78A")
cmd.distance("WeakHBond", "resi 77 & chain A & name O", "PseudoH88A")
cmd.distance("WeakHBond", "resi 89 & chain A & name O", "PseudoH76A")
cmd.distance("WeakHBond", "resi 75 & chain A & name O", "PseudoH90A")
cmd.distance("WeakHBond", "resi 104 & chain A & name O", "PseudoH116A")
cmd.distance("WeakHBond", "resi 115 & chain A & name O", "PseudoH105A")
cmd.distance("WeakHBond", "resi 106 & chain A & name O", "PseudoH114A")
cmd.distance("WeakHBond", "resi 113 & chain A & name O", "PseudoH107A")
cmd.distance("WeakHBond", "resi 130 & chain A & name O", "PseudoH113A")
cmd.distance("WeakHBond", "resi 114 & chain A & name O", "PseudoH129A")
cmd.distance("WeakHBond", "resi 128 & chain A & name O", "PseudoH115A")
cmd.distance("WeakHBond", "resi 146 & chain A & name O", "PseudoH128A")
cmd.distance("WeakHBond", "resi 129 & chain A & name O", "PseudoH145A")
cmd.distance("WeakHBond", "resi 144 & chain A & name O", "PseudoH130A")
cmd.distance("WeakHBond", "resi 131 & chain A & name O", "PseudoH143A")
cmd.distance("WeakHBond", "resi 142 & chain A & name O", "PseudoH132A")
cmd.distance("WeakHBond", "resi 134 & chain A & name O", "PseudoH141A")
cmd.distance("WeakHBond", "resi 140 & chain A & name O", "PseudoH135A")
cmd.distance("WeakHBond", "resi 160 & chain A & name O", "PseudoH140A")
cmd.distance("WeakHBond", "resi 141 & chain A & name O", "PseudoH159A")
cmd.distance("WeakHBond", "resi 143 & chain A & name O", "PseudoH157A")
cmd.distance("WeakHBond", "resi 145 & chain A & name O", "PseudoH155A")
cmd.distance("WeakHBond", "resi 154 & chain A & name O", "PseudoH146A")
cmd.distance("WeakHBond", "resi 147 & chain A & name O", "PseudoH153A")
cmd.distance("WeakHBond", "resi 155 & chain A & name O", "PseudoH60A")
cmd.distance("WeakHBond", "resi 59 & chain A & name O", "PseudoH156A")
cmd.distance("WeakHBond", "resi 157 & chain A & name O", "PseudoH58A")
cmd.distance("WeakHBond", "resi 57 & chain A & name O", "PseudoH158A")
cmd.distance("WeakHBond", "resi 159 & chain A & name O", "PseudoH55A")
cmd.distance("WeakHBond", "resi 54 & chain A & name O", "PseudoH160A")
cmd.distance("WeakHBond", "resi 161 & chain A & name O", "PseudoH53A")
cmd.distance("NonHBond", "resi 88 & chain A & name CB", "resi 78 & chain A & name CB")
cmd.distance("NonHBond", "resi 90 & chain A & name CB", "resi 76 & chain A & name CB")
cmd.distance("NonHBond", "resi 105 & chain A & name CB", "resi 116 & chain A & name CB")
cmd.distance("NonHBond", "resi 107 & chain A & name CB", "resi 114 & chain A & name CB")
cmd.distance("NonHBond", "resi 113 & chain A & name CB", "resi 131 & chain A & name CB")
cmd.distance("NonHBond", "resi 115 & chain A & name CB", "resi 129 & chain A & name CB")
cmd.distance("NonHBond", "resi 128 & chain A & name CB", "resi 147 & chain A & name CB")
cmd.distance("NonHBond", "resi 130 & chain A & name CB", "resi 145 & chain A & name CB")
cmd.distance("NonHBond", "resi 132 & chain A & name CB", "resi 143 & chain A & name CB")
cmd.distance("NonHBond", "resi 135 & chain A & name CB", "resi 141 & chain A & name CB")
cmd.distance("NonHBond", "resi 140 & chain A & name CB", "PseudoR161A")
cmd.distance("NonHBond", "resi 142 & chain A & name CB", "resi 159 & chain A & name CB")
cmd.distance("NonHBond", "resi 144 & chain A & name CB", "resi 157 & chain A & name CB")
cmd.distance("NonHBond", "resi 146 & chain A & name CB", "resi 155 & chain A & name CB")
cmd.distance("NonHBond", "resi 148 & chain A & name CB", "resi 153 & chain A & name CB")
cmd.distance("NonHBond", "resi 156 & chain A & name CB", "resi 60 & chain A & name CB")
cmd.distance("NonHBond", "resi 158 & chain A & name CB", "resi 58 & chain A & name CB")
cmd.distance("NonHBond", "resi 160 & chain A & name CB", "resi 55 & chain A & name CB")
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