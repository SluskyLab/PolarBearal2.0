from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1NYC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-10 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 29-33 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 38-45 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 52-59 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 64-69 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 72-83 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 86-93 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 103-107 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 2-10 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 29-33 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 38-44 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 52-59 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 64-69 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 72-83 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 86-93 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 103-107 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
