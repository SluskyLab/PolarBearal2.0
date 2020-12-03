from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3GP6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22-33 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 52-60 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 66-75 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 81-93 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 101-113 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 121-133 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 136-143 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 152-161 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
