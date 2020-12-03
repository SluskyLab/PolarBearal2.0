from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QO4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 4-12 & chain A, resi 37-43 & chain A, resi 46-53 & chain A, resi 56-63 & chain A, resi 116-124 & chain A, resi 106-113 & chain A, resi 97-103 & chain A, resi 88-92 & chain A, resi 77-85 & chain A, resi 67-71 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-9.90645332266887,18.565399990081787,-1.172613291144371])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
