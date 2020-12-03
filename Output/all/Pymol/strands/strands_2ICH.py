from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 47-57 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 63-73 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 89-98 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 106-114 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 121-123 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 127-130 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 133-137 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 143-148 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 152-159 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 165-166 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 172-174 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 182-199 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 203-217 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 225-235 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 240-248 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 253-261 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 267-270 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 275-284 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 291-300 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 303-309 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 315-317 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 325-335 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 338-348 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Bstrand23", "resi 47-57 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 63-73 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 89-98 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 106-114 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 121-123 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 127-130 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 133-137 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 143-148 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 152-159 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 165-166 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 172-174 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 182-199 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 202-217 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 225-235 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 240-248 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 253-261 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 267-270 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 275-284 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 291-300 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 303-309 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 315-317 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 325-335 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 338-348 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
