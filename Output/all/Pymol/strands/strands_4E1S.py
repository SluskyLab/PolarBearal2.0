from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 212-219 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 225-236 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 240-251 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 254-266 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 271-281 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 286-297 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 300-309 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 314-315 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 323-326 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 329-338 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 341-353 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 371-382 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 385-394 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 398-410 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 446-448 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
