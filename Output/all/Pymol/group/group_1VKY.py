from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 27-32 & chain A, resi 37-42 & chain A, resi 331-334 & chain A, resi 286-290 & chain A, resi 244-247 & chain A, resi 55-63 & chain A, resi 193-201 & chain A, resi 223-226 & chain A, resi 267-269 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[17.110880012512208,35.0519998550415,16.740440015792846])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 67-70 & chain A, resi 78-87 & chain A, resi 90-96 & chain A, resi 126-131 & chain A, resi 113-120 & chain A, resi 106-110 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[38.12582511901856,34.40837516784668,-6.8372249558568])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
