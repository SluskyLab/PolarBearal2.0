from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3BRY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 43-59 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 80-91 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 94-103 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 108-109 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 130-145 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 150-169 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 200-203 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 214-230 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 233-240 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 248-252 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 268-273 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 280-288 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 293-302 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 310-315 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 327-329 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 335-347 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 350-360 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 378-387 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 392-401 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 420-435 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Bstrand20", "resi 43-59 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 80-91 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 94-103 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 108-109 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 130-145 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 150-169 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 200-203 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 214-230 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 233-240 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 248-252 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 268-273 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 280-288 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 293-302 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 310-315 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 327-329 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 335-347 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 350-360 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 378-387 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 392-401 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 420-435 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
