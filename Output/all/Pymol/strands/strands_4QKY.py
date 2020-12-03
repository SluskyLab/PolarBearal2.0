from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4QKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 63-67 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 114-123 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 126-132 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 135-141 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 144-145 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 184-192 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 198-207 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 212-218 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 227-239 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 247-257 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 264-276 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 279-292 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 303-320 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 324-340 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 355-365 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 369-379 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 402-415 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 418-430 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 441-443 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 458-471 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 484-485 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 488-498 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 504-519 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 522-531 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 546-553 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
