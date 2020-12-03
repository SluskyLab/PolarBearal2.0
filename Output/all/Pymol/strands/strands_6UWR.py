from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 235-238 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 241-244 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 300-345 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 349-382 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 387-397 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 403-413 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 418-423 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 430-433 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 438-439 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 447-449 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 461-462 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 477-486 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 489-490 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 496-497 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 514-519 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 526-531 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 558-559 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 564-565 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 577-580 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 610-614 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 618-620 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 655-658 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 668-676 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 684-689 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 694-698 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 705-706 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 709-712 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 721-724 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 732-740 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 768-773 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 782-788 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 802-809 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 815-821 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 826-827 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 836-841 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 858-863 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 869-875 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Bstrand37", "resi 235-238 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 241-244 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 300-345 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 349-382 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 387-397 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 403-413 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 418-423 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 430-433 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 438-439 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 447-449 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 461-462 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("Bstrand48", "resi 477-486 & chain B ")
cmd.color ("red", "Bstrand48")


cmd.select("Bstrand49", "resi 489-490 & chain B ")
cmd.color ("green", "Bstrand49")


cmd.select("Bstrand50", "resi 496-497 & chain B ")
cmd.color ("orange", "Bstrand50")


cmd.select("Bstrand51", "resi 514-519 & chain B ")
cmd.color ("teal", "Bstrand51")


cmd.select("Bstrand52", "resi 526-531 & chain B ")
cmd.color ("yellow", "Bstrand52")


cmd.select("Bstrand53", "resi 558-559 & chain B ")
cmd.color ("blue", "Bstrand53")


cmd.select("Bstrand54", "resi 564-565 & chain B ")
cmd.color ("red", "Bstrand54")


cmd.select("Bstrand55", "resi 577-580 & chain B ")
cmd.color ("green", "Bstrand55")


cmd.select("Bstrand56", "resi 610-614 & chain B ")
cmd.color ("orange", "Bstrand56")


cmd.select("Bstrand57", "resi 618-620 & chain B ")
cmd.color ("teal", "Bstrand57")


cmd.select("Bstrand58", "resi 655-658 & chain B ")
cmd.color ("yellow", "Bstrand58")


cmd.select("Bstrand59", "resi 668-676 & chain B ")
cmd.color ("blue", "Bstrand59")


cmd.select("Bstrand60", "resi 684-689 & chain B ")
cmd.color ("red", "Bstrand60")


cmd.select("Bstrand61", "resi 694-698 & chain B ")
cmd.color ("green", "Bstrand61")


cmd.select("Bstrand62", "resi 705-706 & chain B ")
cmd.color ("orange", "Bstrand62")


cmd.select("Bstrand63", "resi 709-712 & chain B ")
cmd.color ("teal", "Bstrand63")


cmd.select("Bstrand64", "resi 721-724 & chain B ")
cmd.color ("yellow", "Bstrand64")


cmd.select("Bstrand65", "resi 732-740 & chain B ")
cmd.color ("blue", "Bstrand65")


cmd.select("Bstrand66", "resi 768-773 & chain B ")
cmd.color ("red", "Bstrand66")


cmd.select("Bstrand67", "resi 782-788 & chain B ")
cmd.color ("green", "Bstrand67")


cmd.select("Bstrand68", "resi 802-809 & chain B ")
cmd.color ("orange", "Bstrand68")


cmd.select("Bstrand69", "resi 815-821 & chain B ")
cmd.color ("teal", "Bstrand69")


cmd.select("Bstrand70", "resi 826-827 & chain B ")
cmd.color ("yellow", "Bstrand70")


cmd.select("Bstrand71", "resi 836-841 & chain B ")
cmd.color ("blue", "Bstrand71")


cmd.select("Bstrand72", "resi 858-863 & chain B ")
cmd.color ("red", "Bstrand72")


cmd.select("Bstrand73", "resi 869-875 & chain B ")
cmd.color ("green", "Bstrand73")


cmd.select("Cstrand74", "resi 235-238 & chain C ")
cmd.color ("orange", "Cstrand74")


cmd.select("Cstrand75", "resi 241-244 & chain C ")
cmd.color ("teal", "Cstrand75")


cmd.select("Cstrand76", "resi 300-345 & chain C ")
cmd.color ("yellow", "Cstrand76")


cmd.select("Cstrand77", "resi 349-382 & chain C ")
cmd.color ("blue", "Cstrand77")


cmd.select("Cstrand78", "resi 387-397 & chain C ")
cmd.color ("red", "Cstrand78")


cmd.select("Cstrand79", "resi 403-413 & chain C ")
cmd.color ("green", "Cstrand79")


cmd.select("Cstrand80", "resi 418-423 & chain C ")
cmd.color ("orange", "Cstrand80")


cmd.select("Cstrand81", "resi 430-433 & chain C ")
cmd.color ("teal", "Cstrand81")


cmd.select("Cstrand82", "resi 438-439 & chain C ")
cmd.color ("yellow", "Cstrand82")


cmd.select("Cstrand83", "resi 447-449 & chain C ")
cmd.color ("blue", "Cstrand83")


cmd.select("Cstrand84", "resi 461-462 & chain C ")
cmd.color ("red", "Cstrand84")


cmd.select("Cstrand85", "resi 477-486 & chain C ")
cmd.color ("green", "Cstrand85")


cmd.select("Cstrand86", "resi 489-490 & chain C ")
cmd.color ("orange", "Cstrand86")


cmd.select("Cstrand87", "resi 496-497 & chain C ")
cmd.color ("teal", "Cstrand87")


cmd.select("Cstrand88", "resi 514-519 & chain C ")
cmd.color ("yellow", "Cstrand88")


cmd.select("Cstrand89", "resi 526-531 & chain C ")
cmd.color ("blue", "Cstrand89")


cmd.select("Cstrand90", "resi 558-559 & chain C ")
cmd.color ("red", "Cstrand90")


cmd.select("Cstrand91", "resi 564-565 & chain C ")
cmd.color ("green", "Cstrand91")


cmd.select("Cstrand92", "resi 577-580 & chain C ")
cmd.color ("orange", "Cstrand92")


cmd.select("Cstrand93", "resi 610-614 & chain C ")
cmd.color ("teal", "Cstrand93")


cmd.select("Cstrand94", "resi 618-620 & chain C ")
cmd.color ("yellow", "Cstrand94")


cmd.select("Cstrand95", "resi 655-658 & chain C ")
cmd.color ("blue", "Cstrand95")


cmd.select("Cstrand96", "resi 668-676 & chain C ")
cmd.color ("red", "Cstrand96")


cmd.select("Cstrand97", "resi 684-689 & chain C ")
cmd.color ("green", "Cstrand97")


cmd.select("Cstrand98", "resi 694-698 & chain C ")
cmd.color ("orange", "Cstrand98")


