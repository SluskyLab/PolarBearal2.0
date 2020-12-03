from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X9K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 24-39 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 43-54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 65-79 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 83-97 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 106-121 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 126-138 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 149-160 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 166-177 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 188-196 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 204-218 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 233-243 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 248-259 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 268-279 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
