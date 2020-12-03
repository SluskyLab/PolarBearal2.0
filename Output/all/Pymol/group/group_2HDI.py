from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HDI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 50-54 & chain A, resi 130-137 & chain A, resi 151-157 & chain A, resi 99-103 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[28.94447998046875,-22.12604019165039,13.439479999542236])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 77-81 & chain A, resi 87-91 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[41.32779998779297,-14.224100017547608,7.9246000289917])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 165-175 & chain A, resi 183-195 & chain A, resi 199-210 & chain A, resi 231-243 & chain A, resi 249-263 & chain A, resi 271-284 & chain A, resi 289-302 & chain A, resi 310-325 & chain A, resi 330-344 & chain A, resi 357-373 & chain A, resi 376-387 & chain A, resi 391-403 & chain A, resi 408-419 & chain A, resi 450-462 & chain A, resi 472-487 & chain A, resi 514-538 & chain A, resi 439-442 & chain A, resi 431-434 & chain A, resi 503-508 & chain A, resi 543-556 & chain A, resi 563-579 & chain A, resi 587-596 & chain A, resi 612-624 & chain A, resi 627-634 & chain A, resi 654-662 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[31.159265571087598,-18.140346896089614,15.343337496297318])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
