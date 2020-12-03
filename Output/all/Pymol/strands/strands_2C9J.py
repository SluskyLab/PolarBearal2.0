from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2C9J.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-18 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 21-32 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 37-44 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 87-95 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 100-110 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 113-123 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 136-139 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 142-149 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 152-163 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 168-179 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 190-201 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 207-217 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 8-18 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 21-32 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 37-44 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 87-95 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 100-110 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 113-123 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 136-139 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 142-149 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 152-163 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 168-179 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 190-201 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 207-217 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Cstrand24", "resi 8-18 & chain C ")
cmd.color ("red", "Cstrand24")


cmd.select("Cstrand25", "resi 21-32 & chain C ")
cmd.color ("green", "Cstrand25")


cmd.select("Cstrand26", "resi 37-44 & chain C ")
cmd.color ("orange", "Cstrand26")


cmd.select("Cstrand27", "resi 87-95 & chain C ")
cmd.color ("teal", "Cstrand27")


cmd.select("Cstrand28", "resi 100-109 & chain C ")
cmd.color ("yellow", "Cstrand28")


cmd.select("Cstrand29", "resi 114-123 & chain C ")
cmd.color ("blue", "Cstrand29")


cmd.select("Cstrand30", "resi 136-139 & chain C ")
cmd.color ("red", "Cstrand30")


cmd.select("Cstrand31", "resi 142-149 & chain C ")
cmd.color ("green", "Cstrand31")


cmd.select("Cstrand32", "resi 152-163 & chain C ")
cmd.color ("orange", "Cstrand32")


cmd.select("Cstrand33", "resi 168-179 & chain C ")
cmd.color ("teal", "Cstrand33")


cmd.select("Cstrand34", "resi 190-201 & chain C ")
cmd.color ("yellow", "Cstrand34")


cmd.select("Cstrand35", "resi 207-217 & chain C ")
cmd.color ("blue", "Cstrand35")


cmd.select("Dstrand36", "resi 8-18 & chain D ")
cmd.color ("red", "Dstrand36")


cmd.select("Dstrand37", "resi 21-32 & chain D ")
cmd.color ("green", "Dstrand37")


cmd.select("Dstrand38", "resi 37-44 & chain D ")
cmd.color ("orange", "Dstrand38")


cmd.select("Dstrand39", "resi 87-95 & chain D ")
cmd.color ("teal", "Dstrand39")


cmd.select("Dstrand40", "resi 100-110 & chain D ")
cmd.color ("yellow", "Dstrand40")


cmd.select("Dstrand41", "resi 113-123 & chain D ")
cmd.color ("blue", "Dstrand41")


cmd.select("Dstrand42", "resi 136-139 & chain D ")
cmd.color ("red", "Dstrand42")


cmd.select("Dstrand43", "resi 142-149 & chain D ")
cmd.color ("green", "Dstrand43")


cmd.select("Dstrand44", "resi 152-163 & chain D ")
cmd.color ("orange", "Dstrand44")


cmd.select("Dstrand45", "resi 168-179 & chain D ")
cmd.color ("teal", "Dstrand45")


cmd.select("Dstrand46", "resi 190-201 & chain D ")
cmd.color ("yellow", "Dstrand46")


cmd.select("Dstrand47", "resi 207-217 & chain D ")
cmd.color ("blue", "Dstrand47")


cmd.select("Estrand48", "resi 8-18 & chain E ")
cmd.color ("red", "Estrand48")


cmd.select("Estrand49", "resi 21-32 & chain E ")
cmd.color ("green", "Estrand49")


cmd.select("Estrand50", "resi 37-44 & chain E ")
cmd.color ("orange", "Estrand50")


cmd.select("Estrand51", "resi 87-95 & chain E ")
cmd.color ("teal", "Estrand51")


cmd.select("Estrand52", "resi 100-110 & chain E ")
cmd.color ("yellow", "Estrand52")


cmd.select("Estrand53", "resi 113-123 & chain E ")
cmd.color ("blue", "Estrand53")


cmd.select("Estrand54", "resi 136-139 & chain E ")
cmd.color ("red", "Estrand54")


cmd.select("Estrand55", "resi 142-149 & chain E ")
cmd.color ("green", "Estrand55")


cmd.select("Estrand56", "resi 152-163 & chain E ")
cmd.color ("orange", "Estrand56")


cmd.select("Estrand57", "resi 168-179 & chain E ")
cmd.color ("teal", "Estrand57")


