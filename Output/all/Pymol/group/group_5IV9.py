from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IV9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 29-31 & chain A, resi 42-53 & chain A, resi 34-36 & chain A, resi 56-66 & chain A, resi 79-89 & chain A, resi 93-103 & chain A, resi 108-118 & chain A, resi 124-133 & chain A, resi 138-147 & chain A, resi 157-166 & chain A, resi 171-180 & chain A, resi 185-195 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[99.90169903240373,54.8032388265154,13.662150486116916])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 208-212 & chain A, resi 216-220 & chain A, resi 231-240 & chain A, resi 223-228 & chain A, resi 245-256 & chain A, resi 259-268 & chain A, resi 286-297 & chain A, resi 301-310 & chain A, resi 330-340 & chain A, resi 344-355 & chain A, resi 364-379 & chain A, resi 382-395 & chain A, resi 402-417 & chain A, resi 421-437 & chain A, resi 453-472 & chain A, resi 478-489 & chain A, resi 529-540 & chain A, resi 546-557 & chain A, resi 577-587 & chain A, resi 595-602 & chain A, resi 607-617 & chain A, resi 625-632 & chain A, resi 654-661 & chain A, resi 672-678 & chain A, resi 684-694 & chain A, resi 699-712 & chain A, resi 719-731 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[147.56769959603992,28.933168312897383,40.31674590913376])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
