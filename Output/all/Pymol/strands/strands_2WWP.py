from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WWP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 41-50 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 65-71 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 77-85 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 88-98 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-109 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 114-123 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 128-137 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 144-150 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 177-179 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Bstrand9", "resi 41-50 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 65-71 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 77-85 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 88-98 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 104-109 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 114-123 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 128-137 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 144-150 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 177-179 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
