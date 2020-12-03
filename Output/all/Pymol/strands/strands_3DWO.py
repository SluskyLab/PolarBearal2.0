from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3DWO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 44-63 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 93-105 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 110-125 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 138-153 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 158-177 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 201-220 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 226-233 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 239-248 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 275-281 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 287-295 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 300-309 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 316-321 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("Xstrand12", "resi 324-330 & chain X ")
cmd.color ("red", "Xstrand12")


cmd.select("Xstrand13", "resi 336-346 & chain X ")
cmd.color ("green", "Xstrand13")


cmd.select("Xstrand14", "resi 351-360 & chain X ")
cmd.color ("orange", "Xstrand14")


cmd.select("Xstrand15", "resi 378-388 & chain X ")
cmd.color ("teal", "Xstrand15")


cmd.select("Xstrand16", "resi 395-406 & chain X ")
cmd.color ("yellow", "Xstrand16")


cmd.select("Xstrand17", "resi 409-411 & chain X ")
cmd.color ("blue", "Xstrand17")


cmd.select("Xstrand18", "resi 423-441 & chain X ")
cmd.color ("red", "Xstrand18")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
