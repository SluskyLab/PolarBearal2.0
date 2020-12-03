from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EK9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 41-53 & chain A, resi 61-76 & chain A, resi 247-257 & chain A, resi 260-262 & chain A, resi 280-294 & chain A, resi 280-294 & chain B, resi 247-257 & chain B, resi 61-76 & chain B, resi 41-53 & chain B, resi 260-262 & chain B, resi 41-53 & chain C, resi 61-76 & chain C, resi 247-257 & chain C, resi 260-262 & chain C, resi 280-294 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-42.038505663816956,28.475258629897546,29.2042069709164])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 192-196 & chain A, resi 419-424 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-0.0520909076387232,93.09209095348011,43.18609029596502])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 192-196 & chain B, resi 419-424 & chain B, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[31.10054570978338,54.53372712568803,38.09763648293235])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 192-196 & chain C, resi 419-424 & chain C, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[6.608545384623787,60.931000449440695,81.03545587713069])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
