from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1TLY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 13-23 & chain A, resi 35-45 & chain A, resi 48-57 & chain A, resi 77-85 & chain A, resi 99-111 & chain A, resi 120-131 & chain A, resi 138-151 & chain A, resi 159-176 & chain A, resi 179-191 & chain A, resi 213-223 & chain A, resi 227-237 & chain A, resi 261-272 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-14.889241368195107,82.8482827548323,-0.6257172060423883])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 247-249 & chain A, resi 254-256 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-24.804833094278973,112.40633138020833,-0.7321666379769644])
cmd.color ("red", "Centroid1")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
