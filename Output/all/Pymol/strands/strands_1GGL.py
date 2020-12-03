from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GGL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48-54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 60-65 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 70-73 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 81-88 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 93-98 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 105-111 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 114-121 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 124-132 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Bstrand10", "resi 6-14 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 39-45 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 48-54 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 59-65 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 70-73 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 81-88 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 93-98 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 105-111 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 114-121 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 124-132 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
