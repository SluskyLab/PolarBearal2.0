from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AUI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40-47 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 54-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 78-83 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 86-94 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 124-135 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 138-145 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 157-165 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 169-178 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 185-198 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 201-214 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 221-234 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 242-248 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 262-272 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 277-289 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 293-307 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Bstrand16", "resi 2-19 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 40-47 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 54-62 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 78-82 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 87-94 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 124-135 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 138-145 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 157-165 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 169-181 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 184-198 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 201-214 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 221-234 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 242-248 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 262-272 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 277-289 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 294-307 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Cstrand32", "resi 2-19 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 40-47 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 54-62 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 78-82 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 87-94 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 124-135 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 138-145 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 157-165 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 169-181 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 184-198 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 201-214 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 221-234 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 242-248 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 262-272 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 277-289 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 294-307 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
