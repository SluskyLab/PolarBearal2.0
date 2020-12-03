from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1O8V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 36-45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 49-56 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 60-64 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 69-75 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 82-88 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 91-98 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 101-110 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 113-120 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 123-130 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
