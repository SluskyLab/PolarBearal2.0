from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3NSG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13-24 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 32-33 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 36-45 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 52-62 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 74-85 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 89-97 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 130-139 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 149-156 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 172-181 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 184-193 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 209-220 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 223-232 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 238-239 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 246-247 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 251-261 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 269-279 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 288-300 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 306-315 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 332-340 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Bstrand19", "resi 11-23 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 31-33 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 36-46 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 51-62 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 74-85 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 89-97 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 130-131 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 135-139 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 150-156 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 172-181 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 184-193 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 209-218 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 223-230 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 237-238 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 247-248 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 254-261 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 267-278 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 288-289 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 293-301 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 306-315 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 332-340 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Cstrand40", "resi 11-24 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 31-33 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 36-46 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 51-62 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 74-85 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 89-96 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 131-139 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 149-156 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 172-181 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 184-194 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 208-220 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 223-232 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 237-239 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 246-248 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 252-261 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 267-278 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 288-300 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 306-315 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 332-340 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
