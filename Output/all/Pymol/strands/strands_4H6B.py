from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H6B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-19 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 50-53 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 56-59 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 65-79 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 84-94 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 100-108 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 113-120 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 128-137 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 141-149 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Bstrand9", "resi 12-19 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 50-53 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 56-59 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 65-79 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 84-94 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 100-108 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 113-120 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 128-137 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 141-149 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Cstrand18", "resi 12-19 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 50-53 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 56-59 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 65-79 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 84-94 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 100-108 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 113-120 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 128-137 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 141-149 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Dstrand27", "resi 12-19 & chain D ")
cmd.color ("teal", "Dstrand27")


cmd.select("Dstrand28", "resi 50-53 & chain D ")
cmd.color ("yellow", "Dstrand28")


cmd.select("Dstrand29", "resi 56-59 & chain D ")
cmd.color ("blue", "Dstrand29")


cmd.select("Dstrand30", "resi 65-79 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 84-94 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("Dstrand32", "resi 100-108 & chain D ")
cmd.color ("orange", "Dstrand32")


cmd.select("Dstrand33", "resi 113-120 & chain D ")
cmd.color ("teal", "Dstrand33")


cmd.select("Dstrand34", "resi 128-137 & chain D ")
cmd.color ("yellow", "Dstrand34")


cmd.select("Dstrand35", "resi 141-149 & chain D ")
cmd.color ("blue", "Dstrand35")


cmd.select("Estrand36", "resi 12-19 & chain E ")
cmd.color ("red", "Estrand36")


cmd.select("Estrand37", "resi 50-53 & chain E ")
cmd.color ("green", "Estrand37")


cmd.select("Estrand38", "resi 56-59 & chain E ")
cmd.color ("orange", "Estrand38")


cmd.select("Estrand39", "resi 65-79 & chain E ")
cmd.color ("teal", "Estrand39")


cmd.select("Estrand40", "resi 84-94 & chain E ")
cmd.color ("yellow", "Estrand40")


cmd.select("Estrand41", "resi 100-108 & chain E ")
cmd.color ("blue", "Estrand41")


cmd.select("Estrand42", "resi 113-120 & chain E ")
cmd.color ("red", "Estrand42")


cmd.select("Estrand43", "resi 128-137 & chain E ")
cmd.color ("green", "Estrand43")


cmd.select("Estrand44", "resi 141-149 & chain E ")
cmd.color ("orange", "Estrand44")


cmd.select("Fstrand45", "resi 12-19 & chain F ")
cmd.color ("teal", "Fstrand45")


cmd.select("Fstrand46", "resi 50-53 & chain F ")
cmd.color ("yellow", "Fstrand46")


cmd.select("Fstrand47", "resi 56-59 & chain F ")
cmd.color ("blue", "Fstrand47")


cmd.select("Fstrand48", "resi 65-79 & chain F ")
cmd.color ("red", "Fstrand48")


cmd.select("Fstrand49", "resi 84-94 & chain F ")
cmd.color ("green", "Fstrand49")


cmd.select("Fstrand50", "resi 100-108 & chain F ")
cmd.color ("orange", "Fstrand50")


cmd.select("Fstrand51", "resi 113-120 & chain F ")
cmd.color ("teal", "Fstrand51")


cmd.select("Fstrand52", "resi 128-137 & chain F ")
cmd.color ("yellow", "Fstrand52")


cmd.select("Fstrand53", "resi 141-149 & chain F ")
cmd.color ("blue", "Fstrand53")


cmd.select("Gstrand54", "resi 12-19 & chain G ")
cmd.color ("red", "Gstrand54")


cmd.select("Gstrand55", "resi 50-53 & chain G ")
cmd.color ("green", "Gstrand55")


cmd.select("Gstrand56", "resi 56-59 & chain G ")
cmd.color ("orange", "Gstrand56")


cmd.select("Gstrand57", "resi 65-79 & chain G ")
cmd.color ("teal", "Gstrand57")


cmd.select("Gstrand58", "resi 84-94 & chain G ")
cmd.color ("yellow", "Gstrand58")


cmd.select("Gstrand59", "resi 100-108 & chain G ")
cmd.color ("blue", "Gstrand59")


cmd.select("Gstrand60", "resi 113-120 & chain G ")
cmd.color ("red", "Gstrand60")


cmd.select("Gstrand61", "resi 128-137 & chain G ")
cmd.color ("green", "Gstrand61")


cmd.select("Gstrand62", "resi 141-149 & chain G ")
cmd.color ("orange", "Gstrand62")


cmd.select("Hstrand63", "resi 12-19 & chain H ")
cmd.color ("teal", "Hstrand63")


cmd.select("Hstrand64", "resi 50-53 & chain H ")
cmd.color ("yellow", "Hstrand64")


cmd.select("Hstrand65", "resi 56-59 & chain H ")
cmd.color ("blue", "Hstrand65")


cmd.select("Hstrand66", "resi 65-79 & chain H ")
cmd.color ("red", "Hstrand66")


cmd.select("Hstrand67", "resi 84-94 & chain H ")
cmd.color ("green", "Hstrand67")


cmd.select("Hstrand68", "resi 100-108 & chain H ")
cmd.color ("orange", "Hstrand68")


cmd.select("Hstrand69", "resi 113-120 & chain H ")
cmd.color ("teal", "Hstrand69")


cmd.select("Hstrand70", "resi 128-137 & chain H ")
cmd.color ("yellow", "Hstrand70")


cmd.select("Hstrand71", "resi 141-149 & chain H ")
cmd.color ("blue", "Hstrand71")


cmd.select("Istrand72", "resi 12-19 & chain I ")
cmd.color ("red", "Istrand72")


cmd.select("Istrand73", "resi 50-53 & chain I ")
cmd.color ("green", "Istrand73")


cmd.select("Istrand74", "resi 56-59 & chain I ")
cmd.color ("orange", "Istrand74")


cmd.select("Istrand75", "resi 65-79 & chain I ")
cmd.color ("teal", "Istrand75")


cmd.select("Istrand76", "resi 84-94 & chain I ")
cmd.color ("yellow", "Istrand76")


cmd.select("Istrand77", "resi 100-108 & chain I ")
cmd.color ("blue", "Istrand77")


cmd.select("Istrand78", "resi 113-120 & chain I ")
cmd.color ("red", "Istrand78")


cmd.select("Istrand79", "resi 128-137 & chain I ")
cmd.color ("green", "Istrand79")


cmd.select("Istrand80", "resi 141-149 & chain I ")
cmd.color ("orange", "Istrand80")


cmd.select("Jstrand81", "resi 12-19 & chain J ")
cmd.color ("teal", "Jstrand81")


cmd.select("Jstrand82", "resi 50-53 & chain J ")
cmd.color ("yellow", "Jstrand82")


cmd.select("Jstrand83", "resi 56-59 & chain J ")
cmd.color ("blue", "Jstrand83")


cmd.select("Jstrand84", "resi 65-79 & chain J ")
cmd.color ("red", "Jstrand84")


cmd.select("Jstrand85", "resi 84-94 & chain J ")
cmd.color ("green", "Jstrand85")


cmd.select("Jstrand86", "resi 100-108 & chain J ")
cmd.color ("orange", "Jstrand86")


cmd.select("Jstrand87", "resi 113-120 & chain J ")
cmd.color ("teal", "Jstrand87")


cmd.select("Jstrand88", "resi 128-137 & chain J ")
cmd.color ("yellow", "Jstrand88")


cmd.select("Jstrand89", "resi 141-149 & chain J ")
cmd.color ("blue", "Jstrand89")


cmd.select("Kstrand90", "resi 12-19 & chain K ")
cmd.color ("red", "Kstrand90")


cmd.select("Kstrand91", "resi 50-53 & chain K ")
cmd.color ("green", "Kstrand91")


cmd.select("Kstrand92", "resi 56-59 & chain K ")
cmd.color ("orange", "Kstrand92")


cmd.select("Kstrand93", "resi 65-79 & chain K ")
cmd.color ("teal", "Kstrand93")


cmd.select("Kstrand94", "resi 84-94 & chain K ")
cmd.color ("yellow", "Kstrand94")


cmd.select("Kstrand95", "resi 100-108 & chain K ")
cmd.color ("blue", "Kstrand95")


cmd.select("Kstrand96", "resi 113-120 & chain K ")
cmd.color ("red", "Kstrand96")


cmd.select("Kstrand97", "resi 128-137 & chain K ")
cmd.color ("green", "Kstrand97")


cmd.select("Kstrand98", "resi 141-149 & chain K ")
cmd.color ("orange", "Kstrand98")


cmd.select("Lstrand99", "resi 12-19 & chain L ")
cmd.color ("teal", "Lstrand99")


cmd.select("Lstrand100", "resi 50-53 & chain L ")
cmd.color ("yellow", "Lstrand100")


cmd.select("Lstrand101", "resi 56-59 & chain L ")
cmd.color ("blue", "Lstrand101")


cmd.select("Lstrand102", "resi 65-79 & chain L ")
cmd.color ("red", "Lstrand102")


cmd.select("Lstrand103", "resi 84-94 & chain L ")
cmd.color ("green", "Lstrand103")


cmd.select("Lstrand104", "resi 100-108 & chain L ")
cmd.color ("orange", "Lstrand104")


cmd.select("Lstrand105", "resi 113-120 & chain L ")
cmd.color ("teal", "Lstrand105")


cmd.select("Lstrand106", "resi 128-137 & chain L ")
cmd.color ("yellow", "Lstrand106")


cmd.select("Lstrand107", "resi 141-149 & chain L ")
cmd.color ("blue", "Lstrand107")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
