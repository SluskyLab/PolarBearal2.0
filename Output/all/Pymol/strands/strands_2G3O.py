from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2G3O.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 17-28 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 33-40 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 83-91 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 96-105 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 109-119 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 132-135 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 138-144 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 149-160 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 165-176 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 191-199 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 205-215 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 4-14 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 17-28 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 33-40 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 83-91 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 96-105 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 109-117 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 132-135 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 138-145 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 149-160 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 165-176 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 191-199 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 205-215 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Cstrand24", "resi 4-14 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 17-28 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 33-40 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 83-91 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 96-105 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 109-119 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 132-135 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 138-144 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 149-160 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 165-176 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 191-199 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 205-215 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Dstrand36", "resi 4-14 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 17-28 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 33-40 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 83-91 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 96-105 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 109-119 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 132-135 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 138-144 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 149-160 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 165-176 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 191-199 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 205-215 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Estrand48", "resi 4-14 & chain E ")
cmd.color ("red", "Estrand48")


cmd.select("Estrand49", "resi 17-28 & chain E ")
cmd.color ("green", "Estrand49")


cmd.select("Estrand50", "resi 33-40 & chain E ")
cmd.color ("orange", "Estrand50")


cmd.select("Estrand51", "resi 83-91 & chain E ")
cmd.color ("teal", "Estrand51")


cmd.select("Estrand52", "resi 96-105 & chain E ")
cmd.color ("yellow", "Estrand52")


cmd.select("Estrand53", "resi 109-119 & chain E ")
cmd.color ("blue", "Estrand53")


cmd.select("Estrand54", "resi 132-135 & chain E ")
cmd.color ("red", "Estrand54")


cmd.select("Estrand55", "resi 138-144 & chain E ")
cmd.color ("green", "Estrand55")


cmd.select("Estrand56", "resi 149-160 & chain E ")
cmd.color ("orange", "Estrand56")


cmd.select("Estrand57", "resi 165-176 & chain E ")
cmd.color ("teal", "Estrand57")


cmd.select("Estrand58", "resi 191-199 & chain E ")
cmd.color ("yellow", "Estrand58")


cmd.select("Estrand59", "resi 205-215 & chain E ")
cmd.color ("blue", "Estrand59")


cmd.select("Fstrand60", "resi 4-14 & chain F ")
cmd.color ("red", "Fstrand60")


cmd.select("Fstrand61", "resi 17-28 & chain F ")
cmd.color ("green", "Fstrand61")


cmd.select("Fstrand62", "resi 33-40 & chain F ")
cmd.color ("orange", "Fstrand62")


cmd.select("Fstrand63", "resi 83-91 & chain F ")
cmd.color ("teal", "Fstrand63")


cmd.select("Fstrand64", "resi 96-105 & chain F ")
cmd.color ("yellow", "Fstrand64")


cmd.select("Fstrand65", "resi 109-119 & chain F ")
cmd.color ("blue", "Fstrand65")


cmd.select("Fstrand66", "resi 132-135 & chain F ")
cmd.color ("red", "Fstrand66")


cmd.select("Fstrand67", "resi 138-144 & chain F ")
cmd.color ("green", "Fstrand67")


cmd.select("Fstrand68", "resi 149-160 & chain F ")
cmd.color ("orange", "Fstrand68")


cmd.select("Fstrand69", "resi 165-176 & chain F ")
cmd.color ("teal", "Fstrand69")


cmd.select("Fstrand70", "resi 191-199 & chain F ")
cmd.color ("yellow", "Fstrand70")


cmd.select("Fstrand71", "resi 205-215 & chain F ")
cmd.color ("blue", "Fstrand71")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
