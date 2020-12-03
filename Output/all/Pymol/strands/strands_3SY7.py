from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 18-51 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 60-75 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 96-108 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 111-118 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 137-144 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 150-174 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 179-194 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 197-206 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 210-224 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 227-240 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 250-262 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 265-276 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 283-285 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 314-323 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 332-344 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 365-377 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 387-397 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 406-416 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