cmd.select("Cstrand99", "resi 705-706 & chain C ")
cmd.color ("teal", "Cstrand99")


cmd.select("Cstrand100", "resi 709-712 & chain C ")
cmd.color ("yellow", "Cstrand100")


cmd.select("Cstrand101", "resi 721-724 & chain C ")
cmd.color ("blue", "Cstrand101")


cmd.select("Cstrand102", "resi 732-740 & chain C ")
cmd.color ("red", "Cstrand102")


cmd.select("Cstrand103", "resi 768-773 & chain C ")
cmd.color ("green", "Cstrand103")


cmd.select("Cstrand104", "resi 782-788 & chain C ")
cmd.color ("orange", "Cstrand104")


cmd.select("Cstrand105", "resi 802-809 & chain C ")
cmd.color ("teal", "Cstrand105")


cmd.select("Cstrand106", "resi 815-821 & chain C ")
cmd.color ("yellow", "Cstrand106")


cmd.select("Cstrand107", "resi 826-827 & chain C ")
cmd.color ("blue", "Cstrand107")


cmd.select("Cstrand108", "resi 836-841 & chain C ")
cmd.color ("red", "Cstrand108")


cmd.select("Cstrand109", "resi 858-863 & chain C ")
cmd.color ("green", "Cstrand109")


cmd.select("Cstrand110", "resi 869-875 & chain C ")
cmd.color ("orange", "Cstrand110")


cmd.select("Dstrand111", "resi 235-238 & chain D ")
cmd.color ("teal", "Dstrand111")


cmd.select("Dstrand112", "resi 241-244 & chain D ")
cmd.color ("yellow", "Dstrand112")


cmd.select("Dstrand113", "resi 300-345 & chain D ")
cmd.color ("blue", "Dstrand113")


cmd.select("Dstrand114", "resi 349-382 & chain D ")
cmd.color ("red", "Dstrand114")


cmd.select("Dstrand115", "resi 387-397 & chain D ")
cmd.color ("green", "Dstrand115")


cmd.select("Dstrand116", "resi 403-413 & chain D ")
cmd.color ("orange", "Dstrand116")


cmd.select("Dstrand117", "resi 418-423 & chain D ")
cmd.color ("teal", "Dstrand117")


cmd.select("Dstrand118", "resi 430-433 & chain D ")
cmd.color ("yellow", "Dstrand118")


cmd.select("Dstrand119", "resi 438-439 & chain D ")
cmd.color ("blue", "Dstrand119")


cmd.select("Dstrand120", "resi 447-449 & chain D ")
cmd.color ("red", "Dstrand120")


cmd.select("Dstrand121", "resi 461-462 & chain D ")
cmd.color ("green", "Dstrand121")


cmd.select("Dstrand122", "resi 477-486 & chain D ")
cmd.color ("orange", "Dstrand122")


cmd.select("Dstrand123", "resi 489-490 & chain D ")
cmd.color ("teal", "Dstrand123")


cmd.select("Dstrand124", "resi 496-497 & chain D ")
cmd.color ("yellow", "Dstrand124")


cmd.select("Dstrand125", "resi 514-519 & chain D ")
cmd.color ("blue", "Dstrand125")


cmd.select("Dstrand126", "resi 526-531 & chain D ")
cmd.color ("red", "Dstrand126")


cmd.select("Dstrand127", "resi 558-559 & chain D ")
cmd.color ("green", "Dstrand127")


cmd.select("Dstrand128", "resi 564-565 & chain D ")
cmd.color ("orange", "Dstrand128")


cmd.select("Dstrand129", "resi 577-580 & chain D ")
cmd.color ("teal", "Dstrand129")


cmd.select("Dstrand130", "resi 610-614 & chain D ")
cmd.color ("yellow", "Dstrand130")


cmd.select("Dstrand131", "resi 618-620 & chain D ")
cmd.color ("blue", "Dstrand131")


cmd.select("Dstrand132", "resi 655-658 & chain D ")
cmd.color ("red", "Dstrand132")


cmd.select("Dstrand133", "resi 668-676 & chain D ")
cmd.color ("green", "Dstrand133")


cmd.select("Dstrand134", "resi 684-689 & chain D ")
cmd.color ("orange", "Dstrand134")


cmd.select("Dstrand135", "resi 694-698 & chain D ")
cmd.color ("teal", "Dstrand135")


cmd.select("Dstrand136", "resi 705-706 & chain D ")
cmd.color ("yellow", "Dstrand136")


cmd.select("Dstrand137", "resi 709-712 & chain D ")
cmd.color ("blue", "Dstrand137")


cmd.select("Dstrand138", "resi 721-724 & chain D ")
cmd.color ("red", "Dstrand138")


cmd.select("Dstrand139", "resi 732-740 & chain D ")
cmd.color ("green", "Dstrand139")


cmd.select("Dstrand140", "resi 768-773 & chain D ")
cmd.color ("orange", "Dstrand140")


cmd.select("Dstrand141", "resi 782-788 & chain D ")
cmd.color ("teal", "Dstrand141")


cmd.select("Dstrand142", "resi 802-809 & chain D ")
cmd.color ("yellow", "Dstrand142")


cmd.select("Dstrand143", "resi 815-821 & chain D ")
cmd.color ("blue", "Dstrand143")


cmd.select("Dstrand144", "resi 826-827 & chain D ")
cmd.color ("red", "Dstrand144")


cmd.select("Dstrand145", "resi 836-841 & chain D ")
cmd.color ("green", "Dstrand145")


cmd.select("Dstrand146", "resi 858-863 & chain D ")
cmd.color ("orange", "Dstrand146")


cmd.select("Dstrand147", "resi 869-875 & chain D ")
cmd.color ("teal", "Dstrand147")


cmd.select("Estrand148", "resi 235-238 & chain E ")
cmd.color ("yellow", "Estrand148")


cmd.select("Estrand149", "resi 241-244 & chain E ")
cmd.color ("blue", "Estrand149")


cmd.select("Estrand150", "resi 300-345 & chain E ")
cmd.color ("red", "Estrand150")


cmd.select("Estrand151", "resi 349-382 & chain E ")
cmd.color ("green", "Estrand151")


cmd.select("Estrand152", "resi 387-397 & chain E ")
cmd.color ("orange", "Estrand152")


cmd.select("Estrand153", "resi 403-413 & chain E ")
cmd.color ("teal", "Estrand153")


cmd.select("Estrand154", "resi 418-423 & chain E ")
cmd.color ("yellow", "Estrand154")


cmd.select("Estrand155", "resi 430-433 & chain E ")
cmd.color ("blue", "Estrand155")


cmd.select("Estrand156", "resi 438-439 & chain E ")
cmd.color ("red", "Estrand156")


cmd.select("Estrand157", "resi 447-449 & chain E ")
cmd.color ("green", "Estrand157")


