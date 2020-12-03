from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3X2R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 50-52 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 57-58 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 94-95 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 136-146 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 150-180 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 186-208 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 214-224 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Bstrand7", "resi 50-52 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 57-58 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 94-95 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 136-146 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 150-180 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 186-208 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 214-224 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Cstrand14", "resi 50-52 & chain C ")
cmd.color ("orange", "Cstrand14")


cmd.select("Cstrand15", "resi 57-58 & chain C ")
cmd.color ("teal", "Cstrand15")


cmd.select("Cstrand16", "resi 94-95 & chain C ")
cmd.color ("yellow", "Cstrand16")


cmd.select("Cstrand17", "resi 136-146 & chain C ")
cmd.color ("blue", "Cstrand17")


cmd.select("Cstrand18", "resi 150-180 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 186-208 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 214-224 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Dstrand21", "resi 50-52 & chain D ")
cmd.color ("teal", "Dstrand21")


cmd.select("Dstrand22", "resi 57-58 & chain D ")
cmd.color ("yellow", "Dstrand22")


cmd.select("Dstrand23", "resi 94-95 & chain D ")
cmd.color ("blue", "Dstrand23")


cmd.select("Dstrand24", "resi 136-146 & chain D ")
cmd.color ("red", "Dstrand24")


cmd.select("Dstrand25", "resi 150-180 & chain D ")
cmd.color ("green", "Dstrand25")


cmd.select("Dstrand26", "resi 186-208 & chain D ")
cmd.color ("orange", "Dstrand26")


cmd.select("Dstrand27", "resi 214-224 & chain D ")
cmd.color ("teal", "Dstrand27")


cmd.select("Estrand28", "resi 50-52 & chain E ")
cmd.color ("yellow", "Estrand28")


cmd.select("Estrand29", "resi 57-58 & chain E ")
cmd.color ("blue", "Estrand29")


cmd.select("Estrand30", "resi 94-95 & chain E ")
cmd.color ("red", "Estrand30")


cmd.select("Estrand31", "resi 136-146 & chain E ")
cmd.color ("green", "Estrand31")


cmd.select("Estrand32", "resi 150-180 & chain E ")
cmd.color ("orange", "Estrand32")


cmd.select("Estrand33", "resi 186-208 & chain E ")
cmd.color ("teal", "Estrand33")


cmd.select("Estrand34", "resi 214-224 & chain E ")
cmd.color ("yellow", "Estrand34")


cmd.select("Fstrand35", "resi 50-52 & chain F ")
cmd.color ("blue", "Fstrand35")


cmd.select("Fstrand36", "resi 57-58 & chain F ")
cmd.color ("red", "Fstrand36")


cmd.select("Fstrand37", "resi 94-95 & chain F ")
cmd.color ("green", "Fstrand37")


cmd.select("Fstrand38", "resi 136-146 & chain F ")
cmd.color ("orange", "Fstrand38")


cmd.select("Fstrand39", "resi 150-180 & chain F ")
cmd.color ("teal", "Fstrand39")


cmd.select("Fstrand40", "resi 186-208 & chain F ")
cmd.color ("yellow", "Fstrand40")


cmd.select("Fstrand41", "resi 214-224 & chain F ")
cmd.color ("blue", "Fstrand41")


cmd.select("Gstrand42", "resi 50-52 & chain G ")
cmd.color ("red", "Gstrand42")


cmd.select("Gstrand43", "resi 57-58 & chain G ")
cmd.color ("green", "Gstrand43")


cmd.select("Gstrand44", "resi 94-95 & chain G ")
cmd.color ("orange", "Gstrand44")


cmd.select("Gstrand45", "resi 136-146 & chain G ")
cmd.color ("teal", "Gstrand45")


cmd.select("Gstrand46", "resi 150-180 & chain G ")
cmd.color ("yellow", "Gstrand46")


cmd.select("Gstrand47", "resi 186-208 & chain G ")
cmd.color ("blue", "Gstrand47")


cmd.select("Gstrand48", "resi 214-224 & chain G ")
cmd.color ("red", "Gstrand48")


cmd.select("Hstrand49", "resi 50-52 & chain H ")
cmd.color ("green", "Hstrand49")


cmd.select("Hstrand50", "resi 57-58 & chain H ")
cmd.color ("orange", "Hstrand50")


cmd.select("Hstrand51", "resi 94-95 & chain H ")
cmd.color ("teal", "Hstrand51")


cmd.select("Hstrand52", "resi 136-146 & chain H ")
cmd.color ("yellow", "Hstrand52")


cmd.select("Hstrand53", "resi 150-180 & chain H ")
cmd.color ("blue", "Hstrand53")


cmd.select("Hstrand54", "resi 186-208 & chain H ")
cmd.color ("red", "Hstrand54")


cmd.select("Hstrand55", "resi 214-224 & chain H ")
cmd.color ("green", "Hstrand55")


cmd.select("Istrand56", "resi 50-52 & chain I ")
cmd.color ("orange", "Istrand56")


cmd.select("Istrand57", "resi 57-58 & chain I ")
cmd.color ("teal", "Istrand57")


cmd.select("Istrand58", "resi 94-95 & chain I ")
cmd.color ("yellow", "Istrand58")


cmd.select("Istrand59", "resi 136-146 & chain I ")
cmd.color ("blue", "Istrand59")


cmd.select("Istrand60", "resi 150-180 & chain I ")
cmd.color ("red", "Istrand60")


cmd.select("Istrand61", "resi 186-207 & chain I ")
cmd.color ("green", "Istrand61")


cmd.select("Istrand62", "resi 215-224 & chain I ")
cmd.color ("orange", "Istrand62")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand* or Istrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
