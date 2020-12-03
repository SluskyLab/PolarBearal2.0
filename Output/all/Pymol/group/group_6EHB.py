from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 12-16 & chain A, resi 20-35 & chain A, resi 38-41 & chain A, resi 44-56 & chain A, resi 59-69 & chain A, resi 83-94 & chain A, resi 97-103 & chain A, resi 138-145 & chain A, resi 148-155 & chain A, resi 184-192 & chain A, resi 198-207 & chain A, resi 210-220 & chain A, resi 224-236 & chain A, resi 239-252 & chain A, resi 255-266 & chain A, resi 269-284 & chain A, resi 287-296 & chain A, resi 311-319 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-12.588724828980586,72.81711657085116,66.22062959620561])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 159-162 & chain A, resi 176-179 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[19.199750065803528,64.93287372589111,73.24312496185303])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
