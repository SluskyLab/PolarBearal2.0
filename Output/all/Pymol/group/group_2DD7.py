from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2DD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 4-14 & chain A, resi 17-28 & chain A, resi 31-38 & chain A, resi 107-117 & chain A, resi 94-104 & chain A, resi 81-89 & chain A, resi 163-174 & chain A, resi 147-158 & chain A, resi 130-133 & chain A, resi 136-143 & chain A, resi 188-198 & chain A, resi 202-212 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[73.80515836079915,76.28057486216227,67.14514986673991])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
