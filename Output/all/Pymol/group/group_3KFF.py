from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KFF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 17-26 & chain A, resi 41-47 & chain A, resi 51-60 & chain A, resi 63-73 & chain A, resi 80-83 & chain A, resi 87-95 & chain A, resi 100-109 & chain A, resi 112-121 & chain A, resi 148-150 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[11.433324379292694,-32.10777027542527,9.577175661946672])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
