from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UYN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 819-833 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 838-855 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 858-873 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 876-893 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 897-915 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 921-939 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 948-962 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 979-995 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 1000-1011 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 1041-1054 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 1057-1068 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 1071-1083 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
