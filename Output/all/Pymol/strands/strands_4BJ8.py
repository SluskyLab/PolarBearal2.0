from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4BJ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 19-25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 28-34 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 49-56 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 63-69 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 75-84 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 90-99 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 112-121 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 10-14 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 19-24 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 28-34 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 49-56 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 63-69 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 75-84 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 90-99 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 112-121 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Cstrand16", "resi 10-14 & chain C ")
cmd.color ("yellow", "Cstrand16")


cmd.select("Cstrand17", "resi 19-25 & chain C ")
cmd.color ("blue", "Cstrand17")


cmd.select("Cstrand18", "resi 28-34 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 49-56 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 63-69 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 75-84 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 90-99 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 112-121 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Dstrand24", "resi 10-14 & chain D ")
cmd.color ("red", "Dstrand24")


cmd.select("Dstrand25", "resi 19-25 & chain D ")
cmd.color ("green", "Dstrand25")


cmd.select("Dstrand26", "resi 28-34 & chain D ")
cmd.color ("orange", "Dstrand26")


cmd.select("Dstrand27", "resi 49-56 & chain D ")
cmd.color ("teal", "Dstrand27")


cmd.select("Dstrand28", "resi 63-69 & chain D ")
cmd.color ("yellow", "Dstrand28")


cmd.select("Dstrand29", "resi 75-84 & chain D ")
cmd.color ("blue", "Dstrand29")


