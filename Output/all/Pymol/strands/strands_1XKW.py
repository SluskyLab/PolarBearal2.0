from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XKW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 82-87 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 109-115 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 118-123 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 126-127 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 130-133 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 136-137 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 153-160 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 174-180 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 188-196 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 200-210 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 217-229 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 236-251 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 254-268 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 297-314 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 317-338 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 349-375 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 378-398 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 407-408 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 432-448 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 451-465 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 470-471 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 476-488 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 491-502 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 518-531 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 536-553 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 566-586 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 589-604 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 621-630 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 638-647 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 650-654 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 657-661 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 664-674 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 679-686 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 694-696 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 705-706 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 711-719 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
