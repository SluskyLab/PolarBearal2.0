from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ZGV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 68-72 & chain A, resi 175-181 & chain A, resi 196-201 & chain A, resi 127-130 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[25.526636470447887,25.231318127025258,42.41059095209295])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 96-98 & chain A, resi 116-118 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[39.039333979288735,29.25949986775716,48.0434996287028])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 211-219 & chain A, resi 248-259 & chain A, resi 264-281 & chain A, resi 286-304 & chain A, resi 310-317 & chain A, resi 320-325 & chain A, resi 333-348 & chain A, resi 354-371 & chain A, resi 411-427 & chain A, resi 436-454 & chain A, resi 500-518 & chain A, resi 522-533 & chain A, resi 538-550 & chain A, resi 557-567 & chain A, resi 615-626 & chain A, resi 630-642 & chain A, resi 666-677 & chain A, resi 687-701 & chain A, resi 738-748 & chain A, resi 753-762 & chain A, resi 805-817 & chain A, resi 823-830 & chain A, resi 859-866 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[28.564167213280463,22.44917383316568,44.18588635116118])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 376-382 & chain A, resi 402-407 & chain A, resi 458-461 & chain A, resi 493-497 & chain A, resi 583-587 & chain A, resi 599-601 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[53.584132766723634,-8.186599955459435,64.69956652323405])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 646-652 & chain A, resi 655-661 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[43.1110714503697,17.33121429170881,75.24199948992047])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 766-770 & chain A, resi 797-801 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[60.461499786376955,31.860500144958497,52.2569995880127])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 775-777 & chain A, resi 792-794 & chain A, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[66.39900080362956,31.42300001780192,70.28400039672852])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 839-843 & chain A, resi 850-853 & chain A, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[56.84855482313368,24.556889004177517,45.4945560031467])
cmd.color ("blue", "Centroid7")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
