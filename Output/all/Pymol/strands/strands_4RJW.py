from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RJW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 18-22 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 28-42 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 53-69 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 73-80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 93-100 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 107-112 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 150-158 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 162-174 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 180-195 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 198-210 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 234-235 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 257-271 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 274-287 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 295-307 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 315-316 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 321-322 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 334-348 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 363-375 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 380-392 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 402-413 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