cmd.select("Estrand158", "resi 461-462 & chain E ")
cmd.color ("orange", "Estrand158")


cmd.select("Estrand159", "resi 477-486 & chain E ")
cmd.color ("teal", "Estrand159")


cmd.select("Estrand160", "resi 489-490 & chain E ")
cmd.color ("yellow", "Estrand160")


cmd.select("Estrand161", "resi 496-497 & chain E ")
cmd.color ("blue", "Estrand161")


cmd.select("Estrand162", "resi 514-519 & chain E ")
cmd.color ("red", "Estrand162")


cmd.select("Estrand163", "resi 526-531 & chain E ")
cmd.color ("green", "Estrand163")


cmd.select("Estrand164", "resi 558-559 & chain E ")
cmd.color ("orange", "Estrand164")


cmd.select("Estrand165", "resi 564-565 & chain E ")
cmd.color ("teal", "Estrand165")


cmd.select("Estrand166", "resi 577-580 & chain E ")
cmd.color ("yellow", "Estrand166")


cmd.select("Estrand167", "resi 610-614 & chain E ")
cmd.color ("blue", "Estrand167")


cmd.select("Estrand168", "resi 618-620 & chain E ")
cmd.color ("red", "Estrand168")


cmd.select("Estrand169", "resi 655-658 & chain E ")
cmd.color ("green", "Estrand169")


cmd.select("Estrand170", "resi 668-676 & chain E ")
cmd.color ("orange", "Estrand170")


cmd.select("Estrand171", "resi 684-689 & chain E ")
cmd.color ("teal", "Estrand171")


cmd.select("Estrand172", "resi 694-698 & chain E ")
cmd.color ("yellow", "Estrand172")


cmd.select("Estrand173", "resi 705-706 & chain E ")
cmd.color ("blue", "Estrand173")


cmd.select("Estrand174", "resi 709-712 & chain E ")
cmd.color ("red", "Estrand174")


cmd.select("Estrand175", "resi 721-724 & chain E ")
cmd.color ("green", "Estrand175")


cmd.select("Estrand176", "resi 732-740 & chain E ")
cmd.color ("orange", "Estrand176")


cmd.select("Estrand177", "resi 768-773 & chain E ")
cmd.color ("teal", "Estrand177")


cmd.select("Estrand178", "resi 782-788 & chain E ")
cmd.color ("yellow", "Estrand178")


cmd.select("Estrand179", "resi 802-809 & chain E ")
cmd.color ("blue", "Estrand179")


cmd.select("Estrand180", "resi 815-821 & chain E ")
cmd.color ("red", "Estrand180")


cmd.select("Estrand181", "resi 826-827 & chain E ")
cmd.color ("green", "Estrand181")


cmd.select("Estrand182", "resi 836-841 & chain E ")
cmd.color ("orange", "Estrand182")


cmd.select("Estrand183", "resi 858-863 & chain E ")
cmd.color ("teal", "Estrand183")


cmd.select("Estrand184", "resi 869-875 & chain E ")
cmd.color ("yellow", "Estrand184")


cmd.select("Fstrand185", "resi 235-238 & chain F ")
cmd.color ("blue", "Fstrand185")


cmd.select("Fstrand186", "resi 241-244 & chain F ")
cmd.color ("red", "Fstrand186")


cmd.select("Fstrand187", "resi 300-345 & chain F ")
cmd.color ("green", "Fstrand187")


cmd.select("Fstrand188", "resi 349-382 & chain F ")
cmd.color ("orange", "Fstrand188")


cmd.select("Fstrand189", "resi 387-397 & chain F ")
cmd.color ("teal", "Fstrand189")


cmd.select("Fstrand190", "resi 403-413 & chain F ")
cmd.color ("yellow", "Fstrand190")


cmd.select("Fstrand191", "resi 418-423 & chain F ")
cmd.color ("blue", "Fstrand191")


cmd.select("Fstrand192", "resi 430-433 & chain F ")
cmd.color ("red", "Fstrand192")


cmd.select("Fstrand193", "resi 438-439 & chain F ")
cmd.color ("green", "Fstrand193")


cmd.select("Fstrand194", "resi 447-449 & chain F ")
cmd.color ("orange", "Fstrand194")


cmd.select("Fstrand195", "resi 461-462 & chain F ")
cmd.color ("teal", "Fstrand195")


cmd.select("Fstrand196", "resi 477-486 & chain F ")
cmd.color ("yellow", "Fstrand196")


cmd.select("Fstrand197", "resi 489-490 & chain F ")
cmd.color ("blue", "Fstrand197")


cmd.select("Fstrand198", "resi 496-497 & chain F ")
cmd.color ("red", "Fstrand198")


cmd.select("Fstrand199", "resi 514-519 & chain F ")
cmd.color ("green", "Fstrand199")


cmd.select("Fstrand200", "resi 526-531 & chain F ")
cmd.color ("orange", "Fstrand200")


cmd.select("Fstrand201", "resi 558-559 & chain F ")
cmd.color ("teal", "Fstrand201")


cmd.select("Fstrand202", "resi 564-565 & chain F ")
cmd.color ("yellow", "Fstrand202")


cmd.select("Fstrand203", "resi 577-580 & chain F ")
cmd.color ("blue", "Fstrand203")


cmd.select("Fstrand204", "resi 610-614 & chain F ")
cmd.color ("red", "Fstrand204")


cmd.select("Fstrand205", "resi 618-620 & chain F ")
cmd.color ("green", "Fstrand205")


cmd.select("Fstrand206", "resi 655-658 & chain F ")
cmd.color ("orange", "Fstrand206")


cmd.select("Fstrand207", "resi 668-676 & chain F ")
cmd.color ("teal", "Fstrand207")


cmd.select("Fstrand208", "resi 684-689 & chain F ")
cmd.color ("yellow", "Fstrand208")


cmd.select("Fstrand209", "resi 694-698 & chain F ")
cmd.color ("blue", "Fstrand209")


cmd.select("Fstrand210", "resi 705-706 & chain F ")
cmd.color ("red", "Fstrand210")


cmd.select("Fstrand211", "resi 709-712 & chain F ")
cmd.color ("green", "Fstrand211")


cmd.select("Fstrand212", "resi 721-724 & chain F ")
cmd.color ("orange", "Fstrand212")


cmd.select("Fstrand213", "resi 732-740 & chain F ")
cmd.color ("teal", "Fstrand213")


cmd.select("Fstrand214", "resi 768-773 & chain F ")
cmd.color ("yellow", "Fstrand214")


cmd.select("Fstrand215", "resi 782-788 & chain F ")
cmd.color ("blue", "Fstrand215")


cmd.select("Fstrand216", "resi 802-809 & chain F ")
cmd.color ("red", "Fstrand216")


