from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3NSG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 13-24 & chain A, resi 36-45 & chain A, resi 52-62 & chain A, resi 74-85 & chain A, resi 89-97 & chain A, resi 130-139 & chain A, resi 149-156 & chain A, resi 172-181 & chain A, resi 184-193 & chain A, resi 209-220 & chain A, resi 223-232 & chain A, resi 251-261 & chain A, resi 269-279 & chain A, resi 288-300 & chain A, resi 306-315 & chain A, resi 332-340 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-27.449660783722287,-12.507351261607948,8.863250024333995])
cmd.color ("white", "Centroid0")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
