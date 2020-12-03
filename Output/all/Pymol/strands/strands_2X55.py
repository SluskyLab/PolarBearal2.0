from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X55.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14-32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39-62 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 65-74 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 97-122 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 126-144 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 164-185 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 188-208 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 213-236 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 239-250 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 275-292 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
