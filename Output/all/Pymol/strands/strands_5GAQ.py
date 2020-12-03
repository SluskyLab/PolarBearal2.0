from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GAQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 11-28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34-66 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 74-107 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 111-122 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 128-138 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 148-156 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 168-172 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 178-184 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 187-193 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 200-204 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 209-213 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 223-226 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 232-235 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 257-259 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 269-273 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 281-285 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 291-295 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Bstrand17", "resi 11-28 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 34-66 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 74-107 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 111-122 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 128-138 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 148-156 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 168-172 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 178-184 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 187-193 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 200-204 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 209-213 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 223-226 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 232-235 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 257-259 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 269-273 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 281-285 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 291-295 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Cstrand34", "resi 11-28 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 34-66 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Cstrand36", "resi 74-107 & chain C ")
cmd.color ("red", "Cstrand36")


cmd.select("Cstrand37", "resi 111-122 & chain C ")
cmd.color ("green", "Cstrand37")


cmd.select("Cstrand38", "resi 128-138 & chain C ")
cmd.color ("orange", "Cstrand38")


cmd.select("Cstrand39", "resi 148-156 & chain C ")
cmd.color ("teal", "Cstrand39")


cmd.select("Cstrand40", "resi 168-172 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 178-184 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 187-193 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 200-204 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 209-213 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 223-226 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 232-235 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 257-259 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 269-273 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 281-285 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 291-295 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Dstrand51", "resi 11-28 & chain D ")
cmd.color ("teal", "Dstrand51")


cmd.select("Dstrand52", "resi 34-66 & chain D ")
cmd.color ("yellow", "Dstrand52")


cmd.select("Dstrand53", "resi 74-107 & chain D ")
cmd.color ("blue", "Dstrand53")


cmd.select("Dstrand54", "resi 111-122 & chain D ")
cmd.color ("red", "Dstrand54")


cmd.select("Dstrand55", "resi 128-138 & chain D ")
cmd.color ("green", "Dstrand55")


cmd.select("Dstrand56", "resi 148-156 & chain D ")
cmd.color ("orange", "Dstrand56")


cmd.select("Dstrand57", "resi 168-172 & chain D ")
cmd.color ("teal", "Dstrand57")


cmd.select("Dstrand58", "resi 178-184 & chain D ")
cmd.color ("yellow", "Dstrand58")


cmd.select("Dstrand59", "resi 187-193 & chain D ")
cmd.color ("blue", "Dstrand59")


cmd.select("Dstrand60", "resi 200-204 & chain D ")
cmd.color ("red", "Dstrand60")


cmd.select("Dstrand61", "resi 209-213 & chain D ")
cmd.color ("green", "Dstrand61")


cmd.select("Dstrand62", "resi 223-226 & chain D ")
cmd.color ("orange", "Dstrand62")


cmd.select("Dstrand63", "resi 232-235 & chain D ")
cmd.color ("teal", "Dstrand63")


cmd.select("Dstrand64", "resi 257-259 & chain D ")
cmd.color ("yellow", "Dstrand64")


cmd.select("Dstrand65", "resi 269-273 & chain D ")
cmd.color ("blue", "Dstrand65")


cmd.select("Dstrand66", "resi 281-285 & chain D ")
cmd.color ("red", "Dstrand66")


cmd.select("Dstrand67", "resi 291-295 & chain D ")
cmd.color ("green", "Dstrand67")


cmd.select("Estrand68", "resi 11-28 & chain E ")
cmd.color ("orange", "Estrand68")


cmd.select("Estrand69", "resi 34-66 & chain E ")
cmd.color ("teal", "Estrand69")


cmd.select("Estrand70", "resi 74-107 & chain E ")
cmd.color ("yellow", "Estrand70")


cmd.select("Estrand71", "resi 111-122 & chain E ")
cmd.color ("blue", "Estrand71")


cmd.select("Estrand72", "resi 128-138 & chain E ")
cmd.color ("red", "Estrand72")


cmd.select("Estrand73", "resi 148-156 & chain E ")
cmd.color ("green", "Estrand73")


cmd.select("Estrand74", "resi 168-172 & chain E ")
cmd.color ("orange", "Estrand74")


cmd.select("Estrand75", "resi 178-184 & chain E ")
cmd.color ("teal", "Estrand75")


cmd.select("Estrand76", "resi 187-193 & chain E ")
cmd.color ("yellow", "Estrand76")


