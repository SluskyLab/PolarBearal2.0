from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4XMC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 25-32 & chain A, resi 41-50 & chain A, resi 53-62 & chain A, resi 67-76 & chain A, resi 83-91 & chain A, resi 97-99 & chain A, resi 105-115 & chain A, resi 118-127 & chain A, resi 130-140 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[5.146731705927268,-1.505085379612155,8.7487438270118])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