cmd.select("Fstrand217", "resi 815-821 & chain F ")
cmd.color ("green", "Fstrand217")


cmd.select("Fstrand218", "resi 826-827 & chain F ")
cmd.color ("orange", "Fstrand218")


cmd.select("Fstrand219", "resi 836-841 & chain F ")
cmd.color ("teal", "Fstrand219")


cmd.select("Fstrand220", "resi 858-863 & chain F ")
cmd.color ("yellow", "Fstrand220")


cmd.select("Fstrand221", "resi 869-875 & chain F ")
cmd.color ("blue", "Fstrand221")


cmd.select("Gstrand222", "resi 235-238 & chain G ")
cmd.color ("red", "Gstrand222")


cmd.select("Gstrand223", "resi 241-244 & chain G ")
cmd.color ("green", "Gstrand223")


cmd.select("Gstrand224", "resi 300-345 & chain G ")
cmd.color ("orange", "Gstrand224")


cmd.select("Gstrand225", "resi 349-382 & chain G ")
cmd.color ("teal", "Gstrand225")


cmd.select("Gstrand226", "resi 387-397 & chain G ")
cmd.color ("yellow", "Gstrand226")


cmd.select("Gstrand227", "resi 403-413 & chain G ")
cmd.color ("blue", "Gstrand227")


cmd.select("Gstrand228", "resi 418-423 & chain G ")
cmd.color ("red", "Gstrand228")


cmd.select("Gstrand229", "resi 430-433 & chain G ")
cmd.color ("green", "Gstrand229")


cmd.select("Gstrand230", "resi 438-439 & chain G ")
cmd.color ("orange", "Gstrand230")


cmd.select("Gstrand231", "resi 447-449 & chain G ")
cmd.color ("teal", "Gstrand231")


cmd.select("Gstrand232", "resi 461-462 & chain G ")
cmd.color ("yellow", "Gstrand232")


cmd.select("Gstrand233", "resi 477-486 & chain G ")
cmd.color ("blue", "Gstrand233")


cmd.select("Gstrand234", "resi 489-490 & chain G ")
cmd.color ("red", "Gstrand234")


cmd.select("Gstrand235", "resi 496-497 & chain G ")
cmd.color ("green", "Gstrand235")


cmd.select("Gstrand236", "resi 514-519 & chain G ")
cmd.color ("orange", "Gstrand236")


cmd.select("Gstrand237", "resi 526-531 & chain G ")
cmd.color ("teal", "Gstrand237")


cmd.select("Gstrand238", "resi 558-559 & chain G ")
cmd.color ("yellow", "Gstrand238")


cmd.select("Gstrand239", "resi 564-565 & chain G ")
cmd.color ("blue", "Gstrand239")


cmd.select("Gstrand240", "resi 577-580 & chain G ")
cmd.color ("red", "Gstrand240")


cmd.select("Gstrand241", "resi 610-614 & chain G ")
cmd.color ("green", "Gstrand241")


cmd.select("Gstrand242", "resi 618-620 & chain G ")
cmd.color ("orange", "Gstrand242")


cmd.select("Gstrand243", "resi 655-658 & chain G ")
cmd.color ("teal", "Gstrand243")


cmd.select("Gstrand244", "resi 668-676 & chain G ")
cmd.color ("yellow", "Gstrand244")


cmd.select("Gstrand245", "resi 684-689 & chain G ")
cmd.color ("blue", "Gstrand245")


cmd.select("Gstrand246", "resi 694-698 & chain G ")
cmd.color ("red", "Gstrand246")


cmd.select("Gstrand247", "resi 705-706 & chain G ")
cmd.color ("green", "Gstrand247")


cmd.select("Gstrand248", "resi 709-712 & chain G ")
cmd.color ("orange", "Gstrand248")


cmd.select("Gstrand249", "resi 721-724 & chain G ")
cmd.color ("teal", "Gstrand249")


cmd.select("Gstrand250", "resi 732-740 & chain G ")
cmd.color ("yellow", "Gstrand250")


cmd.select("Gstrand251", "resi 768-773 & chain G ")
cmd.color ("blue", "Gstrand251")


cmd.select("Gstrand252", "resi 782-788 & chain G ")
cmd.color ("red", "Gstrand252")


cmd.select("Gstrand253", "resi 802-809 & chain G ")
cmd.color ("green", "Gstrand253")


cmd.select("Gstrand254", "resi 815-821 & chain G ")
cmd.color ("orange", "Gstrand254")


cmd.select("Gstrand255", "resi 826-827 & chain G ")
cmd.color ("teal", "Gstrand255")


cmd.select("Gstrand256", "resi 836-841 & chain G ")
cmd.color ("yellow", "Gstrand256")


cmd.select("Gstrand257", "resi 858-863 & chain G ")
cmd.color ("blue", "Gstrand257")


cmd.select("Gstrand258", "resi 869-875 & chain G ")
cmd.color ("red", "Gstrand258")


cmd.select("Hstrand259", "resi 235-237 & chain H ")
cmd.color ("green", "Hstrand259")


cmd.select("Hstrand260", "resi 242-244 & chain H ")
cmd.color ("orange", "Hstrand260")


cmd.select("Hstrand261", "resi 300-310 & chain H ")
cmd.color ("teal", "Hstrand261")


cmd.select("Hstrand262", "resi 322-330 & chain H ")
cmd.color ("yellow", "Hstrand262")


cmd.select("Hstrand263", "resi 351-354 & chain H ")
cmd.color ("blue", "Hstrand263")


cmd.select("Hstrand264", "resi 362-367 & chain H ")
cmd.color ("red", "Hstrand264")


cmd.select("Hstrand265", "resi 387-397 & chain H ")
cmd.color ("green", "Hstrand265")


cmd.select("Hstrand266", "resi 404-413 & chain H ")
cmd.color ("orange", "Hstrand266")


cmd.select("Hstrand267", "resi 418-423 & chain H ")
cmd.color ("teal", "Hstrand267")


cmd.select("Hstrand268", "resi 438-439 & chain H ")
cmd.color ("yellow", "Hstrand268")


cmd.select("Hstrand269", "resi 447-448 & chain H ")
cmd.color ("blue", "Hstrand269")


cmd.select("Hstrand270", "resi 460-462 & chain H ")
cmd.color ("red", "Hstrand270")


cmd.select("Hstrand271", "resi 477-486 & chain H ")
cmd.color ("green", "Hstrand271")


cmd.select("Hstrand272", "resi 489-490 & chain H ")
cmd.color ("orange", "Hstrand272")


cmd.select("Hstrand273", "resi 496-497 & chain H ")
cmd.color ("teal", "Hstrand273")


cmd.select("Hstrand274", "resi 514-519 & chain H ")
cmd.color ("yellow", "Hstrand274")


cmd.select("Hstrand275", "resi 526-531 & chain H ")
cmd.color ("blue", "Hstrand275")


