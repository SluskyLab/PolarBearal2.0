from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EMN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 26-32 & chain X, resi 38-48 & chain X, resi 54-64 & chain X, resi 69-76 & chain X, resi 81-88 & chain X, resi 95-103 & chain X, resi 110-120 & chain X, resi 123-131 & chain X, resi 137-146 & chain X, resi 149-158 & chain X, resi 163-174 & chain X, resi 178-185 & chain X, resi 189-197 & chain X, resi 202-211 & chain X, resi 214-225 & chain X, resi 231-238 & chain X, resi 242-252 & chain X, resi 255-264 & chain X, resi 274-282 & chain X, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[12.637347840531932,31.328706616940707,17.183668490661226])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
