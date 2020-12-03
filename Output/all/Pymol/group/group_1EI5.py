from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EI5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 24-31 & chain A, resi 34-45 & chain A, resi 306-312 & chain A, resi 294-301 & chain A, resi 282-291 & chain A, resi 274-279 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[36.782902025708964,1.929882356933519,-5.919647018699085])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 205-208 & chain A, resi 212-215 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[27.666750192642212,21.50724983215332,-4.45024998486042])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 228-230 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[46.528666178385414,11.304333368937174,-2.0346666971842446])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 348-351 & chain A, resi 358-363 & chain A, resi 368-372 & chain A, resi 378-384 & chain A, resi 387-389 & chain A, resi 394-398 & chain A, resi 401-406 & chain A, resi 411-417 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[14.166186011114785,0.8330464955679205,15.518186048019764])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 428-432 & chain A, resi 437-444 & chain A, resi 447-454 & chain A, resi 462-468 & chain A, resi 471-476 & chain A, resi 486-494 & chain A, resi 500-507 & chain A, resi 510-517 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[22.691982964337882,20.275440636327712,24.828237404257564])
cmd.color ("yellow", "Centroid4")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
