from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VYF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-14 & chain A, resi 39-45 & chain A, resi 48-54 & chain A, resi 60-64 & chain A, resi 123-131 & chain A, resi 113-120 & chain A, resi 102-110 & chain A, resi 91-97 & chain A, resi 79-88 & chain A, resi 70-73 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[21.122986704508463,32.74638651529948,9.862760018755992])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
