from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T0S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 30-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 51-64 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 87-101 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-111 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 114-115 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 118-119 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 129-137 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 143-154 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 178-186 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 191-200 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 204-216 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 221-234 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 244-256 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 259-269 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 300-309 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 318-330 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 339-351 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 361-371 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 376-390 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
