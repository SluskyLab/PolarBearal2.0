from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Q35.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 42-46 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[15.52919979095459,9.140800189971923,9.550600004196166])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 52-62 & chain A, resi 66-70 & chain A, resi 80-93 & chain A, resi 74-77 & chain A, resi 102-108 & chain A, resi 111-114 & chain A, resi 117-127 & chain A, resi 133-145 & chain A, resi 148-157 & chain A, resi 162-171 & chain A, resi 180-190 & chain A, resi 195-199 & chain A, resi 202-205 & chain A, resi 211-221 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[26.48722956659364,-7.381352443064823,0.8443606654563766])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 230-236 & chain A, resi 242-252 & chain A, resi 255-264 & chain A, resi 269-280 & chain A, resi 284-295 & chain A, resi 310-321 & chain A, resi 326-336 & chain A, resi 354-365 & chain A, resi 368-379 & chain A, resi 387-400 & chain A, resi 406-419 & chain A, resi 424-442 & chain A, resi 445-461 & chain A, resi 470-497 & chain A, resi 505-520 & chain A, resi 555-568 & chain A, resi 575-589 & chain A, resi 603-617 & chain A, resi 620-629 & chain A, resi 637-647 & chain A, resi 650-659 & chain A, resi 682-693 & chain A, resi 697-706 & chain A, resi 714-723 & chain A, resi 726-735 & chain A, resi 745-759 & chain A, resi 738-740 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[58.96584120513387,30.001384419846655,21.456661812737693])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 343-345 & chain A, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[65.90499750773112,12.943333625793457,11.235333442687988])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 382-384 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[81.15966796875,21.998999913533527,25.915000279744465])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 525-527 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[73.90333302815755,33.4130007425944,40.97700119018555])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 530-536 & chain A, resi 544-547 & chain A, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[65.23227240822531,40.03718254782937,29.17345463145863])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 596-599 & chain A, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[80.26399993896484,47.197500228881836,24.80049991607666])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 776-778 & chain A, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[63.547332763671875,24.321000417073567,7.458000183105469])
cmd.color ("purple", "Centroid8")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
