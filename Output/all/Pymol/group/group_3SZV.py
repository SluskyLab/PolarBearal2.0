from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-21 & chain A, resi 32-42 & chain A, resi 50-64 & chain A, resi 89-100 & chain A, resi 103-110 & chain A, resi 128-139 & chain A, resi 142-153 & chain A, resi 175-183 & chain A, resi 188-197 & chain A, resi 201-213 & chain A, resi 219-231 & chain A, resi 239-251 & chain A, resi 254-264 & chain A, resi 294-303 & chain A, resi 312-326 & chain A, resi 329-344 & chain A, resi 354-364 & chain A, resi 370-383 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[25.863475340898795,-22.360735445279175,18.72505833108329])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 163-165 & chain A, resi 169-172 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[20.95437502861023,-31.357875108718872,2.0094999941065907])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
