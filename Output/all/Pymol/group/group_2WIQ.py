from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WIQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-22 & chain A, resi 25-35 & chain A, resi 41-48 & chain A, resi 116-126 & chain A, resi 103-113 & chain A, resi 90-98 & chain A, resi 172-183 & chain A, resi 156-167 & chain A, resi 139-142 & chain A, resi 145-151 & chain A, resi 195-205 & chain A, resi 213-223 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[15.26247107440775,11.886132244790389,9.468644665631135])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
