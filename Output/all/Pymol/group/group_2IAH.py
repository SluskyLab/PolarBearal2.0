from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2IAH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 46-50 & chain A, resi 85-89 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-24.37739963531494,44.21879997253418,184.69109954833985])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 69-72 & chain A, resi 112-116 & chain A, resi 105-109 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-20.03349985395159,49.599643162318635,167.45399802071708])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 168-173 & chain A, resi 243-251 & chain A, resi 263-270 & chain A, resi 217-219 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-9.368961531382341,35.214884537916916,138.80776977539062])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 196-201 & chain A, resi 204-209 & chain A, resi 790-792 & chain A, resi 798-801 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[-6.716473708027287,25.703473542865954,121.18389571340461])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 278-286 & chain A, resi 290-300 & chain A, resi 307-319 & chain A, resi 326-341 & chain A, resi 344-358 & chain A, resi 392-405 & chain A, resi 411-430 & chain A, resi 441-466 & chain A, resi 471-490 & chain A, resi 520-537 & chain A, resi 543-558 & chain A, resi 563-578 & chain A, resi 583-594 & chain A, resi 611-624 & chain A, resi 629-645 & chain A, resi 664-682 & chain A, resi 685-693 & chain A, resi 711-720 & chain A, resi 728-737 & chain A, resi 760-770 & chain A, resi 776-782 & chain A, resi 806-812 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[-6.929693528661324,37.25677090306436,136.32475485032606])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 740-746 & chain A, resi 751-757 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[-15.960142748696464,20.737571511949813,109.74057115827289])
cmd.color ("green", "Centroid5")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
