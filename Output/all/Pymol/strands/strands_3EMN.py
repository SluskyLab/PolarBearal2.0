from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EMN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 26-32 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 38-48 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 54-64 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 69-76 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 81-88 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 95-103 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 110-120 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 123-131 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 137-146 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 149-158 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 163-174 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 178-185 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("Xstrand12", "resi 189-197 & chain X ")
cmd.color ("red", "Xstrand12")


cmd.select("Xstrand13", "resi 202-211 & chain X ")
cmd.color ("green", "Xstrand13")


cmd.select("Xstrand14", "resi 214-225 & chain X ")
cmd.color ("orange", "Xstrand14")


cmd.select("Xstrand15", "resi 231-238 & chain X ")
cmd.color ("teal", "Xstrand15")


cmd.select("Xstrand16", "resi 242-252 & chain X ")
cmd.color ("yellow", "Xstrand16")


cmd.select("Xstrand17", "resi 255-264 & chain X ")
cmd.color ("blue", "Xstrand17")


cmd.select("Xstrand18", "resi 274-282 & chain X ")
cmd.color ("red", "Xstrand18")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
