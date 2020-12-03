from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2JOZ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 19-22 & chain A, resi 35-40 & chain A, resi 44-51 & chain A, resi 55-58 & chain A, resi 62-68 & chain A, resi 74-80 & chain A, resi 87-92 & chain A, resi 98-102 & chain A, resi 105-111 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[0.9283888886372248,2.0262222477683314,-1.465425958925927])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
