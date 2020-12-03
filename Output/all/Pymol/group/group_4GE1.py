from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GE1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 22-30 & chain A, resi 42-49 & chain A, resi 54-63 & chain A, resi 68-77 & chain A, resi 87-95 & chain A, resi 101-114 & chain A, resi 119-126 & chain A, resi 129-139 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[4.646607611847075,3.5977088923129856,47.880936827840685])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
