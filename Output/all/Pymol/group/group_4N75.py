from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4N75.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 427-433 & chain A, resi 437-446 & chain A, resi 455-462 & chain A, resi 466-475 & chain A, resi 484-495 & chain A, resi 505-520 & chain A, resi 523-537 & chain A, resi 564-579 & chain A, resi 590-600 & chain A, resi 608-620 & chain A, resi 628-640 & chain A, resi 710-720 & chain A, resi 733-745 & chain A, resi 767-778 & chain A, resi 781-792 & chain A, resi 799-809 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[37.582868535895095,59.59273677625154,23.60999478776204])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
