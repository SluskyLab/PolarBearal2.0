from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3O44.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 142-151 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 158-160 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 171-173 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 179-190 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 205-211 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 219-221 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 228-232 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 241-260 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 266-271 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 279-299 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 303-334 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 337-344 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 142-151 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 158-160 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 171-173 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 179-190 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 205-211 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 219-221 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 228-232 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 241-260 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 266-271 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 279-298 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 303-334 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 337-344 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Cstrand24", "resi 142-151 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 158-160 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 171-173 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 179-190 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 205-211 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 219-221 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 228-232 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 241-260 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 266-271 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 279-298 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 303-334 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 337-344 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Dstrand36", "resi 142-151 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 158-160 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 171-173 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 179-190 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 205-211 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 219-221 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 228-232 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 241-260 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 266-271 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 279-299 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 303-334 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 337-344 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Estrand48", "resi 142-151 & chain E ")
cmd.color ("red", "Estrand48")


cmd.select("Estrand49", "resi 158-160 & chain E ")
cmd.color ("green", "Estrand49")


cmd.select("Estrand50", "resi 171-173 & chain E ")
cmd.color ("orange", "Estrand50")


cmd.select("Estrand51", "resi 179-190 & chain E ")
cmd.color ("teal", "Estrand51")


cmd.select("Estrand52", "resi 205-211 & chain E ")
cmd.color ("yellow", "Estrand52")


cmd.select("Estrand53", "resi 219-221 & chain E ")
cmd.color ("blue", "Estrand53")


cmd.select("Estrand54", "resi 228-232 & chain E ")
cmd.color ("red", "Estrand54")


cmd.select("Estrand55", "resi 241-260 & chain E ")
cmd.color ("green", "Estrand55")


cmd.select("Estrand56", "resi 266-271 & chain E ")
cmd.color ("orange", "Estrand56")


cmd.select("Estrand57", "resi 279-298 & chain E ")
cmd.color ("teal", "Estrand57")


cmd.select("Estrand58", "resi 303-334 & chain E ")
cmd.color ("yellow", "Estrand58")


cmd.select("Estrand59", "resi 337-344 & chain E ")
cmd.color ("blue", "Estrand59")


cmd.select("Fstrand60", "resi 142-151 & chain F ")
cmd.color ("red", "Fstrand60")


cmd.select("Fstrand61", "resi 158-160 & chain F ")
cmd.color ("green", "Fstrand61")


cmd.select("Fstrand62", "resi 171-173 & chain F ")
cmd.color ("orange", "Fstrand62")


cmd.select("Fstrand63", "resi 179-190 & chain F ")
cmd.color ("teal", "Fstrand63")


cmd.select("Fstrand64", "resi 205-211 & chain F ")
cmd.color ("yellow", "Fstrand64")


cmd.select("Fstrand65", "resi 219-221 & chain F ")
cmd.color ("blue", "Fstrand65")


cmd.select("Fstrand66", "resi 228-232 & chain F ")
cmd.color ("red", "Fstrand66")


cmd.select("Fstrand67", "resi 241-260 & chain F ")
cmd.color ("green", "Fstrand67")


cmd.select("Fstrand68", "resi 265-271 & chain F ")
cmd.color ("orange", "Fstrand68")


cmd.select("Fstrand69", "resi 279-298 & chain F ")
cmd.color ("teal", "Fstrand69")


cmd.select("Fstrand70", "resi 303-334 & chain F ")
cmd.color ("yellow", "Fstrand70")


cmd.select("Fstrand71", "resi 337-344 & chain F ")
cmd.color ("blue", "Fstrand71")


cmd.select("Gstrand72", "resi 142-151 & chain G ")
cmd.color ("red", "Gstrand72")


cmd.select("Gstrand73", "resi 158-160 & chain G ")
cmd.color ("green", "Gstrand73")


cmd.select("Gstrand74", "resi 171-173 & chain G ")
cmd.color ("orange", "Gstrand74")


cmd.select("Gstrand75", "resi 179-190 & chain G ")
cmd.color ("teal", "Gstrand75")


cmd.select("Gstrand76", "resi 205-211 & chain G ")
cmd.color ("yellow", "Gstrand76")


cmd.select("Gstrand77", "resi 219-221 & chain G ")
cmd.color ("blue", "Gstrand77")


cmd.select("Gstrand78", "resi 228-232 & chain G ")
cmd.color ("red", "Gstrand78")


cmd.select("Gstrand79", "resi 241-260 & chain G ")
cmd.color ("green", "Gstrand79")


cmd.select("Gstrand80", "resi 266-271 & chain G ")
cmd.color ("orange", "Gstrand80")


cmd.select("Gstrand81", "resi 279-298 & chain G ")
cmd.color ("teal", "Gstrand81")


cmd.select("Gstrand82", "resi 303-334 & chain G ")
cmd.color ("yellow", "Gstrand82")


