from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PBY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 29-31 & chain A, resi 112-114 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[50.31450080871582,50.034000396728516,24.622000058492024])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 175-183 & chain A, resi 187-198 & chain A, resi 201-209 & chain A, resi 214-224 & chain A, resi 228-235 & chain A, resi 238-247 & chain A, resi 250-257 & chain A, resi 260-271 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[57.692200088500975,24.87953759431839,16.182750000059606])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 277-282 & chain A, resi 292-299 & chain A, resi 322-329 & chain A, resi 311-317 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[75.80324133511247,13.302034493150382,25.662689472066944])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 285-287 & chain A, resi 343-350 & chain A, resi 334-340 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[77.05266613430447,17.3398331006368,34.57611115773519])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 355-359 & chain A, resi 379-387 & chain A, resi 400-405 & chain A, resi 435-438 & chain A, resi 428-430 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[55.12977755511248,15.959074161670825,38.95077783090097])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 362-366 & chain A, resi 471-479 & chain A, resi 455-462 & chain A, resi 408-413 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[45.28935732160296,16.47124993801117,42.81996400015695])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
