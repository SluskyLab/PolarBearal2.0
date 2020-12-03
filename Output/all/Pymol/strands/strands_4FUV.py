from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FUV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 20-26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 29-39 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 42-56 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 64-81 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 95-114 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 119-122 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 125-129 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 134-154 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 162-172 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 177-183 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 186-187 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 213-224 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
