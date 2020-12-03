from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3A2S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-19 & chain X, resi 30-37 & chain X, resi 328-340 & chain X, resi 310-323 & chain X, resi 295-307 & chain X, resi 271-280 & chain X, resi 254-268 & chain X, resi 231-243 & chain X, resi 212-228 & chain X, resi 184-198 & chain X, resi 171-180 & chain X, resi 144-151 & chain X, resi 128-137 & chain X, resi 89-95 & chain X, resi 77-85 & chain X, resi 55-66 & chain X, resi 42-49 & chain X, resi 202-204 & chain X, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[22.080630511485886,9.405325107331493,15.633586198403478])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 71-74 & chain X, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[38.2839994430542,21.610249996185303,18.791499853134155])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 107-111 & chain X, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[17.21339988708496,15.876199722290039,14.057199859619141])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 163-166 & chain X, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[44.470749855041504,-3.8260000348091125,36.3432502746582])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 246-248 & chain X, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[29.1353333791097,-2.606666684150696,44.93000030517578])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 288-290 & chain X, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[11.848333358764648,-0.6043332815170288,38.84933344523112])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
