from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PDF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 5-7 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[42.84733327229818,30.385332743326824,14.94100030263265])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 14-20 & chain A, resi 36-45 & chain A, resi 49-52 & chain A, resi 57-63 & chain A, resi 67-72 & chain A, resi 75-80 & chain A, resi 100-103 & chain A, resi 109-116 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[51.80905767587515,15.769826971567594,18.42926923128275])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 83-86 & chain A, resi 90-93 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[45.51787567138672,34.32849955558777,26.873124837875366])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 210-212 & chain A, resi 387-390 & chain A, resi 396-403 & chain A, resi 377-384 & chain A, resi 346-353 & chain A, resi 414-419 & chain A, resi 361-366 & chain A, resi 431-436 & chain A, resi 308-322 & chain A, resi 292-294 & chain A, resi 258-260 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[23.872999954223634,15.72590001103069,14.219514290349824])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 219-222 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[14.353500127792358,4.937999904155731,12.419749975204468])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
