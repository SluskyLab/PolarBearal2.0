from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4MT4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 84-96 & chain A, resi 109-124 & chain A, resi 299-310 & chain A, resi 322-335 & chain A, resi 84-96 & chain B, resi 109-124 & chain B, resi 299-310 & chain B, resi 322-335 & chain B, resi 84-96 & chain C, resi 109-124 & chain C, resi 299-310 & chain C, resi 322-335 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-5.8576061043323895,25.103375842354513,4.927145475510395])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
