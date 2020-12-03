from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FGR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3-17 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26-31 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 38-48 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 51-60 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 76-83 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 86-90 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 93-94 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 133-134 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 137-141 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 148-155 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 171-179 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 183-196 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 199-213 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 218-230 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 235-249 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 253-264 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 269-281 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 286-297 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 320-331 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
