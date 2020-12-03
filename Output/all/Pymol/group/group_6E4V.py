from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6E4V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 81-85 & chain A, resi 155-162 & chain A, resi 176-182 & chain A, resi 129-132 & chain A, resi 135-138 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[7.824678525328636,14.464535798345294,31.3643570627485])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 109-114 & chain A, resi 117-122 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[20.37499984105428,14.231833140055338,20.51075013478597])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 191-199 & chain A, resi 203-213 & chain A, resi 220-232 & chain A, resi 239-253 & chain A, resi 257-271 & chain A, resi 302-319 & chain A, resi 322-342 & chain A, resi 368-392 & chain A, resi 395-419 & chain A, resi 443-464 & chain A, resi 467-481 & chain A, resi 486-501 & chain A, resi 506-517 & chain A, resi 532-545 & chain A, resi 550-571 & chain A, resi 579-584 & chain A, resi 588-601 & chain A, resi 604-616 & chain A, resi 630-639 & chain A, resi 646-655 & chain A, resi 676-686 & chain A, resi 691-698 & chain A, resi 720-728 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[9.914652678212095,13.29209875221738,30.91084733123551])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 658-664 & chain A, resi 667-673 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[33.0059997013637,23.163071496146067,10.613071373530797])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