cmd.select("Hstrand276", "resi 577-581 & chain H ")
cmd.color ("red", "Hstrand276")


cmd.select("Hstrand277", "resi 610-614 & chain H ")
cmd.color ("green", "Hstrand277")


cmd.select("Hstrand278", "resi 618-620 & chain H ")
cmd.color ("orange", "Hstrand278")


cmd.select("Hstrand279", "resi 657-658 & chain H ")
cmd.color ("teal", "Hstrand279")


cmd.select("Hstrand280", "resi 667-676 & chain H ")
cmd.color ("yellow", "Hstrand280")


cmd.select("Hstrand281", "resi 684-689 & chain H ")
cmd.color ("blue", "Hstrand281")


cmd.select("Hstrand282", "resi 694-698 & chain H ")
cmd.color ("red", "Hstrand282")


cmd.select("Hstrand283", "resi 705-706 & chain H ")
cmd.color ("green", "Hstrand283")


cmd.select("Hstrand284", "resi 709-712 & chain H ")
cmd.color ("orange", "Hstrand284")


cmd.select("Hstrand285", "resi 721-727 & chain H ")
cmd.color ("teal", "Hstrand285")


cmd.select("Hstrand286", "resi 732-743 & chain H ")
cmd.color ("yellow", "Hstrand286")


cmd.select("Hstrand287", "resi 768-773 & chain H ")
cmd.color ("blue", "Hstrand287")


cmd.select("Hstrand288", "resi 782-788 & chain H ")
cmd.color ("red", "Hstrand288")


cmd.select("Hstrand289", "resi 802-809 & chain H ")
cmd.color ("green", "Hstrand289")


cmd.select("Hstrand290", "resi 815-820 & chain H ")
cmd.color ("orange", "Hstrand290")


cmd.select("Hstrand291", "resi 826-827 & chain H ")
cmd.color ("teal", "Hstrand291")


cmd.select("Hstrand292", "resi 836-841 & chain H ")
cmd.color ("yellow", "Hstrand292")


cmd.select("Hstrand293", "resi 859-863 & chain H ")
cmd.color ("blue", "Hstrand293")


cmd.select("Hstrand294", "resi 869-874 & chain H ")
cmd.color ("red", "Hstrand294")


cmd.select("Istrand295", "resi 235-237 & chain I ")
cmd.color ("green", "Istrand295")


cmd.select("Istrand296", "resi 242-244 & chain I ")
cmd.color ("orange", "Istrand296")


cmd.select("Istrand297", "resi 300-310 & chain I ")
cmd.color ("teal", "Istrand297")


cmd.select("Istrand298", "resi 322-330 & chain I ")
cmd.color ("yellow", "Istrand298")


cmd.select("Istrand299", "resi 351-354 & chain I ")
cmd.color ("blue", "Istrand299")


cmd.select("Istrand300", "resi 362-367 & chain I ")
cmd.color ("red", "Istrand300")


cmd.select("Istrand301", "resi 387-397 & chain I ")
cmd.color ("green", "Istrand301")


cmd.select("Istrand302", "resi 404-413 & chain I ")
cmd.color ("orange", "Istrand302")


cmd.select("Istrand303", "resi 418-423 & chain I ")
cmd.color ("teal", "Istrand303")


cmd.select("Istrand304", "resi 438-439 & chain I ")
cmd.color ("yellow", "Istrand304")


cmd.select("Istrand305", "resi 447-448 & chain I ")
cmd.color ("blue", "Istrand305")


cmd.select("Istrand306", "resi 460-462 & chain I ")
cmd.color ("red", "Istrand306")


cmd.select("Istrand307", "resi 477-486 & chain I ")
cmd.color ("green", "Istrand307")


cmd.select("Istrand308", "resi 489-490 & chain I ")
cmd.color ("orange", "Istrand308")


cmd.select("Istrand309", "resi 496-497 & chain I ")
cmd.color ("teal", "Istrand309")


cmd.select("Istrand310", "resi 514-519 & chain I ")
cmd.color ("yellow", "Istrand310")


cmd.select("Istrand311", "resi 526-531 & chain I ")
cmd.color ("blue", "Istrand311")


cmd.select("Istrand312", "resi 577-581 & chain I ")
cmd.color ("red", "Istrand312")


cmd.select("Istrand313", "resi 610-614 & chain I ")
cmd.color ("green", "Istrand313")


cmd.select("Istrand314", "resi 618-620 & chain I ")
cmd.color ("orange", "Istrand314")


cmd.select("Istrand315", "resi 657-658 & chain I ")
cmd.color ("teal", "Istrand315")


cmd.select("Istrand316", "resi 667-676 & chain I ")
cmd.color ("yellow", "Istrand316")


cmd.select("Istrand317", "resi 684-689 & chain I ")
cmd.color ("blue", "Istrand317")


cmd.select("Istrand318", "resi 694-698 & chain I ")
cmd.color ("red", "Istrand318")


cmd.select("Istrand319", "resi 705-706 & chain I ")
cmd.color ("green", "Istrand319")


cmd.select("Istrand320", "resi 709-712 & chain I ")
cmd.color ("orange", "Istrand320")


cmd.select("Istrand321", "resi 721-727 & chain I ")
cmd.color ("teal", "Istrand321")


cmd.select("Istrand322", "resi 732-743 & chain I ")
cmd.color ("yellow", "Istrand322")


cmd.select("Istrand323", "resi 768-773 & chain I ")
cmd.color ("blue", "Istrand323")


cmd.select("Istrand324", "resi 782-788 & chain I ")
cmd.color ("red", "Istrand324")


cmd.select("Istrand325", "resi 802-809 & chain I ")
cmd.color ("green", "Istrand325")


cmd.select("Istrand326", "resi 815-820 & chain I ")
cmd.color ("orange", "Istrand326")


cmd.select("Istrand327", "resi 826-827 & chain I ")
cmd.color ("teal", "Istrand327")


cmd.select("Istrand328", "resi 836-841 & chain I ")
cmd.color ("yellow", "Istrand328")


cmd.select("Istrand329", "resi 859-863 & chain I ")
cmd.color ("blue", "Istrand329")


cmd.select("Istrand330", "resi 869-874 & chain I ")
cmd.color ("red", "Istrand330")


cmd.select("Jstrand331", "resi 235-237 & chain J ")
cmd.color ("green", "Jstrand331")


cmd.select("Jstrand332", "resi 242-244 & chain J ")
cmd.color ("orange", "Jstrand332")


cmd.select("Jstrand333", "resi 300-310 & chain J ")
cmd.color ("teal", "Jstrand333")


cmd.select("Jstrand334", "resi 322-330 & chain J ")
cmd.color ("yellow", "Jstrand334")


cmd.select("Jstrand335", "resi 351-354 & chain J ")
cmd.color ("blue", "Jstrand335")


