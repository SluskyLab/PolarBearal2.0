from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2A13.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 28-38 & chain A, resi 41-53 & chain A, resi 60-67 & chain A, resi 74-84 & chain A, resi 89-96 & chain A, resi 101-109 & chain A, resi 114-123 & chain A, resi 128-138 & chain A, resi 141-150 & chain A, resi 156-165 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[9.088029670390751,71.10081176002427,14.247554478668931])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
