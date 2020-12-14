from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4D65.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-6 & chain A, resi 9-24 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[22.19123815354847,42.44161860148112,24.48852384658087])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 2-6 & chain B, resi 9-23 & chain B, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[39.04375019073486,44.43625030517578,15.968649919331074])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 2-6 & chain C, resi 9-23 & chain C, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[37.821600151062015,44.60199995040894,33.9263500213623])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 2-6 & chain D, resi 9-23 & chain D, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[48.75414981842041,-36.74315013885498,25.042949962615968])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 2-6 & chain E, resi 9-24 & chain E, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[32.6350477309454,-36.89419074285598,16.20057134117399])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 2-6 & chain F, resi 9-23 & chain F, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[33.899999952316286,-37.58895015716553,35.156950283050534])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
