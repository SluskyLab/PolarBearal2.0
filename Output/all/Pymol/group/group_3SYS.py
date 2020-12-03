from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYS.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 10-23 & chain A, resi 34-46 & chain A, resi 55-68 & chain A, resi 91-103 & chain A, resi 106-113 & chain A, resi 131-139 & chain A, resi 145-156 & chain A, resi 179-188 & chain A, resi 193-202 & chain A, resi 206-219 & chain A, resi 222-235 & chain A, resi 245-257 & chain A, resi 260-271 & chain A, resi 301-310 & chain A, resi 319-331 & chain A, resi 339-351 & chain A, resi 361-371 & chain A, resi 377-389 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-19.8229174291322,18.604256822975405,-10.281293552334702])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 166-168 & chain A, resi 171-176 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-29.475555631849502,1.1251110641492739,-14.522999975416395])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
