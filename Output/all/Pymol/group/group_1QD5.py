from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QD5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 39-45 & chain A, resi 65-79 & chain A, resi 86-98 & chain A, resi 109-128 & chain A, resi 131-144 & chain A, resi 154-166 & chain A, resi 169-173 & chain A, resi 176-178 & chain A, resi 197-203 & chain A, resi 206-214 & chain A, resi 221-230 & chain A, resi 236-245 & chain A, resi 255-264 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[34.859838247299194,27.260411718312433,51.52047796810375])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
