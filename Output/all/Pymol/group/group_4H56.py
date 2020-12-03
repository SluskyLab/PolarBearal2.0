from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H56.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 27-35 & chain A, resi 42-50 & chain A, resi 57-63 & chain A, resi 227-233 & chain A, resi 102-107 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[73.33984214381168,-17.389000014254922,-45.61452624672338])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 72-75 & chain A, resi 79-96 & chain A, resi 168-175 & chain A, resi 136-164 & chain A, resi 114-132 & chain A, resi 239-258 & chain A, resi 261-266 & chain A, resi 272-282 & chain A, resi 287-290 & chain A, resi 136-164 & chain B, resi 114-132 & chain B, resi 168-175 & chain B, resi 79-96 & chain B, resi 72-75 & chain B, resi 239-258 & chain B, resi 261-266 & chain B, resi 272-282 & chain B, resi 287-290 & chain B, resi 136-164 & chain C, resi 114-132 & chain C, resi 168-175 & chain C, resi 79-96 & chain C, resi 72-75 & chain C, resi 239-258 & chain C, resi 261-266 & chain C, resi 272-282 & chain C, resi 287-290 & chain C, resi 136-164 & chain D, resi 114-132 & chain D, resi 168-175 & chain D, resi 79-96 & chain D, resi 72-75 & chain D, resi 239-258 & chain D, resi 261-266 & chain D, resi 272-282 & chain D, resi 287-290 & chain D, resi 136-164 & chain E, resi 114-132 & chain E, resi 168-175 & chain E, resi 79-96 & chain E, resi 72-75 & chain E, resi 239-258 & chain E, resi 261-266 & chain E, resi 272-282 & chain E, resi 287-290 & chain E, resi 136-164 & chain F, resi 114-132 & chain F, resi 168-175 & chain F, resi 79-96 & chain F, resi 72-75 & chain F, resi 239-258 & chain F, resi 261-266 & chain F, resi 272-282 & chain F, resi 287-290 & chain F, resi 114-132 & chain G, resi 136-164 & chain G, resi 168-175 & chain G, resi 79-96 & chain G, resi 72-75 & chain G, resi 239-258 & chain G, resi 261-266 & chain G, resi 272-282 & chain G, resi 287-290 & chain G, resi 272-282 & chain N, resi 239-258 & chain N, resi 79-96 & chain N, resi 72-75 & chain N, resi 168-175 & chain N, resi 136-164 & chain N, resi 114-132 & chain M, resi 136-164 & chain M, resi 114-132 & chain L, resi 136-164 & chain L, resi 114-132 & chain K, resi 136-164 & chain K, resi 114-132 & chain J, resi 136-164 & chain J, resi 114-132 & chain I, resi 136-164 & chain I, resi 114-132 & chain H, resi 136-164 & chain H, resi 168-175 & chain H, resi 79-96 & chain H, resi 72-75 & chain H, resi 239-258 & chain H, resi 261-266 & chain H, resi 272-282 & chain H, resi 287-290 & chain H, resi 168-175 & chain I, resi 79-96 & chain I, resi 72-75 & chain I, resi 239-258 & chain I, resi 261-266 & chain I, resi 272-282 & chain I, resi 287-290 & chain I, resi 168-175 & chain J, resi 79-96 & chain J, resi 72-75 & chain J, resi 239-258 & chain J, resi 261-266 & chain J, resi 272-282 & chain J, resi 287-290 & chain J, resi 168-175 & chain K, resi 79-96 & chain K, resi 72-75 & chain K, resi 239-258 & chain K, resi 261-266 & chain K, resi 272-282 & chain K, resi 287-290 & chain K, resi 168-175 & chain L, resi 79-96 & chain L, resi 72-75 & chain L, resi 239-258 & chain L, resi 261-266 & chain L, resi 272-282 & chain L, resi 287-290 & chain L, resi 168-175 & chain M, resi 79-96 & chain M, resi 72-75 & chain M, resi 239-258 & chain M, resi 261-266 & chain M, resi 272-282 & chain M, resi 287-290 & chain M, resi 114-132 & chain N, resi 261-266 & chain N, resi 287-290 & chain N, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[63.48573955796918,-30.33658642815996,-71.51589017223158])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 27-35 & chain B, resi 42-50 & chain B, resi 57-63 & chain B, resi 227-233 & chain B, resi 102-107 & chain B, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[91.54194761577405,-30.164499985544307,-48.33997395164088])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 27-35 & chain C, resi 42-50 & chain C, resi 57-63 & chain C, resi 227-233 & chain C, resi 102-107 & chain C, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[101.5642109921104,-43.793131828308105,-33.62865809390419])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 27-35 & chain D, resi 42-50 & chain D, resi 57-63 & chain D, resi 227-233 & chain D, resi 102-107 & chain D, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[95.84628978528474,-48.1228420859889,-12.392078898454967])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 27-35 & chain E, resi 42-50 & chain E, resi 57-63 & chain E, resi 227-233 & chain E, resi 102-107 & chain E, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[78.7403947930587,-39.56902619412071,-0.7807105213011566])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 27-35 & chain F, resi 42-50 & chain F, resi 57-63 & chain F, resi 227-233 & chain F, resi 102-107 & chain F, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[63.19307919552452,-24.908078946565325,-7.481526329721275])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 27-35 & chain G, resi 42-50 & chain G, resi 57-63 & chain G, resi 227-233 & chain G, resi 102-107 & chain G, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[60.59289480510511,-14.969657985787643,-27.464736938476562])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 27-35 & chain H, resi 42-50 & chain H, resi 57-63 & chain H, resi 227-233 & chain H, resi 102-107 & chain H, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[95.34621168437756,-28.33773678227475,-96.85971049258583])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 27-35 & chain I, resi 42-50 & chain I, resi 57-63 & chain I, resi 227-233 & chain I, resi 102-107 & chain I, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[102.41960525512695,-16.236736862283003,-114.29844705682052])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 27-35 & chain J, resi 42-50 & chain J, resi 57-63 & chain J, resi 227-233 & chain J, resi 102-107 & chain J, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[93.46310545268811,-13.99744737148285,-134.70126222309312])
cmd.color ("orange", "Centroid10")