cmd.select("Jstrand336", "resi 362-367 & chain J ")
cmd.color ("red", "Jstrand336")


cmd.select("Jstrand337", "resi 387-397 & chain J ")
cmd.color ("green", "Jstrand337")


cmd.select("Jstrand338", "resi 404-413 & chain J ")
cmd.color ("orange", "Jstrand338")


cmd.select("Jstrand339", "resi 418-423 & chain J ")
cmd.color ("teal", "Jstrand339")


cmd.select("Jstrand340", "resi 438-439 & chain J ")
cmd.color ("yellow", "Jstrand340")


cmd.select("Jstrand341", "resi 447-448 & chain J ")
cmd.color ("blue", "Jstrand341")


cmd.select("Jstrand342", "resi 460-462 & chain J ")
cmd.color ("red", "Jstrand342")


cmd.select("Jstrand343", "resi 477-486 & chain J ")
cmd.color ("green", "Jstrand343")


cmd.select("Jstrand344", "resi 489-490 & chain J ")
cmd.color ("orange", "Jstrand344")


cmd.select("Jstrand345", "resi 496-497 & chain J ")
cmd.color ("teal", "Jstrand345")


cmd.select("Jstrand346", "resi 514-519 & chain J ")
cmd.color ("yellow", "Jstrand346")


cmd.select("Jstrand347", "resi 526-531 & chain J ")
cmd.color ("blue", "Jstrand347")


cmd.select("Jstrand348", "resi 577-581 & chain J ")
cmd.color ("red", "Jstrand348")


cmd.select("Jstrand349", "resi 610-614 & chain J ")
cmd.color ("green", "Jstrand349")


cmd.select("Jstrand350", "resi 618-620 & chain J ")
cmd.color ("orange", "Jstrand350")


cmd.select("Jstrand351", "resi 657-658 & chain J ")
cmd.color ("teal", "Jstrand351")


cmd.select("Jstrand352", "resi 667-676 & chain J ")
cmd.color ("yellow", "Jstrand352")


cmd.select("Jstrand353", "resi 684-689 & chain J ")
cmd.color ("blue", "Jstrand353")


cmd.select("Jstrand354", "resi 694-698 & chain J ")
cmd.color ("red", "Jstrand354")


cmd.select("Jstrand355", "resi 705-706 & chain J ")
cmd.color ("green", "Jstrand355")


cmd.select("Jstrand356", "resi 709-712 & chain J ")
cmd.color ("orange", "Jstrand356")


cmd.select("Jstrand357", "resi 721-727 & chain J ")
cmd.color ("teal", "Jstrand357")


cmd.select("Jstrand358", "resi 732-743 & chain J ")
cmd.color ("yellow", "Jstrand358")


cmd.select("Jstrand359", "resi 768-773 & chain J ")
cmd.color ("blue", "Jstrand359")


cmd.select("Jstrand360", "resi 782-788 & chain J ")
cmd.color ("red", "Jstrand360")


cmd.select("Jstrand361", "resi 802-809 & chain J ")
cmd.color ("green", "Jstrand361")


cmd.select("Jstrand362", "resi 815-820 & chain J ")
cmd.color ("orange", "Jstrand362")


cmd.select("Jstrand363", "resi 826-827 & chain J ")
cmd.color ("teal", "Jstrand363")


cmd.select("Jstrand364", "resi 836-841 & chain J ")
cmd.color ("yellow", "Jstrand364")


cmd.select("Jstrand365", "resi 859-863 & chain J ")
cmd.color ("blue", "Jstrand365")


cmd.select("Jstrand366", "resi 869-874 & chain J ")
cmd.color ("red", "Jstrand366")


cmd.select("Kstrand367", "resi 235-237 & chain K ")
cmd.color ("green", "Kstrand367")


cmd.select("Kstrand368", "resi 242-244 & chain K ")
cmd.color ("orange", "Kstrand368")


cmd.select("Kstrand369", "resi 300-310 & chain K ")
cmd.color ("teal", "Kstrand369")


cmd.select("Kstrand370", "resi 322-330 & chain K ")
cmd.color ("yellow", "Kstrand370")


cmd.select("Kstrand371", "resi 351-354 & chain K ")
cmd.color ("blue", "Kstrand371")


cmd.select("Kstrand372", "resi 362-367 & chain K ")
cmd.color ("red", "Kstrand372")


cmd.select("Kstrand373", "resi 387-397 & chain K ")
cmd.color ("green", "Kstrand373")


cmd.select("Kstrand374", "resi 404-413 & chain K ")
cmd.color ("orange", "Kstrand374")


cmd.select("Kstrand375", "resi 418-423 & chain K ")
cmd.color ("teal", "Kstrand375")


cmd.select("Kstrand376", "resi 438-439 & chain K ")
cmd.color ("yellow", "Kstrand376")


cmd.select("Kstrand377", "resi 447-448 & chain K ")
cmd.color ("blue", "Kstrand377")


cmd.select("Kstrand378", "resi 460-462 & chain K ")
cmd.color ("red", "Kstrand378")


cmd.select("Kstrand379", "resi 477-486 & chain K ")
cmd.color ("green", "Kstrand379")


cmd.select("Kstrand380", "resi 489-490 & chain K ")
cmd.color ("orange", "Kstrand380")


cmd.select("Kstrand381", "resi 496-497 & chain K ")
cmd.color ("teal", "Kstrand381")


cmd.select("Kstrand382", "resi 514-519 & chain K ")
cmd.color ("yellow", "Kstrand382")


cmd.select("Kstrand383", "resi 526-531 & chain K ")
cmd.color ("blue", "Kstrand383")


cmd.select("Kstrand384", "resi 577-581 & chain K ")
cmd.color ("red", "Kstrand384")


cmd.select("Kstrand385", "resi 610-614 & chain K ")
cmd.color ("green", "Kstrand385")


cmd.select("Kstrand386", "resi 618-620 & chain K ")
cmd.color ("orange", "Kstrand386")


cmd.select("Kstrand387", "resi 657-658 & chain K ")
cmd.color ("teal", "Kstrand387")


cmd.select("Kstrand388", "resi 667-676 & chain K ")
cmd.color ("yellow", "Kstrand388")


cmd.select("Kstrand389", "resi 684-689 & chain K ")
cmd.color ("blue", "Kstrand389")


cmd.select("Kstrand390", "resi 694-698 & chain K ")
cmd.color ("red", "Kstrand390")


cmd.select("Kstrand391", "resi 705-706 & chain K ")
cmd.color ("green", "Kstrand391")


cmd.select("Kstrand392", "resi 709-712 & chain K ")
cmd.color ("orange", "Kstrand392")


cmd.select("Kstrand393", "resi 721-727 & chain K ")
cmd.color ("teal", "Kstrand393")


