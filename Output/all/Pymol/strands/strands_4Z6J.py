from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Z6J.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 18-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 27-34 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 41-49 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 61-69 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 74-82 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 87-99 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106-117 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 120-132 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 18-22 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 27-34 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 41-49 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 61-69 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 74-82 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 87-99 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 106-116 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 121-132 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
