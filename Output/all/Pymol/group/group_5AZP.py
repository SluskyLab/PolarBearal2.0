from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 81-95 & chain A, resi 99-117 & chain A, resi 292-303 & chain A, resi 315-325 & chain A, resi 315-325 & chain B, resi 292-303 & chain B, resi 99-118 & chain B, resi 81-95 & chain B, resi 81-95 & chain C, resi 99-117 & chain C, resi 292-303 & chain C, resi 315-325 & chain C, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-74.99573623741065,-73.45040665092048,-55.99753295982277])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