cmd.select("Estrand77", "resi 200-204 & chain E ")
cmd.color ("blue", "Estrand77")


cmd.select("Estrand78", "resi 209-213 & chain E ")
cmd.color ("red", "Estrand78")


cmd.select("Estrand79", "resi 223-226 & chain E ")
cmd.color ("green", "Estrand79")


cmd.select("Estrand80", "resi 232-235 & chain E ")
cmd.color ("orange", "Estrand80")


cmd.select("Estrand81", "resi 257-259 & chain E ")
cmd.color ("teal", "Estrand81")


cmd.select("Estrand82", "resi 269-273 & chain E ")
cmd.color ("yellow", "Estrand82")


cmd.select("Estrand83", "resi 281-285 & chain E ")
cmd.color ("blue", "Estrand83")


cmd.select("Estrand84", "resi 291-295 & chain E ")
cmd.color ("red", "Estrand84")


cmd.select("Fstrand85", "resi 11-28 & chain F ")
cmd.color ("green", "Fstrand85")


cmd.select("Fstrand86", "resi 34-66 & chain F ")
cmd.color ("orange", "Fstrand86")


cmd.select("Fstrand87", "resi 74-107 & chain F ")
cmd.color ("teal", "Fstrand87")


cmd.select("Fstrand88", "resi 111-122 & chain F ")
cmd.color ("yellow", "Fstrand88")


cmd.select("Fstrand89", "resi 128-138 & chain F ")
cmd.color ("blue", "Fstrand89")


cmd.select("Fstrand90", "resi 148-156 & chain F ")
cmd.color ("red", "Fstrand90")


cmd.select("Fstrand91", "resi 168-172 & chain F ")
cmd.color ("green", "Fstrand91")


cmd.select("Fstrand92", "resi 178-184 & chain F ")
cmd.color ("orange", "Fstrand92")


cmd.select("Fstrand93", "resi 187-193 & chain F ")
cmd.color ("teal", "Fstrand93")


cmd.select("Fstrand94", "resi 200-204 & chain F ")
cmd.color ("yellow", "Fstrand94")


cmd.select("Fstrand95", "resi 209-213 & chain F ")
cmd.color ("blue", "Fstrand95")


cmd.select("Fstrand96", "resi 223-226 & chain F ")
cmd.color ("red", "Fstrand96")


cmd.select("Fstrand97", "resi 232-235 & chain F ")
cmd.color ("green", "Fstrand97")


cmd.select("Fstrand98", "resi 257-259 & chain F ")
cmd.color ("orange", "Fstrand98")


cmd.select("Fstrand99", "resi 269-273 & chain F ")
cmd.color ("teal", "Fstrand99")


cmd.select("Fstrand100", "resi 281-285 & chain F ")
cmd.color ("yellow", "Fstrand100")


cmd.select("Fstrand101", "resi 291-295 & chain F ")
cmd.color ("blue", "Fstrand101")


cmd.select("Gstrand102", "resi 11-28 & chain G ")
cmd.color ("red", "Gstrand102")


cmd.select("Gstrand103", "resi 34-66 & chain G ")
cmd.color ("green", "Gstrand103")


cmd.select("Gstrand104", "resi 74-107 & chain G ")
cmd.color ("orange", "Gstrand104")


cmd.select("Gstrand105", "resi 111-122 & chain G ")
cmd.color ("teal", "Gstrand105")


cmd.select("Gstrand106", "resi 128-138 & chain G ")
cmd.color ("yellow", "Gstrand106")


cmd.select("Gstrand107", "resi 148-156 & chain G ")
cmd.color ("blue", "Gstrand107")


cmd.select("Gstrand108", "resi 168-172 & chain G ")
cmd.color ("red", "Gstrand108")


cmd.select("Gstrand109", "resi 178-184 & chain G ")
cmd.color ("green", "Gstrand109")


cmd.select("Gstrand110", "resi 187-193 & chain G ")
cmd.color ("orange", "Gstrand110")


cmd.select("Gstrand111", "resi 200-204 & chain G ")
cmd.color ("teal", "Gstrand111")


cmd.select("Gstrand112", "resi 209-213 & chain G ")
cmd.color ("yellow", "Gstrand112")


cmd.select("Gstrand113", "resi 223-226 & chain G ")
cmd.color ("blue", "Gstrand113")


cmd.select("Gstrand114", "resi 232-235 & chain G ")
cmd.color ("red", "Gstrand114")


