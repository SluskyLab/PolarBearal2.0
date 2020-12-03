from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ES7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 16-25 & chain A, resi 40-46 & chain A, resi 52-61 & chain A, resi 64-74 & chain A, resi 80-85 & chain A, resi 90-99 & chain A, resi 104-113 & chain A, resi 119-126 & chain A, resi 153-155 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[13.249093287785849,-8.04849329729875,-9.151013351927201])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
