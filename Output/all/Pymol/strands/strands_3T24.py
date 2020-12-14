from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3T24.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 58-66 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 89-101 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-111 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 129-137 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 150-161 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 185-195 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 198-207 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 211-225 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 228-260 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 263-273 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 303-312 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 321-334 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 341-354 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 364-374 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 379-392 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Bstrand17", "resi 7-22 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 29-43 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 58-66 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 88-101 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 104-111 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 129-137 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 150-161 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 185-195 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 198-207 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 211-223 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 228-260 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 263-273 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 303-312 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 321-333 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 342-354 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 364-374 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 379-392 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Cstrand34", "resi 7-23 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 26-27 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 32-43 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 58-61 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 91-101 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 104-111 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 129-137 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 150-161 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 185-193 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 198-207 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 211-225 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 228-260 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 263-273 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 303-312 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 321-334 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 341-354 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 364-374 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 379-392 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
