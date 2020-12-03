from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GGL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-14 & chain A, resi 39-44 & chain A, resi 48-54 & chain A, resi 60-65 & chain A, resi 124-132 & chain A, resi 114-121 & chain A, resi 105-111 & chain A, resi 93-98 & chain A, resi 81-88 & chain A, resi 70-73 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[23.72431433541434,22.9006571497236,8.692600016189473])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
