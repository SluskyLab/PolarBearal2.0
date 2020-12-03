from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5L8I.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 5-13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 37-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 47-54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59-65 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 69-72 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 80-87 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 90-95 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 98-104 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 108-115 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 118-126 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Bstrand10", "resi 5-13 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 37-44 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 47-54 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 58-65 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 69-73 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 79-87 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 90-95 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 98-105 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 108-115 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 118-126 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Cstrand20", "resi 5-13 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 38-44 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 47-54 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 58-65 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 69-71 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 81-87 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 90-95 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 98-105 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 108-114 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 119-126 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