cmd.select("Dstrand30", "resi 90-99 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 112-121 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("Estrand32", "resi 10-14 & chain E ")
cmd.color ("orange", "Estrand32")


cmd.select("Estrand33", "resi 19-25 & chain E ")
cmd.color ("teal", "Estrand33")


cmd.select("Estrand34", "resi 28-34 & chain E ")
cmd.color ("yellow", "Estrand34")


cmd.select("Estrand35", "resi 49-56 & chain E ")
cmd.color ("blue", "Estrand35")


cmd.select("Estrand36", "resi 63-69 & chain E ")
cmd.color ("red", "Estrand36")


cmd.select("Estrand37", "resi 75-84 & chain E ")
cmd.color ("green", "Estrand37")


cmd.select("Estrand38", "resi 90-99 & chain E ")
cmd.color ("orange", "Estrand38")


cmd.select("Estrand39", "resi 112-121 & chain E ")
cmd.color ("teal", "Estrand39")


cmd.select("Fstrand40", "resi 10-14 & chain F ")
cmd.color ("yellow", "Fstrand40")


cmd.select("Fstrand41", "resi 19-25 & chain F ")
cmd.color ("blue", "Fstrand41")


cmd.select("Fstrand42", "resi 28-34 & chain F ")
cmd.color ("red", "Fstrand42")


cmd.select("Fstrand43", "resi 49-56 & chain F ")
cmd.color ("green", "Fstrand43")


cmd.select("Fstrand44", "resi 63-69 & chain F ")
cmd.color ("orange", "Fstrand44")


cmd.select("Fstrand45", "resi 75-84 & chain F ")
cmd.color ("teal", "Fstrand45")


cmd.select("Fstrand46", "resi 90-99 & chain F ")
cmd.color ("yellow", "Fstrand46")


cmd.select("Fstrand47", "resi 112-121 & chain F ")
cmd.color ("blue", "Fstrand47")


cmd.select("Gstrand48", "resi 10-14 & chain G ")
cmd.color ("red", "Gstrand48")


cmd.select("Gstrand49", "resi 19-25 & chain G ")
cmd.color ("green", "Gstrand49")


cmd.select("Gstrand50", "resi 28-34 & chain G ")
cmd.color ("orange", "Gstrand50")


cmd.select("Gstrand51", "resi 49-56 & chain G ")
cmd.color ("teal", "Gstrand51")


cmd.select("Gstrand52", "resi 63-69 & chain G ")
cmd.color ("yellow", "Gstrand52")


cmd.select("Gstrand53", "resi 75-84 & chain G ")
cmd.color ("blue", "Gstrand53")


cmd.select("Gstrand54", "resi 90-99 & chain G ")
cmd.color ("red", "Gstrand54")


cmd.select("Gstrand55", "resi 112-121 & chain G ")
cmd.color ("green", "Gstrand55")


cmd.select("Hstrand56", "resi 10-14 & chain H ")
cmd.color ("orange", "Hstrand56")


cmd.select("Hstrand57", "resi 19-25 & chain H ")
cmd.color ("teal", "Hstrand57")


cmd.select("Hstrand58", "resi 28-34 & chain H ")
cmd.color ("yellow", "Hstrand58")


cmd.select("Hstrand59", "resi 49-56 & chain H ")
cmd.color ("blue", "Hstrand59")


cmd.select("Hstrand60", "resi 63-69 & chain H ")
cmd.color ("red", "Hstrand60")


cmd.select("Hstrand61", "resi 75-84 & chain H ")
cmd.color ("green", "Hstrand61")


cmd.select("Hstrand62", "resi 90-99 & chain H ")
cmd.color ("orange", "Hstrand62")


cmd.select("Hstrand63", "resi 112-121 & chain H ")
cmd.color ("teal", "Hstrand63")


cmd.select("Istrand64", "resi 10-14 & chain I ")
cmd.color ("yellow", "Istrand64")


cmd.select("Istrand65", "resi 19-25 & chain I ")
cmd.color ("blue", "Istrand65")


cmd.select("Istrand66", "resi 28-34 & chain I ")
cmd.color ("red", "Istrand66")


cmd.select("Istrand67", "resi 49-56 & chain I ")
cmd.color ("green", "Istrand67")


cmd.select("Istrand68", "resi 63-69 & chain I ")
cmd.color ("orange", "Istrand68")


cmd.select("Istrand69", "resi 75-84 & chain I ")
cmd.color ("teal", "Istrand69")


cmd.select("Istrand70", "resi 90-99 & chain I ")
cmd.color ("yellow", "Istrand70")


cmd.select("Istrand71", "resi 112-121 & chain I ")
cmd.color ("blue", "Istrand71")


cmd.select("Jstrand72", "resi 10-14 & chain J ")
cmd.color ("red", "Jstrand72")


cmd.select("Jstrand73", "resi 19-25 & chain J ")
cmd.color ("green", "Jstrand73")


cmd.select("Jstrand74", "resi 28-34 & chain J ")
cmd.color ("orange", "Jstrand74")


cmd.select("Jstrand75", "resi 49-56 & chain J ")
cmd.color ("teal", "Jstrand75")


cmd.select("Jstrand76", "resi 63-69 & chain J ")
cmd.color ("yellow", "Jstrand76")


cmd.select("Jstrand77", "resi 75-84 & chain J ")
cmd.color ("blue", "Jstrand77")


cmd.select("Jstrand78", "resi 90-99 & chain J ")
cmd.color ("red", "Jstrand78")


cmd.select("Jstrand79", "resi 112-121 & chain J ")
cmd.color ("green", "Jstrand79")


cmd.select("Kstrand80", "resi 10-14 & chain K ")
cmd.color ("orange", "Kstrand80")


cmd.select("Kstrand81", "resi 19-25 & chain K ")
cmd.color ("teal", "Kstrand81")


cmd.select("Kstrand82", "resi 28-34 & chain K ")
cmd.color ("yellow", "Kstrand82")


cmd.select("Kstrand83", "resi 49-56 & chain K ")
cmd.color ("blue", "Kstrand83")


cmd.select("Kstrand84", "resi 63-69 & chain K ")
cmd.color ("red", "Kstrand84")


cmd.select("Kstrand85", "resi 75-84 & chain K ")
cmd.color ("green", "Kstrand85")


cmd.select("Kstrand86", "resi 90-99 & chain K ")
cmd.color ("orange", "Kstrand86")


cmd.select("Kstrand87", "resi 112-121 & chain K ")
cmd.color ("teal", "Kstrand87")


cmd.select("Lstrand88", "resi 10-14 & chain L ")
cmd.color ("yellow", "Lstrand88")


cmd.select("Lstrand89", "resi 19-25 & chain L ")
cmd.color ("blue", "Lstrand89")


cmd.select("Lstrand90", "resi 28-34 & chain L ")
cmd.color ("red", "Lstrand90")


cmd.select("Lstrand91", "resi 49-56 & chain L ")
cmd.color ("green", "Lstrand91")


cmd.select("Lstrand92", "resi 63-69 & chain L ")
cmd.color ("orange", "Lstrand92")


cmd.select("Lstrand93", "resi 75-84 & chain L ")
cmd.color ("teal", "Lstrand93")


cmd.select("Lstrand94", "resi 90-99 & chain L ")
cmd.color ("yellow", "Lstrand94")


cmd.select("Lstrand95", "resi 112-121 & chain L ")
cmd.color ("blue", "Lstrand95")


cmd.select("Mstrand96", "resi 10-14 & chain M ")
cmd.color ("red", "Mstrand96")


cmd.select("Mstrand97", "resi 19-24 & chain M ")
cmd.color ("green", "Mstrand97")


cmd.select("Mstrand98", "resi 28-34 & chain M ")
cmd.color ("orange", "Mstrand98")


cmd.select("Mstrand99", "resi 49-56 & chain M ")
cmd.color ("teal", "Mstrand99")


cmd.select("Mstrand100", "resi 63-69 & chain M ")
cmd.color ("yellow", "Mstrand100")


cmd.select("Mstrand101", "resi 75-84 & chain M ")
cmd.color ("blue", "Mstrand101")


cmd.select("Mstrand102", "resi 90-99 & chain M ")
cmd.color ("red", "Mstrand102")


cmd.select("Mstrand103", "resi 112-121 & chain M ")
cmd.color ("green", "Mstrand103")


cmd.select("Nstrand104", "resi 10-14 & chain N ")
cmd.color ("orange", "Nstrand104")


cmd.select("Nstrand105", "resi 19-24 & chain N ")
cmd.color ("teal", "Nstrand105")


cmd.select("Nstrand106", "resi 28-34 & chain N ")
cmd.color ("yellow", "Nstrand106")


cmd.select("Nstrand107", "resi 49-56 & chain N ")
cmd.color ("blue", "Nstrand107")


cmd.select("Nstrand108", "resi 63-69 & chain N ")
cmd.color ("red", "Nstrand108")


cmd.select("Nstrand109", "resi 75-84 & chain N ")
cmd.color ("green", "Nstrand109")


cmd.select("Nstrand110", "resi 90-99 & chain N ")
cmd.color ("orange", "Nstrand110")


cmd.select("Nstrand111", "resi 112-121 & chain N ")
cmd.color ("teal", "Nstrand111")


cmd.select("Ostrand112", "resi 10-14 & chain O ")
cmd.color ("yellow", "Ostrand112")


cmd.select("Ostrand113", "resi 19-25 & chain O ")
cmd.color ("blue", "Ostrand113")


cmd.select("Ostrand114", "resi 28-34 & chain O ")
cmd.color ("red", "Ostrand114")


cmd.select("Ostrand115", "resi 49-56 & chain O ")
cmd.color ("green", "Ostrand115")


cmd.select("Ostrand116", "resi 63-69 & chain O ")
cmd.color ("orange", "Ostrand116")


cmd.select("Ostrand117", "resi 75-84 & chain O ")
cmd.color ("teal", "Ostrand117")


cmd.select("Ostrand118", "resi 90-99 & chain O ")
cmd.color ("yellow", "Ostrand118")


cmd.select("Ostrand119", "resi 112-121 & chain O ")
cmd.color ("blue", "Ostrand119")


cmd.select("Pstrand120", "resi 10-14 & chain P ")
cmd.color ("red", "Pstrand120")


cmd.select("Pstrand121", "resi 19-25 & chain P ")
cmd.color ("green", "Pstrand121")


cmd.select("Pstrand122", "resi 28-34 & chain P ")
cmd.color ("orange", "Pstrand122")


cmd.select("Pstrand123", "resi 49-56 & chain P ")
cmd.color ("teal", "Pstrand123")


cmd.select("Pstrand124", "resi 63-69 & chain P ")
cmd.color ("yellow", "Pstrand124")


cmd.select("Pstrand125", "resi 75-84 & chain P ")
cmd.color ("blue", "Pstrand125")


cmd.select("Pstrand126", "resi 90-99 & chain P ")
cmd.color ("red", "Pstrand126")


cmd.select("Pstrand127", "resi 112-121 & chain P ")
cmd.color ("green", "Pstrand127")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand* or Jstrand* or Kstrand* or Lstrand* or Mstrand* or Nstrand* or Ostrand* or Pstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
