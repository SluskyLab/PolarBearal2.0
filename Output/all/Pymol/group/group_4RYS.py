from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RYS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-22 & chain A, resi 25-36 & chain A, resi 41-48 & chain A, resi 118-128 & chain A, resi 105-115 & chain A, resi 92-100 & chain A, resi 176-187 & chain A, resi 160-170 & chain A, resi 148-155 & chain A, resi 199-208 & chain A, resi 217-227 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[29.405685079379346,0.7876929230108036,21.01657485961914])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
