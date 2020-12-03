from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X27.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 10-21 & chain X, resi 45-55 & chain X, resi 60-67 & chain X, resi 96-101 & chain X, resi 111-129 & chain X, resi 85-93 & chain X, resi 70-77 & chain X, resi 39-42 & chain X, resi 146-158 & chain X, resi 163-172 & chain X, resi 199-210 & chain X, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[10.64020535243409,15.819553571087974,47.97626805305481])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 139-143 & chain X, resi 175-181 & chain X, resi 190-196 & chain X, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[11.248578949978477,9.977210496601305,70.50194790488796])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
