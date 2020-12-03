from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X27.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 10-21 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 24-25 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 29-30 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 33-34 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 39-42 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 45-55 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 60-67 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 70-77 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 85-93 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 96-101 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 111-129 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 139-143 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("Xstrand12", "resi 146-158 & chain X ")
cmd.color ("red", "Xstrand12")


cmd.select("Xstrand13", "resi 163-172 & chain X ")
cmd.color ("green", "Xstrand13")


cmd.select("Xstrand14", "resi 175-181 & chain X ")
cmd.color ("orange", "Xstrand14")


cmd.select("Xstrand15", "resi 190-196 & chain X ")
cmd.color ("teal", "Xstrand15")


cmd.select("Xstrand16", "resi 199-210 & chain X ")
cmd.color ("yellow", "Xstrand16")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
