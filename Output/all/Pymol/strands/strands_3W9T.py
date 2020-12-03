from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3W9T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 105-113 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 121-122 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 131-132 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 144-146 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 152-160 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 166-169 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 176-181 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 191-194 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 199-201 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 207-210 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 219-222 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 232-233 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 243-244 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 247-248 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 254-257 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 266-269 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 279-282 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 293-299 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 304-332 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 337-366 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 379-384 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 391-393 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 397-399 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 403-407 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 419-421 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 429-431 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Bstrand26", "resi 105-113 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 119-122 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 131-134 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 144-146 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 152-160 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 166-169 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 176-181 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 191-194 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 199-201 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 207-210 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 219-222 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 232-233 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 243-244 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 247-248 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 254-257 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 266-269 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 279-282 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 293-299 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 304-332 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 337-366 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 379-384 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 391-393 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 397-399 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 403-407 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 419-421 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 429-431 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Cstrand52", "resi 105-113 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 119-122 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 131-134 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 144-146 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 152-160 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 166-169 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 176-181 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 191-194 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("Cstrand60", "resi 199-201 & chain C ")
cmd.color ("red", "Cstrand60")


cmd.select("Cstrand61", "resi 207-210 & chain C ")
cmd.color ("green", "Cstrand61")


cmd.select("Cstrand62", "resi 219-222 & chain C ")
cmd.color ("orange", "Cstrand62")


cmd.select("Cstrand63", "resi 232-233 & chain C ")
cmd.color ("teal", "Cstrand63")


cmd.select("Cstrand64", "resi 243-244 & chain C ")
cmd.color ("yellow", "Cstrand64")


cmd.select("Cstrand65", "resi 247-248 & chain C ")
cmd.color ("blue", "Cstrand65")


cmd.select("Cstrand66", "resi 254-257 & chain C ")
cmd.color ("red", "Cstrand66")


cmd.select("Cstrand67", "resi 266-269 & chain C ")
cmd.color ("green", "Cstrand67")


cmd.select("Cstrand68", "resi 279-282 & chain C ")
cmd.color ("orange", "Cstrand68")


cmd.select("Cstrand69", "resi 293-299 & chain C ")
cmd.color ("teal", "Cstrand69")


cmd.select("Cstrand70", "resi 304-325 & chain C ")
cmd.color ("yellow", "Cstrand70")


cmd.select("Cstrand71", "resi 328-332 & chain C ")
cmd.color ("blue", "Cstrand71")


cmd.select("Cstrand72", "resi 337-366 & chain C ")
cmd.color ("red", "Cstrand72")


cmd.select("Cstrand73", "resi 379-384 & chain C ")
cmd.color ("green", "Cstrand73")


cmd.select("Cstrand74", "resi 391-393 & chain C ")
cmd.color ("orange", "Cstrand74")


cmd.select("Cstrand75", "resi 397-399 & chain C ")
cmd.color ("teal", "Cstrand75")


cmd.select("Cstrand76", "resi 403-407 & chain C ")
cmd.color ("yellow", "Cstrand76")


cmd.select("Cstrand77", "resi 419-421 & chain C ")
cmd.color ("blue", "Cstrand77")


cmd.select("Cstrand78", "resi 429-431 & chain C ")
cmd.color ("red", "Cstrand78")


cmd.select("Dstrand79", "resi 105-113 & chain D ")
cmd.color ("green", "Dstrand79")


cmd.select("Dstrand80", "resi 119-122 & chain D ")
cmd.color ("orange", "Dstrand80")


cmd.select("Dstrand81", "resi 131-134 & chain D ")
cmd.color ("teal", "Dstrand81")


cmd.select("Dstrand82", "resi 144-147 & chain D ")
cmd.color ("yellow", "Dstrand82")


cmd.select("Dstrand83", "resi 152-160 & chain D ")
cmd.color ("blue", "Dstrand83")


cmd.select("Dstrand84", "resi 166-169 & chain D ")
cmd.color ("red", "Dstrand84")


cmd.select("Dstrand85", "resi 176-181 & chain D ")
cmd.color ("green", "Dstrand85")


cmd.select("Dstrand86", "resi 191-194 & chain D ")
cmd.color ("orange", "Dstrand86")


cmd.select("Dstrand87", "resi 199-201 & chain D ")
cmd.color ("teal", "Dstrand87")


cmd.select("Dstrand88", "resi 207-210 & chain D ")
cmd.color ("yellow", "Dstrand88")


cmd.select("Dstrand89", "resi 219-222 & chain D ")
cmd.color ("blue", "Dstrand89")


cmd.select("Dstrand90", "resi 232-233 & chain D ")
cmd.color ("red", "Dstrand90")


cmd.select("Dstrand91", "resi 243-244 & chain D ")
cmd.color ("green", "Dstrand91")


cmd.select("Dstrand92", "resi 247-248 & chain D ")
cmd.color ("orange", "Dstrand92")


cmd.select("Dstrand93", "resi 254-257 & chain D ")
cmd.color ("teal", "Dstrand93")


cmd.select("Dstrand94", "resi 266-269 & chain D ")
cmd.color ("yellow", "Dstrand94")