cmd.select("Gstrand83", "resi 337-344 & chain G ")
cmd.color ("blue", "Gstrand83")


cmd.select("Hstrand84", "resi 142-151 & chain H ")
cmd.color ("red", "Hstrand84")


cmd.select("Hstrand85", "resi 158-160 & chain H ")
cmd.color ("green", "Hstrand85")


cmd.select("Hstrand86", "resi 171-173 & chain H ")
cmd.color ("orange", "Hstrand86")


cmd.select("Hstrand87", "resi 179-190 & chain H ")
cmd.color ("teal", "Hstrand87")


cmd.select("Hstrand88", "resi 205-211 & chain H ")
cmd.color ("yellow", "Hstrand88")


cmd.select("Hstrand89", "resi 219-221 & chain H ")
cmd.color ("blue", "Hstrand89")


cmd.select("Hstrand90", "resi 228-232 & chain H ")
cmd.color ("red", "Hstrand90")


cmd.select("Hstrand91", "resi 241-260 & chain H ")
cmd.color ("green", "Hstrand91")


cmd.select("Hstrand92", "resi 265-271 & chain H ")
cmd.color ("orange", "Hstrand92")


cmd.select("Hstrand93", "resi 279-298 & chain H ")
cmd.color ("teal", "Hstrand93")


cmd.select("Hstrand94", "resi 326-334 & chain H ")
cmd.color ("yellow", "Hstrand94")


cmd.select("Hstrand95", "resi 337-344 & chain H ")
cmd.color ("blue", "Hstrand95")


cmd.select("Istrand96", "resi 142-151 & chain I ")
cmd.color ("red", "Istrand96")


cmd.select("Istrand97", "resi 158-160 & chain I ")
cmd.color ("green", "Istrand97")


cmd.select("Istrand98", "resi 171-173 & chain I ")
cmd.color ("orange", "Istrand98")


cmd.select("Istrand99", "resi 179-190 & chain I ")
cmd.color ("teal", "Istrand99")


cmd.select("Istrand100", "resi 205-211 & chain I ")
cmd.color ("yellow", "Istrand100")


cmd.select("Istrand101", "resi 219-221 & chain I ")
cmd.color ("blue", "Istrand101")


cmd.select("Istrand102", "resi 228-232 & chain I ")
cmd.color ("red", "Istrand102")


cmd.select("Istrand103", "resi 241-260 & chain I ")
cmd.color ("green", "Istrand103")


cmd.select("Istrand104", "resi 265-271 & chain I ")
cmd.color ("orange", "Istrand104")


cmd.select("Istrand105", "resi 279-299 & chain I ")
cmd.color ("teal", "Istrand105")


cmd.select("Istrand106", "resi 303-334 & chain I ")
cmd.color ("yellow", "Istrand106")


cmd.select("Istrand107", "resi 337-344 & chain I ")
cmd.color ("blue", "Istrand107")


cmd.select("Jstrand108", "resi 142-151 & chain J ")
cmd.color ("red", "Jstrand108")


cmd.select("Jstrand109", "resi 158-160 & chain J ")
cmd.color ("green", "Jstrand109")


cmd.select("Jstrand110", "resi 171-173 & chain J ")
cmd.color ("orange", "Jstrand110")


cmd.select("Jstrand111", "resi 179-190 & chain J ")
cmd.color ("teal", "Jstrand111")


cmd.select("Jstrand112", "resi 205-211 & chain J ")
cmd.color ("yellow", "Jstrand112")


cmd.select("Jstrand113", "resi 219-221 & chain J ")
cmd.color ("blue", "Jstrand113")


cmd.select("Jstrand114", "resi 228-232 & chain J ")
cmd.color ("red", "Jstrand114")


cmd.select("Jstrand115", "resi 241-260 & chain J ")
cmd.color ("green", "Jstrand115")


cmd.select("Jstrand116", "resi 265-271 & chain J ")
cmd.color ("orange", "Jstrand116")


cmd.select("Jstrand117", "resi 279-299 & chain J ")
cmd.color ("teal", "Jstrand117")


cmd.select("Jstrand118", "resi 303-334 & chain J ")
cmd.color ("yellow", "Jstrand118")


cmd.select("Jstrand119", "resi 337-344 & chain J ")
cmd.color ("blue", "Jstrand119")


cmd.select("Kstrand120", "resi 142-151 & chain K ")
cmd.color ("red", "Kstrand120")


cmd.select("Kstrand121", "resi 158-160 & chain K ")
cmd.color ("green", "Kstrand121")


cmd.select("Kstrand122", "resi 171-173 & chain K ")
cmd.color ("orange", "Kstrand122")


cmd.select("Kstrand123", "resi 179-190 & chain K ")
cmd.color ("teal", "Kstrand123")


cmd.select("Kstrand124", "resi 205-211 & chain K ")
cmd.color ("yellow", "Kstrand124")


cmd.select("Kstrand125", "resi 219-221 & chain K ")
cmd.color ("blue", "Kstrand125")


