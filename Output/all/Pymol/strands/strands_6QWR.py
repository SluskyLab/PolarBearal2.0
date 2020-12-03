from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6QWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 16-27 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 46-48 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 56-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 67-73 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 78-84 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 94-107 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 118-132 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 140-155 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 162-169 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 172-177 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 187-191 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 194-204 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
