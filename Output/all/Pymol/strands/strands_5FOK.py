from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FOK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 52-55 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 78-81 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 92-95 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 98-99 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 104-106 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 109-110 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 122-128 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 144-149 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 241-242 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 323-350 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 373-376 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 395-397 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 410-413 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 650-651 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 659-660 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 693-696 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 701-704 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Bstrand17", "resi 52-55 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 78-81 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 92-95 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 98-99 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 104-106 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 109-110 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 122-131 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 142-149 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 241-242 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 323-350 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 373-376 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("Bstrand28", "resi 395-397 & chain B ")
cmd.color ("yellow", "Bstrand28")


cmd.select("Bstrand29", "resi 410-413 & chain B ")
cmd.color ("blue", "Bstrand29")


cmd.select("Bstrand30", "resi 650-651 & chain B ")
cmd.color ("red", "Bstrand30")


cmd.select("Bstrand31", "resi 659-660 & chain B ")
cmd.color ("green", "Bstrand31")


cmd.select("Bstrand32", "resi 693-696 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 701-704 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
