from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4EPA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 29-33 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 85-88 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 91-92 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 105-112 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 126-132 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 140-148 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 152-164 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 168-179 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 196-207 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 214-227 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 233-234 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 253-263 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 266-268 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 273-291 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 294-297 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 300-312 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 320-340 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 345-367 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 372-393 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 396-420 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 423-430 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 433-434 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 454-466 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 470-482 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 485-486 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 497-498 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 501-513 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 520-532 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 550-557 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 567-576 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 592-601 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 607-614 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 622-628 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 631-636 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 641-648 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
