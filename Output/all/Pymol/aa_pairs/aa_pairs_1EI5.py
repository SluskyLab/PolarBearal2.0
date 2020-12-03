from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EI5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.remove("hydrogens")
cmd.h_add("(name CA)")
cmd.select("Astrand0", "resi 348+349+350+351 & chain A ")


cmd.select("Astrand1", "resi 358+359+360+361+362+363 & chain A ")


cmd.select("Astrand2", "resi 411+412+413+414+415+416+417 & chain A ")


cmd.select("Astrand3", "resi 368+369+370+371+372 & chain A ")


cmd.select("Astrand4", "resi 401+402+403+404+405+406 & chain A ")


cmd.select("Astrand5", "resi 387+388+389 & chain A ")


cmd.select("Astrand6", "resi 378+379+380+381+382+383+384 & chain A ")


cmd.select("Astrand7", "resi 394+395+396+397+398 & chain A ")


cmd.group("Strands", "*strand*")
cmd.select("barrel", "Astrand*")
cmd.pseudoatom ("PseudoH360A", pos=[13.182762,8.269155,16.489468])
cmd.pseudoatom ("PseudoH349A", pos=[12.391947,8.3836565,18.493614])
cmd.pseudoatom ("PseudoH358A", pos=[17.644892,7.5618324,21.415472])
cmd.pseudoatom ("PseudoH382A", pos=[10.105004,-3.6118865,8.78294])
cmd.pseudoatom ("PseudoH388A", pos=[12.043538,-4.283913,9.999346])
cmd.pseudoatom ("PseudoH380A", pos=[15.711074,-0.47630793,7.133232])
cmd.group("Pseudo_Hydrogens", "PseudoH*")
cmd.group("Pseudo_RGroups", "PseudoR*")
cmd.distance("StrongHBond", "resi 348 & chain A & name O", "resi 361 & chain A & name N")
cmd.distance("StrongHBond", "resi 348 & chain A & name N", "resi 361 & chain A & name O")
cmd.distance("StrongHBond", "resi 350 & chain A & name O", "resi 359 & chain A & name N")
cmd.distance("StrongHBond", "resi 350 & chain A & name N", "resi 359 & chain A & name O")
cmd.distance("StrongHBond", "resi 387 & chain A & name O", "resi 384 & chain A & name N")
cmd.distance("StrongHBond", "resi 387 & chain A & name N", "resi 384 & chain A & name O")
cmd.distance("StrongHBond", "resi 389 & chain A & name O", "resi 381 & chain A & name N")
cmd.distance("StrongHBond", "resi 389 & chain A & name N", "resi 381 & chain A & name O")
cmd.distance("WeakHBond", "resi 348 & chain A & name O", "PseudoH360A")
cmd.distance("WeakHBond", "resi 359 & chain A & name O", "PseudoH349A")
cmd.distance("WeakHBond", "resi 350 & chain A & name O", "PseudoH358A")
cmd.distance("WeakHBond", "resi 387 & chain A & name O", "PseudoH382A")
cmd.distance("WeakHBond", "resi 381 & chain A & name O", "PseudoH388A")
cmd.distance("WeakHBond", "resi 389 & chain A & name O", "PseudoH380A")
cmd.distance("NonHBond", "resi 349 & chain A & name CB", "resi 360 & chain A & name CB")
cmd.distance("NonHBond", "resi 351 & chain A & name CB", "resi 358 & chain A & name CB")
cmd.distance("NonHBond", "resi 388 & chain A & name CB", "resi 382 & chain A & name CB")
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
