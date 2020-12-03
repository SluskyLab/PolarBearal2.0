from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4R0B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 17-26 & chain A, resi 42-48 & chain A, resi 54-61 & chain A, resi 66-75 & chain A, resi 81-86 & chain A, resi 89-97 & chain A, resi 102-109 & chain A, resi 116-123 & chain A, resi 149-152 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-11.83897138855287,21.79915722438267,-4.72944285848311])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
