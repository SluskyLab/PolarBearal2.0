from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EW3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 25-27 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 35-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 59-65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 71-79 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 82-92 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 98-102 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106-114 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 119-126 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 133-140 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 167-169 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
