from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6AT8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-14 & chain A, resi 39-45 & chain A, resi 48-54 & chain A, resi 59-65 & chain A, resi 124-132 & chain A, resi 114-121 & chain A, resi 105-111 & chain A, resi 92-98 & chain A, resi 82-89 & chain A, resi 70-72 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-0.1980357157687346,-0.8825237904453561,13.55246436791051])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