cmd.select("Kstrand394", "resi 732-743 & chain K ")
cmd.color ("yellow", "Kstrand394")


cmd.select("Kstrand395", "resi 768-773 & chain K ")
cmd.color ("blue", "Kstrand395")


cmd.select("Kstrand396", "resi 782-788 & chain K ")
cmd.color ("red", "Kstrand396")


cmd.select("Kstrand397", "resi 802-809 & chain K ")
cmd.color ("green", "Kstrand397")


cmd.select("Kstrand398", "resi 815-820 & chain K ")
cmd.color ("orange", "Kstrand398")


cmd.select("Kstrand399", "resi 826-827 & chain K ")
cmd.color ("teal", "Kstrand399")


cmd.select("Kstrand400", "resi 836-841 & chain K ")
cmd.color ("yellow", "Kstrand400")


cmd.select("Kstrand401", "resi 859-863 & chain K ")
cmd.color ("blue", "Kstrand401")


cmd.select("Kstrand402", "resi 869-874 & chain K ")
cmd.color ("red", "Kstrand402")


cmd.select("Lstrand403", "resi 235-237 & chain L ")
cmd.color ("green", "Lstrand403")


cmd.select("Lstrand404", "resi 242-244 & chain L ")
cmd.color ("orange", "Lstrand404")


cmd.select("Lstrand405", "resi 300-310 & chain L ")
cmd.color ("teal", "Lstrand405")


cmd.select("Lstrand406", "resi 322-330 & chain L ")
cmd.color ("yellow", "Lstrand406")


cmd.select("Lstrand407", "resi 351-354 & chain L ")
cmd.color ("blue", "Lstrand407")


cmd.select("Lstrand408", "resi 362-367 & chain L ")
cmd.color ("red", "Lstrand408")


cmd.select("Lstrand409", "resi 387-397 & chain L ")
cmd.color ("green", "Lstrand409")


cmd.select("Lstrand410", "resi 404-413 & chain L ")
cmd.color ("orange", "Lstrand410")


cmd.select("Lstrand411", "resi 418-423 & chain L ")
cmd.color ("teal", "Lstrand411")


cmd.select("Lstrand412", "resi 438-439 & chain L ")
cmd.color ("yellow", "Lstrand412")


cmd.select("Lstrand413", "resi 447-448 & chain L ")
cmd.color ("blue", "Lstrand413")


cmd.select("Lstrand414", "resi 460-462 & chain L ")
cmd.color ("red", "Lstrand414")


cmd.select("Lstrand415", "resi 477-486 & chain L ")
cmd.color ("green", "Lstrand415")


cmd.select("Lstrand416", "resi 489-490 & chain L ")
cmd.color ("orange", "Lstrand416")


cmd.select("Lstrand417", "resi 496-497 & chain L ")
cmd.color ("teal", "Lstrand417")


cmd.select("Lstrand418", "resi 514-519 & chain L ")
cmd.color ("yellow", "Lstrand418")


cmd.select("Lstrand419", "resi 526-531 & chain L ")
cmd.color ("blue", "Lstrand419")


cmd.select("Lstrand420", "resi 577-581 & chain L ")
cmd.color ("red", "Lstrand420")


cmd.select("Lstrand421", "resi 610-614 & chain L ")
cmd.color ("green", "Lstrand421")


cmd.select("Lstrand422", "resi 618-620 & chain L ")
cmd.color ("orange", "Lstrand422")


cmd.select("Lstrand423", "resi 657-658 & chain L ")
cmd.color ("teal", "Lstrand423")


cmd.select("Lstrand424", "resi 667-676 & chain L ")
cmd.color ("yellow", "Lstrand424")


cmd.select("Lstrand425", "resi 684-689 & chain L ")
cmd.color ("blue", "Lstrand425")


cmd.select("Lstrand426", "resi 694-698 & chain L ")
cmd.color ("red", "Lstrand426")


cmd.select("Lstrand427", "resi 705-706 & chain L ")
cmd.color ("green", "Lstrand427")


cmd.select("Lstrand428", "resi 709-712 & chain L ")
cmd.color ("orange", "Lstrand428")


cmd.select("Lstrand429", "resi 721-727 & chain L ")
cmd.color ("teal", "Lstrand429")


cmd.select("Lstrand430", "resi 732-743 & chain L ")
cmd.color ("yellow", "Lstrand430")


cmd.select("Lstrand431", "resi 768-773 & chain L ")
cmd.color ("blue", "Lstrand431")


cmd.select("Lstrand432", "resi 782-788 & chain L ")
cmd.color ("red", "Lstrand432")


cmd.select("Lstrand433", "resi 802-809 & chain L ")
cmd.color ("green", "Lstrand433")


cmd.select("Lstrand434", "resi 815-820 & chain L ")
cmd.color ("orange", "Lstrand434")


cmd.select("Lstrand435", "resi 826-827 & chain L ")
cmd.color ("teal", "Lstrand435")


cmd.select("Lstrand436", "resi 836-841 & chain L ")
cmd.color ("yellow", "Lstrand436")


cmd.select("Lstrand437", "resi 859-863 & chain L ")
cmd.color ("blue", "Lstrand437")


cmd.select("Lstrand438", "resi 869-874 & chain L ")
cmd.color ("red", "Lstrand438")


cmd.select("Mstrand439", "resi 235-237 & chain M ")
cmd.color ("green", "Mstrand439")


cmd.select("Mstrand440", "resi 242-244 & chain M ")
cmd.color ("orange", "Mstrand440")


cmd.select("Mstrand441", "resi 300-310 & chain M ")
cmd.color ("teal", "Mstrand441")


cmd.select("Mstrand442", "resi 322-330 & chain M ")
cmd.color ("yellow", "Mstrand442")


cmd.select("Mstrand443", "resi 351-354 & chain M ")
cmd.color ("blue", "Mstrand443")


cmd.select("Mstrand444", "resi 362-367 & chain M ")
cmd.color ("red", "Mstrand444")


cmd.select("Mstrand445", "resi 387-397 & chain M ")
cmd.color ("green", "Mstrand445")


cmd.select("Mstrand446", "resi 404-413 & chain M ")
cmd.color ("orange", "Mstrand446")


cmd.select("Mstrand447", "resi 418-423 & chain M ")
cmd.color ("teal", "Mstrand447")


cmd.select("Mstrand448", "resi 438-439 & chain M ")
cmd.color ("yellow", "Mstrand448")


cmd.select("Mstrand449", "resi 447-448 & chain M ")
cmd.color ("blue", "Mstrand449")


cmd.select("Mstrand450", "resi 460-462 & chain M ")
cmd.color ("red", "Mstrand450")


cmd.select("Mstrand451", "resi 477-486 & chain M ")
cmd.color ("green", "Mstrand451")


cmd.select("Mstrand452", "resi 489-490 & chain M ")
cmd.color ("orange", "Mstrand452")


