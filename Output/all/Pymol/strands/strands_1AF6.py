from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AF6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40-53 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 56-68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 80-89 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 99-105 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 124-132 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 138-148 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 167-179 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 186-196 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 211-223 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 226-236 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 267-280 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 284-296 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 303-316 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 320-333 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 339-352 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 362-373 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 408-420 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Bstrand18", "resi 2-14 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 40-53 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 56-68 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 80-89 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 99-105 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 124-132 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 138-148 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 167-179 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 186-196 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 211-223 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 226-236 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 267-280 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 284-296 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 303-316 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 320-333 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 339-352 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 362-373 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 408-420 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Cstrand36", "resi 2-14 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 40-53 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 56-68 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 80-89 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 99-105 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 124-132 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 138-148 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 167-179 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 186-196 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 211-223 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 226-236 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 267-280 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 284-296 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 303-316 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 320-333 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 339-352 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 362-373 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 408-420 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
