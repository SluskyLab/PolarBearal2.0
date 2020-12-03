from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2MAF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 43-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 55-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 65-71 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 89-90 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 115-124 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 131-142 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 191-201 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 206-212 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 230-237 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
