from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H56.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 27-35 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 42-50 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 57-63 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 72-75 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 79-96 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 102-107 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 114-132 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 136-164 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 168-175 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 227-233 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 239-258 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 261-266 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 272-282 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 287-290 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Bstrand14", "resi 27-35 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 42-50 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 57-63 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 72-75 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 79-96 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 102-107 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 114-132 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 136-164 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 168-175 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 227-233 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 239-258 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 261-266 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 272-282 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 287-290 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Cstrand28", "resi 27-35 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 42-50 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 57-63 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 72-75 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 79-96 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 102-107 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 114-132 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 136-164 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 168-175 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 227-233 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 239-258 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 261-266 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 272-282 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 287-290 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Dstrand42", "resi 27-35 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 42-50 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 57-63 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 72-75 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 79-96 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 102-107 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Dstrand48", "resi 114-132 & chain D ")
cmd.color ("red", "Dstrand48")


cmd.select("Dstrand49", "resi 136-164 & chain D ")
cmd.color ("green", "Dstrand49")


cmd.select("Dstrand50", "resi 168-175 & chain D ")
cmd.color ("orange", "Dstrand50")


cmd.select("Dstrand51", "resi 227-233 & chain D ")
cmd.color ("teal", "Dstrand51")


cmd.select("Dstrand52", "resi 239-258 & chain D ")
cmd.color ("yellow", "Dstrand52")


cmd.select("Dstrand53", "resi 261-266 & chain D ")
cmd.color ("blue", "Dstrand53")


cmd.select("Dstrand54", "resi 272-282 & chain D ")
cmd.color ("red", "Dstrand54")


cmd.select("Dstrand55", "resi 287-290 & chain D ")
cmd.color ("green", "Dstrand55")


cmd.select("Estrand56", "resi 27-35 & chain E ")
cmd.color ("orange", "Estrand56")


cmd.select("Estrand57", "resi 42-50 & chain E ")
cmd.color ("teal", "Estrand57")


cmd.select("Estrand58", "resi 57-63 & chain E ")
cmd.color ("yellow", "Estrand58")


cmd.select("Estrand59", "resi 72-75 & chain E ")
cmd.color ("blue", "Estrand59")


cmd.select("Estrand60", "resi 79-96 & chain E ")
cmd.color ("red", "Estrand60")


cmd.select("Estrand61", "resi 102-107 & chain E ")
cmd.color ("green", "Estrand61")


cmd.select("Estrand62", "resi 114-132 & chain E ")
cmd.color ("orange", "Estrand62")


cmd.select("Estrand63", "resi 136-164 & chain E ")
cmd.color ("teal", "Estrand63")


cmd.select("Estrand64", "resi 168-175 & chain E ")
cmd.color ("yellow", "Estrand64")


cmd.select("Estrand65", "resi 227-233 & chain E ")
cmd.color ("blue", "Estrand65")


cmd.select("Estrand66", "resi 239-258 & chain E ")
cmd.color ("red", "Estrand66")


cmd.select("Estrand67", "resi 261-266 & chain E ")
cmd.color ("green", "Estrand67")


cmd.select("Estrand68", "resi 272-282 & chain E ")
cmd.color ("orange", "Estrand68")


cmd.select("Estrand69", "resi 287-290 & chain E ")
cmd.color ("teal", "Estrand69")


cmd.select("Fstrand70", "resi 27-35 & chain F ")
cmd.color ("yellow", "Fstrand70")


cmd.select("Fstrand71", "resi 42-50 & chain F ")
cmd.color ("blue", "Fstrand71")


cmd.select("Fstrand72", "resi 57-63 & chain F ")
cmd.color ("red", "Fstrand72")


cmd.select("Fstrand73", "resi 72-75 & chain F ")
cmd.color ("green", "Fstrand73")


cmd.select("Fstrand74", "resi 79-96 & chain F ")
cmd.color ("orange", "Fstrand74")


cmd.select("Fstrand75", "resi 102-107 & chain F ")
cmd.color ("teal", "Fstrand75")


cmd.select("Fstrand76", "resi 114-132 & chain F ")
cmd.color ("yellow", "Fstrand76")


cmd.select("Fstrand77", "resi 136-164 & chain F ")
cmd.color ("blue", "Fstrand77")


cmd.select("Fstrand78", "resi 168-175 & chain F ")
cmd.color ("red", "Fstrand78")


cmd.select("Fstrand79", "resi 227-233 & chain F ")
cmd.color ("green", "Fstrand79")


