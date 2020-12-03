from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ALO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3-3 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 7-8 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 11-11 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 14-14 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 34-43 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 48-50 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 53-58 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 62-70 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 75-84 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 92-97 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 100-110 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 115-124 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 128-142 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 159-159 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 165-169 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 173-174 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Bstrand16", "resi 3-3 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 7-8 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 11-11 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 14-15 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 25-25 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 28-36 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 39-43 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 48-50 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 53-59 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 62-70 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 75-84 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 92-97 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 100-110 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 115-124 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 128-142 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 159-159 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 165-169 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 173-173 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
