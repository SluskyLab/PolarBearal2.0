from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 43-90 & chain A, resi 98-111 & chain A, resi 137-150 & chain A, resi 153-160 & chain A, resi 178-189 & chain A, resi 192-203 & chain A, resi 227-237 & chain A, resi 240-249 & chain A, resi 253-264 & chain A, resi 272-284 & chain A, resi 294-306 & chain A, resi 309-319 & chain A, resi 349-358 & chain A, resi 367-380 & chain A, resi 402-416 & chain A, resi 426-436 & chain A, resi 445-457 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[29.082425410930927,27.204995517817018,-0.4501402687567931])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
