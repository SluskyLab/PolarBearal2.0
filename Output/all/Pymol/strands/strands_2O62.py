from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2O62.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 28-41 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 46-53 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59-63 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 70-72 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 78-80 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 92-99 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 102-110 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 116-126 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 144-154 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 161-171 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 177-183 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 186-195 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 198-201 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 209-213 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 218-223 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 232-241 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 244-252 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 258-268 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Bstrand19", "resi 13-22 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 28-41 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 46-53 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 59-63 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 70-72 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 78-81 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 92-99 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 102-110 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 116-126 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 144-154 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 161-171 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 177-182 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 187-195 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 198-201 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 209-213 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 218-223 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 232-241 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 244-252 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 258-268 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
