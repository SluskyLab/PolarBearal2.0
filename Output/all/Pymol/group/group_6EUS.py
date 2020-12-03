from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EUS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 70-86 & chain A, resi 105-109 & chain A, resi 391-399 & chain A, resi 375-386 & chain A, resi 355-367 & chain A, resi 330-341 & chain A, resi 309-327 & chain A, resi 284-290 & chain A, resi 261-274 & chain A, resi 243-256 & chain A, resi 229-238 & chain A, resi 203-210 & chain A, resi 189-200 & chain A, resi 159-165 & chain A, resi 148-156 & chain A, resi 126-135 & chain A, resi 114-123 & chain A, resi 303-306 & chain A, resi 402-404 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[36.44077427203839,37.62762053073981,135.27167170597957])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
