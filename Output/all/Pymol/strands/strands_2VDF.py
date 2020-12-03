from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2VDF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 9-23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48-65 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 85-103 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 106-122 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131-150 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 153-171 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 182-185 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 188-200 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 206-218 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 240-252 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
