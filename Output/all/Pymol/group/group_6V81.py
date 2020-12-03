from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6V81.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 47-51 & chain A, resi 130-137 & chain A, resi 150-156 & chain A, resi 105-108 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[19.578083475430805,26.975374778111775,26.084166606267292])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 74-77 & chain A, resi 87-90 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[12.044249892234802,21.351500034332275,16.86537516117096])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 164-172 & chain A, resi 176-186 & chain A, resi 196-207 & chain A, resi 216-228 & chain A, resi 234-247 & chain A, resi 273-288 & chain A, resi 293-309 & chain A, resi 326-342 & chain A, resi 350-368 & chain A, resi 386-408 & chain A, resi 411-428 & chain A, resi 440-456 & chain A, resi 461-468 & chain A, resi 500-509 & chain A, resi 512-523 & chain A, resi 545-558 & chain A, resi 562-575 & chain A, resi 596-604 & chain A, resi 611-619 & chain A, resi 635-648 & chain A, resi 651-660 & chain A, resi 688-698 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[20.786989886150618,23.49071721807875,24.326249157213404])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 527-533 & chain A, resi 536-541 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[22.090923309326172,16.65615408237164,-5.877769231796265])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 667-671 & chain A, resi 681-684 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[4.833333326710595,9.395777702331543,13.757777637905544])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
