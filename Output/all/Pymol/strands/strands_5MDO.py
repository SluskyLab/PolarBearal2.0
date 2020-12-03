from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5MDO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 20-35 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 47-52 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 55-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 70-76 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 96-102 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 106-114 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 148-156 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 164-172 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 184-194 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 197-211 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 214-228 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 233-246 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 251-265 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 268-277 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 281-282 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 285-286 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 292-304 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 307-317 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 338-349 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Bstrand19", "resi 20-35 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 47-52 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 55-62 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 70-76 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 96-102 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 106-114 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 148-156 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 164-172 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 184-194 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 197-211 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 214-228 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 233-246 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 251-265 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 268-277 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 281-282 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 285-286 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 292-304 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 307-317 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 338-349 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Cstrand38", "resi 20-35 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 47-52 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 55-62 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 70-76 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 96-102 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 106-114 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 148-156 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 164-172 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 184-194 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 197-211 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 214-228 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 233-246 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 251-265 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 268-277 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 281-282 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 285-286 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 292-304 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 307-317 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 338-349 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Dstrand57", "resi 20-35 & chain D ")
cmd.color ("teal", "Dstrand57")


cmd.select("Dstrand58", "resi 47-52 & chain D ")
cmd.color ("yellow", "Dstrand58")


cmd.select("Dstrand59", "resi 55-62 & chain D ")
cmd.color ("blue", "Dstrand59")


cmd.select("Dstrand60", "resi 70-76 & chain D ")
cmd.color ("red", "Dstrand60")


cmd.select("Dstrand61", "resi 96-102 & chain D ")
cmd.color ("green", "Dstrand61")


cmd.select("Dstrand62", "resi 106-114 & chain D ")
cmd.color ("orange", "Dstrand62")


cmd.select("Dstrand63", "resi 148-156 & chain D ")
cmd.color ("teal", "Dstrand63")


cmd.select("Dstrand64", "resi 164-172 & chain D ")
cmd.color ("yellow", "Dstrand64")


cmd.select("Dstrand65", "resi 184-194 & chain D ")
cmd.color ("blue", "Dstrand65")


cmd.select("Dstrand66", "resi 197-211 & chain D ")
cmd.color ("red", "Dstrand66")


cmd.select("Dstrand67", "resi 214-228 & chain D ")
cmd.color ("green", "Dstrand67")


cmd.select("Dstrand68", "resi 233-246 & chain D ")
cmd.color ("orange", "Dstrand68")


cmd.select("Dstrand69", "resi 251-265 & chain D ")
cmd.color ("teal", "Dstrand69")


cmd.select("Dstrand70", "resi 268-277 & chain D ")
cmd.color ("yellow", "Dstrand70")


cmd.select("Dstrand71", "resi 281-282 & chain D ")
cmd.color ("blue", "Dstrand71")


cmd.select("Dstrand72", "resi 285-286 & chain D ")
cmd.color ("red", "Dstrand72")


cmd.select("Dstrand73", "resi 292-304 & chain D ")
cmd.color ("green", "Dstrand73")


cmd.select("Dstrand74", "resi 307-317 & chain D ")
cmd.color ("orange", "Dstrand74")


cmd.select("Dstrand75", "resi 338-349 & chain D ")
cmd.color ("teal", "Dstrand75")


cmd.select("Estrand76", "resi 20-35 & chain E ")
cmd.color ("yellow", "Estrand76")


cmd.select("Estrand77", "resi 47-52 & chain E ")
cmd.color ("blue", "Estrand77")


cmd.select("Estrand78", "resi 55-62 & chain E ")
cmd.color ("red", "Estrand78")


cmd.select("Estrand79", "resi 70-76 & chain E ")
cmd.color ("green", "Estrand79")


cmd.select("Estrand80", "resi 96-102 & chain E ")
cmd.color ("orange", "Estrand80")


cmd.select("Estrand81", "resi 106-114 & chain E ")
cmd.color ("teal", "Estrand81")


cmd.select("Estrand82", "resi 148-156 & chain E ")
cmd.color ("yellow", "Estrand82")


cmd.select("Estrand83", "resi 164-172 & chain E ")
cmd.color ("blue", "Estrand83")


cmd.select("Estrand84", "resi 184-194 & chain E ")
cmd.color ("red", "Estrand84")


cmd.select("Estrand85", "resi 197-211 & chain E ")
cmd.color ("green", "Estrand85")


cmd.select("Estrand86", "resi 214-228 & chain E ")
cmd.color ("orange", "Estrand86")


cmd.select("Estrand87", "resi 233-246 & chain E ")
cmd.color ("teal", "Estrand87")


cmd.select("Estrand88", "resi 251-265 & chain E ")
cmd.color ("yellow", "Estrand88")


cmd.select("Estrand89", "resi 268-277 & chain E ")
cmd.color ("blue", "Estrand89")


cmd.select("Estrand90", "resi 281-282 & chain E ")
cmd.color ("red", "Estrand90")


cmd.select("Estrand91", "resi 285-286 & chain E ")
cmd.color ("green", "Estrand91")


cmd.select("Estrand92", "resi 292-304 & chain E ")
cmd.color ("orange", "Estrand92")


cmd.select("Estrand93", "resi 307-317 & chain E ")
cmd.color ("teal", "Estrand93")


cmd.select("Estrand94", "resi 338-349 & chain E ")
cmd.color ("yellow", "Estrand94")


cmd.select("Fstrand95", "resi 20-35 & chain F ")
cmd.color ("blue", "Fstrand95")


cmd.select("Fstrand96", "resi 47-52 & chain F ")
cmd.color ("red", "Fstrand96")


cmd.select("Fstrand97", "resi 55-62 & chain F ")
cmd.color ("green", "Fstrand97")


cmd.select("Fstrand98", "resi 70-76 & chain F ")
cmd.color ("orange", "Fstrand98")


cmd.select("Fstrand99", "resi 96-102 & chain F ")
cmd.color ("teal", "Fstrand99")


cmd.select("Fstrand100", "resi 106-114 & chain F ")
cmd.color ("yellow", "Fstrand100")


cmd.select("Fstrand101", "resi 148-156 & chain F ")
cmd.color ("blue", "Fstrand101")


cmd.select("Fstrand102", "resi 164-172 & chain F ")
cmd.color ("red", "Fstrand102")


cmd.select("Fstrand103", "resi 184-194 & chain F ")
cmd.color ("green", "Fstrand103")


cmd.select("Fstrand104", "resi 197-211 & chain F ")
cmd.color ("orange", "Fstrand104")


cmd.select("Fstrand105", "resi 214-228 & chain F ")
cmd.color ("teal", "Fstrand105")


cmd.select("Fstrand106", "resi 233-246 & chain F ")
cmd.color ("yellow", "Fstrand106")


cmd.select("Fstrand107", "resi 251-265 & chain F ")
cmd.color ("blue", "Fstrand107")


cmd.select("Fstrand108", "resi 268-277 & chain F ")
cmd.color ("red", "Fstrand108")


cmd.select("Fstrand109", "resi 281-282 & chain F ")
cmd.color ("green", "Fstrand109")


cmd.select("Fstrand110", "resi 285-286 & chain F ")
cmd.color ("orange", "Fstrand110")


cmd.select("Fstrand111", "resi 292-304 & chain F ")
cmd.color ("teal", "Fstrand111")


cmd.select("Fstrand112", "resi 307-317 & chain F ")
cmd.color ("yellow", "Fstrand112")


cmd.select("Fstrand113", "resi 338-349 & chain F ")
cmd.color ("blue", "Fstrand113")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
