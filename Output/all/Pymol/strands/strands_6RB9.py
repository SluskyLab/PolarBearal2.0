from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6RB9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 57-60 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 68-71 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 87-93 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 97-132 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 136-171 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 176-188 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 192-198 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 202-204 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 236-242 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 247-257 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Bstrand10", "resi 57-60 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 68-71 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 87-93 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 97-132 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 136-171 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 176-188 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 192-198 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 202-204 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 236-242 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 247-257 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Cstrand20", "resi 57-60 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 68-71 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 87-93 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 97-132 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Cstrand24", "resi 136-171 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 176-188 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 192-198 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 202-204 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 236-242 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 247-257 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Dstrand30", "resi 57-60 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 68-71 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("Dstrand32", "resi 87-93 & chain D ")
cmd.color ("orange", "Dstrand32")


cmd.select("Dstrand33", "resi 97-132 & chain D ")
cmd.color ("teal", "Dstrand33")


cmd.select("Dstrand34", "resi 136-171 & chain D ")
cmd.color ("yellow", "Dstrand34")


cmd.select("Dstrand35", "resi 176-188 & chain D ")
cmd.color ("blue", "Dstrand35")


cmd.select("Dstrand36", "resi 192-198 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 202-204 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 236-242 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 247-257 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Estrand40", "resi 57-60 & chain E ")
cmd.color ("yellow", "Estrand40")


cmd.select("Estrand41", "resi 68-71 & chain E ")
cmd.color ("blue", "Estrand41")


cmd.select("Estrand42", "resi 87-93 & chain E ")
cmd.color ("red", "Estrand42")


cmd.select("Estrand43", "resi 97-132 & chain E ")
cmd.color ("green", "Estrand43")


cmd.select("Estrand44", "resi 136-171 & chain E ")
cmd.color ("orange", "Estrand44")


cmd.select("Estrand45", "resi 176-188 & chain E ")
cmd.color ("teal", "Estrand45")


cmd.select("Estrand46", "resi 192-198 & chain E ")
cmd.color ("yellow", "Estrand46")


cmd.select("Estrand47", "resi 202-204 & chain E ")
cmd.color ("blue", "Estrand47")


cmd.select("Estrand48", "resi 236-242 & chain E ")
cmd.color ("red", "Estrand48")


cmd.select("Estrand49", "resi 247-257 & chain E ")
cmd.color ("green", "Estrand49")


cmd.select("Fstrand50", "resi 57-60 & chain F ")
cmd.color ("orange", "Fstrand50")


cmd.select("Fstrand51", "resi 68-71 & chain F ")
cmd.color ("teal", "Fstrand51")


cmd.select("Fstrand52", "resi 87-93 & chain F ")
cmd.color ("yellow", "Fstrand52")


cmd.select("Fstrand53", "resi 97-132 & chain F ")
cmd.color ("blue", "Fstrand53")


cmd.select("Fstrand54", "resi 136-171 & chain F ")
cmd.color ("red", "Fstrand54")


cmd.select("Fstrand55", "resi 176-188 & chain F ")
cmd.color ("green", "Fstrand55")


cmd.select("Fstrand56", "resi 192-198 & chain F ")
cmd.color ("orange", "Fstrand56")


cmd.select("Fstrand57", "resi 202-204 & chain F ")
cmd.color ("teal", "Fstrand57")


cmd.select("Fstrand58", "resi 236-242 & chain F ")
cmd.color ("yellow", "Fstrand58")


cmd.select("Fstrand59", "resi 247-257 & chain F ")
cmd.color ("blue", "Fstrand59")


cmd.select("Gstrand60", "resi 57-60 & chain G ")
cmd.color ("red", "Gstrand60")


cmd.select("Gstrand61", "resi 68-71 & chain G ")
cmd.color ("green", "Gstrand61")


cmd.select("Gstrand62", "resi 87-93 & chain G ")
cmd.color ("orange", "Gstrand62")


cmd.select("Gstrand63", "resi 97-132 & chain G ")
cmd.color ("teal", "Gstrand63")


cmd.select("Gstrand64", "resi 136-171 & chain G ")
cmd.color ("yellow", "Gstrand64")


cmd.select("Gstrand65", "resi 176-188 & chain G ")
cmd.color ("blue", "Gstrand65")


cmd.select("Gstrand66", "resi 192-198 & chain G ")
cmd.color ("red", "Gstrand66")


cmd.select("Gstrand67", "resi 202-204 & chain G ")
cmd.color ("green", "Gstrand67")


cmd.select("Gstrand68", "resi 236-242 & chain G ")
cmd.color ("orange", "Gstrand68")


cmd.select("Gstrand69", "resi 247-257 & chain G ")
cmd.color ("teal", "Gstrand69")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
