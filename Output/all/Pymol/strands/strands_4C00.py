from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4C00.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 26-29 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 78-82 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 94-99 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 105-114 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 162-171 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 176-184 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 193-197 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 236-243 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 256-262 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 267-276 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 280-288 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 297-305 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 308-318 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 326-339 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 342-357 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 361-376 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 379-398 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 404-416 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 426-439 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 442-456 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 497-511 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 514-526 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 535-546 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 549-558 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 568-573 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
