from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PIB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 9-19 & chain A, resi 22-33 & chain A, resi 38-47 & chain A, resi 114-124 & chain A, resi 101-111 & chain A, resi 88-96 & chain A, resi 169-180 & chain A, resi 153-164 & chain A, resi 137-140 & chain A, resi 143-150 & chain A, resi 193-205 & chain A, resi 210-220 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[30.865389690679663,-13.740882319672142,-0.38622057268067317])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
