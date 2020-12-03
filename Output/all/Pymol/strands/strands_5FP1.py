from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FP1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 40-44 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 68-69 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 82-84 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 87-88 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 93-95 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 98-99 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 111-118 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 132-138 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 231-235 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 240-245 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 312-338 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 343-365 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 371-372 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 388-390 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 597-600 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 603-606 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 647-648 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 656-657 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 690-693 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 698-701 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
