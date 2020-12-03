from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FID.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-9 & chain A, resi 33-44 & chain A, resi 49-60 & chain A, resi 80-94 & chain A, resi 97-108 & chain A, resi 140-151 & chain A, resi 160-173 & chain A, resi 154-157 & chain A, resi 176-188 & chain A, resi 215-231 & chain A, resi 251-263 & chain A, resi 266-275 & chain A, resi 285-295 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[36.44177116443908,19.65194115295909,9.939895424870105])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