cmd.select("Fstrand80", "resi 239-258 & chain F ")
cmd.color ("orange", "Fstrand80")


cmd.select("Fstrand81", "resi 261-266 & chain F ")
cmd.color ("teal", "Fstrand81")


cmd.select("Fstrand82", "resi 272-282 & chain F ")
cmd.color ("yellow", "Fstrand82")


cmd.select("Fstrand83", "resi 287-290 & chain F ")
cmd.color ("blue", "Fstrand83")


cmd.select("Gstrand84", "resi 27-35 & chain G ")
cmd.color ("red", "Gstrand84")


cmd.select("Gstrand85", "resi 42-50 & chain G ")
cmd.color ("green", "Gstrand85")


cmd.select("Gstrand86", "resi 57-63 & chain G ")
cmd.color ("orange", "Gstrand86")


cmd.select("Gstrand87", "resi 72-75 & chain G ")
cmd.color ("teal", "Gstrand87")


cmd.select("Gstrand88", "resi 79-96 & chain G ")
cmd.color ("yellow", "Gstrand88")


cmd.select("Gstrand89", "resi 102-107 & chain G ")
cmd.color ("blue", "Gstrand89")


cmd.select("Gstrand90", "resi 114-132 & chain G ")
cmd.color ("red", "Gstrand90")


cmd.select("Gstrand91", "resi 136-164 & chain G ")
cmd.color ("green", "Gstrand91")


cmd.select("Gstrand92", "resi 168-175 & chain G ")
cmd.color ("orange", "Gstrand92")


cmd.select("Gstrand93", "resi 227-233 & chain G ")
cmd.color ("teal", "Gstrand93")


cmd.select("Gstrand94", "resi 239-258 & chain G ")
cmd.color ("yellow", "Gstrand94")


cmd.select("Gstrand95", "resi 261-266 & chain G ")
cmd.color ("blue", "Gstrand95")


cmd.select("Gstrand96", "resi 272-282 & chain G ")
cmd.color ("red", "Gstrand96")


cmd.select("Gstrand97", "resi 287-290 & chain G ")
cmd.color ("green", "Gstrand97")


cmd.select("Hstrand98", "resi 27-35 & chain H ")
cmd.color ("orange", "Hstrand98")


cmd.select("Hstrand99", "resi 42-50 & chain H ")
cmd.color ("teal", "Hstrand99")


cmd.select("Hstrand100", "resi 57-63 & chain H ")
cmd.color ("yellow", "Hstrand100")


cmd.select("Hstrand101", "resi 72-75 & chain H ")
cmd.color ("blue", "Hstrand101")


cmd.select("Hstrand102", "resi 79-96 & chain H ")
cmd.color ("red", "Hstrand102")


cmd.select("Hstrand103", "resi 102-107 & chain H ")
cmd.color ("green", "Hstrand103")


cmd.select("Hstrand104", "resi 114-132 & chain H ")
cmd.color ("orange", "Hstrand104")


cmd.select("Hstrand105", "resi 136-164 & chain H ")
cmd.color ("teal", "Hstrand105")


cmd.select("Hstrand106", "resi 168-175 & chain H ")
cmd.color ("yellow", "Hstrand106")


cmd.select("Hstrand107", "resi 227-233 & chain H ")
cmd.color ("blue", "Hstrand107")


cmd.select("Hstrand108", "resi 239-258 & chain H ")
cmd.color ("red", "Hstrand108")


cmd.select("Hstrand109", "resi 261-266 & chain H ")
cmd.color ("green", "Hstrand109")


cmd.select("Hstrand110", "resi 272-282 & chain H ")
cmd.color ("orange", "Hstrand110")


cmd.select("Hstrand111", "resi 287-290 & chain H ")
cmd.color ("teal", "Hstrand111")


cmd.select("Istrand112", "resi 27-35 & chain I ")
cmd.color ("yellow", "Istrand112")


cmd.select("Istrand113", "resi 42-50 & chain I ")
cmd.color ("blue", "Istrand113")


cmd.select("Istrand114", "resi 57-63 & chain I ")
cmd.color ("red", "Istrand114")


cmd.select("Istrand115", "resi 72-75 & chain I ")
cmd.color ("green", "Istrand115")


cmd.select("Istrand116", "resi 79-96 & chain I ")
cmd.color ("orange", "Istrand116")


cmd.select("Istrand117", "resi 102-107 & chain I ")
cmd.color ("teal", "Istrand117")


cmd.select("Istrand118", "resi 114-132 & chain I ")
cmd.color ("yellow", "Istrand118")


