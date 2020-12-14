from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FP2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 37-41 & chain A, resi 128-135 & chain A, resi 149-155 & chain A, resi 91-95 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[28.164199600219728,31.302120208740234,87.12151977539062])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 64-66 & chain A, resi 81-83 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[37.23783302307129,38.50716590881348,81.88816579182942])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 163-173 & chain A, resi 181-191 & chain A, resi 196-207 & chain A, resi 232-246 & chain A, resi 249-261 & chain A, resi 289-303 & chain A, resi 306-320 & chain A, resi 342-358 & chain A, resi 364-378 & chain A, resi 405-422 & chain A, resi 425-436 & chain A, resi 440-452 & chain A, resi 457-468 & chain A, resi 508-521 & chain A, resi 524-535 & chain A, resi 564-578 & chain A, resi 581-592 & chain A, resi 607-616 & chain A, resi 622-631 & chain A, resi 656-666 & chain A, resi 671-678 & chain A, resi 705-713 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[29.42718563079834,30.114525020122528,86.8769643511091])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 556-560 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[59.55740051269531,32.12280006408692,85.45440063476562])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
