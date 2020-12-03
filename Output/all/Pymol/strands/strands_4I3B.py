from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4I3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40-46 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 50-56 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 64-70 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 75-77 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 86-93 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 96-103 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 106-115 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 118-125 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 128-135 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Bstrand10", "resi 7-15 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 40-46 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 50-56 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 64-70 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 75-77 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 86-93 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 96-103 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 106-115 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 118-125 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 128-136 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Cstrand20", "resi 7-15 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 40-46 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 50-56 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 64-70 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 75-77 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 86-93 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 96-103 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 106-115 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 118-125 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 128-136 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Dstrand30", "resi 7-15 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 40-46 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("Dstrand32", "resi 50-56 & chain D ")
cmd.color ("orange", "Dstrand32")


cmd.select("Dstrand33", "resi 64-70 & chain D ")
cmd.color ("teal", "Dstrand33")


cmd.select("Dstrand34", "resi 75-77 & chain D ")
cmd.color ("yellow", "Dstrand34")


cmd.select("Dstrand35", "resi 86-93 & chain D ")
cmd.color ("blue", "Dstrand35")


cmd.select("Dstrand36", "resi 96-103 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 106-115 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 118-125 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 128-136 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Estrand40", "resi 7-15 & chain E ")
cmd.color ("yellow", "Estrand40")


cmd.select("Estrand41", "resi 40-46 & chain E ")
cmd.color ("blue", "Estrand41")


cmd.select("Estrand42", "resi 50-56 & chain E ")
cmd.color ("red", "Estrand42")


cmd.select("Estrand43", "resi 64-70 & chain E ")
cmd.color ("green", "Estrand43")


cmd.select("Estrand44", "resi 75-77 & chain E ")
cmd.color ("orange", "Estrand44")


cmd.select("Estrand45", "resi 86-93 & chain E ")
cmd.color ("teal", "Estrand45")


cmd.select("Estrand46", "resi 96-103 & chain E ")
cmd.color ("yellow", "Estrand46")


cmd.select("Estrand47", "resi 106-115 & chain E ")
cmd.color ("blue", "Estrand47")


cmd.select("Estrand48", "resi 118-125 & chain E ")
cmd.color ("red", "Estrand48")


cmd.select("Estrand49", "resi 128-136 & chain E ")
cmd.color ("green", "Estrand49")


cmd.select("Fstrand50", "resi 7-15 & chain F ")
cmd.color ("orange", "Fstrand50")


cmd.select("Fstrand51", "resi 40-46 & chain F ")
cmd.color ("teal", "Fstrand51")


cmd.select("Fstrand52", "resi 50-56 & chain F ")
cmd.color ("yellow", "Fstrand52")


cmd.select("Fstrand53", "resi 64-70 & chain F ")
cmd.color ("blue", "Fstrand53")


cmd.select("Fstrand54", "resi 75-77 & chain F ")
cmd.color ("red", "Fstrand54")


cmd.select("Fstrand55", "resi 86-93 & chain F ")
cmd.color ("green", "Fstrand55")


cmd.select("Fstrand56", "resi 96-103 & chain F ")
cmd.color ("orange", "Fstrand56")


cmd.select("Fstrand57", "resi 106-115 & chain F ")
cmd.color ("teal", "Fstrand57")


cmd.select("Fstrand58", "resi 118-125 & chain F ")
cmd.color ("yellow", "Fstrand58")


cmd.select("Fstrand59", "resi 128-136 & chain F ")
cmd.color ("blue", "Fstrand59")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
