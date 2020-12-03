from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FRX.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 11-22 & chain A, resi 31-44 & chain A, resi 53-65 & chain A, resi 96-108 & chain A, resi 111-118 & chain A, resi 136-144 & chain A, resi 150-161 & chain A, resi 168-170 & chain A, resi 189-197 & chain A, resi 202-211 & chain A, resi 215-228 & chain A, resi 231-244 & chain A, resi 274-286 & chain A, resi 289-299 & chain A, resi 334-343 & chain A, resi 352-364 & chain A, resi 371-383 & chain A, resi 393-428 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[26.711151372402085,-11.393761470273068,47.06024330034168])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
