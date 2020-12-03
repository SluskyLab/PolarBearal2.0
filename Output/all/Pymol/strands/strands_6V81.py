from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6V81.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 47-51 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 74-77 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 87-90 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 105-108 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 111-112 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 130-137 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 150-156 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 164-172 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 176-186 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 196-207 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 216-228 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 234-247 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 273-288 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 293-309 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 326-342 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 350-368 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 386-408 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 411-428 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 440-456 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 461-468 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 471-472 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 496-497 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 500-509 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 512-523 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 527-533 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 536-541 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 545-558 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 562-575 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 596-604 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 611-619 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 622-623 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 631-632 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 635-648 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 651-660 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 667-671 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 681-684 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 688-698 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
