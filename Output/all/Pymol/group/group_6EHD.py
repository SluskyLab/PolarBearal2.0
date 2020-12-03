from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-6 & chain A, resi 9-24 & chain A, resi 37-47 & chain A, resi 50-59 & chain A, resi 67-77 & chain A, resi 80-88 & chain A, resi 117-128 & chain A, resi 131-138 & chain A, resi 147-157 & chain A, resi 160-181 & chain A, resi 184-205 & chain A, resi 208-221 & chain A, resi 227-242 & chain A, resi 245-258 & chain A, resi 263-278 & chain A, resi 281-299 & chain A, resi 304-324 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[42.2886749079198,-0.5424979583747348,16.894333352890524])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
