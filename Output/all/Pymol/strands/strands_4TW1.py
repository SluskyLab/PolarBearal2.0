from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4TW1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 19-29 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 51-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 66-67 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 75-90 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 97-103 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 111-123 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 139-157 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 165-172 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 175-177 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 180-182 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 226-227 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 231-237 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 244-265 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 268-272 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 275-291 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 297-302 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Bstrand17", "resi 45-55 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 60-70 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 77-88 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 92-95 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 103-118 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 123-129 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 136-148 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 159-180 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 188-200 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 203-206 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 242-243 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 247-253 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 259-275 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 285-302 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 307-316 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Cstrand32", "resi 19-29 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 34-44 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 51-62 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 66-67 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 75-90 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 97-103 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 110-125 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 135-149 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 153-157 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 165-172 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 175-177 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 180-182 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 226-227 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 231-237 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 244-263 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 270-280 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 283-291 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 297-303 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Dstrand50", "resi 48-55 & chain D ")
cmd.color ("orange", "Dstrand50")


cmd.select("Dstrand51", "resi 60-69 & chain D ")
cmd.color ("teal", "Dstrand51")


cmd.select("Dstrand52", "resi 77-83 & chain D ")
cmd.color ("yellow", "Dstrand52")


cmd.select("Dstrand53", "resi 87-88 & chain D ")
cmd.color ("blue", "Dstrand53")


cmd.select("Dstrand54", "resi 92-95 & chain D ")
cmd.color ("red", "Dstrand54")


cmd.select("Dstrand55", "resi 103-106 & chain D ")
cmd.color ("green", "Dstrand55")


cmd.select("Dstrand56", "resi 110-117 & chain D ")
cmd.color ("orange", "Dstrand56")


cmd.select("Dstrand57", "resi 123-129 & chain D ")
cmd.color ("teal", "Dstrand57")


cmd.select("Dstrand58", "resi 138-152 & chain D ")
cmd.color ("yellow", "Dstrand58")


cmd.select("Dstrand59", "resi 158-173 & chain D ")
cmd.color ("blue", "Dstrand59")


cmd.select("Dstrand60", "resi 176-180 & chain D ")
cmd.color ("red", "Dstrand60")


cmd.select("Dstrand61", "resi 188-200 & chain D ")
cmd.color ("green", "Dstrand61")


cmd.select("Dstrand62", "resi 203-206 & chain D ")
cmd.color ("orange", "Dstrand62")


cmd.select("Dstrand63", "resi 242-243 & chain D ")
cmd.color ("teal", "Dstrand63")


cmd.select("Dstrand64", "resi 247-253 & chain D ")
cmd.color ("yellow", "Dstrand64")


cmd.select("Dstrand65", "resi 259-275 & chain D ")
cmd.color ("blue", "Dstrand65")


cmd.select("Dstrand66", "resi 285-302 & chain D ")
cmd.color ("red", "Dstrand66")


cmd.select("Dstrand67", "resi 307-316 & chain D ")
cmd.color ("green", "Dstrand67")


cmd.select("Estrand68", "resi 19-29 & chain E ")
cmd.color ("orange", "Estrand68")


cmd.select("Estrand69", "resi 34-44 & chain E ")
cmd.color ("teal", "Estrand69")


cmd.select("Estrand70", "resi 51-62 & chain E ")
cmd.color ("yellow", "Estrand70")


cmd.select("Estrand71", "resi 66-67 & chain E ")
cmd.color ("blue", "Estrand71")


cmd.select("Estrand72", "resi 75-90 & chain E ")
cmd.color ("red", "Estrand72")


cmd.select("Estrand73", "resi 97-103 & chain E ")
cmd.color ("green", "Estrand73")


cmd.select("Estrand74", "resi 111-128 & chain E ")
cmd.color ("orange", "Estrand74")


cmd.select("Estrand75", "resi 131-149 & chain E ")
cmd.color ("teal", "Estrand75")


cmd.select("Estrand76", "resi 153-158 & chain E ")
cmd.color ("yellow", "Estrand76")


cmd.select("Estrand77", "resi 165-172 & chain E ")
cmd.color ("blue", "Estrand77")


cmd.select("Estrand78", "resi 175-177 & chain E ")
cmd.color ("red", "Estrand78")


cmd.select("Estrand79", "resi 180-182 & chain E ")
cmd.color ("green", "Estrand79")


