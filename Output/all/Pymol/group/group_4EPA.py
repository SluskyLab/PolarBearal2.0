from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4EPA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 29-33 & chain A, resi 105-112 & chain A, resi 126-132 & chain A, resi 85-88 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[70.98987483978271,73.99741649627686,120.10091654459636])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 140-148 & chain A, resi 152-164 & chain A, resi 168-179 & chain A, resi 196-207 & chain A, resi 214-227 & chain A, resi 253-263 & chain A, resi 266-268 & chain A, resi 273-291 & chain A, resi 294-297 & chain A, resi 300-312 & chain A, resi 320-340 & chain A, resi 345-367 & chain A, resi 372-393 & chain A, resi 396-420 & chain A, resi 423-430 & chain A, resi 454-466 & chain A, resi 470-482 & chain A, resi 501-513 & chain A, resi 520-532 & chain A, resi 550-557 & chain A, resi 567-576 & chain A, resi 592-601 & chain A, resi 607-614 & chain A, resi 641-648 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[69.7857679728589,76.84885283077465,126.44642796235927])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 622-628 & chain A, resi 631-636 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[70.0627682025616,65.04999982393704,148.98123286320612])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