cmd.select("Kstrand126", "resi 228-232 & chain K ")
cmd.color ("red", "Kstrand126")


cmd.select("Kstrand127", "resi 241-260 & chain K ")
cmd.color ("green", "Kstrand127")


cmd.select("Kstrand128", "resi 266-271 & chain K ")
cmd.color ("orange", "Kstrand128")


cmd.select("Kstrand129", "resi 279-298 & chain K ")
cmd.color ("teal", "Kstrand129")


cmd.select("Kstrand130", "resi 303-334 & chain K ")
cmd.color ("yellow", "Kstrand130")


cmd.select("Kstrand131", "resi 337-344 & chain K ")
cmd.color ("blue", "Kstrand131")


cmd.select("Lstrand132", "resi 142-151 & chain L ")
cmd.color ("red", "Lstrand132")


cmd.select("Lstrand133", "resi 158-160 & chain L ")
cmd.color ("green", "Lstrand133")


cmd.select("Lstrand134", "resi 171-173 & chain L ")
cmd.color ("orange", "Lstrand134")


cmd.select("Lstrand135", "resi 179-190 & chain L ")
cmd.color ("teal", "Lstrand135")


cmd.select("Lstrand136", "resi 205-211 & chain L ")
cmd.color ("yellow", "Lstrand136")


cmd.select("Lstrand137", "resi 219-221 & chain L ")
cmd.color ("blue", "Lstrand137")


cmd.select("Lstrand138", "resi 228-232 & chain L ")
cmd.color ("red", "Lstrand138")


cmd.select("Lstrand139", "resi 241-260 & chain L ")
cmd.color ("green", "Lstrand139")


cmd.select("Lstrand140", "resi 265-271 & chain L ")
cmd.color ("orange", "Lstrand140")


cmd.select("Lstrand141", "resi 279-299 & chain L ")
cmd.color ("teal", "Lstrand141")


cmd.select("Lstrand142", "resi 303-334 & chain L ")
cmd.color ("yellow", "Lstrand142")


cmd.select("Lstrand143", "resi 337-344 & chain L ")
cmd.color ("blue", "Lstrand143")


cmd.select("Mstrand144", "resi 142-151 & chain M ")
cmd.color ("red", "Mstrand144")


cmd.select("Mstrand145", "resi 158-160 & chain M ")
cmd.color ("green", "Mstrand145")


cmd.select("Mstrand146", "resi 171-173 & chain M ")
cmd.color ("orange", "Mstrand146")


cmd.select("Mstrand147", "resi 179-190 & chain M ")
cmd.color ("teal", "Mstrand147")


cmd.select("Mstrand148", "resi 205-211 & chain M ")
cmd.color ("yellow", "Mstrand148")


cmd.select("Mstrand149", "resi 219-221 & chain M ")
cmd.color ("blue", "Mstrand149")


cmd.select("Mstrand150", "resi 228-232 & chain M ")
cmd.color ("red", "Mstrand150")


cmd.select("Mstrand151", "resi 241-260 & chain M ")
cmd.color ("green", "Mstrand151")


cmd.select("Mstrand152", "resi 265-271 & chain M ")
cmd.color ("orange", "Mstrand152")


cmd.select("Mstrand153", "resi 279-299 & chain M ")
cmd.color ("teal", "Mstrand153")


cmd.select("Mstrand154", "resi 303-334 & chain M ")
cmd.color ("yellow", "Mstrand154")


cmd.select("Mstrand155", "resi 337-344 & chain M ")
cmd.color ("blue", "Mstrand155")


cmd.select("Nstrand156", "resi 142-151 & chain N ")
cmd.color ("red", "Nstrand156")


cmd.select("Nstrand157", "resi 158-160 & chain N ")
cmd.color ("green", "Nstrand157")


cmd.select("Nstrand158", "resi 171-173 & chain N ")
cmd.color ("orange", "Nstrand158")


cmd.select("Nstrand159", "resi 179-190 & chain N ")
cmd.color ("teal", "Nstrand159")


cmd.select("Nstrand160", "resi 205-211 & chain N ")
cmd.color ("yellow", "Nstrand160")


cmd.select("Nstrand161", "resi 219-221 & chain N ")
cmd.color ("blue", "Nstrand161")


cmd.select("Nstrand162", "resi 228-232 & chain N ")
cmd.color ("red", "Nstrand162")


cmd.select("Nstrand163", "resi 241-260 & chain N ")
cmd.color ("green", "Nstrand163")


cmd.select("Nstrand164", "resi 266-271 & chain N ")
cmd.color ("orange", "Nstrand164")


cmd.select("Nstrand165", "resi 279-298 & chain N ")
cmd.color ("teal", "Nstrand165")


cmd.select("Nstrand166", "resi 303-334 & chain N ")
cmd.color ("yellow", "Nstrand166")


cmd.select("Nstrand167", "resi 337-344 & chain N ")
cmd.color ("blue", "Nstrand167")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
