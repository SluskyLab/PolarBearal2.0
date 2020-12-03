from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FVN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-6 & chain A, resi 9-23 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[34.480545564131305,-9.496181902560322,43.062727668068625])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 2-6 & chain B, resi 9-24 & chain B, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[19.952809560866584,-15.071285835689022,41.06904720124744])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 2-6 & chain C, resi 9-23 & chain C, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[22.92454993724823,1.8502999782562255,42.14575004577637])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 2-6 & chain D, resi 9-24 & chain D, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[15.282333242041725,-6.952333370844523,74.79171462286087])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 2-6 & chain E, resi 9-24 & chain E, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[30.579095386323473,-15.717904725245067,75.03914315359933])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 2-6 & chain F, resi 9-24 & chain F, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[30.51342855181013,1.936285715727579,74.96671513148716])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