cmd.select("Estrand80", "resi 226-227 & chain E ")
cmd.color ("orange", "Estrand80")


cmd.select("Estrand81", "resi 231-237 & chain E ")
cmd.color ("teal", "Estrand81")


cmd.select("Estrand82", "resi 244-263 & chain E ")
cmd.color ("yellow", "Estrand82")


cmd.select("Estrand83", "resi 270-276 & chain E ")
cmd.color ("blue", "Estrand83")


cmd.select("Estrand84", "resi 281-291 & chain E ")
cmd.color ("red", "Estrand84")


cmd.select("Estrand85", "resi 296-303 & chain E ")
cmd.color ("green", "Estrand85")


cmd.select("Fstrand86", "resi 45-47 & chain F ")
cmd.color ("orange", "Fstrand86")


cmd.select("Fstrand87", "resi 50-55 & chain F ")
cmd.color ("teal", "Fstrand87")


cmd.select("Fstrand88", "resi 60-70 & chain F ")
cmd.color ("yellow", "Fstrand88")


cmd.select("Fstrand89", "resi 77-88 & chain F ")
cmd.color ("blue", "Fstrand89")


cmd.select("Fstrand90", "resi 92-95 & chain F ")
cmd.color ("red", "Fstrand90")


cmd.select("Fstrand91", "resi 103-118 & chain F ")
cmd.color ("green", "Fstrand91")


cmd.select("Fstrand92", "resi 123-129 & chain F ")
cmd.color ("orange", "Fstrand92")


cmd.select("Fstrand93", "resi 138-149 & chain F ")
cmd.color ("teal", "Fstrand93")


cmd.select("Fstrand94", "resi 159-180 & chain F ")
cmd.color ("yellow", "Fstrand94")


cmd.select("Fstrand95", "resi 188-200 & chain F ")
cmd.color ("blue", "Fstrand95")


cmd.select("Fstrand96", "resi 203-206 & chain F ")
cmd.color ("red", "Fstrand96")


cmd.select("Fstrand97", "resi 242-243 & chain F ")
cmd.color ("green", "Fstrand97")


cmd.select("Fstrand98", "resi 247-253 & chain F ")
cmd.color ("orange", "Fstrand98")


cmd.select("Fstrand99", "resi 259-275 & chain F ")
cmd.color ("teal", "Fstrand99")


cmd.select("Fstrand100", "resi 285-302 & chain F ")
cmd.color ("yellow", "Fstrand100")


cmd.select("Fstrand101", "resi 307-316 & chain F ")
cmd.color ("blue", "Fstrand101")


cmd.select("Gstrand102", "resi 19-29 & chain G ")
cmd.color ("red", "Gstrand102")


cmd.select("Gstrand103", "resi 34-44 & chain G ")
cmd.color ("green", "Gstrand103")


cmd.select("Gstrand104", "resi 51-57 & chain G ")
cmd.color ("orange", "Gstrand104")


cmd.select("Gstrand105", "resi 60-62 & chain G ")
cmd.color ("teal", "Gstrand105")


cmd.select("Gstrand106", "resi 66-67 & chain G ")
cmd.color ("yellow", "Gstrand106")


cmd.select("Gstrand107", "resi 75-90 & chain G ")
cmd.color ("blue", "Gstrand107")


cmd.select("Gstrand108", "resi 97-103 & chain G ")
cmd.color ("red", "Gstrand108")


cmd.select("Gstrand109", "resi 110-127 & chain G ")
cmd.color ("green", "Gstrand109")


cmd.select("Gstrand110", "resi 132-137 & chain G ")
cmd.color ("orange", "Gstrand110")


cmd.select("Gstrand111", "resi 153-157 & chain G ")
cmd.color ("teal", "Gstrand111")


cmd.select("Gstrand112", "resi 165-172 & chain G ")
cmd.color ("yellow", "Gstrand112")


cmd.select("Gstrand113", "resi 175-177 & chain G ")
cmd.color ("blue", "Gstrand113")


cmd.select("Gstrand114", "resi 180-182 & chain G ")
cmd.color ("red", "Gstrand114")


cmd.select("Gstrand115", "resi 226-227 & chain G ")
cmd.color ("green", "Gstrand115")


cmd.select("Gstrand116", "resi 231-237 & chain G ")
cmd.color ("orange", "Gstrand116")


