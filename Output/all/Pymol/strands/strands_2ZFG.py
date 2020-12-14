from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZFG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-6 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 9-23 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 36-37 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 40-50 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 55-66 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 80-90 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 94-102 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 132-141 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 151-158 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 173-182 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 185-195 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 210-222 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 225-235 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 239-242 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 247-250 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 253-263 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 269-283 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 287-304 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 307-316 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 331-339 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
