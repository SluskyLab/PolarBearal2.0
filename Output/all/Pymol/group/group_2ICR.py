from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-22 & chain A, resi 25-36 & chain A, resi 41-50 & chain A, resi 119-129 & chain A, resi 104-114 & chain A, resi 91-99 & chain A, resi 176-187 & chain A, resi 160-171 & chain A, resi 142-145 & chain A, resi 148-155 & chain A, resi 198-208 & chain A, resi 216-226 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-53.706411207875895,-17.57034680247307,-14.197612864536143])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
