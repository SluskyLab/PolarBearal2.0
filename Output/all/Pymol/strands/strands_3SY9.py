from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14-28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 37-48 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 56-69 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 100-112 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 115-122 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 125-126 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 129-130 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 141-148 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 154-163 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 189-201 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 204-213 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 217-229 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 234-247 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 257-269 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 272-282 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 313-322 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 331-341 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 366-377 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 387-398 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 408-421 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Bstrand20", "resi 14-28 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 37-48 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 57-69 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 100-112 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 115-122 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 141-151 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 154-163 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 189-198 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 204-213 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 217-229 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 234-247 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 257-269 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 272-282 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 313-322 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 331-341 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 366-377 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 387-398 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 408-421 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Cstrand38", "resi 14-27 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 37-48 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 57-69 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 100-112 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 115-122 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 125-126 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 129-130 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 141-148 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 154-163 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 189-198 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 204-213 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 217-229 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 234-247 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 257-269 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 272-282 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 313-322 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 331-341 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 366-377 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 387-398 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 408-420 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Dstrand58", "resi 14-27 & chain D ")
cmd.color ("yellow", "Dstrand58")


cmd.select("Dstrand59", "resi 38-48 & chain D ")
cmd.color ("blue", "Dstrand59")


cmd.select("Dstrand60", "resi 57-69 & chain D ")
cmd.color ("red", "Dstrand60")


cmd.select("Dstrand61", "resi 100-112 & chain D ")
cmd.color ("green", "Dstrand61")


cmd.select("Dstrand62", "resi 115-122 & chain D ")
cmd.color ("orange", "Dstrand62")


cmd.select("Dstrand63", "resi 125-126 & chain D ")
cmd.color ("teal", "Dstrand63")


cmd.select("Dstrand64", "resi 129-130 & chain D ")
cmd.color ("yellow", "Dstrand64")


cmd.select("Dstrand65", "resi 141-148 & chain D ")
cmd.color ("blue", "Dstrand65")


cmd.select("Dstrand66", "resi 154-163 & chain D ")
cmd.color ("red", "Dstrand66")


cmd.select("Dstrand67", "resi 189-198 & chain D ")
cmd.color ("green", "Dstrand67")


cmd.select("Dstrand68", "resi 205-213 & chain D ")
cmd.color ("orange", "Dstrand68")


cmd.select("Dstrand69", "resi 217-225 & chain D ")
cmd.color ("teal", "Dstrand69")


cmd.select("Dstrand70", "resi 228-229 & chain D ")
cmd.color ("yellow", "Dstrand70")


cmd.select("Dstrand71", "resi 234-247 & chain D ")
cmd.color ("blue", "Dstrand71")


cmd.select("Dstrand72", "resi 257-269 & chain D ")
cmd.color ("red", "Dstrand72")


cmd.select("Dstrand73", "resi 272-282 & chain D ")
cmd.color ("green", "Dstrand73")


cmd.select("Dstrand74", "resi 313-322 & chain D ")
cmd.color ("orange", "Dstrand74")


cmd.select("Dstrand75", "resi 331-341 & chain D ")
cmd.color ("teal", "Dstrand75")


cmd.select("Dstrand76", "resi 366-377 & chain D ")
cmd.color ("yellow", "Dstrand76")


cmd.select("Dstrand77", "resi 387-397 & chain D ")
cmd.color ("blue", "Dstrand77")


cmd.select("Dstrand78", "resi 408-421 & chain D ")
cmd.color ("red", "Dstrand78")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
