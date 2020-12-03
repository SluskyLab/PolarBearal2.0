from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5LDV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 13-28 & chain A, resi 42-58 & chain A, resi 61-73 & chain A, resi 89-99 & chain A, resi 104-112 & chain A, resi 126-134 & chain A, resi 140-150 & chain A, resi 184-194 & chain A, resi 198-209 & chain A, resi 213-224 & chain A, resi 231-243 & chain A, resi 256-267 & chain A, resi 270-286 & chain A, resi 316-331 & chain A, resi 335-347 & chain A, resi 357-369 & chain A, resi 374-385 & chain A, resi 395-407 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[25.713914181029846,41.28106861360083,4.921961343947142])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 164-167 & chain A, resi 170-174 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[24.88022232055664,45.952333238389755,-20.502333535088432])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
