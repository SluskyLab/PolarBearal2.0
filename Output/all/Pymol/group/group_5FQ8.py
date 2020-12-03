from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FQ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 44-48 & chain B, resi 138-144 & chain B, resi 161-166 & chain B, resi 101-103 & chain B, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[44.13228552682059,46.73933356148856,5.3538571539379305])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 71-75 & chain B, resi 84-88 & chain B, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[50.47529945373535,59.426200485229494,2.320600003004074])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 113-115 & chain B, resi 125-128 & chain B, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[53.77285712105887,63.772142137799946,15.636714117867607])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 177-188 & chain B, resi 252-264 & chain B, resi 268-280 & chain B, resi 289-303 & chain B, resi 306-320 & chain B, resi 376-394 & chain B, resi 398-417 & chain B, resi 446-469 & chain B, resi 472-495 & chain B, resi 513-534 & chain B, resi 538-549 & chain B, resi 558-569 & chain B, resi 582-596 & chain B, resi 643-656 & chain B, resi 661-673 & chain B, resi 697-712 & chain B, resi 716-731 & chain B, resi 802-812 & chain B, resi 815-825 & chain B, resi 904-915 & chain B, resi 928-941 & chain B, resi 973-983 & chain B, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[45.92403586610349,50.54737416570058,7.721745493325466])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 222-229 & chain B, resi 232-237 & chain B, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[92.31721551077706,83.40249960763114,12.317999839782715])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 607-614 & chain B, resi 617-620 & chain B, resi 629-631 & chain B, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[44.918799845377606,88.51393280029296,23.41273333231608])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 676-680 & chain B, resi 689-693 & chain B, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[34.3810998916626,79.20009994506836,7.90669994354248])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 741-746 & chain B, resi 752-756 & chain B, resi 761-766 & chain B, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[47.061470704920154,79.55811803481159,-0.877823589479222])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 828-831 & chain B, resi 899-901 & chain B, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[58.96528516496931,74.505857195173,-4.062571421265602])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 859-865 & chain B, resi 868-873 & chain B, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[60.8050771859976,103.11969346266527,-18.37430763244629])
cmd.color ("red", "Centroid9")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
