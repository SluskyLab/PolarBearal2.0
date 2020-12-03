from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KZA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 17-26 & chain A, resi 42-48 & chain A, resi 54-59 & chain A, resi 69-75 & chain A, resi 81-86 & chain A, resi 89-97 & chain A, resi 102-108 & chain A, resi 118-123 & chain A, resi 147-150 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[35.10350002781038,-34.294226031149584,12.660854790720247])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
