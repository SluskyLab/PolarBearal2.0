from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3JTY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 38-52 & chain A, resi 61-74 & chain A, resi 82-97 & chain A, resi 119-131 & chain A, resi 134-141 & chain A, resi 159-167 & chain A, resi 173-184 & chain A, resi 207-216 & chain A, resi 221-230 & chain A, resi 234-247 & chain A, resi 250-263 & chain A, resi 273-285 & chain A, resi 288-299 & chain A, resi 329-338 & chain A, resi 347-359 & chain A, resi 367-379 & chain A, resi 389-399 & chain A, resi 406-418 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[14.844263646497645,28.354486352747138,5.626472694765438])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 194-196 & chain A, resi 199-204 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[29.43566640218099,37.345556047227646,-6.2308888170454235])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
