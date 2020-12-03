from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QTT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-7 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 10-10 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 14-16 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 19-19 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 22-25 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 29-38 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 41-51 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 56-58 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 70-74 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 78-80 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 85-88 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 91-95 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 98-106 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 113-115 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
