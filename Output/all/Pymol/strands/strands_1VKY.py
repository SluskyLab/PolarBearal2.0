from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 27-32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 37-42 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 55-63 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 67-70 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 78-87 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 90-96 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106-110 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 113-120 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 126-131 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 193-201 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 223-226 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 244-247 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 267-269 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 286-290 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 331-334 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Bstrand15", "resi 27-32 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 37-42 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 55-63 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 67-71 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 77-87 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 90-96 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 106-110 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 113-120 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 126-131 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 193-201 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 222-226 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 244-247 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 267-269 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 286-290 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 331-334 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
