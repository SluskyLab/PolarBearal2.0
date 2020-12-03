from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6BPM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 74-79 & chain A, resi 147-154 & chain A, resi 168-174 & chain A, resi 129-131 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-55.12650012969971,52.53183364868164,37.76383320490519])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 182-190 & chain A, resi 194-204 & chain A, resi 209-221 & chain A, resi 229-241 & chain A, resi 247-260 & chain A, resi 302-319 & chain A, resi 322-343 & chain A, resi 360-386 & chain A, resi 391-410 & chain A, resi 434-455 & chain A, resi 460-480 & chain A, resi 500-522 & chain A, resi 527-538 & chain A, resi 564-577 & chain A, resi 582-599 & chain A, resi 605-625 & chain A, resi 628-643 & chain A, resi 661-669 & chain A, resi 675-684 & chain A, resi 704-714 & chain A, resi 719-726 & chain A, resi 751-759 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-53.39557019730061,51.843532238787375,32.35067842974823])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 734-737 & chain A, resi 743-746 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-61.37837600708008,31.28350043296814,23.41575002670288])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
