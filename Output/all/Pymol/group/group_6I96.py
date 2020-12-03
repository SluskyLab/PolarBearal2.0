from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6I96.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 158-162 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[-19.41619987487793,33.953600311279295,35.59039993286133])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 179-183 & chain A, resi 256-263 & chain A, resi 277-283 & chain A, resi 232-234 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[-14.221652217533277,34.65330439028533,25.68278287804645])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 291-299 & chain A, resi 304-313 & chain A, resi 320-332 & chain A, resi 339-354 & chain A, resi 357-371 & chain A, resi 404-419 & chain A, resi 424-447 & chain A, resi 454-481 & chain A, resi 484-512 & chain A, resi 529-548 & chain A, resi 551-568 & chain A, resi 574-590 & chain A, resi 596-607 & chain A, resi 622-633 & chain A, resi 641-656 & chain A, resi 665-683 & chain A, resi 687-702 & chain A, resi 718-727 & chain A, resi 736-745 & chain A, resi 761-771 & chain A, resi 780-787 & chain A, resi 811-819 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[-11.531195316066933,35.56235209442455,20.22750297653318])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 795-800 & chain A, resi 803-806 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[-20.729899978637697,26.296900367736818,1.6355000257492065])
cmd.color ("purple", "Centroid3")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