cmd.select("Dstrand95", "resi 279-282 & chain D ")
cmd.color ("blue", "Dstrand95")


cmd.select("Dstrand96", "resi 293-299 & chain D ")
cmd.color ("red", "Dstrand96")


cmd.select("Dstrand97", "resi 304-332 & chain D ")
cmd.color ("green", "Dstrand97")


cmd.select("Dstrand98", "resi 337-366 & chain D ")
cmd.color ("orange", "Dstrand98")


cmd.select("Dstrand99", "resi 379-384 & chain D ")
cmd.color ("teal", "Dstrand99")


cmd.select("Dstrand100", "resi 391-393 & chain D ")
cmd.color ("yellow", "Dstrand100")


cmd.select("Dstrand101", "resi 397-399 & chain D ")
cmd.color ("blue", "Dstrand101")


cmd.select("Dstrand102", "resi 403-407 & chain D ")
cmd.color ("red", "Dstrand102")


cmd.select("Dstrand103", "resi 419-421 & chain D ")
cmd.color ("green", "Dstrand103")


cmd.select("Dstrand104", "resi 429-431 & chain D ")
cmd.color ("orange", "Dstrand104")


cmd.select("Estrand105", "resi 105-113 & chain E ")
cmd.color ("teal", "Estrand105")


cmd.select("Estrand106", "resi 119-122 & chain E ")
cmd.color ("yellow", "Estrand106")


cmd.select("Estrand107", "resi 131-134 & chain E ")
cmd.color ("blue", "Estrand107")


cmd.select("Estrand108", "resi 143-146 & chain E ")
cmd.color ("red", "Estrand108")


cmd.select("Estrand109", "resi 152-160 & chain E ")
cmd.color ("green", "Estrand109")


cmd.select("Estrand110", "resi 166-169 & chain E ")
cmd.color ("orange", "Estrand110")


cmd.select("Estrand111", "resi 176-181 & chain E ")
cmd.color ("teal", "Estrand111")


cmd.select("Estrand112", "resi 191-194 & chain E ")
cmd.color ("yellow", "Estrand112")


cmd.select("Estrand113", "resi 199-201 & chain E ")
cmd.color ("blue", "Estrand113")


cmd.select("Estrand114", "resi 207-210 & chain E ")
cmd.color ("red", "Estrand114")


cmd.select("Estrand115", "resi 219-222 & chain E ")
cmd.color ("green", "Estrand115")


cmd.select("Estrand116", "resi 232-233 & chain E ")
cmd.color ("orange", "Estrand116")


cmd.select("Estrand117", "resi 243-244 & chain E ")
cmd.color ("teal", "Estrand117")


cmd.select("Estrand118", "resi 247-248 & chain E ")
cmd.color ("yellow", "Estrand118")


cmd.select("Estrand119", "resi 254-257 & chain E ")
cmd.color ("blue", "Estrand119")


cmd.select("Estrand120", "resi 266-269 & chain E ")
cmd.color ("red", "Estrand120")


cmd.select("Estrand121", "resi 279-282 & chain E ")
cmd.color ("green", "Estrand121")


cmd.select("Estrand122", "resi 293-299 & chain E ")
cmd.color ("orange", "Estrand122")


cmd.select("Estrand123", "resi 304-332 & chain E ")
cmd.color ("teal", "Estrand123")


cmd.select("Estrand124", "resi 337-366 & chain E ")
cmd.color ("yellow", "Estrand124")


cmd.select("Estrand125", "resi 379-384 & chain E ")
cmd.color ("blue", "Estrand125")


cmd.select("Estrand126", "resi 391-393 & chain E ")
cmd.color ("red", "Estrand126")


cmd.select("Estrand127", "resi 397-399 & chain E ")
cmd.color ("green", "Estrand127")


cmd.select("Estrand128", "resi 403-407 & chain E ")
cmd.color ("orange", "Estrand128")


cmd.select("Estrand129", "resi 419-421 & chain E ")
cmd.color ("teal", "Estrand129")


cmd.select("Estrand130", "resi 429-431 & chain E ")
cmd.color ("yellow", "Estrand130")


cmd.select("Fstrand131", "resi 105-113 & chain F ")
cmd.color ("blue", "Fstrand131")


cmd.select("Fstrand132", "resi 119-122 & chain F ")
cmd.color ("red", "Fstrand132")


cmd.select("Fstrand133", "resi 131-134 & chain F ")
cmd.color ("green", "Fstrand133")


cmd.select("Fstrand134", "resi 144-146 & chain F ")
cmd.color ("orange", "Fstrand134")


cmd.select("Fstrand135", "resi 152-160 & chain F ")
cmd.color ("teal", "Fstrand135")


cmd.select("Fstrand136", "resi 166-169 & chain F ")
cmd.color ("yellow", "Fstrand136")


cmd.select("Fstrand137", "resi 176-181 & chain F ")
cmd.color ("blue", "Fstrand137")


cmd.select("Fstrand138", "resi 191-194 & chain F ")
cmd.color ("red", "Fstrand138")


