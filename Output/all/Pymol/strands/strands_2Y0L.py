from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y0L.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 21-33 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 42-52 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 62-111 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 114-121 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 129-130 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 139-147 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 153-164 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 191-198 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 204-213 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 217-229 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 234-246 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 256-268 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 271-281 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 292-293 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 311-320 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 329-339 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 352-362 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 372-382 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 388-400 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
