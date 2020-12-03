from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5T3R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 212-224 & chain D, resi 303-315 & chain D, resi 319-331 & chain D, resi 339-353 & chain D, resi 357-371 & chain D, resi 421-435 & chain D, resi 441-460 & chain D, resi 475-494 & chain D, resi 502-524 & chain D, resi 543-564 & chain D, resi 569-580 & chain D, resi 591-599 & chain D, resi 620-627 & chain D, resi 686-693 & chain D, resi 704-716 & chain D, resi 696-698 & chain D, resi 740-754 & chain D, resi 761-777 & chain D, resi 859-869 & chain D, resi 872-882 & chain D, resi 948-959 & chain D, resi 972-980 & chain D, resi 984-986 & chain D, resi 1006-1015 & chain D, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[10.49156776822863,392.1922129969443,152.86683246243385])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 260-265 & chain D, resi 271-277 & chain D, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[54.811846219576324,392.56007502629205,110.82630861722507])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 719-723 & chain D, resi 733-737 & chain D, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[3.275799995660782,377.80260314941404,128.45680084228516])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 804-806 & chain D, resi 850-853 & chain D, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[25.636999947684153,368.0689958844866,128.3154285975865])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 809-812 & chain D, resi 833-835 & chain D, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[39.18442862374442,369.3452933175223,120.9020004272461])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 885-887 & chain D, resi 943-945 & chain D, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[31.2624994913737,375.8885040283203,134.31683349609375])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
