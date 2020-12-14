from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NXR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-4 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 9-23 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 35-36 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 39-49 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 54-65 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 75-86 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 90-98 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 129-138 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 148-155 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 175-185 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 188-198 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 207-210 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 213-216 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 222-234 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 237-247 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 251-252 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 257-258 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 261-271 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 277-289 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 298-311 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 316-325 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 343-351 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Bstrand22", "resi 2-4 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 9-23 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 35-36 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 39-49 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 54-65 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 75-86 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 90-98 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 129-138 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 148-155 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 175-185 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 188-198 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 207-210 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 213-216 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 222-234 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 237-247 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 251-252 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 257-258 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 261-271 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 277-289 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 298-311 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 316-325 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 343-351 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Cstrand44", "resi 2-4 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 9-24 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 35-36 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 39-49 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 54-65 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 75-86 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 90-98 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 129-138 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 148-155 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 175-185 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 188-198 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 207-210 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 213-216 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 222-234 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 237-247 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 251-252 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("Cstrand60", "resi 257-258 & chain C ")
cmd.color ("red", "Cstrand60")


cmd.select("Cstrand61", "resi 261-271 & chain C ")
cmd.color ("green", "Cstrand61")


cmd.select("Cstrand62", "resi 277-289 & chain C ")
cmd.color ("orange", "Cstrand62")


cmd.select("Cstrand63", "resi 298-311 & chain C ")
cmd.color ("teal", "Cstrand63")


cmd.select("Cstrand64", "resi 316-325 & chain C ")
cmd.color ("yellow", "Cstrand64")


cmd.select("Cstrand65", "resi 343-351 & chain C ")
cmd.color ("blue", "Cstrand65")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
