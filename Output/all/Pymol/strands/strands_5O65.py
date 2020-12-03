from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5O65.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 108-119 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 144-160 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 164-203 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 207-215 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 223-231 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 266-277 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 280-291 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 294-296 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 309-312 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 316-326 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 331-342 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 345-349 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 355-357 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 362-374 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 380-388 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 396-405 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Bstrand16", "resi 108-119 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 144-160 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 164-180 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 194-203 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 207-215 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 223-231 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 243-244 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 254-255 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 266-277 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 280-291 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 294-296 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 309-312 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 316-326 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 331-342 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 345-349 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 355-357 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 362-374 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 380-388 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 396-404 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Cstrand35", "resi 108-120 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 145-160 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 164-179 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 195-203 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 207-215 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 223-231 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 243-244 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 254-255 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 266-277 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 280-291 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 294-296 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 309-312 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 316-326 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 331-342 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 346-349 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 355-356 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 362-374 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 380-388 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 396-405 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
