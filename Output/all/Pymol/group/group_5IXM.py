from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IXM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-11 & chain A, resi 15-19 & chain A, resi 30-39 & chain A, resi 43-54 & chain A, resi 57-69 & chain A, resi 82-95 & chain A, resi 99-108 & chain A, resi 128-138 & chain A, resi 142-153 & chain A, resi 164-178 & chain A, resi 181-193 & chain A, resi 201-216 & chain A, resi 221-236 & chain A, resi 253-266 & chain A, resi 280-292 & chain A, resi 269-272 & chain A, resi 330-342 & chain A, resi 348-359 & chain A, resi 378-389 & chain A, resi 394-403 & chain A, resi 409-419 & chain A, resi 425-433 & chain A, resi 454-464 & chain A, resi 469-478 & chain A, resi 483-494 & chain A, resi 499-511 & chain A, resi 518-527 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[109.40433671739366,80.67429430344525,79.30011108498168])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