cmd.select("Mstrand453", "resi 496-497 & chain M ")
cmd.color ("teal", "Mstrand453")


cmd.select("Mstrand454", "resi 514-519 & chain M ")
cmd.color ("yellow", "Mstrand454")


cmd.select("Mstrand455", "resi 526-531 & chain M ")
cmd.color ("blue", "Mstrand455")


cmd.select("Mstrand456", "resi 577-581 & chain M ")
cmd.color ("red", "Mstrand456")


cmd.select("Mstrand457", "resi 610-614 & chain M ")
cmd.color ("green", "Mstrand457")


cmd.select("Mstrand458", "resi 618-620 & chain M ")
cmd.color ("orange", "Mstrand458")


cmd.select("Mstrand459", "resi 657-658 & chain M ")
cmd.color ("teal", "Mstrand459")


cmd.select("Mstrand460", "resi 667-676 & chain M ")
cmd.color ("yellow", "Mstrand460")


cmd.select("Mstrand461", "resi 684-689 & chain M ")
cmd.color ("blue", "Mstrand461")


cmd.select("Mstrand462", "resi 694-698 & chain M ")
cmd.color ("red", "Mstrand462")


cmd.select("Mstrand463", "resi 705-706 & chain M ")
cmd.color ("green", "Mstrand463")


cmd.select("Mstrand464", "resi 709-712 & chain M ")
cmd.color ("orange", "Mstrand464")


cmd.select("Mstrand465", "resi 721-727 & chain M ")
cmd.color ("teal", "Mstrand465")


cmd.select("Mstrand466", "resi 732-743 & chain M ")
cmd.color ("yellow", "Mstrand466")


cmd.select("Mstrand467", "resi 768-773 & chain M ")
cmd.color ("blue", "Mstrand467")


cmd.select("Mstrand468", "resi 782-788 & chain M ")
cmd.color ("red", "Mstrand468")


cmd.select("Mstrand469", "resi 802-809 & chain M ")
cmd.color ("green", "Mstrand469")


cmd.select("Mstrand470", "resi 815-820 & chain M ")
cmd.color ("orange", "Mstrand470")


cmd.select("Mstrand471", "resi 826-827 & chain M ")
cmd.color ("teal", "Mstrand471")


cmd.select("Mstrand472", "resi 836-841 & chain M ")
cmd.color ("yellow", "Mstrand472")


cmd.select("Mstrand473", "resi 859-863 & chain M ")
cmd.color ("blue", "Mstrand473")


cmd.select("Mstrand474", "resi 869-874 & chain M ")
cmd.color ("red", "Mstrand474")


cmd.select("Nstrand475", "resi 235-237 & chain N ")
cmd.color ("green", "Nstrand475")


cmd.select("Nstrand476", "resi 242-244 & chain N ")
cmd.color ("orange", "Nstrand476")


cmd.select("Nstrand477", "resi 300-310 & chain N ")
cmd.color ("teal", "Nstrand477")


cmd.select("Nstrand478", "resi 322-330 & chain N ")
cmd.color ("yellow", "Nstrand478")


cmd.select("Nstrand479", "resi 351-354 & chain N ")
cmd.color ("blue", "Nstrand479")


cmd.select("Nstrand480", "resi 362-367 & chain N ")
cmd.color ("red", "Nstrand480")


cmd.select("Nstrand481", "resi 387-397 & chain N ")
cmd.color ("green", "Nstrand481")


cmd.select("Nstrand482", "resi 404-413 & chain N ")
cmd.color ("orange", "Nstrand482")


cmd.select("Nstrand483", "resi 418-423 & chain N ")
cmd.color ("teal", "Nstrand483")


cmd.select("Nstrand484", "resi 438-439 & chain N ")
cmd.color ("yellow", "Nstrand484")


cmd.select("Nstrand485", "resi 447-448 & chain N ")
cmd.color ("blue", "Nstrand485")


cmd.select("Nstrand486", "resi 460-462 & chain N ")
cmd.color ("red", "Nstrand486")


cmd.select("Nstrand487", "resi 477-486 & chain N ")
cmd.color ("green", "Nstrand487")


cmd.select("Nstrand488", "resi 489-490 & chain N ")
cmd.color ("orange", "Nstrand488")


cmd.select("Nstrand489", "resi 496-497 & chain N ")
cmd.color ("teal", "Nstrand489")


cmd.select("Nstrand490", "resi 514-519 & chain N ")
cmd.color ("yellow", "Nstrand490")


cmd.select("Nstrand491", "resi 526-531 & chain N ")
cmd.color ("blue", "Nstrand491")


cmd.select("Nstrand492", "resi 577-581 & chain N ")
cmd.color ("red", "Nstrand492")


cmd.select("Nstrand493", "resi 610-614 & chain N ")
cmd.color ("green", "Nstrand493")


cmd.select("Nstrand494", "resi 618-620 & chain N ")
cmd.color ("orange", "Nstrand494")


cmd.select("Nstrand495", "resi 657-658 & chain N ")
cmd.color ("teal", "Nstrand495")


cmd.select("Nstrand496", "resi 667-676 & chain N ")
cmd.color ("yellow", "Nstrand496")


cmd.select("Nstrand497", "resi 684-689 & chain N ")
cmd.color ("blue", "Nstrand497")


cmd.select("Nstrand498", "resi 694-698 & chain N ")
cmd.color ("red", "Nstrand498")


cmd.select("Nstrand499", "resi 705-706 & chain N ")
cmd.color ("green", "Nstrand499")


cmd.select("Nstrand500", "resi 709-712 & chain N ")
cmd.color ("orange", "Nstrand500")


cmd.select("Nstrand501", "resi 721-727 & chain N ")
cmd.color ("teal", "Nstrand501")


cmd.select("Nstrand502", "resi 732-743 & chain N ")
cmd.color ("yellow", "Nstrand502")


cmd.select("Nstrand503", "resi 768-773 & chain N ")
cmd.color ("blue", "Nstrand503")


cmd.select("Nstrand504", "resi 782-788 & chain N ")
cmd.color ("red", "Nstrand504")


cmd.select("Nstrand505", "resi 802-809 & chain N ")
cmd.color ("green", "Nstrand505")


cmd.select("Nstrand506", "resi 815-820 & chain N ")
cmd.color ("orange", "Nstrand506")


cmd.select("Nstrand507", "resi 826-827 & chain N ")
cmd.color ("teal", "Nstrand507")


cmd.select("Nstrand508", "resi 836-841 & chain N ")
cmd.color ("yellow", "Nstrand508")


cmd.select("Nstrand509", "resi 859-863 & chain N ")
cmd.color ("blue", "Nstrand509")


cmd.select("Nstrand510", "resi 869-874 & chain N ")
cmd.color ("red", "Nstrand510")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
