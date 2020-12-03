from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3B07.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 18-28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 33-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 49-61 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 74-88 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 95-101 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 108-125 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 130-154 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 162-169 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 221-222 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 225-233 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 239-257 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 262-282 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 287-299 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Bstrand13", "resi 13-22 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 27-36 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 44-55 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 59-62 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 70-84 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 89-95 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 102-118 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 122-150 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 153-165 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 168-171 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 204-205 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 208-215 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 222-241 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 244-266 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 271-278 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Cstrand28", "resi 18-28 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 33-43 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 49-61 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 74-88 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 95-101 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 108-125 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 130-154 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 162-169 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 221-222 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 225-233 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 239-257 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 262-282 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 287-299 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Dstrand41", "resi 12-22 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 27-37 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 44-55 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 59-62 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 70-84 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 89-95 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 102-118 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Dstrand48", "resi 122-150 & chain D ")
cmd.color ("red", "Dstrand48")


cmd.select("Dstrand49", "resi 153-165 & chain D ")
cmd.color ("green", "Dstrand49")


cmd.select("Dstrand50", "resi 168-171 & chain D ")
cmd.color ("orange", "Dstrand50")


cmd.select("Dstrand51", "resi 204-205 & chain D ")
cmd.color ("teal", "Dstrand51")


cmd.select("Dstrand52", "resi 208-215 & chain D ")
cmd.color ("yellow", "Dstrand52")


cmd.select("Dstrand53", "resi 222-241 & chain D ")
cmd.color ("blue", "Dstrand53")


cmd.select("Dstrand54", "resi 244-266 & chain D ")
cmd.color ("red", "Dstrand54")


cmd.select("Dstrand55", "resi 271-278 & chain D ")
cmd.color ("green", "Dstrand55")


cmd.select("Estrand56", "resi 18-28 & chain E ")
cmd.color ("orange", "Estrand56")


cmd.select("Estrand57", "resi 33-43 & chain E ")
cmd.color ("teal", "Estrand57")


cmd.select("Estrand58", "resi 49-61 & chain E ")
cmd.color ("yellow", "Estrand58")


cmd.select("Estrand59", "resi 74-88 & chain E ")
cmd.color ("blue", "Estrand59")


cmd.select("Estrand60", "resi 95-101 & chain E ")
cmd.color ("red", "Estrand60")


cmd.select("Estrand61", "resi 108-125 & chain E ")
cmd.color ("green", "Estrand61")


cmd.select("Estrand62", "resi 130-154 & chain E ")
cmd.color ("orange", "Estrand62")


cmd.select("Estrand63", "resi 162-169 & chain E ")
cmd.color ("teal", "Estrand63")


cmd.select("Estrand64", "resi 221-222 & chain E ")
cmd.color ("yellow", "Estrand64")


cmd.select("Estrand65", "resi 225-233 & chain E ")
cmd.color ("blue", "Estrand65")


cmd.select("Estrand66", "resi 239-257 & chain E ")
cmd.color ("red", "Estrand66")


cmd.select("Estrand67", "resi 262-282 & chain E ")
cmd.color ("green", "Estrand67")


cmd.select("Estrand68", "resi 287-299 & chain E ")
cmd.color ("orange", "Estrand68")


cmd.select("Fstrand69", "resi 12-22 & chain F ")
cmd.color ("teal", "Fstrand69")


cmd.select("Fstrand70", "resi 27-37 & chain F ")
cmd.color ("yellow", "Fstrand70")


cmd.select("Fstrand71", "resi 44-55 & chain F ")
cmd.color ("blue", "Fstrand71")


cmd.select("Fstrand72", "resi 59-62 & chain F ")
cmd.color ("red", "Fstrand72")


cmd.select("Fstrand73", "resi 70-84 & chain F ")
cmd.color ("green", "Fstrand73")


cmd.select("Fstrand74", "resi 89-95 & chain F ")
cmd.color ("orange", "Fstrand74")


cmd.select("Fstrand75", "resi 102-118 & chain F ")
cmd.color ("teal", "Fstrand75")


cmd.select("Fstrand76", "resi 122-150 & chain F ")
cmd.color ("yellow", "Fstrand76")


