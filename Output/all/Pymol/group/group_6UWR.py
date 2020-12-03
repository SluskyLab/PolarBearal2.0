from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 235-237 & chain H, resi 242-244 & chain H, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[247.15066782633463,223.4885025024414,105.59400049845378])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 300-310 & chain H, resi 322-330 & chain H, resi 362-367 & chain H, resi 387-397 & chain H, resi 460-462 & chain H, resi 477-486 & chain H, resi 404-413 & chain H, resi 418-423 & chain H, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[241.25375689882222,219.71048574736625,150.5899544918176])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 351-354 & chain H, resi 577-581 & chain H, resi 610-614 & chain H, resi 514-519 & chain H, resi 526-531 & chain H, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[257.3050771859976,214.9229231614333,133.0871913616474])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 618-620 & chain H, resi 732-743 & chain H, resi 667-676 & chain H, resi 709-712 & chain H, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[271.4572764429553,224.53893043254985,142.0267939074286])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 684-689 & chain H, resi 694-698 & chain H, resi 721-727 & chain H, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[281.891108194987,225.50194464789496,147.99911075168185])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 768-773 & chain H, resi 782-788 & chain H, resi 836-841 & chain H, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[246.07200140702096,214.2372637296978,209.76905260587992])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 802-809 & chain H, resi 815-820 & chain H, resi 859-863 & chain H, resi 869-874 & chain H, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[255.83152099609376,207.34828063964844,204.251162109375])
cmd.color ("cyan", "Centroid6")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
