from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-16 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 20-35 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 38-41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 44-56 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 59-69 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 83-94 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 97-103 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 138-145 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 148-155 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 159-162 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 176-179 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 184-192 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 198-207 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 210-220 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 224-236 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 239-252 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 255-266 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 269-284 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 287-296 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 311-319 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Bstrand20", "resi 12-17 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 20-35 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 38-41 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 44-56 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 59-69 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 83-94 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 97-103 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 138-145 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 148-155 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 159-162 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 176-179 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 184-192 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 198-207 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 210-221 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 224-236 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 239-252 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 255-266 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 269-284 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 287-296 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 311-319 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Cstrand40", "resi 12-17 & chain C ")
cmd.color ("yellow", "Cstrand40")


cmd.select("Cstrand41", "resi 20-35 & chain C ")
cmd.color ("blue", "Cstrand41")


cmd.select("Cstrand42", "resi 38-41 & chain C ")
cmd.color ("red", "Cstrand42")


cmd.select("Cstrand43", "resi 44-56 & chain C ")
cmd.color ("green", "Cstrand43")


cmd.select("Cstrand44", "resi 59-69 & chain C ")
cmd.color ("orange", "Cstrand44")


cmd.select("Cstrand45", "resi 83-94 & chain C ")
cmd.color ("teal", "Cstrand45")


cmd.select("Cstrand46", "resi 97-103 & chain C ")
cmd.color ("yellow", "Cstrand46")


cmd.select("Cstrand47", "resi 138-145 & chain C ")
cmd.color ("blue", "Cstrand47")


cmd.select("Cstrand48", "resi 148-155 & chain C ")
cmd.color ("red", "Cstrand48")


cmd.select("Cstrand49", "resi 159-162 & chain C ")
cmd.color ("green", "Cstrand49")


cmd.select("Cstrand50", "resi 176-179 & chain C ")
cmd.color ("orange", "Cstrand50")


cmd.select("Cstrand51", "resi 184-192 & chain C ")
cmd.color ("teal", "Cstrand51")


cmd.select("Cstrand52", "resi 198-207 & chain C ")
cmd.color ("yellow", "Cstrand52")


cmd.select("Cstrand53", "resi 210-221 & chain C ")
cmd.color ("blue", "Cstrand53")


cmd.select("Cstrand54", "resi 224-236 & chain C ")
cmd.color ("red", "Cstrand54")


cmd.select("Cstrand55", "resi 239-252 & chain C ")
cmd.color ("green", "Cstrand55")


cmd.select("Cstrand56", "resi 255-266 & chain C ")
cmd.color ("orange", "Cstrand56")


cmd.select("Cstrand57", "resi 269-284 & chain C ")
cmd.color ("teal", "Cstrand57")


cmd.select("Cstrand58", "resi 287-296 & chain C ")
cmd.color ("yellow", "Cstrand58")


cmd.select("Cstrand59", "resi 311-319 & chain C ")
cmd.color ("blue", "Cstrand59")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
