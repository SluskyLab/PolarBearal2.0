from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4I3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-15 & chain A, resi 40-46 & chain A, resi 50-56 & chain A, resi 64-70 & chain A, resi 128-135 & chain A, resi 118-125 & chain A, resi 106-115 & chain A, resi 96-103 & chain A, resi 86-93 & chain A, resi 75-77 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-4.82902199275546,-2.841362643618505,55.76700021932413])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
