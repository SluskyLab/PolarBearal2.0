from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3W9T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 105-113 & chain A, resi 144-146 & chain A, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[91.12100156148274,134.33641497294107,3.5974167163173356])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 152-160 & chain A, resi 166-169 & chain A, resi 176-181 & chain A, resi 219-222 & chain A, resi 207-210 & chain A, resi 199-201 & chain A, resi 191-194 & chain A, resi 266-269 & chain A, resi 254-257 & chain A, resi 279-282 & chain A, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[74.02558716483738,109.44923948205036,-3.9286086935064066])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 293-299 & chain A, resi 379-384 & chain A, resi 403-407 & chain A, resi 403-407 & chain B, resi 379-384 & chain B, resi 293-299 & chain B, resi 403-407 & chain C, resi 379-384 & chain C, resi 293-299 & chain C, resi 403-407 & chain D, resi 379-384 & chain D, resi 293-299 & chain D, resi 403-407 & chain E, resi 379-384 & chain E, resi 293-299 & chain E, resi 403-407 & chain F, resi 379-384 & chain F, resi 293-299 & chain F, resi 293-299 & chain G, resi 379-384 & chain G, resi 403-407 & chain G, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[97.00379374670604,61.1237539866614,-27.741468217637802])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 304-332 & chain A, resi 337-366 & chain A, resi 337-366 & chain B, resi 304-332 & chain B, resi 337-366 & chain C, resi 304-325 & chain C, resi 328-332 & chain C, resi 337-366 & chain D, resi 304-332 & chain D, resi 337-366 & chain E, resi 304-332 & chain E, resi 337-366 & chain F, resi 304-332 & chain F, resi 304-332 & chain G, resi 337-366 & chain G, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[81.80146963114866,61.19550114652536,-60.65413148327755])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 391-393 & chain A, resi 397-399 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[92.9716682434082,81.95883305867513,-39.734832763671875])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 419-421 & chain A, resi 429-431 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[84.4496676127116,88.07716751098633,-10.641166845957438])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 105-113 & chain B, resi 119-122 & chain B, resi 131-134 & chain B, resi 144-146 & chain B, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[42.97174987792969,96.07565040588379,22.412249946594237])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 152-160 & chain B, resi 166-169 & chain B, resi 176-181 & chain B, resi 219-222 & chain B, resi 207-210 & chain B, resi 199-201 & chain B, resi 191-194 & chain B, resi 266-269 & chain B, resi 254-257 & chain B, resi 279-282 & chain B, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[49.84697839488154,67.06078280573306,6.55202176000761])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 391-393 & chain B, resi 397-399 & chain B, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[77.73316701253255,75.21233495076497,-32.84516620635986])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 419-421 & chain B, resi 429-431 & chain B, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[71.40183512369792,63.396999994913735,-4.9793334404627485])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 105-113 & chain C, resi 119-122 & chain C, resi 131-134 & chain C, resi 144-146 & chain C, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[42.1643500328064,28.251549816131593,22.873449897766115])
cmd.color ("orange", "Centroid10")


cmd.select("Group11", "(resi 152-160 & chain C, resi 166-169 & chain C, resi 176-181 & chain C, resi 219-222 & chain C, resi 207-210 & chain C, resi 199-201 & chain C, resi 191-194 & chain C, resi 266-269 & chain C, resi 254-257 & chain C, resi 279-282 & chain C, )")
cmd.color ("yellow", "Group11")


cmd.pseudoatom ("Centroid11", pos=[65.55321710006051,20.315999995107237,-0.04556524202875469])
cmd.color ("yellow", "Centroid11")


cmd.select("Group12", "(resi 391-393 & chain C, resi 397-399 & chain C, )")
cmd.color ("green", "Group12")


cmd.pseudoatom ("Centroid12", pos=[73.08466720581055,57.82849947611491,-30.627833048502605])
cmd.color ("green", "Centroid12")


cmd.select("Group13", "(resi 419-421 & chain C, resi 429-431 & chain C, )")
cmd.color ("cyan", "Group13")


cmd.pseudoatom ("Centroid13", pos=[81.24816640218098,37.10233370463053,-9.141833384831747])
cmd.color ("cyan", "Centroid13")


cmd.select("Group14", "(resi 105-113 & chain D, resi 119-122 & chain D, resi 131-134 & chain D, resi 144-147 & chain D, )")
cmd.color ("blue", "Group14")


cmd.pseudoatom ("Centroid14", pos=[90.11023821149554,-14.625095140366327,0.23057138618259204])
cmd.color ("blue", "Centroid14")


cmd.select("Group15", "(resi 152-160 & chain D, resi 166-169 & chain D, resi 176-181 & chain D, resi 219-222 & chain D, resi 207-210 & chain D, resi 199-201 & chain D, resi 191-194 & chain D, resi 266-269 & chain D, resi 254-257 & chain D, resi 279-282 & chain D, )")
cmd.color ("purple", "Group15")


cmd.pseudoatom ("Centroid15", pos=[107.98408707328464,3.995565253107444,-20.330586993176006])
cmd.color ("purple", "Centroid15")


