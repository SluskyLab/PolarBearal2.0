from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UYN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 819-833 & chain X, resi 838-855 & chain X, resi 858-873 & chain X, resi 876-893 & chain X, resi 897-915 & chain X, resi 921-939 & chain X, resi 948-962 & chain X, resi 979-995 & chain X, resi 1000-1011 & chain X, resi 1041-1054 & chain X, resi 1057-1068 & chain X, resi 1071-1083 & chain X, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[9.998680843912224,17.87628193738613,179.15169151793134])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
