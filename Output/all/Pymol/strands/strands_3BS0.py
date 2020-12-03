from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3BS0.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 44-60 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 66-69 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 80-90 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 93-108 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 129-136 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 139-143 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 151-155 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 158-169 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 182-183 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 199-204 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 214-228 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 233-240 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 244-245 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 248-257 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 263-272 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 280-288 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 293-302 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 314-317 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 320-324 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 333-343 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 348-356 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 376-385 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 390-405 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 417-433 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Bstrand24", "resi 44-60 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 66-69 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 80-90 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 93-108 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 129-136 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 139-143 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 151-155 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 158-169 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 182-183 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 199-204 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 214-228 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 233-240 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 244-245 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 248-257 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 263-272 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 280-288 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("Bstrand40", "resi 293-302 & chain B ")
cmd.color ("yellow", "Bstrand40")


cmd.select("Bstrand41", "resi 314-317 & chain B ")
cmd.color ("blue", "Bstrand41")


cmd.select("Bstrand42", "resi 320-324 & chain B ")
cmd.color ("red", "Bstrand42")


cmd.select("Bstrand43", "resi 333-343 & chain B ")
cmd.color ("green", "Bstrand43")


cmd.select("Bstrand44", "resi 348-356 & chain B ")
cmd.color ("orange", "Bstrand44")


cmd.select("Bstrand45", "resi 376-385 & chain B ")
cmd.color ("teal", "Bstrand45")


cmd.select("Bstrand46", "resi 390-405 & chain B ")
cmd.color ("yellow", "Bstrand46")


cmd.select("Bstrand47", "resi 417-433 & chain B ")
cmd.color ("blue", "Bstrand47")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
