from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5O8O.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 67-76 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 79-85 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 95-102 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 105-113 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 117-124 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131-137 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 143-151 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 155-162 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 166-167 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 170-182 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 187-197 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 204-215 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 220-225 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 231-238 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 243-252 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 266-275 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 280-288 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 291-299 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 305-314 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 319-329 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
