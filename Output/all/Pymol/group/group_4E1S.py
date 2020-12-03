from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 212-219 & chain A, resi 225-236 & chain A, resi 240-251 & chain A, resi 254-266 & chain A, resi 271-281 & chain A, resi 286-297 & chain A, resi 300-309 & chain A, resi 329-338 & chain A, resi 341-353 & chain A, resi 371-382 & chain A, resi 385-394 & chain A, resi 398-410 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-29.523384507719452,-15.205251700394637,7.774566469596816])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 323-326 & chain A, resi 446-448 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-50.604000091552734,-11.614714077540807,0.34442855630602154])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
