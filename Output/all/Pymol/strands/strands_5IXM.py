from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-11 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 15-19 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 22-23 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 30-39 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 43-54 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 57-69 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 82-95 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 99-108 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 128-138 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 142-153 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 164-178 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 181-193 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 201-216 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 221-236 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 253-266 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 269-272 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 280-292 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 330-342 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 348-359 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 378-389 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 394-403 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 409-419 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 425-433 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 454-464 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 469-478 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 483-494 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 499-511 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 518-527 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Bstrand28", "resi 6-7 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 18-21 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 54-69 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 75-89 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 95-107 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Cstrand33", "resi 7-11 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 15-19 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 22-23 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 30-39 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 43-54 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 57-66 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 84-95 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 99-108 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 128-138 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 142-153 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 164-178 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 181-193 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 201-216 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 220-236 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 253-272 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 280-292 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 330-342 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 348-359 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 378-389 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 394-403 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 409-419 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 425-433 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 454-463 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 469-478 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 483-494 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 499-511 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 518-527 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("Dstrand60", "resi 6-7 & chain D ")
cmd.color ("red", "Dstrand60")


cmd.select("Dstrand61", "resi 16-21 & chain D ")
cmd.color ("green", "Dstrand61")


cmd.select("Dstrand62", "resi 42-44 & chain D ")
cmd.color ("orange", "Dstrand62")


cmd.select("Dstrand63", "resi 54-69 & chain D ")
cmd.color ("teal", "Dstrand63")


cmd.select("Dstrand64", "resi 75-89 & chain D ")
cmd.color ("yellow", "Dstrand64")


cmd.select("Dstrand65", "resi 95-107 & chain D ")
cmd.color ("blue", "Dstrand65")


cmd.select("Estrand66", "resi 7-10 & chain E ")
cmd.color ("red", "Estrand66")


cmd.select("Estrand67", "resi 16-19 & chain E ")
cmd.color ("green", "Estrand67")


cmd.select("Estrand68", "resi 22-23 & chain E ")
cmd.color ("orange", "Estrand68")


cmd.select("Estrand69", "resi 30-39 & chain E ")
cmd.color ("teal", "Estrand69")


cmd.select("Estrand70", "resi 43-54 & chain E ")
cmd.color ("yellow", "Estrand70")


cmd.select("Estrand71", "resi 57-66 & chain E ")
cmd.color ("blue", "Estrand71")


cmd.select("Estrand72", "resi 84-95 & chain E ")
cmd.color ("red", "Estrand72")


cmd.select("Estrand73", "resi 99-108 & chain E ")
cmd.color ("green", "Estrand73")


cmd.select("Estrand74", "resi 128-138 & chain E ")
cmd.color ("orange", "Estrand74")


cmd.select("Estrand75", "resi 142-153 & chain E ")
cmd.color ("teal", "Estrand75")


cmd.select("Estrand76", "resi 164-178 & chain E ")
cmd.color ("yellow", "Estrand76")


cmd.select("Estrand77", "resi 181-193 & chain E ")
cmd.color ("blue", "Estrand77")


cmd.select("Estrand78", "resi 201-216 & chain E ")
cmd.color ("red", "Estrand78")


cmd.select("Estrand79", "resi 221-236 & chain E ")
cmd.color ("green", "Estrand79")


cmd.select("Estrand80", "resi 253-266 & chain E ")
cmd.color ("orange", "Estrand80")


cmd.select("Estrand81", "resi 269-272 & chain E ")
cmd.color ("teal", "Estrand81")


cmd.select("Estrand82", "resi 280-292 & chain E ")
cmd.color ("yellow", "Estrand82")


cmd.select("Estrand83", "resi 330-342 & chain E ")
cmd.color ("blue", "Estrand83")


cmd.select("Estrand84", "resi 348-359 & chain E ")
cmd.color ("red", "Estrand84")


cmd.select("Estrand85", "resi 378-389 & chain E ")
cmd.color ("green", "Estrand85")


cmd.select("Estrand86", "resi 394-403 & chain E ")
cmd.color ("orange", "Estrand86")


cmd.select("Estrand87", "resi 409-419 & chain E ")
cmd.color ("teal", "Estrand87")


cmd.select("Estrand88", "resi 425-433 & chain E ")
cmd.color ("yellow", "Estrand88")


cmd.select("Estrand89", "resi 454-465 & chain E ")
cmd.color ("blue", "Estrand89")


cmd.select("Estrand90", "resi 469-478 & chain E ")
cmd.color ("red", "Estrand90")


cmd.select("Estrand91", "resi 483-493 & chain E ")
cmd.color ("green", "Estrand91")