cmd.select("Gstrand117", "resi 244-265 & chain G ")
cmd.color ("teal", "Gstrand117")


cmd.select("Gstrand118", "resi 268-291 & chain G ")
cmd.color ("yellow", "Gstrand118")


cmd.select("Gstrand119", "resi 296-303 & chain G ")
cmd.color ("blue", "Gstrand119")


cmd.select("Hstrand120", "resi 45-55 & chain H ")
cmd.color ("red", "Hstrand120")


cmd.select("Hstrand121", "resi 60-70 & chain H ")
cmd.color ("green", "Hstrand121")


cmd.select("Hstrand122", "resi 77-88 & chain H ")
cmd.color ("orange", "Hstrand122")


cmd.select("Hstrand123", "resi 92-95 & chain H ")
cmd.color ("teal", "Hstrand123")


cmd.select("Hstrand124", "resi 103-118 & chain H ")
cmd.color ("yellow", "Hstrand124")


cmd.select("Hstrand125", "resi 123-129 & chain H ")
cmd.color ("blue", "Hstrand125")


cmd.select("Hstrand126", "resi 138-152 & chain H ")
cmd.color ("red", "Hstrand126")


cmd.select("Hstrand127", "resi 157-173 & chain H ")
cmd.color ("green", "Hstrand127")


cmd.select("Hstrand128", "resi 176-180 & chain H ")
cmd.color ("orange", "Hstrand128")


cmd.select("Hstrand129", "resi 188-200 & chain H ")
cmd.color ("teal", "Hstrand129")


cmd.select("Hstrand130", "resi 203-206 & chain H ")
cmd.color ("yellow", "Hstrand130")


cmd.select("Hstrand131", "resi 242-243 & chain H ")
cmd.color ("blue", "Hstrand131")


cmd.select("Hstrand132", "resi 247-253 & chain H ")
cmd.color ("red", "Hstrand132")


cmd.select("Hstrand133", "resi 259-275 & chain H ")
cmd.color ("green", "Hstrand133")


cmd.select("Hstrand134", "resi 285-302 & chain H ")
cmd.color ("orange", "Hstrand134")


cmd.select("Hstrand135", "resi 307-316 & chain H ")
cmd.color ("teal", "Hstrand135")


cmd.select("Istrand136", "resi 19-29 & chain I ")
cmd.color ("yellow", "Istrand136")


cmd.select("Istrand137", "resi 34-44 & chain I ")
cmd.color ("blue", "Istrand137")


cmd.select("Istrand138", "resi 51-62 & chain I ")
cmd.color ("red", "Istrand138")


cmd.select("Istrand139", "resi 66-67 & chain I ")
cmd.color ("green", "Istrand139")


cmd.select("Istrand140", "resi 75-90 & chain I ")
cmd.color ("orange", "Istrand140")


cmd.select("Istrand141", "resi 97-103 & chain I ")
cmd.color ("teal", "Istrand141")


cmd.select("Istrand142", "resi 110-123 & chain I ")
cmd.color ("yellow", "Istrand142")


cmd.select("Istrand143", "resi 135-157 & chain I ")
cmd.color ("blue", "Istrand143")


cmd.select("Istrand144", "resi 165-172 & chain I ")
cmd.color ("red", "Istrand144")


cmd.select("Istrand145", "resi 175-177 & chain I ")
cmd.color ("green", "Istrand145")


cmd.select("Istrand146", "resi 180-182 & chain I ")
cmd.color ("orange", "Istrand146")


cmd.select("Istrand147", "resi 226-227 & chain I ")
cmd.color ("teal", "Istrand147")


cmd.select("Istrand148", "resi 231-237 & chain I ")
cmd.color ("yellow", "Istrand148")


cmd.select("Istrand149", "resi 244-265 & chain I ")
cmd.color ("blue", "Istrand149")


cmd.select("Istrand150", "resi 268-291 & chain I ")
cmd.color ("red", "Istrand150")


cmd.select("Istrand151", "resi 296-303 & chain I ")
cmd.color ("green", "Istrand151")


cmd.select("Jstrand152", "resi 40-50 & chain J ")
cmd.color ("orange", "Jstrand152")


cmd.select("Jstrand153", "resi 55-65 & chain J ")
cmd.color ("teal", "Jstrand153")


