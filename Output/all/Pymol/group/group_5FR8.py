from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FR8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 38-42 & chain A, resi 129-136 & chain A, resi 150-156 & chain A, resi 92-96 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-14.645919952392578,-40.466439971923826,78.07323944091797])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 65-68 & chain A, resi 81-84 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-8.141874969005585,-30.101125240325928,72.8090009689331])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 164-174 & chain A, resi 182-194 & chain A, resi 198-209 & chain A, resi 229-244 & chain A, resi 247-261 & chain A, resi 287-302 & chain A, resi 305-320 & chain A, resi 340-358 & chain A, resi 362-377 & chain A, resi 404-419 & chain A, resi 424-435 & chain A, resi 439-451 & chain A, resi 456-467 & chain A, resi 506-518 & chain A, resi 522-538 & chain A, resi 561-588 & chain A, resi 495-498 & chain A, resi 479-482 & chain A, resi 545-550 & chain A, resi 591-605 & chain A, resi 618-627 & chain A, resi 632-641 & chain A, resi 675-684 & chain A, resi 690-697 & chain A, resi 721-728 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-16.36922505737748,-37.85213437080383,74.01892497539521])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
