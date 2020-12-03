from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2G3O.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 4-14 & chain A, resi 17-28 & chain A, resi 33-40 & chain A, resi 109-119 & chain A, resi 96-105 & chain A, resi 83-91 & chain A, resi 165-176 & chain A, resi 149-160 & chain A, resi 132-135 & chain A, resi 138-144 & chain A, resi 191-199 & chain A, resi 205-215 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[44.527801727426464,-42.281689495875916,2.0729137990495254])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
