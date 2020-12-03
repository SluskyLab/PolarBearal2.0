from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5M9B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 30-34 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 57-60 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 73-76 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 84-88 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 121-128 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 142-148 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 156-166 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 174-186 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 189-200 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 229-242 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 247-261 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 284-298 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 303-318 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 337-355 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 361-375 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 401-418 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 421-432 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 436-450 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 453-464 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 476-479 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 491-494 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 502-515 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 518-535 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 554-576 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 581-595 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 608-616 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 622-631 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 657-669 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 672-679 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 712-720 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
