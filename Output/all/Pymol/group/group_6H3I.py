from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H3I.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 72-78 & chain F, resi 88-98 & chain F, resi 104-116 & chain F, resi 139-146 & chain F, resi 152-162 & chain F, resi 178-189 & chain F, resi 201-208 & chain F, resi 231-240 & chain F, resi 246-254 & chain F, resi 323-328 & chain F, resi 336-344 & chain F, resi 357-362 & chain F, resi 367-372 & chain F, resi 389-394 & chain F, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[148.54215603187436,150.92397533479283,147.88906447613826])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
