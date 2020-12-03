from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H7F.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 43-45 & chain A, resi 51-53 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-37.30757195608957,42.17485754830496,12.043999944414411])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 61-65 & chain A, resi 132-139 & chain A, resi 156-162 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-45.18969993591308,36.37469997406006,10.125900003314019])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 170-178 & chain A, resi 181-193 & chain A, resi 199-211 & chain A, resi 218-231 & chain A, resi 235-249 & chain A, resi 279-296 & chain A, resi 299-322 & chain A, resi 328-355 & chain A, resi 358-378 & chain A, resi 388-391 & chain A, resi 409-428 & chain A, resi 433-448 & chain A, resi 458-470 & chain A, resi 475-486 & chain A, resi 505-517 & chain A, resi 521-543 & chain A, resi 546-550 & chain A, resi 553-566 & chain A, resi 572-587 & chain A, resi 604-615 & chain A, resi 619-630 & chain A, resi 646-659 & chain A, resi 662-671 & chain A, resi 694-702 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-51.439052927128785,36.7964790896785,8.403036232653767])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
