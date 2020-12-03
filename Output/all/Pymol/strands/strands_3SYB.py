from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 43-90 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 98-111 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 137-150 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 153-160 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 163-164 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 167-168 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 178-189 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 192-203 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 227-237 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 240-249 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 253-264 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 272-284 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 294-306 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 309-319 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 349-358 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 367-380 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 402-416 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 426-436 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 445-457 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
