from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5NEC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 52-55 & chain A, resi 122-128 & chain A, resi 144-149 & chain A, resi 104-106 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[32.74405031204223,29.407600116729736,-20.149100017547607])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 78-81 & chain A, resi 92-95 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[32.52999949455261,16.25837516784668,-25.941874980926514])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 157-165 & chain A, resi 170-180 & chain A, resi 185-198 & chain A, resi 201-217 & chain A, resi 223-236 & chain A, resi 274-289 & chain A, resi 294-314 & chain A, resi 325-352 & chain A, resi 355-377 & chain A, resi 401-403 & chain A, resi 417-419 & chain A, resi 424-442 & chain A, resi 445-462 & chain A, resi 469-486 & chain A, resi 492-501 & chain A, resi 532-543 & chain A, resi 548-559 & chain A, resi 577-589 & chain A, resi 594-607 & chain A, resi 637-648 & chain A, resi 651-660 & chain A, resi 676-686 & chain A, resi 691-698 & chain A, resi 722-731 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[31.18483744223425,25.38229139450869,-18.71929454006986])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 706-709 & chain A, resi 714-717 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[23.936124801635742,9.094375014305115,-30.948124885559082])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
