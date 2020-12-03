from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FOK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 52-55 & chain A, resi 122-128 & chain A, resi 144-149 & chain A, resi 104-106 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[30.082950019836424,-21.468800163269044,4.571050031483173])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 78-81 & chain A, resi 92-95 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[20.78125,-10.639250040054321,5.155750006437302])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 323-350 & chain A, resi 395-397 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[33.814096696915165,-6.686451456239147,2.3093548965069557])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 373-376 & chain A, resi 410-413 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[30.89400005340576,13.798500061035156,-12.725375175476074])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 693-696 & chain A, resi 701-704 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[13.660000205039978,-5.16162496805191,-3.3313750326633453])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 52-55 & chain B, resi 122-131 & chain B, resi 142-149 & chain B, resi 104-106 & chain B, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[25.362960205078124,43.67651992797852,19.01048002243042])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 78-81 & chain B, resi 92-95 & chain B, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[17.52275002002716,33.02550029754639,18.985124826431274])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 323-350 & chain B, resi 395-397 & chain B, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[29.761838862972876,29.810451599859423,24.079064736443183])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 373-376 & chain B, resi 410-413 & chain B, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[25.171374797821045,8.760625004768372,37.7776255607605])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 693-696 & chain B, resi 701-704 & chain B, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[8.99462515115738,27.16950035095215,25.844124794006348])
cmd.color ("red", "Centroid9")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
