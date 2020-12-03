from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-21 & chain A, resi 31-43 & chain A, resi 51-64 & chain A, resi 90-102 & chain A, resi 105-112 & chain A, resi 130-138 & chain A, resi 144-155 & chain A, resi 183-191 & chain A, resi 195-204 & chain A, resi 208-220 & chain A, resi 225-238 & chain A, resi 248-260 & chain A, resi 263-273 & chain A, resi 303-312 & chain A, resi 326-338 & chain A, resi 348-360 & chain A, resi 369-380 & chain A, resi 391-403 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-1.8778650942583417,-34.67241399010947,-23.67723259482273])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
