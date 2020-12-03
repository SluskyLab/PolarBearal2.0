from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F1V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 6-16 & chain A, resi 36-46 & chain A, resi 51-58 & chain A, resi 82-88 & chain A, resi 96-114 & chain A, resi 71-79 & chain A, resi 61-67 & chain A, resi 131-143 & chain A, resi 148-157 & chain A, resi 181-191 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-14.77852825026186,-14.931726436007697,34.47485856290133])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 123-128 & chain A, resi 160-167 & chain A, resi 174-177 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[0.7522777914483514,-9.493388937579262,16.549166944291855])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
