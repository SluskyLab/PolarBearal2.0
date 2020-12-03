from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4UU3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 15-21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26-33 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 36-41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 50-62 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 65-71 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 77-83 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 88-95 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 130-143 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 15-21 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 26-33 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 36-41 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 50-62 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 65-71 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 77-83 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 88-95 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 130-143 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