cmd.select("Jstrand154", "resi 72-81 & chain J ")
cmd.color ("yellow", "Jstrand154")


cmd.select("Jstrand155", "resi 88-90 & chain J ")
cmd.color ("blue", "Jstrand155")


cmd.select("Jstrand156", "resi 98-100 & chain J ")
cmd.color ("red", "Jstrand156")


cmd.select("Jstrand157", "resi 103-113 & chain J ")
cmd.color ("green", "Jstrand157")


cmd.select("Jstrand158", "resi 118-124 & chain J ")
cmd.color ("orange", "Jstrand158")


cmd.select("Jstrand159", "resi 131-147 & chain J ")
cmd.color ("teal", "Jstrand159")


cmd.select("Jstrand160", "resi 154-168 & chain J ")
cmd.color ("yellow", "Jstrand160")


cmd.select("Jstrand161", "resi 171-175 & chain J ")
cmd.color ("blue", "Jstrand161")


cmd.select("Jstrand162", "resi 183-195 & chain J ")
cmd.color ("red", "Jstrand162")


cmd.select("Jstrand163", "resi 198-201 & chain J ")
cmd.color ("green", "Jstrand163")


cmd.select("Jstrand164", "resi 242-248 & chain J ")
cmd.color ("orange", "Jstrand164")


cmd.select("Jstrand165", "resi 254-270 & chain J ")
cmd.color ("teal", "Jstrand165")


cmd.select("Jstrand166", "resi 280-297 & chain J ")
cmd.color ("yellow", "Jstrand166")


cmd.select("Jstrand167", "resi 302-311 & chain J ")
cmd.color ("blue", "Jstrand167")


cmd.select("Kstrand168", "resi 19-29 & chain K ")
cmd.color ("red", "Kstrand168")


cmd.select("Kstrand169", "resi 34-44 & chain K ")
cmd.color ("green", "Kstrand169")


cmd.select("Kstrand170", "resi 51-62 & chain K ")
cmd.color ("orange", "Kstrand170")


cmd.select("Kstrand171", "resi 66-67 & chain K ")
cmd.color ("teal", "Kstrand171")


cmd.select("Kstrand172", "resi 75-90 & chain K ")
cmd.color ("yellow", "Kstrand172")


cmd.select("Kstrand173", "resi 97-103 & chain K ")
cmd.color ("blue", "Kstrand173")


cmd.select("Kstrand174", "resi 111-125 & chain K ")
cmd.color ("red", "Kstrand174")


cmd.select("Kstrand175", "resi 136-157 & chain K ")
cmd.color ("green", "Kstrand175")


cmd.select("Kstrand176", "resi 165-172 & chain K ")
cmd.color ("orange", "Kstrand176")


cmd.select("Kstrand177", "resi 175-177 & chain K ")
cmd.color ("teal", "Kstrand177")


cmd.select("Kstrand178", "resi 180-182 & chain K ")
cmd.color ("yellow", "Kstrand178")


cmd.select("Kstrand179", "resi 226-227 & chain K ")
cmd.color ("blue", "Kstrand179")


cmd.select("Kstrand180", "resi 231-237 & chain K ")
cmd.color ("red", "Kstrand180")


cmd.select("Kstrand181", "resi 244-263 & chain K ")
cmd.color ("green", "Kstrand181")


cmd.select("Kstrand182", "resi 270-291 & chain K ")
cmd.color ("orange", "Kstrand182")


cmd.select("Kstrand183", "resi 297-303 & chain K ")
cmd.color ("teal", "Kstrand183")


cmd.select("Lstrand184", "resi 45-55 & chain L ")
cmd.color ("yellow", "Lstrand184")


cmd.select("Lstrand185", "resi 60-70 & chain L ")
cmd.color ("blue", "Lstrand185")


cmd.select("Lstrand186", "resi 77-88 & chain L ")
cmd.color ("red", "Lstrand186")


cmd.select("Lstrand187", "resi 92-95 & chain L ")
cmd.color ("green", "Lstrand187")


cmd.select("Lstrand188", "resi 103-118 & chain L ")
cmd.color ("orange", "Lstrand188")


cmd.select("Lstrand189", "resi 123-129 & chain L ")
cmd.color ("teal", "Lstrand189")


cmd.select("Lstrand190", "resi 136-151 & chain L ")
cmd.color ("yellow", "Lstrand190")


