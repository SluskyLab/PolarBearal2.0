from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 14-28 & chain A, resi 37-48 & chain A, resi 56-69 & chain A, resi 100-112 & chain A, resi 115-122 & chain A, resi 141-148 & chain A, resi 154-163 & chain A, resi 189-201 & chain A, resi 204-213 & chain A, resi 217-229 & chain A, resi 234-247 & chain A, resi 257-269 & chain A, resi 272-282 & chain A, resi 313-322 & chain A, resi 331-341 & chain A, resi 366-377 & chain A, resi 387-398 & chain A, resi 408-421 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-14.75860096801055,-28.32378403345744,-6.283032879373278])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
