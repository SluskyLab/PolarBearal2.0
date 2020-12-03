from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4D5B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22-37 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 43-60 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 65-80 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 83-103 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 106-122 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 127-146 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 151-165 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 171-187 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 190-206 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 212-230 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 236-250 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 262-278 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 282-297 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 309-323 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Bstrand14", "resi 22-37 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 43-60 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 65-80 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 83-103 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 106-122 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 127-146 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 151-165 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 171-187 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 190-206 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 212-230 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 236-250 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 262-278 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 282-297 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 309-323 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
