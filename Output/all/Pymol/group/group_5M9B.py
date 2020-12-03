from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5M9B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 30-34 & chain A, resi 121-128 & chain A, resi 142-148 & chain A, resi 84-88 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[83.08107971191406,53.35775985717773,46.097000427246094])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 57-60 & chain A, resi 73-76 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[87.22387409210205,57.937625885009766,57.76212453842163])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 156-166 & chain A, resi 174-186 & chain A, resi 189-200 & chain A, resi 229-242 & chain A, resi 247-261 & chain A, resi 284-298 & chain A, resi 303-318 & chain A, resi 337-355 & chain A, resi 361-375 & chain A, resi 401-418 & chain A, resi 421-432 & chain A, resi 436-450 & chain A, resi 453-464 & chain A, resi 502-515 & chain A, resi 518-535 & chain A, resi 554-576 & chain A, resi 491-494 & chain A, resi 476-479 & chain A, resi 581-595 & chain A, resi 608-616 & chain A, resi 622-631 & chain A, resi 657-669 & chain A, resi 672-679 & chain A, resi 712-720 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[82.31022931967571,51.957464971360125,49.2429904512539])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
