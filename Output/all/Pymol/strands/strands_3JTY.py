from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3JTY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 38-52 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 61-74 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 82-97 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 119-131 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 134-141 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 144-145 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 148-149 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 159-167 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 173-184 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 194-196 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 199-204 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 207-216 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 221-230 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 234-247 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 250-263 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 273-285 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 288-299 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 329-338 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 347-359 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 367-379 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 389-399 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 406-418 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Bstrand22", "resi 38-52 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 61-74 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 82-97 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 119-131 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 134-141 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 144-145 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 148-149 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 159-167 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 173-184 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 194-196 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 199-204 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 207-216 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 221-230 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 234-246 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 251-263 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 273-285 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 288-299 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 329-338 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 347-361 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 364-379 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 389-399 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 406-418 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Cstrand44", "resi 38-52 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 61-74 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 82-97 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 119-131 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 134-141 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 144-145 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 148-149 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 159-167 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 173-184 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 194-196 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 199-204 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 207-216 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 221-230 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 234-246 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 251-263 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 273-285 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("Cstrand60", "resi 288-298 & chain C ")
cmd.color ("red", "Cstrand60")


cmd.select("Cstrand61", "resi 329-338 & chain C ")
cmd.color ("green", "Cstrand61")


cmd.select("Cstrand62", "resi 347-360 & chain C ")
cmd.color ("orange", "Cstrand62")


cmd.select("Cstrand63", "resi 365-379 & chain C ")
cmd.color ("teal", "Cstrand63")


cmd.select("Cstrand64", "resi 389-399 & chain C ")
cmd.color ("yellow", "Cstrand64")


cmd.select("Cstrand65", "resi 406-418 & chain C ")
cmd.color ("blue", "Cstrand65")


cmd.select("Dstrand66", "resi 38-52 & chain D ")
cmd.color ("red", "Dstrand66")


cmd.select("Dstrand67", "resi 61-74 & chain D ")
cmd.color ("green", "Dstrand67")


cmd.select("Dstrand68", "resi 82-97 & chain D ")
cmd.color ("orange", "Dstrand68")


cmd.select("Dstrand69", "resi 119-131 & chain D ")
cmd.color ("teal", "Dstrand69")


cmd.select("Dstrand70", "resi 134-141 & chain D ")
cmd.color ("yellow", "Dstrand70")


cmd.select("Dstrand71", "resi 144-145 & chain D ")
cmd.color ("blue", "Dstrand71")


cmd.select("Dstrand72", "resi 148-149 & chain D ")
cmd.color ("red", "Dstrand72")


cmd.select("Dstrand73", "resi 159-167 & chain D ")
cmd.color ("green", "Dstrand73")


cmd.select("Dstrand74", "resi 173-184 & chain D ")
cmd.color ("orange", "Dstrand74")


cmd.select("Dstrand75", "resi 194-195 & chain D ")
cmd.color ("teal", "Dstrand75")


cmd.select("Dstrand76", "resi 203-204 & chain D ")
cmd.color ("yellow", "Dstrand76")


cmd.select("Dstrand77", "resi 207-215 & chain D ")
cmd.color ("blue", "Dstrand77")


cmd.select("Dstrand78", "resi 221-230 & chain D ")
cmd.color ("red", "Dstrand78")


cmd.select("Dstrand79", "resi 234-247 & chain D ")
cmd.color ("green", "Dstrand79")


cmd.select("Dstrand80", "resi 250-263 & chain D ")
cmd.color ("orange", "Dstrand80")


cmd.select("Dstrand81", "resi 273-285 & chain D ")
cmd.color ("teal", "Dstrand81")


cmd.select("Dstrand82", "resi 288-299 & chain D ")
cmd.color ("yellow", "Dstrand82")


cmd.select("Dstrand83", "resi 329-338 & chain D ")
cmd.color ("blue", "Dstrand83")


cmd.select("Dstrand84", "resi 347-359 & chain D ")
cmd.color ("red", "Dstrand84")


cmd.select("Dstrand85", "resi 367-379 & chain D ")
cmd.color ("green", "Dstrand85")


cmd.select("Dstrand86", "resi 389-399 & chain D ")
cmd.color ("orange", "Dstrand86")


cmd.select("Dstrand87", "resi 406-418 & chain D ")
cmd.color ("teal", "Dstrand87")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
