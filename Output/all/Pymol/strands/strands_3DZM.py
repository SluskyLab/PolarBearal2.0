from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DZM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3-13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 16-25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 33-43 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 69-83 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 93-110 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 120-141 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 144-155 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 160-165 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 171-176 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 195-206 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Bstrand10", "resi 3-13 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 16-25 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 33-43 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 69-83 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 93-110 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 120-141 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 144-155 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 160-165 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 171-176 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 195-206 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Cstrand20", "resi 4-13 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 16-24 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 33-43 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 69-83 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 93-110 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 120-141 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 144-155 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 160-165 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 171-176 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 195-206 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
