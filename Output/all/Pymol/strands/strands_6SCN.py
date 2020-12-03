from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SCN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("astrand0", "resi 174-177 & chain a ")
cmd.color ("red", "astrand0")


cmd.select("astrand1", "resi 210-213 & chain a ")
cmd.color ("green", "astrand1")


cmd.select("astrand2", "resi 262-271 & chain a ")
cmd.color ("orange", "astrand2")


cmd.select("astrand3", "resi 276-278 & chain a ")
cmd.color ("teal", "astrand3")


cmd.select("astrand4", "resi 293-303 & chain a ")
cmd.color ("yellow", "astrand4")


cmd.select("astrand5", "resi 357-366 & chain a ")
cmd.color ("blue", "astrand5")


cmd.select("astrand6", "resi 374-376 & chain a ")
cmd.color ("red", "astrand6")


cmd.select("astrand7", "resi 381-391 & chain a ")
cmd.color ("green", "astrand7")


cmd.select("astrand8", "resi 429-434 & chain a ")
cmd.color ("orange", "astrand8")


cmd.select("Astrand9", "resi 156-158 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 173-177 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 210-213 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 262-271 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 276-278 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 293-303 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 357-366 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 374-376 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 381-391 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 429-434 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("bstrand19", "resi 156-158 & chain b ")
cmd.color ("green", "bstrand19")


cmd.select("bstrand20", "resi 173-176 & chain b ")
cmd.color ("orange", "bstrand20")


cmd.select("bstrand21", "resi 210-212 & chain b ")
cmd.color ("teal", "bstrand21")


cmd.select("bstrand22", "resi 262-271 & chain b ")
cmd.color ("yellow", "bstrand22")


cmd.select("bstrand23", "resi 276-278 & chain b ")
cmd.color ("blue", "bstrand23")


cmd.select("bstrand24", "resi 292-303 & chain b ")
cmd.color ("red", "bstrand24")


cmd.select("bstrand25", "resi 357-367 & chain b ")
cmd.color ("green", "bstrand25")


cmd.select("bstrand26", "resi 374-376 & chain b ")
cmd.color ("orange", "bstrand26")


cmd.select("bstrand27", "resi 381-391 & chain b ")
cmd.color ("teal", "bstrand27")


cmd.select("bstrand28", "resi 429-434 & chain b ")
cmd.color ("yellow", "bstrand28")


cmd.select("Bstrand29", "resi 156-158 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 173-177 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 210-213 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 262-271 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 276-278 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 292-303 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 357-367 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 374-376 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 381-391 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 429-434 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("cstrand39", "resi 156-158 & chain c ")
cmd.color ("teal", "cstrand39")


cmd.select("cstrand40", "resi 173-177 & chain c ")
cmd.color ("yellow", "cstrand40")


cmd.select("cstrand41", "resi 210-213 & chain c ")
cmd.color ("blue", "cstrand41")


cmd.select("cstrand42", "resi 262-271 & chain c ")
cmd.color ("red", "cstrand42")


cmd.select("cstrand43", "resi 276-278 & chain c ")
cmd.color ("green", "cstrand43")


cmd.select("cstrand44", "resi 293-303 & chain c ")
cmd.color ("orange", "cstrand44")


cmd.select("cstrand45", "resi 357-366 & chain c ")
cmd.color ("teal", "cstrand45")


cmd.select("cstrand46", "resi 374-376 & chain c ")
cmd.color ("yellow", "cstrand46")


cmd.select("cstrand47", "resi 381-391 & chain c ")
cmd.color ("blue", "cstrand47")


cmd.select("cstrand48", "resi 429-434 & chain c ")
cmd.color ("red", "cstrand48")


cmd.select("Cstrand49", "resi 156-158 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 173-176 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 210-212 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 262-271 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 276-278 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 292-303 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 357-367 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 374-376 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 381-391 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 429-434 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("dstrand59", "resi 174-177 & chain d ")
cmd.color ("blue", "dstrand59")


cmd.select("dstrand60", "resi 210-213 & chain d ")
cmd.color ("red", "dstrand60")


cmd.select("dstrand61", "resi 262-271 & chain d ")
cmd.color ("green", "dstrand61")


cmd.select("dstrand62", "resi 276-278 & chain d ")
cmd.color ("orange", "dstrand62")


cmd.select("dstrand63", "resi 292-303 & chain d ")
cmd.color ("teal", "dstrand63")


cmd.select("dstrand64", "resi 357-367 & chain d ")
cmd.color ("yellow", "dstrand64")


cmd.select("dstrand65", "resi 374-376 & chain d ")
cmd.color ("blue", "dstrand65")


cmd.select("dstrand66", "resi 381-391 & chain d ")
cmd.color ("red", "dstrand66")


cmd.select("dstrand67", "resi 429-434 & chain d ")
cmd.color ("green", "dstrand67")


cmd.select("Dstrand68", "resi 156-158 & chain D ")
cmd.color ("orange", "Dstrand68")


cmd.select("Dstrand69", "resi 173-177 & chain D ")
cmd.color ("teal", "Dstrand69")


cmd.select("Dstrand70", "resi 210-213 & chain D ")
cmd.color ("yellow", "Dstrand70")


cmd.select("Dstrand71", "resi 262-271 & chain D ")
cmd.color ("blue", "Dstrand71")


cmd.select("Dstrand72", "resi 276-278 & chain D ")
cmd.color ("red", "Dstrand72")


cmd.select("Dstrand73", "resi 292-303 & chain D ")
cmd.color ("green", "Dstrand73")


cmd.select("Dstrand74", "resi 357-367 & chain D ")
cmd.color ("orange", "Dstrand74")


cmd.select("Dstrand75", "resi 374-376 & chain D ")
cmd.color ("teal", "Dstrand75")


cmd.select("Dstrand76", "resi 381-391 & chain D ")
cmd.color ("yellow", "Dstrand76")


cmd.select("Dstrand77", "resi 429-434 & chain D ")
cmd.color ("blue", "Dstrand77")


cmd.select("estrand78", "resi 155-158 & chain e ")
cmd.color ("red", "estrand78")


cmd.select("estrand79", "resi 173-177 & chain e ")
cmd.color ("green", "estrand79")


cmd.select("estrand80", "resi 210-213 & chain e ")
cmd.color ("orange", "estrand80")


cmd.select("estrand81", "resi 262-271 & chain e ")
cmd.color ("teal", "estrand81")


cmd.select("estrand82", "resi 276-278 & chain e ")
cmd.color ("yellow", "estrand82")


cmd.select("estrand83", "resi 292-303 & chain e ")
cmd.color ("blue", "estrand83")


cmd.select("estrand84", "resi 357-367 & chain e ")
cmd.color ("red", "estrand84")


cmd.select("estrand85", "resi 374-376 & chain e ")
cmd.color ("green", "estrand85")


cmd.select("estrand86", "resi 381-391 & chain e ")
cmd.color ("orange", "estrand86")


cmd.select("estrand87", "resi 429-434 & chain e ")
cmd.color ("teal", "estrand87")


cmd.select("Estrand88", "resi 174-176 & chain E ")
cmd.color ("yellow", "Estrand88")


cmd.select("Estrand89", "resi 210-212 & chain E ")
cmd.color ("blue", "Estrand89")


cmd.select("Estrand90", "resi 262-271 & chain E ")
cmd.color ("red", "Estrand90")


cmd.select("Estrand91", "resi 276-278 & chain E ")
cmd.color ("green", "Estrand91")


cmd.select("Estrand92", "resi 293-303 & chain E ")
cmd.color ("orange", "Estrand92")


cmd.select("Estrand93", "resi 357-366 & chain E ")
cmd.color ("teal", "Estrand93")


cmd.select("Estrand94", "resi 374-376 & chain E ")
cmd.color ("yellow", "Estrand94")


cmd.select("Estrand95", "resi 381-391 & chain E ")
cmd.color ("blue", "Estrand95")


cmd.select("Estrand96", "resi 429-434 & chain E ")
cmd.color ("red", "Estrand96")


cmd.select("fstrand97", "resi 156-158 & chain f ")
cmd.color ("green", "fstrand97")


cmd.select("fstrand98", "resi 173-177 & chain f ")
cmd.color ("orange", "fstrand98")


cmd.select("fstrand99", "resi 210-213 & chain f ")
cmd.color ("teal", "fstrand99")


cmd.select("fstrand100", "resi 262-271 & chain f ")
cmd.color ("yellow", "fstrand100")


cmd.select("fstrand101", "resi 276-278 & chain f ")
cmd.color ("blue", "fstrand101")


cmd.select("fstrand102", "resi 292-303 & chain f ")
cmd.color ("red", "fstrand102")


cmd.select("fstrand103", "resi 357-367 & chain f ")
cmd.color ("green", "fstrand103")


cmd.select("fstrand104", "resi 374-376 & chain f ")
cmd.color ("orange", "fstrand104")


cmd.select("fstrand105", "resi 381-391 & chain f ")
cmd.color ("teal", "fstrand105")


cmd.select("fstrand106", "resi 429-434 & chain f ")
cmd.color ("yellow", "fstrand106")


cmd.select("Fstrand107", "resi 156-158 & chain F ")
cmd.color ("blue", "Fstrand107")


cmd.select("Fstrand108", "resi 173-176 & chain F ")
cmd.color ("red", "Fstrand108")


cmd.select("Fstrand109", "resi 210-212 & chain F ")
cmd.color ("green", "Fstrand109")


cmd.select("Fstrand110", "resi 262-271 & chain F ")
cmd.color ("orange", "Fstrand110")


cmd.select("Fstrand111", "resi 276-278 & chain F ")
cmd.color ("teal", "Fstrand111")


cmd.select("Fstrand112", "resi 293-303 & chain F ")
cmd.color ("yellow", "Fstrand112")


cmd.select("Fstrand113", "resi 357-366 & chain F ")
cmd.color ("blue", "Fstrand113")


cmd.select("Fstrand114", "resi 374-376 & chain F ")
cmd.color ("red", "Fstrand114")


cmd.select("Fstrand115", "resi 381-391 & chain F ")
cmd.color ("green", "Fstrand115")


cmd.select("Fstrand116", "resi 429-434 & chain F ")
cmd.color ("orange", "Fstrand116")


cmd.select("gstrand117", "resi 262-271 & chain g ")
cmd.color ("teal", "gstrand117")


cmd.select("gstrand118", "resi 276-278 & chain g ")
cmd.color ("yellow", "gstrand118")


cmd.select("gstrand119", "resi 292-303 & chain g ")
cmd.color ("blue", "gstrand119")


cmd.select("gstrand120", "resi 357-367 & chain g ")
cmd.color ("red", "gstrand120")


cmd.select("gstrand121", "resi 374-376 & chain g ")
cmd.color ("green", "gstrand121")


cmd.select("gstrand122", "resi 381-391 & chain g ")
cmd.color ("orange", "gstrand122")


cmd.select("gstrand123", "resi 429-434 & chain g ")
cmd.color ("teal", "gstrand123")


cmd.select("Gstrand124", "resi 156-158 & chain G ")
cmd.color ("yellow", "Gstrand124")


cmd.select("Gstrand125", "resi 173-176 & chain G ")
cmd.color ("blue", "Gstrand125")


cmd.select("Gstrand126", "resi 210-212 & chain G ")
cmd.color ("red", "Gstrand126")


cmd.select("Gstrand127", "resi 262-271 & chain G ")
cmd.color ("green", "Gstrand127")


cmd.select("Gstrand128", "resi 276-278 & chain G ")
cmd.color ("orange", "Gstrand128")


cmd.select("Gstrand129", "resi 292-303 & chain G ")
cmd.color ("teal", "Gstrand129")


cmd.select("Gstrand130", "resi 357-367 & chain G ")
cmd.color ("yellow", "Gstrand130")


cmd.select("Gstrand131", "resi 374-376 & chain G ")
cmd.color ("blue", "Gstrand131")


cmd.select("Gstrand132", "resi 381-391 & chain G ")
cmd.color ("red", "Gstrand132")


cmd.select("Gstrand133", "resi 429-434 & chain G ")
cmd.color ("green", "Gstrand133")


cmd.select("Hstrand134", "resi 174-177 & chain H ")
cmd.color ("orange", "Hstrand134")


cmd.select("Hstrand135", "resi 210-213 & chain H ")
cmd.color ("teal", "Hstrand135")


cmd.select("Hstrand136", "resi 262-271 & chain H ")
cmd.color ("yellow", "Hstrand136")


cmd.select("Hstrand137", "resi 276-278 & chain H ")
cmd.color ("blue", "Hstrand137")


cmd.select("Hstrand138", "resi 292-303 & chain H ")
cmd.color ("red", "Hstrand138")


cmd.select("Hstrand139", "resi 357-367 & chain H ")
cmd.color ("green", "Hstrand139")


cmd.select("Hstrand140", "resi 374-376 & chain H ")
cmd.color ("orange", "Hstrand140")


cmd.select("Hstrand141", "resi 381-391 & chain H ")
cmd.color ("teal", "Hstrand141")


cmd.select("Hstrand142", "resi 429-434 & chain H ")
cmd.color ("yellow", "Hstrand142")


cmd.select("Istrand143", "resi 155-158 & chain I ")
cmd.color ("blue", "Istrand143")


cmd.select("Istrand144", "resi 173-177 & chain I ")
cmd.color ("red", "Istrand144")


cmd.select("Istrand145", "resi 210-213 & chain I ")
cmd.color ("green", "Istrand145")


cmd.select("Istrand146", "resi 262-271 & chain I ")
cmd.color ("orange", "Istrand146")


cmd.select("Istrand147", "resi 276-278 & chain I ")
cmd.color ("teal", "Istrand147")


cmd.select("Istrand148", "resi 292-303 & chain I ")
cmd.color ("yellow", "Istrand148")


cmd.select("Istrand149", "resi 357-367 & chain I ")
cmd.color ("blue", "Istrand149")


cmd.select("Istrand150", "resi 374-376 & chain I ")
cmd.color ("red", "Istrand150")


cmd.select("Istrand151", "resi 381-391 & chain I ")
cmd.color ("green", "Istrand151")


cmd.select("Istrand152", "resi 429-434 & chain I ")
cmd.color ("orange", "Istrand152")


cmd.select("Jstrand153", "resi 156-158 & chain J ")
cmd.color ("teal", "Jstrand153")


cmd.select("Jstrand154", "resi 173-177 & chain J ")
cmd.color ("yellow", "Jstrand154")


cmd.select("Jstrand155", "resi 210-213 & chain J ")
cmd.color ("blue", "Jstrand155")


cmd.select("Jstrand156", "resi 262-271 & chain J ")
cmd.color ("red", "Jstrand156")


cmd.select("Jstrand157", "resi 276-278 & chain J ")
cmd.color ("green", "Jstrand157")


cmd.select("Jstrand158", "resi 292-303 & chain J ")
cmd.color ("orange", "Jstrand158")


cmd.select("Jstrand159", "resi 357-367 & chain J ")
cmd.color ("teal", "Jstrand159")


cmd.select("Jstrand160", "resi 374-376 & chain J ")
cmd.color ("yellow", "Jstrand160")


cmd.select("Jstrand161", "resi 381-391 & chain J ")
cmd.color ("blue", "Jstrand161")


cmd.select("Jstrand162", "resi 429-434 & chain J ")
cmd.color ("red", "Jstrand162")


cmd.select("Kstrand163", "resi 262-271 & chain K ")
cmd.color ("green", "Kstrand163")


cmd.select("Kstrand164", "resi 276-278 & chain K ")
cmd.color ("orange", "Kstrand164")


cmd.select("Kstrand165", "resi 292-303 & chain K ")
cmd.color ("teal", "Kstrand165")


cmd.select("Kstrand166", "resi 357-367 & chain K ")
cmd.color ("yellow", "Kstrand166")


cmd.select("Kstrand167", "resi 374-376 & chain K ")
cmd.color ("blue", "Kstrand167")


cmd.select("Kstrand168", "resi 381-391 & chain K ")
cmd.color ("red", "Kstrand168")


cmd.select("Kstrand169", "resi 429-434 & chain K ")
cmd.color ("green", "Kstrand169")


cmd.select("Lstrand170", "resi 156-158 & chain L ")
cmd.color ("orange", "Lstrand170")


cmd.select("Lstrand171", "resi 173-176 & chain L ")
cmd.color ("teal", "Lstrand171")


cmd.select("Lstrand172", "resi 210-212 & chain L ")
cmd.color ("yellow", "Lstrand172")


cmd.select("Lstrand173", "resi 262-271 & chain L ")
cmd.color ("blue", "Lstrand173")


cmd.select("Lstrand174", "resi 276-278 & chain L ")
cmd.color ("red", "Lstrand174")


cmd.select("Lstrand175", "resi 292-303 & chain L ")
cmd.color ("green", "Lstrand175")


cmd.select("Lstrand176", "resi 357-367 & chain L ")
cmd.color ("orange", "Lstrand176")


cmd.select("Lstrand177", "resi 374-376 & chain L ")
cmd.color ("teal", "Lstrand177")


cmd.select("Lstrand178", "resi 381-391 & chain L ")
cmd.color ("yellow", "Lstrand178")


cmd.select("Lstrand179", "resi 429-434 & chain L ")
cmd.color ("blue", "Lstrand179")


cmd.select("Mstrand180", "resi 174-177 & chain M ")
cmd.color ("red", "Mstrand180")


cmd.select("Mstrand181", "resi 210-213 & chain M ")
cmd.color ("green", "Mstrand181")


cmd.select("Mstrand182", "resi 262-271 & chain M ")
cmd.color ("orange", "Mstrand182")


cmd.select("Mstrand183", "resi 276-278 & chain M ")
cmd.color ("teal", "Mstrand183")


cmd.select("Mstrand184", "resi 292-303 & chain M ")
cmd.color ("yellow", "Mstrand184")


cmd.select("Mstrand185", "resi 357-367 & chain M ")
cmd.color ("blue", "Mstrand185")


cmd.select("Mstrand186", "resi 374-376 & chain M ")
cmd.color ("red", "Mstrand186")


cmd.select("Mstrand187", "resi 381-391 & chain M ")
cmd.color ("green", "Mstrand187")


cmd.select("Mstrand188", "resi 429-434 & chain M ")
cmd.color ("orange", "Mstrand188")


cmd.select("Nstrand189", "resi 155-158 & chain N ")
cmd.color ("teal", "Nstrand189")


cmd.select("Nstrand190", "resi 173-176 & chain N ")
cmd.color ("yellow", "Nstrand190")


cmd.select("Nstrand191", "resi 210-212 & chain N ")
cmd.color ("blue", "Nstrand191")


cmd.select("Nstrand192", "resi 262-271 & chain N ")
cmd.color ("red", "Nstrand192")


cmd.select("Nstrand193", "resi 276-278 & chain N ")
cmd.color ("green", "Nstrand193")


cmd.select("Nstrand194", "resi 292-303 & chain N ")
cmd.color ("orange", "Nstrand194")


cmd.select("Nstrand195", "resi 357-367 & chain N ")
cmd.color ("teal", "Nstrand195")


cmd.select("Nstrand196", "resi 374-376 & chain N ")
cmd.color ("yellow", "Nstrand196")


cmd.select("Nstrand197", "resi 381-391 & chain N ")
cmd.color ("blue", "Nstrand197")


cmd.select("Nstrand198", "resi 429-434 & chain N ")
cmd.color ("red", "Nstrand198")


cmd.select("Ostrand199", "resi 156-158 & chain O ")
cmd.color ("green", "Ostrand199")


cmd.select("Ostrand200", "resi 173-177 & chain O ")
cmd.color ("orange", "Ostrand200")


cmd.select("Ostrand201", "resi 210-213 & chain O ")
cmd.color ("teal", "Ostrand201")


cmd.select("Ostrand202", "resi 262-271 & chain O ")
cmd.color ("yellow", "Ostrand202")


cmd.select("Ostrand203", "resi 276-278 & chain O ")
cmd.color ("blue", "Ostrand203")


cmd.select("Ostrand204", "resi 292-303 & chain O ")
cmd.color ("red", "Ostrand204")


cmd.select("Ostrand205", "resi 357-367 & chain O ")
cmd.color ("green", "Ostrand205")


cmd.select("Ostrand206", "resi 374-376 & chain O ")
cmd.color ("orange", "Ostrand206")


cmd.select("Ostrand207", "resi 381-391 & chain O ")
cmd.color ("teal", "Ostrand207")


cmd.select("Ostrand208", "resi 429-434 & chain O ")
cmd.color ("yellow", "Ostrand208")


cmd.select("Pstrand209", "resi 174-177 & chain P ")
cmd.color ("blue", "Pstrand209")


cmd.select("Pstrand210", "resi 210-213 & chain P ")
cmd.color ("red", "Pstrand210")


cmd.select("Pstrand211", "resi 262-271 & chain P ")
cmd.color ("green", "Pstrand211")


cmd.select("Pstrand212", "resi 276-278 & chain P ")
cmd.color ("orange", "Pstrand212")


cmd.select("Pstrand213", "resi 293-303 & chain P ")
cmd.color ("teal", "Pstrand213")


cmd.select("Pstrand214", "resi 357-366 & chain P ")
cmd.color ("yellow", "Pstrand214")


cmd.select("Pstrand215", "resi 374-376 & chain P ")
cmd.color ("blue", "Pstrand215")


cmd.select("Pstrand216", "resi 381-391 & chain P ")
cmd.color ("red", "Pstrand216")


cmd.select("Pstrand217", "resi 429-434 & chain P ")
cmd.color ("green", "Pstrand217")


cmd.select("Qstrand218", "resi 156-158 & chain Q ")
cmd.color ("orange", "Qstrand218")


cmd.select("Qstrand219", "resi 173-177 & chain Q ")
cmd.color ("teal", "Qstrand219")


cmd.select("Qstrand220", "resi 210-213 & chain Q ")
cmd.color ("yellow", "Qstrand220")


cmd.select("Qstrand221", "resi 262-271 & chain Q ")
cmd.color ("blue", "Qstrand221")


cmd.select("Qstrand222", "resi 276-278 & chain Q ")
cmd.color ("red", "Qstrand222")


cmd.select("Qstrand223", "resi 292-303 & chain Q ")
cmd.color ("green", "Qstrand223")


cmd.select("Qstrand224", "resi 357-367 & chain Q ")
cmd.color ("orange", "Qstrand224")


cmd.select("Qstrand225", "resi 374-376 & chain Q ")
cmd.color ("teal", "Qstrand225")


cmd.select("Qstrand226", "resi 381-391 & chain Q ")
cmd.color ("yellow", "Qstrand226")


cmd.select("Qstrand227", "resi 429-434 & chain Q ")
cmd.color ("blue", "Qstrand227")


cmd.select("Rstrand228", "resi 156-158 & chain R ")
cmd.color ("red", "Rstrand228")


cmd.select("Rstrand229", "resi 173-176 & chain R ")
cmd.color ("green", "Rstrand229")


cmd.select("Rstrand230", "resi 210-212 & chain R ")
cmd.color ("orange", "Rstrand230")


cmd.select("Rstrand231", "resi 262-271 & chain R ")
cmd.color ("teal", "Rstrand231")


cmd.select("Rstrand232", "resi 276-278 & chain R ")
cmd.color ("yellow", "Rstrand232")


cmd.select("Rstrand233", "resi 293-303 & chain R ")
cmd.color ("blue", "Rstrand233")


cmd.select("Rstrand234", "resi 357-366 & chain R ")
cmd.color ("red", "Rstrand234")


cmd.select("Rstrand235", "resi 374-376 & chain R ")
cmd.color ("green", "Rstrand235")


cmd.select("Rstrand236", "resi 381-391 & chain R ")
cmd.color ("orange", "Rstrand236")


cmd.select("Rstrand237", "resi 429-434 & chain R ")
cmd.color ("teal", "Rstrand237")


cmd.select("Sstrand238", "resi 174-177 & chain S ")
cmd.color ("yellow", "Sstrand238")


cmd.select("Sstrand239", "resi 210-213 & chain S ")
cmd.color ("blue", "Sstrand239")


cmd.select("Sstrand240", "resi 262-271 & chain S ")
cmd.color ("red", "Sstrand240")


cmd.select("Sstrand241", "resi 276-278 & chain S ")
cmd.color ("green", "Sstrand241")


cmd.select("Sstrand242", "resi 292-303 & chain S ")
cmd.color ("orange", "Sstrand242")


cmd.select("Sstrand243", "resi 357-367 & chain S ")
cmd.color ("teal", "Sstrand243")


cmd.select("Sstrand244", "resi 374-376 & chain S ")
cmd.color ("yellow", "Sstrand244")


cmd.select("Sstrand245", "resi 381-391 & chain S ")
cmd.color ("blue", "Sstrand245")


cmd.select("Sstrand246", "resi 429-434 & chain S ")
cmd.color ("red", "Sstrand246")


cmd.select("Tstrand247", "resi 155-158 & chain T ")
cmd.color ("green", "Tstrand247")


cmd.select("Tstrand248", "resi 173-177 & chain T ")
cmd.color ("orange", "Tstrand248")


cmd.select("Tstrand249", "resi 210-213 & chain T ")
cmd.color ("teal", "Tstrand249")


cmd.select("Tstrand250", "resi 262-271 & chain T ")
cmd.color ("yellow", "Tstrand250")


cmd.select("Tstrand251", "resi 276-278 & chain T ")
cmd.color ("blue", "Tstrand251")


cmd.select("Tstrand252", "resi 292-303 & chain T ")
cmd.color ("red", "Tstrand252")


cmd.select("Tstrand253", "resi 357-367 & chain T ")
cmd.color ("green", "Tstrand253")


cmd.select("Tstrand254", "resi 374-376 & chain T ")
cmd.color ("orange", "Tstrand254")


cmd.select("Tstrand255", "resi 381-391 & chain T ")
cmd.color ("teal", "Tstrand255")


cmd.select("Tstrand256", "resi 429-434 & chain T ")
cmd.color ("yellow", "Tstrand256")


cmd.select("Ustrand257", "resi 156-158 & chain U ")
cmd.color ("blue", "Ustrand257")


cmd.select("Ustrand258", "resi 173-177 & chain U ")
cmd.color ("red", "Ustrand258")


cmd.select("Ustrand259", "resi 210-213 & chain U ")
cmd.color ("green", "Ustrand259")


cmd.select("Ustrand260", "resi 262-271 & chain U ")
cmd.color ("orange", "Ustrand260")


cmd.select("Ustrand261", "resi 276-278 & chain U ")
cmd.color ("teal", "Ustrand261")


cmd.select("Ustrand262", "resi 292-303 & chain U ")
cmd.color ("yellow", "Ustrand262")


cmd.select("Ustrand263", "resi 357-367 & chain U ")
cmd.color ("blue", "Ustrand263")


cmd.select("Ustrand264", "resi 374-376 & chain U ")
cmd.color ("red", "Ustrand264")


cmd.select("Ustrand265", "resi 381-391 & chain U ")
cmd.color ("green", "Ustrand265")


cmd.select("Ustrand266", "resi 429-434 & chain U ")
cmd.color ("orange", "Ustrand266")


cmd.select("Vstrand267", "resi 262-271 & chain V ")
cmd.color ("teal", "Vstrand267")


cmd.select("Vstrand268", "resi 276-278 & chain V ")
cmd.color ("yellow", "Vstrand268")


cmd.select("Vstrand269", "resi 292-303 & chain V ")
cmd.color ("blue", "Vstrand269")


cmd.select("Vstrand270", "resi 357-367 & chain V ")
cmd.color ("red", "Vstrand270")


cmd.select("Vstrand271", "resi 374-376 & chain V ")
cmd.color ("green", "Vstrand271")


cmd.select("Vstrand272", "resi 381-391 & chain V ")
cmd.color ("orange", "Vstrand272")


cmd.select("Vstrand273", "resi 429-434 & chain V ")
cmd.color ("teal", "Vstrand273")


cmd.select("Wstrand274", "resi 156-158 & chain W ")
cmd.color ("yellow", "Wstrand274")


cmd.select("Wstrand275", "resi 173-177 & chain W ")
cmd.color ("blue", "Wstrand275")


cmd.select("Wstrand276", "resi 210-213 & chain W ")
cmd.color ("red", "Wstrand276")


cmd.select("Wstrand277", "resi 262-271 & chain W ")
cmd.color ("green", "Wstrand277")


cmd.select("Wstrand278", "resi 276-278 & chain W ")
cmd.color ("orange", "Wstrand278")


cmd.select("Wstrand279", "resi 292-303 & chain W ")
cmd.color ("teal", "Wstrand279")


cmd.select("Wstrand280", "resi 357-367 & chain W ")
cmd.color ("yellow", "Wstrand280")


cmd.select("Wstrand281", "resi 374-376 & chain W ")
cmd.color ("blue", "Wstrand281")


cmd.select("Wstrand282", "resi 381-391 & chain W ")
cmd.color ("red", "Wstrand282")


cmd.select("Wstrand283", "resi 429-434 & chain W ")
cmd.color ("green", "Wstrand283")


cmd.select("Xstrand284", "resi 174-177 & chain X ")
cmd.color ("orange", "Xstrand284")


cmd.select("Xstrand285", "resi 210-213 & chain X ")
cmd.color ("teal", "Xstrand285")


cmd.select("Xstrand286", "resi 262-271 & chain X ")
cmd.color ("yellow", "Xstrand286")


cmd.select("Xstrand287", "resi 276-278 & chain X ")
cmd.color ("blue", "Xstrand287")


cmd.select("Xstrand288", "resi 292-303 & chain X ")
cmd.color ("red", "Xstrand288")


cmd.select("Xstrand289", "resi 357-367 & chain X ")
cmd.color ("green", "Xstrand289")


cmd.select("Xstrand290", "resi 374-376 & chain X ")
cmd.color ("orange", "Xstrand290")


cmd.select("Xstrand291", "resi 381-391 & chain X ")
cmd.color ("teal", "Xstrand291")


cmd.select("Xstrand292", "resi 429-434 & chain X ")
cmd.color ("yellow", "Xstrand292")


cmd.select("Ystrand293", "resi 156-158 & chain Y ")
cmd.color ("blue", "Ystrand293")


cmd.select("Ystrand294", "resi 173-176 & chain Y ")
cmd.color ("red", "Ystrand294")


cmd.select("Ystrand295", "resi 210-212 & chain Y ")
cmd.color ("green", "Ystrand295")


cmd.select("Ystrand296", "resi 262-271 & chain Y ")
cmd.color ("orange", "Ystrand296")


cmd.select("Ystrand297", "resi 276-278 & chain Y ")
cmd.color ("teal", "Ystrand297")


cmd.select("Ystrand298", "resi 292-303 & chain Y ")
cmd.color ("yellow", "Ystrand298")


cmd.select("Ystrand299", "resi 357-367 & chain Y ")
cmd.color ("blue", "Ystrand299")


cmd.select("Ystrand300", "resi 374-376 & chain Y ")
cmd.color ("red", "Ystrand300")


cmd.select("Ystrand301", "resi 381-391 & chain Y ")
cmd.color ("green", "Ystrand301")


cmd.select("Ystrand302", "resi 429-434 & chain Y ")
cmd.color ("orange", "Ystrand302")


cmd.select("Zstrand303", "resi 156-158 & chain Z ")
cmd.color ("teal", "Zstrand303")


cmd.select("Zstrand304", "resi 173-177 & chain Z ")
cmd.color ("yellow", "Zstrand304")


cmd.select("Zstrand305", "resi 210-213 & chain Z ")
cmd.color ("blue", "Zstrand305")


cmd.select("Zstrand306", "resi 262-271 & chain Z ")
cmd.color ("red", "Zstrand306")


cmd.select("Zstrand307", "resi 276-278 & chain Z ")
cmd.color ("green", "Zstrand307")


cmd.select("Zstrand308", "resi 292-303 & chain Z ")
cmd.color ("orange", "Zstrand308")


cmd.select("Zstrand309", "resi 357-367 & chain Z ")
cmd.color ("teal", "Zstrand309")


cmd.select("Zstrand310", "resi 374-376 & chain Z ")
cmd.color ("yellow", "Zstrand310")


cmd.select("Zstrand311", "resi 381-391 & chain Z ")
cmd.color ("blue", "Zstrand311")


cmd.select("Zstrand312", "resi 429-434 & chain Z ")
cmd.color ("red", "Zstrand312")


cmd.select("barrel", "astrand* or Astrand* or bstrand* or Bstrand* or cstrand* or Cstrand* or dstrand* or Dstrand* or estrand* or Estrand* or fstrand* or Fstrand* or gstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand* or Ostrand* or Pstrand* or Qstrand* or Rstrand* or Sstrand* or Tstrand* or Ustrand* or Vstrand* or Wstrand* or Xstrand* or Ystrand* or Zstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
