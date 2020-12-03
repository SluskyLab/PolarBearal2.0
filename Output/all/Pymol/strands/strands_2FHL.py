from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FHL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-12 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 17-20 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 28-34 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 47-53 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 61-67 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 74-83 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 89-98 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 111-120 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 208-212 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 217-220 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 228-234 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 247-253 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 261-267 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 274-283 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 289-298 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 311-320 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
