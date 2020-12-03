from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HPW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 15-25 & chain A, resi 28-39 & chain A, resi 44-51 & chain A, resi 119-129 & chain A, resi 106-116 & chain A, resi 93-101 & chain A, resi 177-188 & chain A, resi 161-171 & chain A, resi 149-156 & chain A, resi 200-209 & chain A, resi 219-229 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[3.593017554482478,-15.34236838747012,-36.747236837420544])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
