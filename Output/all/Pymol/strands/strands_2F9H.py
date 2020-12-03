from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F9H.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4-12 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 23-27 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 40-43 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 57-60 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 63-70 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 84-87 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 102-106 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 118-122 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 6-12 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 23-27 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 39-43 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 57-60 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 63-70 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 84-87 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 102-106 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 118-122 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
