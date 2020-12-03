from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F1V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-16 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 32-33 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 36-46 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 51-58 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 61-67 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 71-79 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 82-88 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 96-114 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 123-128 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 131-143 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 148-157 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 160-167 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 174-177 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 181-191 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Bstrand14", "resi 6-16 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 32-33 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 36-46 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 51-58 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 61-67 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 71-79 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 82-88 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 96-114 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 123-128 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 131-143 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 148-157 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 160-167 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 174-177 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 181-191 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Cstrand28", "resi 6-16 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 32-33 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 36-46 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 51-58 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 61-67 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 71-79 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 82-88 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 96-114 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 123-128 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 131-143 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 148-157 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 160-167 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 174-177 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 181-191 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Dstrand42", "resi 6-16 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 32-33 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 36-46 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 51-58 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 61-67 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 71-79 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Dstrand48", "resi 82-88 & chain D ")
cmd.color ("red", "Dstrand48")


cmd.select("Dstrand49", "resi 96-114 & chain D ")
cmd.color ("green", "Dstrand49")


cmd.select("Dstrand50", "resi 123-128 & chain D ")
cmd.color ("orange", "Dstrand50")


cmd.select("Dstrand51", "resi 131-143 & chain D ")
cmd.color ("teal", "Dstrand51")


cmd.select("Dstrand52", "resi 148-157 & chain D ")
cmd.color ("yellow", "Dstrand52")


cmd.select("Dstrand53", "resi 160-167 & chain D ")
cmd.color ("blue", "Dstrand53")


cmd.select("Dstrand54", "resi 174-177 & chain D ")
cmd.color ("red", "Dstrand54")


cmd.select("Dstrand55", "resi 181-191 & chain D ")
cmd.color ("green", "Dstrand55")


cmd.select("Estrand56", "resi 6-16 & chain E ")
cmd.color ("orange", "Estrand56")


cmd.select("Estrand57", "resi 32-33 & chain E ")
cmd.color ("teal", "Estrand57")


cmd.select("Estrand58", "resi 36-46 & chain E ")
cmd.color ("yellow", "Estrand58")


cmd.select("Estrand59", "resi 51-58 & chain E ")
cmd.color ("blue", "Estrand59")


cmd.select("Estrand60", "resi 61-67 & chain E ")
cmd.color ("red", "Estrand60")


cmd.select("Estrand61", "resi 71-79 & chain E ")
cmd.color ("green", "Estrand61")


cmd.select("Estrand62", "resi 82-88 & chain E ")
cmd.color ("orange", "Estrand62")


cmd.select("Estrand63", "resi 96-114 & chain E ")
cmd.color ("teal", "Estrand63")


cmd.select("Estrand64", "resi 123-128 & chain E ")
cmd.color ("yellow", "Estrand64")


cmd.select("Estrand65", "resi 131-143 & chain E ")
cmd.color ("blue", "Estrand65")


cmd.select("Estrand66", "resi 148-157 & chain E ")
cmd.color ("red", "Estrand66")


cmd.select("Estrand67", "resi 160-167 & chain E ")
cmd.color ("green", "Estrand67")


cmd.select("Estrand68", "resi 174-177 & chain E ")
cmd.color ("orange", "Estrand68")


cmd.select("Estrand69", "resi 181-191 & chain E ")
cmd.color ("teal", "Estrand69")


cmd.select("Fstrand70", "resi 6-16 & chain F ")
cmd.color ("yellow", "Fstrand70")


cmd.select("Fstrand71", "resi 32-33 & chain F ")
cmd.color ("blue", "Fstrand71")


cmd.select("Fstrand72", "resi 36-46 & chain F ")
cmd.color ("red", "Fstrand72")


cmd.select("Fstrand73", "resi 51-58 & chain F ")
cmd.color ("green", "Fstrand73")


cmd.select("Fstrand74", "resi 61-67 & chain F ")
cmd.color ("orange", "Fstrand74")


cmd.select("Fstrand75", "resi 71-79 & chain F ")
cmd.color ("teal", "Fstrand75")


cmd.select("Fstrand76", "resi 82-88 & chain F ")
cmd.color ("yellow", "Fstrand76")


cmd.select("Fstrand77", "resi 96-114 & chain F ")
cmd.color ("blue", "Fstrand77")


cmd.select("Fstrand78", "resi 123-128 & chain F ")
cmd.color ("red", "Fstrand78")


cmd.select("Fstrand79", "resi 131-143 & chain F ")
cmd.color ("green", "Fstrand79")


cmd.select("Fstrand80", "resi 148-157 & chain F ")
cmd.color ("orange", "Fstrand80")


cmd.select("Fstrand81", "resi 160-167 & chain F ")
cmd.color ("teal", "Fstrand81")


cmd.select("Fstrand82", "resi 174-177 & chain F ")
cmd.color ("yellow", "Fstrand82")


cmd.select("Fstrand83", "resi 181-191 & chain F ")
cmd.color ("blue", "Fstrand83")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
