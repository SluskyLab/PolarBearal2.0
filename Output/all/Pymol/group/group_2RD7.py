from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2RD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 29-38 & chain C, resi 54-58 & chain C, resi 65-72 & chain C, resi 75-82 & chain C, resi 127-132 & chain C, resi 115-121 & chain C, resi 103-110 & chain C, resi 91-94 & chain C, resi 176-178 & chain C, resi 159-161 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-28.858984220595588,7.39957136909167,27.131174541655042])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