cmd.select("Estrand92", "resi 501-511 & chain E ")
cmd.color ("orange", "Estrand92")


cmd.select("Estrand93", "resi 518-527 & chain E ")
cmd.color ("teal", "Estrand93")


cmd.select("Fstrand94", "resi 18-21 & chain F ")
cmd.color ("yellow", "Fstrand94")


cmd.select("Fstrand95", "resi 54-69 & chain F ")
cmd.color ("blue", "Fstrand95")


cmd.select("Fstrand96", "resi 75-89 & chain F ")
cmd.color ("red", "Fstrand96")


cmd.select("Fstrand97", "resi 95-107 & chain F ")
cmd.color ("green", "Fstrand97")


cmd.select("Gstrand98", "resi 7-11 & chain G ")
cmd.color ("orange", "Gstrand98")


cmd.select("Gstrand99", "resi 15-19 & chain G ")
cmd.color ("teal", "Gstrand99")


cmd.select("Gstrand100", "resi 22-27 & chain G ")
cmd.color ("yellow", "Gstrand100")


cmd.select("Gstrand101", "resi 30-39 & chain G ")
cmd.color ("blue", "Gstrand101")


cmd.select("Gstrand102", "resi 43-54 & chain G ")
cmd.color ("red", "Gstrand102")


cmd.select("Gstrand103", "resi 57-69 & chain G ")
cmd.color ("green", "Gstrand103")


cmd.select("Gstrand104", "resi 82-95 & chain G ")
cmd.color ("orange", "Gstrand104")


cmd.select("Gstrand105", "resi 99-108 & chain G ")
cmd.color ("teal", "Gstrand105")


cmd.select("Gstrand106", "resi 128-138 & chain G ")
cmd.color ("yellow", "Gstrand106")


cmd.select("Gstrand107", "resi 142-153 & chain G ")
cmd.color ("blue", "Gstrand107")


cmd.select("Gstrand108", "resi 164-178 & chain G ")
cmd.color ("red", "Gstrand108")


cmd.select("Gstrand109", "resi 181-193 & chain G ")
cmd.color ("green", "Gstrand109")


cmd.select("Gstrand110", "resi 201-216 & chain G ")
cmd.color ("orange", "Gstrand110")


cmd.select("Gstrand111", "resi 221-236 & chain G ")
cmd.color ("teal", "Gstrand111")


cmd.select("Gstrand112", "resi 253-266 & chain G ")
cmd.color ("yellow", "Gstrand112")


cmd.select("Gstrand113", "resi 269-272 & chain G ")
cmd.color ("blue", "Gstrand113")


cmd.select("Gstrand114", "resi 280-292 & chain G ")
cmd.color ("red", "Gstrand114")


cmd.select("Gstrand115", "resi 330-342 & chain G ")
cmd.color ("green", "Gstrand115")


cmd.select("Gstrand116", "resi 348-359 & chain G ")
cmd.color ("orange", "Gstrand116")


cmd.select("Gstrand117", "resi 378-389 & chain G ")
cmd.color ("teal", "Gstrand117")


cmd.select("Gstrand118", "resi 394-403 & chain G ")
cmd.color ("yellow", "Gstrand118")


cmd.select("Gstrand119", "resi 409-419 & chain G ")
cmd.color ("blue", "Gstrand119")


cmd.select("Gstrand120", "resi 425-433 & chain G ")
cmd.color ("red", "Gstrand120")


cmd.select("Gstrand121", "resi 454-465 & chain G ")
cmd.color ("green", "Gstrand121")


cmd.select("Gstrand122", "resi 469-478 & chain G ")
cmd.color ("orange", "Gstrand122")


cmd.select("Gstrand123", "resi 483-495 & chain G ")
cmd.color ("teal", "Gstrand123")


cmd.select("Gstrand124", "resi 498-511 & chain G ")
cmd.color ("yellow", "Gstrand124")


cmd.select("Gstrand125", "resi 518-527 & chain G ")
cmd.color ("blue", "Gstrand125")


cmd.select("Hstrand126", "resi 6-7 & chain H ")
cmd.color ("red", "Hstrand126")


cmd.select("Hstrand127", "resi 16-21 & chain H ")
cmd.color ("green", "Hstrand127")


cmd.select("Hstrand128", "resi 42-43 & chain H ")
cmd.color ("orange", "Hstrand128")


cmd.select("Hstrand129", "resi 54-69 & chain H ")
cmd.color ("teal", "Hstrand129")


cmd.select("Hstrand130", "resi 75-89 & chain H ")
cmd.color ("yellow", "Hstrand130")


cmd.select("Hstrand131", "resi 95-107 & chain H ")
cmd.color ("blue", "Hstrand131")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
