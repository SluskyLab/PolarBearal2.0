from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3X2R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 50-52 & chain A, resi 136-146 & chain A, resi 150-180 & chain A, resi 186-208 & chain A, resi 214-224 & chain A, resi 214-224 & chain B, resi 186-208 & chain B, resi 150-180 & chain B, resi 136-146 & chain B, resi 50-52 & chain B, resi 214-224 & chain E, resi 186-208 & chain E, resi 150-180 & chain E, resi 136-146 & chain E, resi 50-52 & chain E, resi 214-224 & chain H, resi 186-208 & chain H, resi 150-180 & chain H, resi 214-224 & chain F, resi 186-208 & chain F, resi 150-180 & chain F, resi 214-224 & chain D, resi 186-208 & chain D, resi 150-180 & chain D, resi 214-224 & chain C, resi 186-208 & chain C, resi 150-180 & chain C, resi 136-146 & chain C, resi 50-52 & chain C, resi 136-146 & chain D, resi 50-52 & chain D, resi 136-146 & chain F, resi 50-52 & chain F, resi 214-224 & chain G, resi 186-208 & chain G, resi 150-180 & chain G, resi 136-146 & chain G, resi 50-52 & chain G, resi 136-146 & chain H, resi 50-52 & chain H, resi 150-180 & chain I, resi 136-146 & chain I, resi 50-52 & chain I, resi 186-207 & chain I, resi 215-224 & chain I, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[206.86904104472217,36.50867276866782,19.409314564414775])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