cmd.select("Lstrand191", "resi 157-173 & chain L ")
cmd.color ("blue", "Lstrand191")


cmd.select("Lstrand192", "resi 176-180 & chain L ")
cmd.color ("red", "Lstrand192")


cmd.select("Lstrand193", "resi 188-200 & chain L ")
cmd.color ("green", "Lstrand193")


cmd.select("Lstrand194", "resi 203-206 & chain L ")
cmd.color ("orange", "Lstrand194")


cmd.select("Lstrand195", "resi 242-243 & chain L ")
cmd.color ("teal", "Lstrand195")


cmd.select("Lstrand196", "resi 247-253 & chain L ")
cmd.color ("yellow", "Lstrand196")


cmd.select("Lstrand197", "resi 259-275 & chain L ")
cmd.color ("blue", "Lstrand197")


cmd.select("Lstrand198", "resi 285-302 & chain L ")
cmd.color ("red", "Lstrand198")


cmd.select("Lstrand199", "resi 307-316 & chain L ")
cmd.color ("green", "Lstrand199")


cmd.select("Mstrand200", "resi 19-29 & chain M ")
cmd.color ("orange", "Mstrand200")


cmd.select("Mstrand201", "resi 34-44 & chain M ")
cmd.color ("teal", "Mstrand201")


cmd.select("Mstrand202", "resi 51-57 & chain M ")
cmd.color ("yellow", "Mstrand202")


cmd.select("Mstrand203", "resi 60-62 & chain M ")
cmd.color ("blue", "Mstrand203")


cmd.select("Mstrand204", "resi 66-67 & chain M ")
cmd.color ("red", "Mstrand204")


cmd.select("Mstrand205", "resi 75-90 & chain M ")
cmd.color ("green", "Mstrand205")


cmd.select("Mstrand206", "resi 97-103 & chain M ")
cmd.color ("orange", "Mstrand206")


cmd.select("Mstrand207", "resi 111-127 & chain M ")
cmd.color ("teal", "Mstrand207")


cmd.select("Mstrand208", "resi 133-157 & chain M ")
cmd.color ("yellow", "Mstrand208")


cmd.select("Mstrand209", "resi 165-172 & chain M ")
cmd.color ("blue", "Mstrand209")


cmd.select("Mstrand210", "resi 175-177 & chain M ")
cmd.color ("red", "Mstrand210")


cmd.select("Mstrand211", "resi 180-182 & chain M ")
cmd.color ("green", "Mstrand211")


cmd.select("Mstrand212", "resi 226-227 & chain M ")
cmd.color ("orange", "Mstrand212")


cmd.select("Mstrand213", "resi 231-237 & chain M ")
cmd.color ("teal", "Mstrand213")


cmd.select("Mstrand214", "resi 244-265 & chain M ")
cmd.color ("yellow", "Mstrand214")


cmd.select("Mstrand215", "resi 268-291 & chain M ")
cmd.color ("blue", "Mstrand215")


cmd.select("Mstrand216", "resi 296-302 & chain M ")
cmd.color ("red", "Mstrand216")


cmd.select("Nstrand217", "resi 45-55 & chain N ")
cmd.color ("green", "Nstrand217")


cmd.select("Nstrand218", "resi 60-70 & chain N ")
cmd.color ("orange", "Nstrand218")


cmd.select("Nstrand219", "resi 77-88 & chain N ")
cmd.color ("teal", "Nstrand219")


cmd.select("Nstrand220", "resi 92-95 & chain N ")
cmd.color ("yellow", "Nstrand220")


cmd.select("Nstrand221", "resi 103-118 & chain N ")
cmd.color ("blue", "Nstrand221")


cmd.select("Nstrand222", "resi 123-129 & chain N ")
cmd.color ("red", "Nstrand222")


cmd.select("Nstrand223", "resi 136-152 & chain N ")
cmd.color ("green", "Nstrand223")


cmd.select("Nstrand224", "resi 156-173 & chain N ")
cmd.color ("orange", "Nstrand224")


cmd.select("Nstrand225", "resi 176-180 & chain N ")
cmd.color ("teal", "Nstrand225")


cmd.select("Nstrand226", "resi 188-200 & chain N ")
cmd.color ("yellow", "Nstrand226")


cmd.select("Nstrand227", "resi 203-206 & chain N ")
cmd.color ("blue", "Nstrand227")


