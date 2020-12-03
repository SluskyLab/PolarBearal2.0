from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PPT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 7-15 & chain A, resi 40-46 & chain A, resi 49-55 & chain A, resi 60-66 & chain A, resi 122-131 & chain A, resi 112-119 & chain A, resi 102-109 & chain A, resi 91-97 & chain A, resi 80-88 & chain A, resi 71-74 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[20.28703165556255,48.749568296733656,-0.06402104567540319])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
