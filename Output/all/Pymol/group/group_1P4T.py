from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1P4T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 4-18 & chain A, resi 23-27 & chain A, resi 40-51 & chain A, resi 30-37 & chain A, resi 60-71 & chain A, resi 78-95 & chain A, resi 98-101 & chain A, resi 105-119 & chain A, resi 122-136 & chain A, resi 139-154 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[37.17157506942749,16.932575035095216,32.62565003236135])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
