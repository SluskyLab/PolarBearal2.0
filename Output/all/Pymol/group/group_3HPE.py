from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3HPE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 28-35 & chain A, resi 39-44 & chain A, resi 167-180 & chain A, resi 141-152 & chain A, resi 119-134 & chain A, resi 109-116 & chain A, resi 97-106 & chain A, resi 60-69 & chain A, resi 48-55 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[2.3851847814234053,-10.290728325105231,31.62729341050853])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
