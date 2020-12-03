from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 28-31 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 74-79 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 82-87 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 93-99 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 147-156 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 162-171 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 175-176 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 180-182 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 239-243 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 252-253 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 256-259 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 322-328 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 335-341 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 353-354 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 397-403 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 413-419 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 425-433 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 437-449 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 454-462 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 466-479 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 483-494 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 507-520 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 526-539 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 564-580 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 591-600 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 609-620 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 626-635 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 670-673 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 677-680 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 685-695 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 706-718 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 749-759 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 764-773 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 784-789 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
