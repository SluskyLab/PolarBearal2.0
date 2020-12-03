from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 10-24 & chain A, resi 32-44 & chain A, resi 57-72 & chain A, resi 48-54 & chain A, resi 96-108 & chain A, resi 111-118 & chain A, resi 136-145 & chain A, resi 150-161 & chain A, resi 185-193 & chain A, resi 198-207 & chain A, resi 211-223 & chain A, resi 228-240 & chain A, resi 248-260 & chain A, resi 263-273 & chain A, resi 304-313 & chain A, resi 321-334 & chain A, resi 340-353 & chain A, resi 362-373 & chain A, resi 379-391 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-34.97809296345289,12.46366816752516,-44.245146093115345])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 172-175 & chain A, resi 178-181 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-33.78587508201599,9.09612500667572,-21.824125051498413])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