cmd.select("Istrand119", "resi 136-164 & chain I ")
cmd.color ("blue", "Istrand119")


cmd.select("Istrand120", "resi 168-175 & chain I ")
cmd.color ("red", "Istrand120")


cmd.select("Istrand121", "resi 227-233 & chain I ")
cmd.color ("green", "Istrand121")


cmd.select("Istrand122", "resi 239-258 & chain I ")
cmd.color ("orange", "Istrand122")


cmd.select("Istrand123", "resi 261-266 & chain I ")
cmd.color ("teal", "Istrand123")


cmd.select("Istrand124", "resi 272-282 & chain I ")
cmd.color ("yellow", "Istrand124")


cmd.select("Istrand125", "resi 287-290 & chain I ")
cmd.color ("blue", "Istrand125")


cmd.select("Jstrand126", "resi 27-35 & chain J ")
cmd.color ("red", "Jstrand126")


cmd.select("Jstrand127", "resi 42-50 & chain J ")
cmd.color ("green", "Jstrand127")


cmd.select("Jstrand128", "resi 57-63 & chain J ")
cmd.color ("orange", "Jstrand128")


cmd.select("Jstrand129", "resi 72-75 & chain J ")
cmd.color ("teal", "Jstrand129")


cmd.select("Jstrand130", "resi 79-96 & chain J ")
cmd.color ("yellow", "Jstrand130")


cmd.select("Jstrand131", "resi 102-107 & chain J ")
cmd.color ("blue", "Jstrand131")


cmd.select("Jstrand132", "resi 114-132 & chain J ")
cmd.color ("red", "Jstrand132")


cmd.select("Jstrand133", "resi 136-164 & chain J ")
cmd.color ("green", "Jstrand133")


cmd.select("Jstrand134", "resi 168-175 & chain J ")
cmd.color ("orange", "Jstrand134")


cmd.select("Jstrand135", "resi 227-233 & chain J ")
cmd.color ("teal", "Jstrand135")


cmd.select("Jstrand136", "resi 239-258 & chain J ")
cmd.color ("yellow", "Jstrand136")


cmd.select("Jstrand137", "resi 261-266 & chain J ")
cmd.color ("blue", "Jstrand137")


cmd.select("Jstrand138", "resi 272-282 & chain J ")
cmd.color ("red", "Jstrand138")


cmd.select("Jstrand139", "resi 287-290 & chain J ")
cmd.color ("green", "Jstrand139")


cmd.select("Kstrand140", "resi 27-35 & chain K ")
cmd.color ("orange", "Kstrand140")


cmd.select("Kstrand141", "resi 42-50 & chain K ")
cmd.color ("teal", "Kstrand141")


cmd.select("Kstrand142", "resi 57-63 & chain K ")
cmd.color ("yellow", "Kstrand142")


cmd.select("Kstrand143", "resi 72-75 & chain K ")
cmd.color ("blue", "Kstrand143")


cmd.select("Kstrand144", "resi 79-96 & chain K ")
cmd.color ("red", "Kstrand144")


cmd.select("Kstrand145", "resi 102-107 & chain K ")
cmd.color ("green", "Kstrand145")


cmd.select("Kstrand146", "resi 114-132 & chain K ")
cmd.color ("orange", "Kstrand146")


cmd.select("Kstrand147", "resi 136-164 & chain K ")
cmd.color ("teal", "Kstrand147")


cmd.select("Kstrand148", "resi 168-175 & chain K ")
cmd.color ("yellow", "Kstrand148")


cmd.select("Kstrand149", "resi 227-233 & chain K ")
cmd.color ("blue", "Kstrand149")


cmd.select("Kstrand150", "resi 239-258 & chain K ")
cmd.color ("red", "Kstrand150")


cmd.select("Kstrand151", "resi 261-266 & chain K ")
cmd.color ("green", "Kstrand151")


cmd.select("Kstrand152", "resi 272-282 & chain K ")
cmd.color ("orange", "Kstrand152")


cmd.select("Kstrand153", "resi 287-290 & chain K ")
cmd.color ("teal", "Kstrand153")


cmd.select("Lstrand154", "resi 27-35 & chain L ")
cmd.color ("yellow", "Lstrand154")


cmd.select("Lstrand155", "resi 42-50 & chain L ")
cmd.color ("blue", "Lstrand155")


cmd.select("Lstrand156", "resi 57-63 & chain L ")
cmd.color ("red", "Lstrand156")


cmd.select("Lstrand157", "resi 72-75 & chain L ")
cmd.color ("green", "Lstrand157")


