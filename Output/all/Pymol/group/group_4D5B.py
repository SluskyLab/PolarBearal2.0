from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4D5B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 22-37 & chain A, resi 43-60 & chain A, resi 65-80 & chain A, resi 83-103 & chain A, resi 106-122 & chain A, resi 127-146 & chain A, resi 151-165 & chain A, resi 171-187 & chain A, resi 190-206 & chain A, resi 212-230 & chain A, resi 236-250 & chain A, resi 262-278 & chain A, resi 282-297 & chain A, resi 309-323 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[155.42774462989468,15.24036029958532,37.057384587492535])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
