from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RDR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 35-38 & chain A, resi 109-115 & chain A, resi 131-136 & chain A, resi 82-85 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-35.789952414376394,37.865523928687686,35.801000140962145])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 59-64 & chain A, resi 68-73 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-35.11383326848348,33.74499988555908,21.27708355585734])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 148-157 & chain A, resi 163-172 & chain A, resi 177-188 & chain A, resi 207-218 & chain A, resi 223-237 & chain A, resi 302-317 & chain A, resi 324-342 & chain A, resi 345-363 & chain A, resi 369-386 & chain A, resi 397-415 & chain A, resi 418-432 & chain A, resi 456-470 & chain A, resi 475-486 & chain A, resi 515-528 & chain A, resi 531-550 & chain A, resi 567-590 & chain A, resi 504-507 & chain A, resi 496-499 & chain A, resi 593-607 & chain A, resi 639-647 & chain A, resi 653-661 & chain A, resi 677-689 & chain A, resi 694-702 & chain A, resi 725-733 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-35.36615786832922,33.49598450114483,32.136160998152505])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 248-251 & chain A, resi 282-285 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[-39.7153754234314,7.145749926567078,7.039250135421753])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
