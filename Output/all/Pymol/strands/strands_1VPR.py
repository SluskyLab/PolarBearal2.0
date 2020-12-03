from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VPR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 894-895 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 898-899 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 912-914 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 917-919 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 1028-1034 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 1071-1077 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 1080-1084 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 1094-1098 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 1102-1106 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 1112-1118 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 1124-1131 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 1137-1147 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 1150-1159 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 1162-1172 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
