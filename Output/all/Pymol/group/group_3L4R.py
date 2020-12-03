from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3L4R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 17-26 & chain A, resi 41-48 & chain A, resi 51-59 & chain A, resi 64-73 & chain A, resi 79-83 & chain A, resi 87-96 & chain A, resi 100-109 & chain A, resi 112-121 & chain A, resi 148-150 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[16.331341692163974,21.302645562570305,4.137746836612873])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
