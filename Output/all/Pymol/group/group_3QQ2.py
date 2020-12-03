from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QQ2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 748-761 & chain A, resi 768-785 & chain A, resi 788-805 & chain A, resi 809-826 & chain A, resi 830-848 & chain A, resi 854-876 & chain A, resi 881-899 & chain A, resi 904-909 & chain A, resi 912-928 & chain A, resi 933-947 & chain A, resi 967-978 & chain A, resi 982-993 & chain A, resi 996-1008 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[16.711083338541144,-6.963676475024983,29.163357850967667])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
