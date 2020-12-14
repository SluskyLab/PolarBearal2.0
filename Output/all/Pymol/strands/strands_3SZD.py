from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14-28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 36-49 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 57-70 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 94-106 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 109-116 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 119-120 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 123-124 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 134-145 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 148-159 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 169-171 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 174-179 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 182-191 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 196-205 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 209-222 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 225-238 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 248-260 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 263-273 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 304-313 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 322-336 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 340-355 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 365-375 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 383-395 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Bstrand22", "resi 14-28 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 36-49 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 58-70 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 94-106 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 109-116 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 119-120 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 123-124 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 134-142 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 148-159 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 169-170 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 178-179 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 182-191 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 196-205 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 209-222 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 225-238 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 248-260 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 263-273 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 304-313 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 322-336 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 340-355 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 365-375 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 383-395 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
