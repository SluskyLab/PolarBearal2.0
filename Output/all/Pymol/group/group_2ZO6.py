from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZO6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-18 & chain A, resi 21-32 & chain A, resi 37-46 & chain A, resi 113-123 & chain A, resi 100-110 & chain A, resi 87-95 & chain A, resi 167-178 & chain A, resi 151-162 & chain A, resi 135-138 & chain A, resi 141-148 & chain A, resi 189-200 & chain A, resi 203-213 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[12.354162640930191,43.74287792919128,10.925268272861716])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
