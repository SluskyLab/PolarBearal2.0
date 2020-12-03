from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1AVG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Hstrand0", "resi 30-35 & chain H ")
cmd.color ("red", "Hstrand0")


cmd.select("Hstrand1", "resi 39-45 & chain H ")
cmd.color ("green", "Hstrand1")


cmd.select("Hstrand2", "resi 51-54 & chain H ")
cmd.color ("orange", "Hstrand2")


cmd.select("Hstrand3", "resi 64-68 & chain H ")
cmd.color ("teal", "Hstrand3")


cmd.select("Hstrand4", "resi 81-90 & chain H ")
cmd.color ("yellow", "Hstrand4")


cmd.select("Hstrand5", "resi 104-108 & chain H ")
cmd.color ("blue", "Hstrand5")


cmd.select("Hstrand6", "resi 135-140 & chain H ")
cmd.color ("red", "Hstrand6")


cmd.select("Hstrand7", "resi 156-161 & chain H ")
cmd.color ("green", "Hstrand7")


cmd.select("Hstrand8", "resi 180-183 & chain H ")
cmd.color ("orange", "Hstrand8")


cmd.select("Hstrand9", "resi 198-202 & chain H ")
cmd.color ("teal", "Hstrand9")


cmd.select("Hstrand10", "resi 207-215 & chain H ")
cmd.color ("yellow", "Hstrand10")


cmd.select("Hstrand11", "resi 226-230 & chain H ")
cmd.color ("blue", "Hstrand11")


cmd.select("Istrand12", "resi 24-28 & chain I ")
cmd.color ("red", "Istrand12")


cmd.select("Istrand13", "resi 37-43 & chain I ")
cmd.color ("green", "Istrand13")


cmd.select("Istrand14", "resi 51-56 & chain I ")
cmd.color ("orange", "Istrand14")


cmd.select("Istrand15", "resi 66-71 & chain I ")
cmd.color ("teal", "Istrand15")


cmd.select("Istrand16", "resi 80-86 & chain I ")
cmd.color ("yellow", "Istrand16")


cmd.select("Istrand17", "resi 92-101 & chain I ")
cmd.color ("blue", "Istrand17")


cmd.select("Istrand18", "resi 106-115 & chain I ")
cmd.color ("red", "Istrand18")


cmd.select("Istrand19", "resi 122-128 & chain I ")
cmd.color ("green", "Istrand19")


cmd.select("barrel", "Hstrand* or Istrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