cmd.select("Group11", "(resi 27-35 & chain K, resi 42-50 & chain K, resi 57-63 & chain K, resi 227-233 & chain K, resi 102-107 & chain K, )")
cmd.color ("yellow", "Group11")


cmd.pseudoatom ("Centroid11", pos=[75.33834216469212,-23.874342090205143,-142.69842047440378])
cmd.color ("yellow", "Centroid11")


cmd.select("Group12", "(resi 27-35 & chain L, resi 42-50 & chain L, resi 57-63 & chain L, resi 227-233 & chain L, resi 102-107 & chain L, )")
cmd.color ("green", "Group12")


cmd.pseudoatom ("Centroid12", pos=[61.72607903731497,-38.23860489694696,-132.4227365192614])
cmd.color ("green", "Centroid12")


cmd.select("Group13", "(resi 27-35 & chain M, resi 42-50 & chain M, resi 57-63 & chain M, resi 227-233 & chain M, resi 102-107 & chain M, )")
cmd.color ("cyan", "Group13")


cmd.pseudoatom ("Centroid13", pos=[62.62881590190687,-46.20273710552015,-111.4554473475406])
cmd.color ("cyan", "Centroid13")


cmd.select("Group14", "(resi 27-35 & chain N, resi 42-50 & chain N, resi 57-63 & chain N, resi 227-233 & chain N, resi 102-107 & chain N, )")
cmd.color ("blue", "Group14")


cmd.pseudoatom ("Centroid14", pos=[77.57599991246273,-41.68692137065687,-95.61157889115184])
cmd.color ("blue", "Centroid14")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
