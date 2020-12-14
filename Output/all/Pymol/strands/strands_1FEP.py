from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1FEP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 28-32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 55-59 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 70-74 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 82-86 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 121-126 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 140-145 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 154-161 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 172-182 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 187-198 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 227-239 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 245-259 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 282-296 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 302-316 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 338-345 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 348-356 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 360-373 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 407-417 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 424-435 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 439-450 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 456-459 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 462-467 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 479-481 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 495-497 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 505-518 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 521-538 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 552-571 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 581-592 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 606-611 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 623-628 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 654-664 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 669-676 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 715-717 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 720-723 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
