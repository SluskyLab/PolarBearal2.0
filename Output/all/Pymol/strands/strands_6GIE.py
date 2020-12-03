from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6GIE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 0-13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 21-35 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 52-61 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 72-83 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 90-124 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 127-135 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 168-178 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 185-194 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 198-209 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 212-220 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 230-241 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 244-254 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 263-273 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