cmd.select("Fstrand139", "resi 199-201 & chain F ")
cmd.color ("green", "Fstrand139")


cmd.select("Fstrand140", "resi 207-210 & chain F ")
cmd.color ("orange", "Fstrand140")


cmd.select("Fstrand141", "resi 219-222 & chain F ")
cmd.color ("teal", "Fstrand141")


cmd.select("Fstrand142", "resi 232-233 & chain F ")
cmd.color ("yellow", "Fstrand142")


cmd.select("Fstrand143", "resi 243-244 & chain F ")
cmd.color ("blue", "Fstrand143")


cmd.select("Fstrand144", "resi 247-248 & chain F ")
cmd.color ("red", "Fstrand144")


cmd.select("Fstrand145", "resi 254-257 & chain F ")
cmd.color ("green", "Fstrand145")


cmd.select("Fstrand146", "resi 266-269 & chain F ")
cmd.color ("orange", "Fstrand146")


cmd.select("Fstrand147", "resi 279-282 & chain F ")
cmd.color ("teal", "Fstrand147")


cmd.select("Fstrand148", "resi 293-299 & chain F ")
cmd.color ("yellow", "Fstrand148")


cmd.select("Fstrand149", "resi 304-332 & chain F ")
cmd.color ("blue", "Fstrand149")


cmd.select("Fstrand150", "resi 337-366 & chain F ")
cmd.color ("red", "Fstrand150")


cmd.select("Fstrand151", "resi 379-384 & chain F ")
cmd.color ("green", "Fstrand151")


cmd.select("Fstrand152", "resi 391-393 & chain F ")
cmd.color ("orange", "Fstrand152")


cmd.select("Fstrand153", "resi 397-399 & chain F ")
cmd.color ("teal", "Fstrand153")


cmd.select("Fstrand154", "resi 403-407 & chain F ")
cmd.color ("yellow", "Fstrand154")


cmd.select("Fstrand155", "resi 419-421 & chain F ")
cmd.color ("blue", "Fstrand155")


cmd.select("Fstrand156", "resi 429-431 & chain F ")
cmd.color ("red", "Fstrand156")


cmd.select("Gstrand157", "resi 105-113 & chain G ")
cmd.color ("green", "Gstrand157")


cmd.select("Gstrand158", "resi 119-122 & chain G ")
cmd.color ("orange", "Gstrand158")


cmd.select("Gstrand159", "resi 131-134 & chain G ")
cmd.color ("teal", "Gstrand159")


cmd.select("Gstrand160", "resi 144-146 & chain G ")
cmd.color ("yellow", "Gstrand160")


cmd.select("Gstrand161", "resi 152-160 & chain G ")
cmd.color ("blue", "Gstrand161")


cmd.select("Gstrand162", "resi 166-169 & chain G ")
cmd.color ("red", "Gstrand162")


cmd.select("Gstrand163", "resi 176-181 & chain G ")
cmd.color ("green", "Gstrand163")


cmd.select("Gstrand164", "resi 191-194 & chain G ")
cmd.color ("orange", "Gstrand164")


cmd.select("Gstrand165", "resi 199-201 & chain G ")
cmd.color ("teal", "Gstrand165")


cmd.select("Gstrand166", "resi 207-210 & chain G ")
cmd.color ("yellow", "Gstrand166")


cmd.select("Gstrand167", "resi 219-222 & chain G ")
cmd.color ("blue", "Gstrand167")


cmd.select("Gstrand168", "resi 232-233 & chain G ")
cmd.color ("red", "Gstrand168")


cmd.select("Gstrand169", "resi 243-244 & chain G ")
cmd.color ("green", "Gstrand169")


cmd.select("Gstrand170", "resi 247-248 & chain G ")
cmd.color ("orange", "Gstrand170")


cmd.select("Gstrand171", "resi 254-257 & chain G ")
cmd.color ("teal", "Gstrand171")


cmd.select("Gstrand172", "resi 266-269 & chain G ")
cmd.color ("yellow", "Gstrand172")


cmd.select("Gstrand173", "resi 279-282 & chain G ")
cmd.color ("blue", "Gstrand173")


cmd.select("Gstrand174", "resi 293-299 & chain G ")
cmd.color ("red", "Gstrand174")


cmd.select("Gstrand175", "resi 304-332 & chain G ")
cmd.color ("green", "Gstrand175")


cmd.select("Gstrand176", "resi 337-366 & chain G ")
cmd.color ("orange", "Gstrand176")


cmd.select("Gstrand177", "resi 379-384 & chain G ")
cmd.color ("teal", "Gstrand177")


cmd.select("Gstrand178", "resi 391-393 & chain G ")
cmd.color ("yellow", "Gstrand178")


cmd.select("Gstrand179", "resi 397-399 & chain G ")
cmd.color ("blue", "Gstrand179")


cmd.select("Gstrand180", "resi 403-407 & chain G ")
cmd.color ("red", "Gstrand180")


cmd.select("Gstrand181", "resi 419-421 & chain G ")
cmd.color ("green", "Gstrand181")


cmd.select("Gstrand182", "resi 429-431 & chain G ")
cmd.color ("orange", "Gstrand182")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
