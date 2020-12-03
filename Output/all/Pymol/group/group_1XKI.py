from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XKI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 15-24 & chain A, resi 39-43 & chain A, resi 49-55 & chain A, resi 62-70 & chain A, resi 76-79 & chain A, resi 84-90 & chain A, resi 96-103 & chain A, resi 110-117 & chain A, resi 143-145 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[22.534836135926795,35.77095084893899,2.5726557369725627])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
