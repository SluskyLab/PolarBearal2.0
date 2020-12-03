from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 151-159 & chain A, resi 166-173 & chain A, resi 181-192 & chain A, resi 176-178 & chain A, resi 195-208 & chain A, resi 211-221 & chain A, resi 227-238 & chain A, resi 241-249 & chain A, resi 252-257 & chain A, resi 263-279 & chain A, resi 285-295 & chain A, resi 312-323 & chain A, resi 326-335 & chain A, resi 340-351 & chain A, resi 380-389 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-11.843634641777056,26.95586545077654,4.623692315835983])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
