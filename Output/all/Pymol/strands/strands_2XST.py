from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2XST.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 35-44 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 59-65 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 71-76 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 85-92 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 98-101 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 106-114 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 119-128 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 131-140 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
