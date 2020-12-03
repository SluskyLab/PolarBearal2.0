from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1R0U.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 5-17 & chain A, resi 20-35 & chain A, resi 38-47 & chain A, resi 52-59 & chain A, resi 62-68 & chain A, resi 71-78 & chain A, resi 81-89 & chain A, resi 92-108 & chain A, resi 111-121 & chain A, resi 129-137 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[25.17358335742244,25.241722080442642,8.368638859371897])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
