from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3C.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 318-321 & chain A, resi 336-339 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[0.08137502695899457,4.283499993383884,-116.2698745727539])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 345-352 & chain A, resi 408-417 & chain A, resi 392-397 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[5.868875039120515,26.11704166730245,-98.24166647593181])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 421-430 & chain A, resi 434-446 & chain A, resi 451-459 & chain A, resi 463-475 & chain A, resi 481-492 & chain A, resi 503-515 & chain A, resi 521-535 & chain A, resi 564-566 & chain A, resi 569-578 & chain A, resi 589-599 & chain A, resi 607-619 & chain A, resi 627-639 & chain A, resi 691-701 & chain A, resi 714-726 & chain A, resi 750-761 & chain A, resi 764-775 & chain A, resi 782-792 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-2.044793887275089,13.215304088040696,-59.03724733332998])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 670-673 & chain A, resi 681-686 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[-3.893200010061264,11.342599964141845,-31.943400192260743])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
