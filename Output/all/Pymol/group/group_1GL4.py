from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GL4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 371-376 & chain A, resi 379-383 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[7.397909142754295,-7.173818143931302,38.72690894386985])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 394-396 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[8.657000064849854,6.5689999262491865,43.52566655476888])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 400-414 & chain A, resi 419-433 & chain A, resi 438-446 & chain A, resi 515-525 & chain A, resi 500-507 & chain A, resi 485-494 & chain A, resi 573-584 & chain A, resi 550-562 & chain A, resi 534-547 & chain A, resi 600-613 & chain A, resi 618-628 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[22.694386350386072,22.35049243768056,34.79288637276852])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
