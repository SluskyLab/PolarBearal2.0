from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3D5K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 88-99 & chain A, resi 110-126 & chain A, resi 299-310 & chain A, resi 322-335 & chain A, resi 322-335 & chain B, resi 299-310 & chain B, resi 110-126 & chain B, resi 88-99 & chain B, resi 88-99 & chain C, resi 110-126 & chain C, resi 299-310 & chain C, resi 322-335 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-25.913945469711766,-0.7753999891070028,4.018090882265207])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