cmd.select("Lstrand158", "resi 79-96 & chain L ")
cmd.color ("orange", "Lstrand158")


cmd.select("Lstrand159", "resi 102-107 & chain L ")
cmd.color ("teal", "Lstrand159")


cmd.select("Lstrand160", "resi 114-132 & chain L ")
cmd.color ("yellow", "Lstrand160")


cmd.select("Lstrand161", "resi 136-164 & chain L ")
cmd.color ("blue", "Lstrand161")


cmd.select("Lstrand162", "resi 168-175 & chain L ")
cmd.color ("red", "Lstrand162")


cmd.select("Lstrand163", "resi 227-233 & chain L ")
cmd.color ("green", "Lstrand163")


cmd.select("Lstrand164", "resi 239-258 & chain L ")
cmd.color ("orange", "Lstrand164")


cmd.select("Lstrand165", "resi 261-266 & chain L ")
cmd.color ("teal", "Lstrand165")


cmd.select("Lstrand166", "resi 272-282 & chain L ")
cmd.color ("yellow", "Lstrand166")


cmd.select("Lstrand167", "resi 287-290 & chain L ")
cmd.color ("blue", "Lstrand167")


cmd.select("Mstrand168", "resi 27-35 & chain M ")
cmd.color ("red", "Mstrand168")


cmd.select("Mstrand169", "resi 42-50 & chain M ")
cmd.color ("green", "Mstrand169")


cmd.select("Mstrand170", "resi 57-63 & chain M ")
cmd.color ("orange", "Mstrand170")


cmd.select("Mstrand171", "resi 72-75 & chain M ")
cmd.color ("teal", "Mstrand171")


cmd.select("Mstrand172", "resi 79-96 & chain M ")
cmd.color ("yellow", "Mstrand172")


cmd.select("Mstrand173", "resi 102-107 & chain M ")
cmd.color ("blue", "Mstrand173")


cmd.select("Mstrand174", "resi 114-132 & chain M ")
cmd.color ("red", "Mstrand174")


cmd.select("Mstrand175", "resi 136-164 & chain M ")
cmd.color ("green", "Mstrand175")


cmd.select("Mstrand176", "resi 168-175 & chain M ")
cmd.color ("orange", "Mstrand176")


cmd.select("Mstrand177", "resi 227-233 & chain M ")
cmd.color ("teal", "Mstrand177")


cmd.select("Mstrand178", "resi 239-258 & chain M ")
cmd.color ("yellow", "Mstrand178")


cmd.select("Mstrand179", "resi 261-266 & chain M ")
cmd.color ("blue", "Mstrand179")


cmd.select("Mstrand180", "resi 272-282 & chain M ")
cmd.color ("red", "Mstrand180")


cmd.select("Mstrand181", "resi 287-290 & chain M ")
cmd.color ("green", "Mstrand181")


cmd.select("Nstrand182", "resi 27-35 & chain N ")
cmd.color ("orange", "Nstrand182")


cmd.select("Nstrand183", "resi 42-50 & chain N ")
cmd.color ("teal", "Nstrand183")


cmd.select("Nstrand184", "resi 57-63 & chain N ")
cmd.color ("yellow", "Nstrand184")


cmd.select("Nstrand185", "resi 72-75 & chain N ")
cmd.color ("blue", "Nstrand185")


cmd.select("Nstrand186", "resi 79-96 & chain N ")
cmd.color ("red", "Nstrand186")


cmd.select("Nstrand187", "resi 102-107 & chain N ")
cmd.color ("green", "Nstrand187")


cmd.select("Nstrand188", "resi 114-132 & chain N ")
cmd.color ("orange", "Nstrand188")


cmd.select("Nstrand189", "resi 136-164 & chain N ")
cmd.color ("teal", "Nstrand189")


cmd.select("Nstrand190", "resi 168-175 & chain N ")
cmd.color ("yellow", "Nstrand190")


cmd.select("Nstrand191", "resi 227-233 & chain N ")
cmd.color ("blue", "Nstrand191")


cmd.select("Nstrand192", "resi 239-258 & chain N ")
cmd.color ("red", "Nstrand192")


cmd.select("Nstrand193", "resi 261-266 & chain N ")
cmd.color ("green", "Nstrand193")


cmd.select("Nstrand194", "resi 272-282 & chain N ")
cmd.color ("orange", "Nstrand194")


cmd.select("Nstrand195", "resi 287-290 & chain N ")
cmd.color ("teal", "Nstrand195")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
