from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 28-31 & chain A, resi 82-87 & chain A, resi 74-79 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-13.766874879598618,-76.43524980545044,6.482937514781952])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 93-99 & chain A, resi 162-171 & chain A, resi 147-156 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-0.7300370710867422,-42.942962929054545,11.934407375476978])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 180-182 & chain A, resi 256-259 & chain A, resi 239-243 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[30.80541706085205,-35.194249629974365,-8.512999931971232])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 322-328 & chain A, resi 335-341 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[22.78721421105521,-36.34764289855957,-36.05078615461077])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 397-403 & chain A, resi 413-419 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[-4.938071463789258,-25.48721422467913,-23.993285724094935])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 425-433 & chain A, resi 437-449 & chain A, resi 454-462 & chain A, resi 466-479 & chain A, resi 483-494 & chain A, resi 507-520 & chain A, resi 526-539 & chain A, resi 564-580 & chain A, resi 591-600 & chain A, resi 609-620 & chain A, resi 626-635 & chain A, resi 685-695 & chain A, resi 706-718 & chain A, resi 749-759 & chain A, resi 764-773 & chain A, resi 784-789 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[-15.905042981027917,6.705860217091858,-22.191349397743902])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 670-673 & chain A, resi 677-680 & chain A, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[-12.236249923706055,32.41487503051758,-27.351624965667725])
cmd.color ("cyan", "Centroid6")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