cmd.select("Nstrand228", "resi 242-243 & chain N ")
cmd.color ("red", "Nstrand228")


cmd.select("Nstrand229", "resi 248-253 & chain N ")
cmd.color ("green", "Nstrand229")


cmd.select("Nstrand230", "resi 259-275 & chain N ")
cmd.color ("orange", "Nstrand230")


cmd.select("Nstrand231", "resi 285-302 & chain N ")
cmd.color ("teal", "Nstrand231")


cmd.select("Nstrand232", "resi 307-316 & chain N ")
cmd.color ("yellow", "Nstrand232")


cmd.select("Ostrand233", "resi 19-29 & chain O ")
cmd.color ("blue", "Ostrand233")


cmd.select("Ostrand234", "resi 34-44 & chain O ")
cmd.color ("red", "Ostrand234")


cmd.select("Ostrand235", "resi 51-62 & chain O ")
cmd.color ("green", "Ostrand235")


cmd.select("Ostrand236", "resi 66-67 & chain O ")
cmd.color ("orange", "Ostrand236")


cmd.select("Ostrand237", "resi 75-90 & chain O ")
cmd.color ("teal", "Ostrand237")


cmd.select("Ostrand238", "resi 97-103 & chain O ")
cmd.color ("yellow", "Ostrand238")


cmd.select("Ostrand239", "resi 111-126 & chain O ")
cmd.color ("blue", "Ostrand239")


cmd.select("Ostrand240", "resi 134-157 & chain O ")
cmd.color ("red", "Ostrand240")


cmd.select("Ostrand241", "resi 165-172 & chain O ")
cmd.color ("green", "Ostrand241")


cmd.select("Ostrand242", "resi 175-177 & chain O ")
cmd.color ("orange", "Ostrand242")


cmd.select("Ostrand243", "resi 180-182 & chain O ")
cmd.color ("teal", "Ostrand243")


cmd.select("Ostrand244", "resi 226-227 & chain O ")
cmd.color ("yellow", "Ostrand244")


cmd.select("Ostrand245", "resi 231-237 & chain O ")
cmd.color ("blue", "Ostrand245")


cmd.select("Ostrand246", "resi 244-265 & chain O ")
cmd.color ("red", "Ostrand246")


cmd.select("Ostrand247", "resi 268-291 & chain O ")
cmd.color ("green", "Ostrand247")


cmd.select("Ostrand248", "resi 296-302 & chain O ")
cmd.color ("orange", "Ostrand248")


cmd.select("Pstrand249", "resi 45-55 & chain P ")
cmd.color ("teal", "Pstrand249")


cmd.select("Pstrand250", "resi 60-70 & chain P ")
cmd.color ("yellow", "Pstrand250")


cmd.select("Pstrand251", "resi 77-88 & chain P ")
cmd.color ("blue", "Pstrand251")


cmd.select("Pstrand252", "resi 92-95 & chain P ")
cmd.color ("red", "Pstrand252")


cmd.select("Pstrand253", "resi 103-117 & chain P ")
cmd.color ("green", "Pstrand253")


cmd.select("Pstrand254", "resi 123-129 & chain P ")
cmd.color ("orange", "Pstrand254")


cmd.select("Pstrand255", "resi 136-151 & chain P ")
cmd.color ("teal", "Pstrand255")


cmd.select("Pstrand256", "resi 157-180 & chain P ")
cmd.color ("yellow", "Pstrand256")


cmd.select("Pstrand257", "resi 188-200 & chain P ")
cmd.color ("blue", "Pstrand257")


cmd.select("Pstrand258", "resi 203-206 & chain P ")
cmd.color ("red", "Pstrand258")


cmd.select("Pstrand259", "resi 242-243 & chain P ")
cmd.color ("green", "Pstrand259")


cmd.select("Pstrand260", "resi 247-253 & chain P ")
cmd.color ("orange", "Pstrand260")


cmd.select("Pstrand261", "resi 259-275 & chain P ")
cmd.color ("teal", "Pstrand261")


cmd.select("Pstrand262", "resi 285-302 & chain P ")
cmd.color ("yellow", "Pstrand262")


cmd.select("Pstrand263", "resi 307-316 & chain P ")
cmd.color ("blue", "Pstrand263")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand* or Ostrand* or Pstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
