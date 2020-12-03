from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Q03.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 32-42 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 46-60 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 63-76 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 79-92 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 95-102 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 108-109 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 114-122 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 127-136 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Bstrand9", "resi 8-26 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 32-42 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 46-60 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 63-76 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 79-92 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 95-102 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 108-109 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 115-122 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 127-134 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
