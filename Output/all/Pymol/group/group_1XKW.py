from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XKW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 82-87 & chain A, resi 153-160 & chain A, resi 174-180 & chain A, resi 130-133 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[9.900440063476562,8.237760045900941,51.121520080566405])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 109-115 & chain A, resi 118-123 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-2.270769252226903,5.631769296068412,60.86099976759691])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 188-196 & chain A, resi 200-210 & chain A, resi 217-229 & chain A, resi 236-251 & chain A, resi 254-268 & chain A, resi 297-314 & chain A, resi 317-338 & chain A, resi 349-375 & chain A, resi 378-398 & chain A, resi 432-448 & chain A, resi 451-465 & chain A, resi 476-488 & chain A, resi 491-502 & chain A, resi 518-531 & chain A, resi 536-553 & chain A, resi 566-586 & chain A, resi 589-604 & chain A, resi 621-630 & chain A, resi 638-647 & chain A, resi 664-674 & chain A, resi 679-686 & chain A, resi 711-719 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[8.56891718159424,9.49594171462792,53.433009282211586])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 650-654 & chain A, resi 657-661 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[-11.133200120925903,-5.25299996137619,68.99900016784667])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 694-696 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[-11.429333368937174,0.8223333557446798,59.92033259073893])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
