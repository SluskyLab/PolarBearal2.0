from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GW3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-18 & chain A, resi 21-32 & chain A, resi 37-46 & chain A, resi 113-123 & chain A, resi 100-110 & chain A, resi 87-95 & chain A, resi 167-179 & chain A, resi 152-163 & chain A, resi 136-139 & chain A, resi 142-149 & chain A, resi 190-201 & chain A, resi 207-217 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[109.39987890182003,65.0602984889861,16.48349193796035])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
