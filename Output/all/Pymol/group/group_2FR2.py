from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FR2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 17-25 & chain A, resi 33-43 & chain A, resi 48-57 & chain A, resi 63-73 & chain A, resi 78-85 & chain A, resi 89-100 & chain A, resi 103-109 & chain A, resi 115-118 & chain A, resi 125-135 & chain A, resi 138-147 & chain A, resi 150-162 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[6.354862430910452,25.680412869934642,16.729724799000888])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
