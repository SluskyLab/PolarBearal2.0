from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AW8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 37+38+39+40+41 & chain A ")


cmd.select("Astrand1", "resi 175+176+177+178 & chain A ")


cmd.select("Astrand2", "resi 120+121+122+123+124+125+126+127+128 & chain A ")


cmd.select("Astrand3", "resi 138+139+140+141+142 & chain A ")


cmd.select("Astrand4", "resi 99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114 & chain A ")


cmd.select("Astrand5", "resi 154+155+156+157+158+159 & chain A ")


cmd.select("Astrand6", "resi 91+92+93+94+95+96 & chain A ")


cmd.select("Astrand7", "resi 82+83+84+85+86+87+88 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH178A", pos=[7.427347,6.7345905,-3.908934])
cmd.pseudoatom ("PseudoH39A", pos=[9.717755,6.3332686,-2.2854638])
cmd.pseudoatom ("PseudoH176A", pos=[13.825028,9.0222025,-5.210424])
cmd.pseudoatom ("PseudoH41A", pos=[16.181097,7.725523,-4.988471])
cmd.pseudoatom ("PseudoH142A", pos=[11.968835,21.482046,-3.9792244])
cmd.pseudoatom ("PseudoH123A", pos=[12.865857,23.782286,-2.2909448])
cmd.pseudoatom ("PseudoH140A", pos=[14.853114,21.314688,2.1843145])
cmd.pseudoatom ("PseudoH125A", pos=[14.256278,23.19114,3.8456695])
cmd.pseudoatom ("PseudoH138A", pos=[18.511393,20.599054,7.800255])
cmd.pseudoatom ("PseudoH87A", pos=[9.085299,10.204485,6.554164])
cmd.pseudoatom ("PseudoH92A", pos=[11.407896,10.847253,7.3895802])
cmd.pseudoatom ("PseudoH85A", pos=[14.258184,7.2976813,3.3341997])
cmd.pseudoatom ("PseudoH94A", pos=[16.60519,7.6283503,4.870115])
cmd.pseudoatom ("PseudoH82A", pos=[20.802444,6.202072,1.4170494])
cmd.pseudoatom ("PseudoH40A", pos=[13.854635,4.635686,-2.7933044])
cmd.pseudoatom ("PseudoH84A", pos=[14.862191,4.858339,-0.44193655])
cmd.pseudoatom ("PseudoH38A", pos=[8.705816,5.7534623,1.9190841])
cmd.pseudoatom ("PseudoH86A", pos=[9.860314,6.8895984,3.6474376])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.pseudoatom ("PseudoR86A", pos=[10.438764,6.1326947,5.147253])
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 40 & chain A & name O", "resi 177 & chain A & name N")
cmd.distance("StrongHBond", "resi 40 & chain A & name N", "resi 177 & chain A & name O")
cmd.distance("StrongHBond", "resi 124 & chain A & name O", "resi 141 & chain A & name N")
cmd.distance("StrongHBond", "resi 124 & chain A & name N", "resi 141 & chain A & name O")
cmd.distance("StrongHBond", "resi 126 & chain A & name O", "resi 139 & chain A & name N")
cmd.distance("StrongHBond", "resi 126 & chain A & name N", "resi 139 & chain A & name O")
cmd.distance("StrongHBond", "resi 91 & chain A & name O", "resi 88 & chain A & name N")
cmd.distance("StrongHBond", "resi 91 & chain A & name N", "resi 88 & chain A & name O")
cmd.distance("StrongHBond", "resi 93 & chain A & name O", "resi 86 & chain A & name N")
cmd.distance("StrongHBond", "resi 93 & chain A & name N", "resi 86 & chain A & name O")
cmd.distance("StrongHBond", "resi 95 & chain A & name O", "resi 84 & chain A & name N")
cmd.distance("StrongHBond", "resi 95 & chain A & name N", "resi 84 & chain A & name O")
cmd.distance("StrongHBond", "resi 85 & chain A & name O", "resi 39 & chain A & name N")
cmd.distance("StrongHBond", "resi 85 & chain A & name N", "resi 39 & chain A & name O")
cmd.distance("StrongHBond", "resi 87 & chain A & name O", "resi 37 & chain A & name N")
cmd.distance("StrongHBond", "resi 87 & chain A & name N", "resi 37 & chain A & name O")
cmd.distance("WeakHBond", "resi 38 & chain A & name O", "PseudoH178A")
cmd.distance("WeakHBond", "resi 177 & chain A & name O", "PseudoH39A")
cmd.distance("WeakHBond", "resi 40 & chain A & name O", "PseudoH176A")
cmd.distance("WeakHBond", "resi 175 & chain A & name O", "PseudoH41A")
cmd.distance("WeakHBond", "resi 122 & chain A & name O", "PseudoH142A")
cmd.distance("WeakHBond", "resi 141 & chain A & name O", "PseudoH123A")
cmd.distance("WeakHBond", "resi 124 & chain A & name O", "PseudoH140A")
cmd.distance("WeakHBond", "resi 139 & chain A & name O", "PseudoH125A")
cmd.distance("WeakHBond", "resi 126 & chain A & name O", "PseudoH138A")
cmd.distance("WeakHBond", "resi 91 & chain A & name O", "PseudoH87A")
cmd.distance("WeakHBond", "resi 86 & chain A & name O", "PseudoH92A")
cmd.distance("WeakHBond", "resi 93 & chain A & name O", "PseudoH85A")
cmd.distance("WeakHBond", "resi 84 & chain A & name O", "PseudoH94A")
cmd.distance("WeakHBond", "resi 95 & chain A & name O", "PseudoH82A")
cmd.distance("WeakHBond", "resi 83 & chain A & name O", "PseudoH40A")
cmd.distance("WeakHBond", "resi 39 & chain A & name O", "PseudoH84A")
cmd.distance("WeakHBond", "resi 85 & chain A & name O", "PseudoH38A")
cmd.distance("WeakHBond", "resi 37 & chain A & name O", "PseudoH86A")
cmd.distance("NonHBond", "resi 39 & chain A & name CB", "resi 178 & chain A & name CB")
cmd.distance("NonHBond", "resi 41 & chain A & name CB", "resi 176 & chain A & name CB")
cmd.distance("NonHBond", "resi 123 & chain A & name CB", "resi 142 & chain A & name CB")
cmd.distance("NonHBond", "resi 125 & chain A & name CB", "resi 140 & chain A & name CB")
cmd.distance("NonHBond", "resi 127 & chain A & name CB", "resi 138 & chain A & name CB")
cmd.distance("NonHBond", "resi 92 & chain A & name CB", "resi 87 & chain A & name CB")
cmd.distance("NonHBond", "resi 94 & chain A & name CB", "resi 85 & chain A & name CB")
cmd.distance("NonHBond", "resi 96 & chain A & name CB", "resi 82 & chain A & name CB")
cmd.distance("NonHBond", "resi 84 & chain A & name CB", "resi 40 & chain A & name CB")
cmd.distance("NonHBond", "PseudoR86A", "resi 38 & chain A & name CB")
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