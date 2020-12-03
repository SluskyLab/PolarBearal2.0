from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ICH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 47-57 & chain A, resi 63-73 & chain A, resi 89-98 & chain A, resi 106-114 & chain A, resi 203-217 & chain A, resi 182-199 & chain A, resi 152-159 & chain A, resi 143-148 & chain A, resi 133-137 & chain A, resi 127-130 & chain A, resi 121-123 & chain A, resi 172-174 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[8.600038456229063,28.411942271085884,17.118394267100555])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 225-235 & chain A, resi 240-248 & chain A, resi 253-261 & chain A, resi 267-270 & chain A, resi 338-348 & chain A, resi 325-335 & chain A, resi 303-309 & chain A, resi 291-300 & chain A, resi 275-284 & chain A, resi 315-317 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[13.228500046702319,10.829011657903362,11.334872056578481])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
