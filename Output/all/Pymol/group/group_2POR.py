from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2POR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 2-15 & chain A, resi 18-35 & chain A, resi 39-46 & chain A, resi 59-65 & chain A, resi 68-74 & chain A, resi 118-125 & chain A, resi 128-135 & chain A, resi 148-158 & chain A, resi 161-171 & chain A, resi 181-192 & chain A, resi 195-206 & chain A, resi 227-240 & chain A, resi 243-254 & chain A, resi 258-271 & chain A, resi 275-285 & chain A, resi 292-300 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[3.005789735185152,-24.72585788640109,20.963943180712786])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
