from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10-24 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 32-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48-54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 57-72 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 86-87 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 92-93 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 96-108 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 111-118 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 136-145 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 150-161 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 172-175 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 178-181 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 185-193 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 198-207 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 211-223 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 228-240 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 248-260 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 263-273 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 304-313 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 321-334 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 340-353 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 362-373 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 379-391 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Bstrand23", "resi 10-24 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 32-44 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 48-54 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 57-72 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 86-87 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 92-93 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 96-108 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 111-118 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 136-145 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 150-161 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 172-175 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 178-181 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 185-195 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 198-207 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 211-223 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 228-240 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 248-260 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 263-273 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 304-313 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 321-334 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 340-353 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 362-373 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 379-391 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
