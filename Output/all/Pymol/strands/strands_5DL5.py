from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14-28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 35-47 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 55-68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 91-103 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 106-113 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 116-117 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 120-121 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 131-142 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 145-156 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 175-185 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 188-197 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 201-214 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 218-231 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 258-271 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 274-285 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 317-326 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 336-350 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 354-369 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 379-389 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 401-414 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")