from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WJR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 3-10 & chain A, resi 15-25 & chain A, resi 30-41 & chain A, resi 54-61 & chain A, resi 69-80 & chain A, resi 83-97 & chain A, resi 100-111 & chain A, resi 127-137 & chain A, resi 142-153 & chain A, resi 165-175 & chain A, resi 181-189 & chain A, resi 205-213 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[3.4912900962219893,-23.212542038837462,-21.350267202799557])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 194-196 & chain A, resi 199-202 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-1.9892857032162803,-21.191999980381556,0.7381428139550346])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
