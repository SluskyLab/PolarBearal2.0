from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3CSL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 123-126 & chain A, resi 203-210 & chain A, resi 224-230 & chain A, resi 174-177 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[54.19530420717986,62.98439125392748,230.83300051481828])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 243-252 & chain A, resi 258-266 & chain A, resi 271-282 & chain A, resi 322-335 & chain A, resi 339-355 & chain A, resi 373-390 & chain A, resi 400-415 & chain A, resi 426-448 & chain A, resi 451-470 & chain A, resi 482-497 & chain A, resi 501-518 & chain A, resi 554-571 & chain A, resi 578-589 & chain A, resi 617-631 & chain A, resi 639-652 & chain A, resi 682-695 & chain A, resi 699-709 & chain A, resi 766-773 & chain A, resi 782-789 & chain A, resi 810-820 & chain A, resi 825-831 & chain A, resi 857-864 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[52.580645455963236,64.02046483017529,232.39953536732142])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 521-524 & chain A, resi 548-551 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[41.42512512207031,77.96162509918213,274.5957450866699])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 656-658 & chain A, resi 673-677 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[53.04674959182739,70.4526252746582,260.1541233062744])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 725-727 & chain A, resi 738-740 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[52.186667124430336,84.34416580200195,279.8548329671224])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