cmd.select("Group16", "(resi 391-393 & chain D, resi 397-399 & chain D, )")
cmd.color ("red", "Group16")


cmd.pseudoatom ("Centroid16", pos=[82.34183247884114,43.01349894205729,-35.09249941507975])
cmd.color ("red", "Centroid16")


cmd.select("Group17", "(resi 419-421 & chain D, resi 429-431 & chain D, )")
cmd.color ("orange", "Group17")


cmd.pseudoatom ("Centroid17", pos=[105.71416600545247,28.594166437784832,-20.842833518981934])
cmd.color ("orange", "Centroid17")


cmd.select("Group18", "(resi 105-113 & chain E, resi 119-122 & chain E, resi 131-134 & chain E, resi 143-146 & chain E, )")
cmd.color ("yellow", "Group18")


cmd.pseudoatom ("Centroid18", pos=[149.9517604282924,-1.1618095267386663,-27.739428474789573])
cmd.color ("yellow", "Centroid18")


cmd.select("Group19", "(resi 152-160 & chain E, resi 166-169 & chain E, resi 176-181 & chain E, resi 219-222 & chain E, resi 207-210 & chain E, resi 199-201 & chain E, resi 191-194 & chain E, resi 266-269 & chain E, resi 254-257 & chain E, resi 279-282 & chain E, )")
cmd.color ("green", "Group19")


cmd.pseudoatom ("Centroid19", pos=[146.12039250912875,30.724630521691363,-37.522804260253906])
cmd.color ("green", "Centroid19")


cmd.select("Group20", "(resi 391-393 & chain E, resi 397-399 & chain E, )")
cmd.color ("cyan", "Group20")


cmd.pseudoatom ("Centroid20", pos=[98.71533203125,41.823500315348305,-42.712666829427086])
cmd.color ("cyan", "Centroid20")


cmd.select("Group21", "(resi 419-421 & chain E, resi 429-431 & chain E, )")
cmd.color ("blue", "Group21")


cmd.pseudoatom ("Centroid21", pos=[126.94483311971028,44.606499989827476,-30.392332712809246])
cmd.color ("blue", "Centroid21")


cmd.select("Group22", "(resi 105-113 & chain F, resi 119-122 & chain F, resi 131-134 & chain F, resi 144-146 & chain F, )")
cmd.color ("purple", "Group22")


cmd.pseudoatom ("Centroid22", pos=[177.34835052490234,59.78769950866699,-39.915549755096436])
cmd.color ("purple", "Centroid22")


cmd.select("Group23", "(resi 152-160 & chain F, resi 166-169 & chain F, resi 176-181 & chain F, resi 219-222 & chain F, resi 207-210 & chain F, resi 199-201 & chain F, resi 191-194 & chain F, resi 266-269 & chain F, resi 254-257 & chain F, resi 279-282 & chain F, )")
cmd.color ("red", "Group23")


cmd.pseudoatom ("Centroid23", pos=[151.00786855946416,80.42582619708517,-39.70215221073317])
cmd.color ("red", "Centroid23")


cmd.select("Group24", "(resi 391-393 & chain F, resi 397-399 & chain F, )")
cmd.color ("orange", "Group24")


cmd.pseudoatom ("Centroid24", pos=[109.73450088500977,55.19550005594889,-47.52433331807455])
cmd.color ("orange", "Centroid24")


cmd.select("Group25", "(resi 419-421 & chain F, resi 429-431 & chain F, )")
cmd.color ("yellow", "Group25")


cmd.pseudoatom ("Centroid25", pos=[128.90216700236002,73.24816513061523,-31.262667020161945])
cmd.color ("yellow", "Centroid25")


cmd.select("Group26", "(resi 105-113 & chain G, resi 119-122 & chain G, resi 131-134 & chain G, resi 144-146 & chain G, )")
cmd.color ("green", "Group26")


cmd.pseudoatom ("Centroid26", pos=[151.8145004272461,121.78375053405762,-28.822249984741212])
cmd.color ("green", "Centroid26")


cmd.select("Group27", "(resi 152-160 & chain G, resi 166-169 & chain G, resi 176-181 & chain G, resi 219-222 & chain G, resi 207-210 & chain G, resi 199-201 & chain G, resi 191-194 & chain G, resi 266-269 & chain G, resi 254-257 & chain G, resi 279-282 & chain G, )")
cmd.color ("cyan", "Group27")


cmd.pseudoatom ("Centroid27", pos=[118.84004360696544,115.62047842274542,-25.228608691174053])
cmd.color ("cyan", "Centroid27")


cmd.select("Group28", "(resi 391-393 & chain G, resi 397-399 & chain G, )")
cmd.color ("blue", "Group28")


cmd.pseudoatom ("Centroid28", pos=[107.13166681925456,73.12033335367839,-46.48316637674967])
cmd.color ("blue", "Centroid28")


cmd.select("Group29", "(resi 419-421 & chain G, resi 429-431 & chain G, )")
cmd.color ("purple", "Group29")


cmd.pseudoatom ("Centroid29", pos=[110.07483291625977,92.64233271280925,-22.66499964396159])
cmd.color ("purple", "Centroid29")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
