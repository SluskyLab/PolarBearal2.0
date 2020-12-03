from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4C00.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 26-29 & chain A, resi 94-99 & chain A, resi 78-82 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-14.06993325551351,16.36133321126302,-7.761200046539306])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 105-114 & chain A, resi 176-184 & chain A, resi 162-171 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[8.342689643646109,6.696931086737534,18.182207008887982])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 193-197 & chain A, resi 256-262 & chain A, resi 236-243 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[40.44835033416748,32.641249656677246,14.208150148391724])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 267-276 & chain A, resi 280-288 & chain A, resi 297-305 & chain A, resi 308-318 & chain A, resi 326-339 & chain A, resi 342-357 & chain A, resi 361-376 & chain A, resi 379-398 & chain A, resi 404-416 & chain A, resi 426-439 & chain A, resi 442-456 & chain A, resi 497-511 & chain A, resi 514-526 & chain A, resi 535-546 & chain A, resi 549-558 & chain A, resi 568-573 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[25.66674159702502,66.04940668133457,13.310765571321882])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
