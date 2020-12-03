from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AIP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 67-72 & chain A, resi 144-151 & chain A, resi 165-171 & chain A, resi 118-121 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-20.4560799407959,-0.02848003387451172,-24.01748001098633])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 95-97 & chain A, resi 107-109 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-28.496166865030926,-4.494833310445149,-33.511500676472984])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 185-194 & chain A, resi 198-209 & chain A, resi 212-223 & chain A, resi 246-259 & chain A, resi 264-279 & chain A, resi 302-318 & chain A, resi 323-339 & chain A, resi 355-373 & chain A, resi 376-390 & chain A, resi 438-452 & chain A, resi 455-469 & chain A, resi 475-492 & chain A, resi 495-506 & chain A, resi 532-544 & chain A, resi 548-560 & chain A, resi 582-597 & chain A, resi 600-609 & chain A, resi 635-644 & chain A, resi 648-658 & chain A, resi 685-695 & chain A, resi 702-709 & chain A, resi 733-741 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-21.586853224669706,1.286791791586339,-23.80378487258641])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 522-525 & chain A, resi 575-578 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[-54.50762462615967,4.807500027120113,-22.42925000190735])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
