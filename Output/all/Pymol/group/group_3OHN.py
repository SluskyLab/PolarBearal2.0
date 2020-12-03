from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3OHN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 141-153 & chain A, resi 159-171 & chain A, resi 176-187 & chain A, resi 197-209 & chain A, resi 214-222 & chain A, resi 232-239 & chain A, resi 329-339 & chain A, resi 349-358 & chain A, resi 364-372 & chain A, resi 375-387 & chain A, resi 390-402 & chain A, resi 408-420 & chain A, resi 430-437 & chain A, resi 480-492 & chain A, resi 496-507 & chain A, resi 513-524 & chain A, resi 529-538 & chain A, resi 545-556 & chain A, resi 575-583 & chain A, resi 586-597 & chain A, resi 602-611 & chain A, resi 619-628 & chain A, resi 633-641 & chain A, resi 645-655 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[19.461520713511504,29.93701132648396,43.42296230388138])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 257-260 & chain A, resi 283-286 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[19.355499982833862,39.29299974441528,52.89324998855591])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 264-270 & chain A, resi 273-280 & chain A, resi 299-305 & chain A, resi 310-315 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[11.63692855834961,31.685106890542166,48.58885669708252])
cmd.color ("orange", "Centroid2")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