cmd.select("Gstrand115", "resi 257-259 & chain G ")
cmd.color ("green", "Gstrand115")


cmd.select("Gstrand116", "resi 269-273 & chain G ")
cmd.color ("orange", "Gstrand116")


cmd.select("Gstrand117", "resi 281-285 & chain G ")
cmd.color ("teal", "Gstrand117")


cmd.select("Gstrand118", "resi 291-295 & chain G ")
cmd.color ("yellow", "Gstrand118")


cmd.select("Hstrand119", "resi 11-28 & chain H ")
cmd.color ("blue", "Hstrand119")


cmd.select("Hstrand120", "resi 34-66 & chain H ")
cmd.color ("red", "Hstrand120")


cmd.select("Hstrand121", "resi 74-107 & chain H ")
cmd.color ("green", "Hstrand121")


cmd.select("Hstrand122", "resi 111-122 & chain H ")
cmd.color ("orange", "Hstrand122")


cmd.select("Hstrand123", "resi 128-138 & chain H ")
cmd.color ("teal", "Hstrand123")


cmd.select("Hstrand124", "resi 148-156 & chain H ")
cmd.color ("yellow", "Hstrand124")


cmd.select("Hstrand125", "resi 168-172 & chain H ")
cmd.color ("blue", "Hstrand125")


cmd.select("Hstrand126", "resi 178-184 & chain H ")
cmd.color ("red", "Hstrand126")


cmd.select("Hstrand127", "resi 187-193 & chain H ")
cmd.color ("green", "Hstrand127")


cmd.select("Hstrand128", "resi 200-204 & chain H ")
cmd.color ("orange", "Hstrand128")


cmd.select("Hstrand129", "resi 209-213 & chain H ")
cmd.color ("teal", "Hstrand129")


cmd.select("Hstrand130", "resi 223-226 & chain H ")
cmd.color ("yellow", "Hstrand130")


cmd.select("Hstrand131", "resi 232-235 & chain H ")
cmd.color ("blue", "Hstrand131")


cmd.select("Hstrand132", "resi 257-259 & chain H ")
cmd.color ("red", "Hstrand132")


cmd.select("Hstrand133", "resi 269-273 & chain H ")
cmd.color ("green", "Hstrand133")


cmd.select("Hstrand134", "resi 281-285 & chain H ")
cmd.color ("orange", "Hstrand134")


cmd.select("Hstrand135", "resi 291-295 & chain H ")
cmd.color ("teal", "Hstrand135")


cmd.select("Istrand136", "resi 11-28 & chain I ")
cmd.color ("yellow", "Istrand136")


cmd.select("Istrand137", "resi 34-66 & chain I ")
cmd.color ("blue", "Istrand137")


cmd.select("Istrand138", "resi 74-107 & chain I ")
cmd.color ("red", "Istrand138")


cmd.select("Istrand139", "resi 111-122 & chain I ")
cmd.color ("green", "Istrand139")


cmd.select("Istrand140", "resi 128-138 & chain I ")
cmd.color ("orange", "Istrand140")


cmd.select("Istrand141", "resi 148-156 & chain I ")
cmd.color ("teal", "Istrand141")


cmd.select("Istrand142", "resi 168-172 & chain I ")
cmd.color ("yellow", "Istrand142")


cmd.select("Istrand143", "resi 178-184 & chain I ")
cmd.color ("blue", "Istrand143")


cmd.select("Istrand144", "resi 187-193 & chain I ")
cmd.color ("red", "Istrand144")


cmd.select("Istrand145", "resi 200-204 & chain I ")
cmd.color ("green", "Istrand145")


cmd.select("Istrand146", "resi 209-213 & chain I ")
cmd.color ("orange", "Istrand146")


cmd.select("Istrand147", "resi 223-226 & chain I ")
cmd.color ("teal", "Istrand147")


cmd.select("Istrand148", "resi 232-235 & chain I ")
cmd.color ("yellow", "Istrand148")


cmd.select("Istrand149", "resi 257-259 & chain I ")
cmd.color ("blue", "Istrand149")


cmd.select("Istrand150", "resi 269-273 & chain I ")
cmd.color ("red", "Istrand150")


cmd.select("Istrand151", "resi 281-285 & chain I ")
cmd.color ("green", "Istrand151")


cmd.select("Istrand152", "resi 291-295 & chain I ")
cmd.color ("orange", "Istrand152")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