cmd.select("Estrand58", "resi 190-201 & chain E ")
cmd.color ("yellow", "Estrand58")


cmd.select("Estrand59", "resi 207-217 & chain E ")
cmd.color ("blue", "Estrand59")


cmd.select("Fstrand60", "resi 8-18 & chain F ")
cmd.color ("red", "Fstrand60")


cmd.select("Fstrand61", "resi 21-32 & chain F ")
cmd.color ("green", "Fstrand61")


cmd.select("Fstrand62", "resi 37-44 & chain F ")
cmd.color ("orange", "Fstrand62")


cmd.select("Fstrand63", "resi 87-95 & chain F ")
cmd.color ("teal", "Fstrand63")


cmd.select("Fstrand64", "resi 100-110 & chain F ")
cmd.color ("yellow", "Fstrand64")


cmd.select("Fstrand65", "resi 113-123 & chain F ")
cmd.color ("blue", "Fstrand65")


cmd.select("Fstrand66", "resi 136-139 & chain F ")
cmd.color ("red", "Fstrand66")


cmd.select("Fstrand67", "resi 142-149 & chain F ")
cmd.color ("green", "Fstrand67")


cmd.select("Fstrand68", "resi 152-163 & chain F ")
cmd.color ("orange", "Fstrand68")


cmd.select("Fstrand69", "resi 168-179 & chain F ")
cmd.color ("teal", "Fstrand69")


cmd.select("Fstrand70", "resi 190-201 & chain F ")
cmd.color ("yellow", "Fstrand70")


cmd.select("Fstrand71", "resi 207-217 & chain F ")
cmd.color ("blue", "Fstrand71")


cmd.select("Gstrand72", "resi 8-18 & chain G ")
cmd.color ("red", "Gstrand72")


cmd.select("Gstrand73", "resi 21-32 & chain G ")
cmd.color ("green", "Gstrand73")


cmd.select("Gstrand74", "resi 37-44 & chain G ")
cmd.color ("orange", "Gstrand74")


cmd.select("Gstrand75", "resi 87-95 & chain G ")
cmd.color ("teal", "Gstrand75")


cmd.select("Gstrand76", "resi 100-110 & chain G ")
cmd.color ("yellow", "Gstrand76")


cmd.select("Gstrand77", "resi 113-123 & chain G ")
cmd.color ("blue", "Gstrand77")


cmd.select("Gstrand78", "resi 136-139 & chain G ")
cmd.color ("red", "Gstrand78")


cmd.select("Gstrand79", "resi 142-149 & chain G ")
cmd.color ("green", "Gstrand79")


cmd.select("Gstrand80", "resi 152-163 & chain G ")
cmd.color ("orange", "Gstrand80")


cmd.select("Gstrand81", "resi 168-179 & chain G ")
cmd.color ("teal", "Gstrand81")


cmd.select("Gstrand82", "resi 190-201 & chain G ")
cmd.color ("yellow", "Gstrand82")


cmd.select("Gstrand83", "resi 207-217 & chain G ")
cmd.color ("blue", "Gstrand83")


cmd.select("Hstrand84", "resi 8-18 & chain H ")
cmd.color ("red", "Hstrand84")


cmd.select("Hstrand85", "resi 21-32 & chain H ")
cmd.color ("green", "Hstrand85")


cmd.select("Hstrand86", "resi 37-44 & chain H ")
cmd.color ("orange", "Hstrand86")


cmd.select("Hstrand87", "resi 87-95 & chain H ")
cmd.color ("teal", "Hstrand87")


cmd.select("Hstrand88", "resi 100-109 & chain H ")
cmd.color ("yellow", "Hstrand88")


cmd.select("Hstrand89", "resi 114-123 & chain H ")
cmd.color ("blue", "Hstrand89")


cmd.select("Hstrand90", "resi 136-139 & chain H ")
cmd.color ("red", "Hstrand90")


cmd.select("Hstrand91", "resi 142-149 & chain H ")
cmd.color ("green", "Hstrand91")


cmd.select("Hstrand92", "resi 152-163 & chain H ")
cmd.color ("orange", "Hstrand92")


cmd.select("Hstrand93", "resi 168-179 & chain H ")
cmd.color ("teal", "Hstrand93")


cmd.select("Hstrand94", "resi 190-201 & chain H ")
cmd.color ("yellow", "Hstrand94")


cmd.select("Hstrand95", "resi 207-217 & chain H ")
cmd.color ("blue", "Hstrand95")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand* or Estrand* or Fstrand* or Gstrand* or Hstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
