from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QFT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 30-34 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 50-54 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 62-69 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 78-87 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 97-102 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 107-116 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 119-124 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 133-138 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 30-34 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 50-57 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 62-69 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 78-87 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 97-102 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 107-116 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 119-124 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 133-138 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
