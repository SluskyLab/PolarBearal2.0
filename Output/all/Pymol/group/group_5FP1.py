from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FP1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 40-44 & chain A, resi 111-118 & chain A, resi 132-138 & chain A, resi 93-95 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[45.12408288319906,78.9540828069051,46.91570806503296])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 82-84 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[46.292667388916016,83.59833272298177,57.747999827067055])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 231-235 & chain A, resi 240-245 & chain A, resi 698-701 & chain A, resi 690-693 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[58.155737023604544,83.20726213957134,73.18536778500206])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 312-338 & chain A, resi 343-365 & chain A, resi 388-390 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[37.7265554357458,70.69059273048684,57.292722136886034])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 597-600 & chain A, resi 603-606 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[38.44462537765503,87.09137439727783,81.8596248626709])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