cmd.select("Fstrand77", "resi 153-165 & chain F ")
cmd.color ("blue", "Fstrand77")


cmd.select("Fstrand78", "resi 168-171 & chain F ")
cmd.color ("red", "Fstrand78")


cmd.select("Fstrand79", "resi 204-205 & chain F ")
cmd.color ("green", "Fstrand79")


cmd.select("Fstrand80", "resi 208-215 & chain F ")
cmd.color ("orange", "Fstrand80")


cmd.select("Fstrand81", "resi 222-241 & chain F ")
cmd.color ("teal", "Fstrand81")


cmd.select("Fstrand82", "resi 244-266 & chain F ")
cmd.color ("yellow", "Fstrand82")


cmd.select("Fstrand83", "resi 271-278 & chain F ")
cmd.color ("blue", "Fstrand83")


cmd.select("Gstrand84", "resi 18-28 & chain G ")
cmd.color ("red", "Gstrand84")


cmd.select("Gstrand85", "resi 33-43 & chain G ")
cmd.color ("green", "Gstrand85")


cmd.select("Gstrand86", "resi 49-61 & chain G ")
cmd.color ("orange", "Gstrand86")


cmd.select("Gstrand87", "resi 74-88 & chain G ")
cmd.color ("teal", "Gstrand87")


cmd.select("Gstrand88", "resi 95-101 & chain G ")
cmd.color ("yellow", "Gstrand88")


cmd.select("Gstrand89", "resi 108-125 & chain G ")
cmd.color ("blue", "Gstrand89")


cmd.select("Gstrand90", "resi 130-154 & chain G ")
cmd.color ("red", "Gstrand90")


cmd.select("Gstrand91", "resi 162-169 & chain G ")
cmd.color ("green", "Gstrand91")


cmd.select("Gstrand92", "resi 221-222 & chain G ")
cmd.color ("orange", "Gstrand92")


cmd.select("Gstrand93", "resi 225-233 & chain G ")
cmd.color ("teal", "Gstrand93")


cmd.select("Gstrand94", "resi 239-257 & chain G ")
cmd.color ("yellow", "Gstrand94")


cmd.select("Gstrand95", "resi 262-282 & chain G ")
cmd.color ("blue", "Gstrand95")


cmd.select("Gstrand96", "resi 287-299 & chain G ")
cmd.color ("red", "Gstrand96")


cmd.select("Hstrand97", "resi 12-22 & chain H ")
cmd.color ("green", "Hstrand97")


cmd.select("Hstrand98", "resi 27-37 & chain H ")
cmd.color ("orange", "Hstrand98")


cmd.select("Hstrand99", "resi 44-55 & chain H ")
cmd.color ("teal", "Hstrand99")


cmd.select("Hstrand100", "resi 59-62 & chain H ")
cmd.color ("yellow", "Hstrand100")


cmd.select("Hstrand101", "resi 70-84 & chain H ")
cmd.color ("blue", "Hstrand101")


cmd.select("Hstrand102", "resi 89-95 & chain H ")
cmd.color ("red", "Hstrand102")


cmd.select("Hstrand103", "resi 102-118 & chain H ")
cmd.color ("green", "Hstrand103")


cmd.select("Hstrand104", "resi 122-150 & chain H ")
cmd.color ("orange", "Hstrand104")


cmd.select("Hstrand105", "resi 153-165 & chain H ")
cmd.color ("teal", "Hstrand105")


cmd.select("Hstrand106", "resi 168-171 & chain H ")
cmd.color ("yellow", "Hstrand106")


cmd.select("Hstrand107", "resi 204-205 & chain H ")
cmd.color ("blue", "Hstrand107")


cmd.select("Hstrand108", "resi 208-215 & chain H ")
cmd.color ("red", "Hstrand108")


cmd.select("Hstrand109", "resi 222-241 & chain H ")
cmd.color ("green", "Hstrand109")


cmd.select("Hstrand110", "resi 244-266 & chain H ")
cmd.color ("orange", "Hstrand110")


cmd.select("Hstrand111", "resi 271-278 & chain H ")
cmd.color ("teal", "Hstrand111")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
