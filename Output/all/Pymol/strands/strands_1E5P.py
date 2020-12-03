from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1E5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-19 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 27-27 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 30-32 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 35-39 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 44-53 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 56-67 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 71-76 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 79-83 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 86-88 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 91-99 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 105-113 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 116-116 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 119-119 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 135-135 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 140-142 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 147-147 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Bstrand16", "resi 7-19 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 30-32 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 35-39 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 44-53 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 56-67 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 71-76 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 79-83 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 86-88 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 91-100 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 105-113 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 135-135 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 140-142 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 149-149 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Cstrand29", "resi 9-19 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 30-32 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 35-39 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 44-53 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 56-67 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 71-76 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 79-83 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 86-88 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 91-100 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 105-113 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 135-135 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 140-142 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 147-149 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Dstrand42", "resi 9-19 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 30-32 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 35-39 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 44-53 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 56-67 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 71-76 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Dstrand48", "resi 79-83 & chain D ")
cmd.color ("red", "Dstrand48")


cmd.select("Dstrand49", "resi 86-88 & chain D ")
cmd.color ("green", "Dstrand49")


cmd.select("Dstrand50", "resi 91-99 & chain D ")
cmd.color ("orange", "Dstrand50")


cmd.select("Dstrand51", "resi 105-113 & chain D ")
cmd.color ("teal", "Dstrand51")


cmd.select("Dstrand52", "resi 119-119 & chain D ")
cmd.color ("yellow", "Dstrand52")


cmd.select("Dstrand53", "resi 135-135 & chain D ")
cmd.color ("blue", "Dstrand53")


cmd.select("Dstrand54", "resi 140-142 & chain D ")
cmd.color ("red", "Dstrand54")


cmd.select("Dstrand55", "resi 147-149 & chain D ")
cmd.color ("green", "Dstrand55")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
