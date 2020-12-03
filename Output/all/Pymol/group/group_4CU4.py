from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4CU4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 50-54 & chain A, resi 126-133 & chain A, resi 147-153 & chain A, resi 104-106 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-16.550708254178364,-46.42312510808309,4.869916623458266])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 161-169 & chain A, resi 173-183 & chain A, resi 190-202 & chain A, resi 209-224 & chain A, resi 227-238 & chain A, resi 274-289 & chain A, resi 294-317 & chain A, resi 340-367 & chain A, resi 370-401 & chain A, resi 431-453 & chain A, resi 456-473 & chain A, resi 478-495 & chain A, resi 501-512 & chain A, resi 527-538 & chain A, resi 545-562 & chain A, resi 570-588 & chain A, resi 593-608 & chain A, resi 623-633 & chain A, resi 641-650 & chain A, resi 666-676 & chain A, resi 686-692 & chain A, resi 716-724 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-15.201271737220488,-40.04941911780076,5.132242781922996])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 700-705 & chain A, resi 708-711 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-24.734300231933595,-24.44689998626709,-7.428499937057495])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
