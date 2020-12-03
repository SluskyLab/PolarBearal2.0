from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2YNK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 52-56 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[108.69720001220703,63.475199127197264,17.792199516296385])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 92-99 & chain A, resi 115-127 & chain A, resi 130-142 & chain A, resi 156-161 & chain A, resi 164-170 & chain A, resi 193-199 & chain A, resi 216-224 & chain A, resi 235-246 & chain A, resi 249-259 & chain A, resi 289-299 & chain A, resi 308-320 & chain A, resi 323-338 & chain A, resi 343-352 & chain A, resi 389-398 & chain A, resi 404-414 & chain A, resi 429-443 & chain A, resi 446-456 & chain A, resi 465-475 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[115.68457192489781,64.502551540886,25.502149492194974])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
