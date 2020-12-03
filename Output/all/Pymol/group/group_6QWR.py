from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6QWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 16-27 & chain A, resi 56-62 & chain A, resi 67-73 & chain A, resi 94-107 & chain A, resi 78-84 & chain A, resi 46-48 & chain A, resi 118-132 & chain A, resi 140-155 & chain A, resi 162-169 & chain A, resi 172-177 & chain A, resi 187-191 & chain A, resi 194-204 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-40.70318923125396,-18.20916224385167,-31.248954910415787])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
