from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SLJ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 122-125 & chain A, resi 200-206 & chain A, resi 223-228 & chain A, resi 179-182 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[26.729856945219495,81.18728601364862,22.4959047408331])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 239-250 & chain A, resi 329-340 & chain A, resi 345-357 & chain A, resi 365-378 & chain A, resi 383-397 & chain A, resi 455-470 & chain A, resi 476-495 & chain A, resi 507-517 & chain A, resi 520-530 & chain A, resi 535-560 & chain A, resi 581-600 & chain A, resi 604-615 & chain A, resi 624-634 & chain A, resi 647-661 & chain A, resi 698-711 & chain A, resi 716-728 & chain A, resi 751-764 & chain A, resi 774-788 & chain A, resi 864-873 & chain A, resi 877-887 & chain A, resi 946-957 & chain A, resi 971-979 & chain A, resi 983-985 & chain A, resi 1006-1016 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[28.325956191122533,80.21965006589889,26.665334355086088])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 673-675 & chain A, resi 685-687 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[14.144000053405762,73.09566752115886,64.15549914042155])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 731-735 & chain A, resi 744-748 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[12.593799829483032,88.10239944458007,49.645600128173825])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 795-798 & chain A, resi 803-806 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[18.097624897956848,101.7393741607666,49.84625005722046])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 818-821 & chain A, resi 828-830 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[34.66400037493025,117.60500008719308,56.10014288766043])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
