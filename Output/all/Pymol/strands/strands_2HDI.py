from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HDI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 33-34 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 42-43 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 50-54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 77-81 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 87-91 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 99-103 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106-107 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 130-137 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 151-157 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 165-175 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 183-195 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 199-210 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 231-243 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 249-263 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 271-284 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 289-302 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 310-325 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 330-344 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 357-373 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 376-387 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 391-403 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 408-419 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 431-434 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 439-442 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 450-462 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 472-487 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 490-491 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 503-508 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 514-538 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 543-556 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 563-579 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 587-596 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 612-624 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 627-634 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 654-662 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Bstrand35", "resi 298-308 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 316-326 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
