from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EI5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 348+349+350+351 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 358+359+360+361+362+363 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 411+412+413+414+415+416+417 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 368+369+370+371+372 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 401+402+403+404+405+406 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 387+388+389 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 378+379+380+381+382+383+384 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 394+395+396+397+398 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
