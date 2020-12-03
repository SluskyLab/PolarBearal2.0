from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 83-94 & chain A, resi 105-121 & chain A, resi 295-306 & chain A, resi 318-331 & chain A, resi 83-94 & chain B, resi 105-121 & chain B, resi 295-306 & chain B, resi 318-331 & chain B, resi 83-94 & chain C, resi 105-120 & chain C, resi 295-306 & chain C, resi 318-331 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-56.6115792204694,-3.82207317311294,65.22549350087236])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
