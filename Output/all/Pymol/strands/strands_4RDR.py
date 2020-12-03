from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RDR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 35-38 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 59-64 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 68-73 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 82-85 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 88-89 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 109-115 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 131-136 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 148-157 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 163-172 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 177-188 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 207-218 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 223-237 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 248-251 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 282-285 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 302-317 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 324-342 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 345-363 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 369-386 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 397-415 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 418-432 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 456-470 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 475-486 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 496-499 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 504-507 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 515-528 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 531-550 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 567-590 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 593-607 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 612-613 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 624-625 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 630-631 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 639-647 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 653-661 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 677-689 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 694-702 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 725-733 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
