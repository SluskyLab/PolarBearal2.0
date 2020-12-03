from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1KMO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 104-108 & chain A, resi 189-195 & chain A, resi 211-216 & chain A, resi 161-164 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[27.623909083279695,3.537999955767935,26.19322733445601])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 224-233 & chain A, resi 243-253 & chain A, resi 258-269 & chain A, resi 278-289 & chain A, resi 295-309 & chain A, resi 332-346 & chain A, resi 352-371 & chain A, resi 374-377 & chain A, resi 380-397 & chain A, resi 400-423 & chain A, resi 436-457 & chain A, resi 460-477 & chain A, resi 483-502 & chain A, resi 505-516 & chain A, resi 535-547 & chain A, resi 551-565 & chain A, resi 579-593 & chain A, resi 604-617 & chain A, resi 634-642 & chain A, resi 647-656 & chain A, resi 681-691 & chain A, resi 700-706 & chain A, resi 732-740 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[28.559838620922232,2.3961202907788604,21.499987336653696])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 714-717 & chain A, resi 724-727 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[13.820249915122986,14.88462495803833,4.8230000250041485])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
