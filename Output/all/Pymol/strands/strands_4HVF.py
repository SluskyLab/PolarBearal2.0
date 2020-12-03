from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4HVF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 18-29 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 34-41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 85-93 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 98-108 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 111-121 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 134-137 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 140-148 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 151-162 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 168-178 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 192-202 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 206-216 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 6-15 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 18-29 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 34-41 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 66-67 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 71-72 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 85-93 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 98-108 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 111-121 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 134-137 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 140-148 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 151-162 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 168-178 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 192-202 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 206-216 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Cstrand26", "resi 6-15 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 18-29 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 34-41 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 85-93 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 98-108 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 111-121 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 134-137 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 140-148 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 151-162 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 168-178 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 192-202 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 206-216 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Dstrand38", "resi 6-15 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 18-29 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 34-41 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 85-93 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 98-108 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 111-121 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 134-137 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 140-148 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 151-162 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 167-178 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Dstrand48", "resi 192-202 & chain D ")
cmd.color ("red", "Dstrand48")


cmd.select("Dstrand49", "resi 206-216 & chain D ")
cmd.color ("green", "Dstrand49")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
