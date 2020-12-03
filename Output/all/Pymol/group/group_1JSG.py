from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JSG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-10 & chain A, resi 91-100 & chain A, resi 84-86 & chain A, resi 75-78 & chain A, resi 17-22 & chain A, resi 25-28 & chain A, resi 34-42 & chain A, resi 46-53 & chain A, resi 103-111 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[18.93233929361616,12.088178583553859,39.77496440070016])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
