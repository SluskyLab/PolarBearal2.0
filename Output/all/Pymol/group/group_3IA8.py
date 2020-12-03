from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3IA8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 18-22 & chain A, resi 33-45 & chain A, resi 26-30 & chain A, resi 51-59 & chain A, resi 66-76 & chain A, resi 82-89 & chain A, resi 93-102 & chain A, resi 105-115 & chain A, resi 124-133 & chain A, resi 139-147 & chain A, resi 150-163 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[28.550290940024635,37.9913910779086,51.389045437899505])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
