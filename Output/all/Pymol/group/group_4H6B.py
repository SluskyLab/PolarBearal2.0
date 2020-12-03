from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H6B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-19 & chain A, resi 56-59 & chain A, resi 65-79 & chain A, resi 50-53 & chain A, resi 84-94 & chain A, resi 100-108 & chain A, resi 113-120 & chain A, resi 128-137 & chain A, resi 141-149 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-14.900775027275085,-4.131037501618266,-25.548750042915344])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
