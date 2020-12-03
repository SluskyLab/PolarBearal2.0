from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4QKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 63-67 & chain A, resi 126-132 & chain A, resi 114-123 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[15.936863595789129,-3.5016363357955758,27.959136442704633])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 135-141 & chain A, resi 198-207 & chain A, resi 184-192 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[5.115461528301239,13.257999961192791,2.5297692492604256])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 212-218 & chain A, resi 227-239 & chain A, resi 247-257 & chain A, resi 264-276 & chain A, resi 279-292 & chain A, resi 303-320 & chain A, resi 324-340 & chain A, resi 355-365 & chain A, resi 369-379 & chain A, resi 402-415 & chain A, resi 418-430 & chain A, resi 458-471 & chain A, resi 441-443 & chain A, resi 488-498 & chain A, resi 504-519 & chain A, resi 522-531 & chain A, resi 546-553 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[31.053347947550755,34.883254831912474,-7.818656886471253])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
