from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 8-21 & chain A, resi 31-43 & chain A, resi 52-66 & chain A, resi 89-101 & chain A, resi 104-111 & chain A, resi 129-137 & chain A, resi 143-154 & chain A, resi 161-163 & chain A, resi 181-191 & chain A, resi 194-203 & chain A, resi 207-219 & chain A, resi 224-235 & chain A, resi 248-259 & chain A, resi 262-272 & chain A, resi 302-311 & chain A, resi 319-333 & chain A, resi 338-354 & chain A, resi 362-373 & chain A, resi 384-397 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[27.368026876023837,41.5564865384783,24.385687470436096])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
