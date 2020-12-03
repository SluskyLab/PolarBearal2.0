from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SCN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 174-177 & chain a, resi 210-213 & chain a, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[200.96437644958496,261.3244972229004,177.36300086975098])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 262-271 & chain a, resi 381-391 & chain a, resi 429-434 & chain a, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[212.4259270562066,259.2619996247468,155.82629620587383])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 276-278 & chain a, resi 374-376 & chain a, resi 276-278 & chain b, resi 374-376 & chain b, resi 276-278 & chain c, resi 374-376 & chain c, resi 276-278 & chain d, resi 374-376 & chain d, resi 276-278 & chain e, resi 374-376 & chain e, resi 276-278 & chain f, resi 374-376 & chain f, resi 276-278 & chain g, resi 374-376 & chain g, resi 276-278 & chain A, resi 374-376 & chain A, resi 276-278 & chain B, resi 374-376 & chain B, resi 276-278 & chain C, resi 374-376 & chain C, resi 276-278 & chain D, resi 374-376 & chain D, resi 276-278 & chain E, resi 374-376 & chain E, resi 276-278 & chain F, resi 374-376 & chain F, resi 276-278 & chain G, resi 374-376 & chain G, resi 276-278 & chain H, resi 374-376 & chain H, resi 276-278 & chain I, resi 374-376 & chain I, resi 276-278 & chain J, resi 374-376 & chain J, resi 276-278 & chain K, resi 374-376 & chain K, resi 276-278 & chain L, resi 374-376 & chain L, resi 276-278 & chain M, resi 374-376 & chain M, resi 276-278 & chain N, resi 374-376 & chain N, resi 276-278 & chain O, resi 374-376 & chain O, resi 276-278 & chain P, resi 374-376 & chain P, resi 276-278 & chain Q, resi 374-376 & chain Q, resi 276-278 & chain R, resi 374-376 & chain R, resi 276-278 & chain S, resi 374-376 & chain S, resi 276-278 & chain T, resi 374-376 & chain T, resi 276-278 & chain U, resi 374-376 & chain U, resi 276-278 & chain V, resi 374-376 & chain V, resi 276-278 & chain W, resi 374-376 & chain W, resi 276-278 & chain X, resi 374-376 & chain X, resi 276-278 & chain Y, resi 374-376 & chain Y, resi 276-278 & chain Z, resi 374-376 & chain Z, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[177.55071223865855,177.55279263583097,145.12520707255663])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 293-303 & chain a, resi 357-366 & chain a, resi 357-367 & chain b, resi 292-303 & chain b, resi 357-366 & chain c, resi 293-303 & chain c, resi 357-367 & chain d, resi 292-303 & chain d, resi 357-367 & chain e, resi 292-303 & chain e, resi 357-367 & chain f, resi 292-303 & chain f, resi 357-367 & chain g, resi 292-303 & chain g, resi 357-366 & chain A, resi 293-303 & chain A, resi 357-367 & chain B, resi 292-303 & chain B, resi 357-367 & chain C, resi 292-303 & chain C, resi 357-367 & chain D, resi 292-303 & chain D, resi 357-366 & chain E, resi 293-303 & chain E, resi 357-366 & chain F, resi 293-303 & chain F, resi 357-367 & chain G, resi 292-303 & chain G, resi 357-367 & chain H, resi 292-303 & chain H, resi 357-367 & chain I, resi 292-303 & chain I, resi 357-367 & chain J, resi 292-303 & chain J, resi 357-367 & chain K, resi 292-303 & chain K, resi 357-367 & chain L, resi 292-303 & chain L, resi 357-367 & chain M, resi 292-303 & chain M, resi 357-367 & chain N, resi 292-303 & chain N, resi 357-367 & chain O, resi 292-303 & chain O, resi 357-366 & chain P, resi 293-303 & chain P, resi 357-367 & chain Q, resi 292-303 & chain Q, resi 357-366 & chain R, resi 293-303 & chain R, resi 357-367 & chain S, resi 292-303 & chain S, resi 357-367 & chain T, resi 292-303 & chain T, resi 357-367 & chain U, resi 292-303 & chain U, resi 357-367 & chain V, resi 292-303 & chain V, resi 357-367 & chain W, resi 292-303 & chain W, resi 357-367 & chain X, resi 292-303 & chain X, resi 357-367 & chain Y, resi 292-303 & chain Y, resi 292-303 & chain Z, resi 357-367 & chain Z, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[177.39685243952195,177.63447766400023,110.74718383174614])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 156-158 & chain A, resi 173-177 & chain A, resi 210-213 & chain A, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[234.19499969482422,177.00524775187174,181.61750157674155])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 262-271 & chain A, resi 381-391 & chain A, resi 429-434 & chain A, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[265.1550750732422,162.9398148148148,155.84474125614872])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 156-158 & chain b, resi 173-176 & chain b, resi 210-212 & chain b, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[198.50749816894532,228.68449859619142,180.9770980834961])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 262-271 & chain b, resi 381-391 & chain b, resi 429-434 & chain b, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[227.26648231788917,251.2107786955657,155.8218152081525])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 156-158 & chain B, resi 173-177 & chain B, resi 210-213 & chain B, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[263.2640864054362,161.48266728719076,177.99766540527344])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 262-271 & chain B, resi 381-391 & chain B, resi 429-434 & chain B, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[260.8157766836661,146.61074094419126,155.83133273654514])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 156-158 & chain c, resi 173-177 & chain c, resi 210-213 & chain c, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[213.16775131225586,221.56108220418295,181.52791849772134])
cmd.color ("orange", "Centroid10")


cmd.select("Group11", "(resi 262-271 & chain c, resi 381-391 & chain c, resi 429-434 & chain c, )")
cmd.color ("yellow", "Group11")


cmd.pseudoatom ("Centroid11", pos=[240.28600000452113,240.44903564453125,155.85725967972368])
cmd.color ("yellow", "Centroid11")


cmd.select("Group12", "(resi 156-158 & chain C, resi 173-176 & chain C, resi 210-212 & chain C, )")
cmd.color ("green", "Group12")


cmd.pseudoatom ("Centroid12", pos=[230.10419921875,160.48639831542968,180.91690063476562])
cmd.color ("green", "Centroid12")


cmd.select("Group13", "(resi 262-271 & chain C, resi 381-391 & chain C, resi 429-434 & chain C, )")
cmd.color ("cyan", "Group13")


cmd.pseudoatom ("Centroid13", pos=[253.43037018952546,131.4138525503653,155.84403709129052])
cmd.color ("cyan", "Centroid13")


cmd.select("Group14", "(resi 174-177 & chain d, resi 210-213 & chain d, )")
cmd.color ("blue", "Group14")


cmd.pseudoatom ("Centroid14", pos=[243.2730007171631,235.0713768005371,177.4360008239746])
cmd.color ("blue", "Centroid14")


cmd.select("Group15", "(resi 262-271 & chain d, resi 381-391 & chain d, resi 429-434 & chain d, )")
cmd.color ("purple", "Group15")


cmd.pseudoatom ("Centroid15", pos=[251.04459296332465,227.43803631817852,155.81166811342592])
cmd.color ("purple", "Centroid15")


cmd.select("Group16", "(resi 156-158 & chain D, resi 173-177 & chain D, resi 210-213 & chain D, )")
cmd.color ("red", "Group16")


cmd.pseudoatom ("Centroid16", pos=[223.88199996948242,145.2950007120768,181.49116643269858])
cmd.color ("red", "Centroid16")


cmd.select("Group17", "(resi 262-271 & chain D, resi 381-391 & chain D, resi 429-434 & chain D, )")
cmd.color ("orange", "Group17")


cmd.pseudoatom ("Centroid17", pos=[243.34585119176793,117.89155578613281,155.85103578920717])
cmd.color ("orange", "Centroid17")


cmd.select("Group18", "(resi 155-158 & chain e, resi 173-177 & chain e, resi 210-213 & chain e, )")
cmd.color ("yellow", "Group18")


cmd.pseudoatom ("Centroid18", pos=[224.68323223407452,208.84861520620493,182.00423020582932])
cmd.color ("yellow", "Centroid18")


cmd.select("Group19", "(resi 262-271 & chain e, resi 381-391 & chain e, resi 429-434 & chain e, )")
cmd.color ("green", "Group19")


cmd.pseudoatom ("Centroid19", pos=[259.1530750415943,212.60722068504052,155.85259388111257])
cmd.color ("green", "Centroid19")


cmd.select("Group20", "(resi 174-176 & chain E, resi 210-212 & chain E, )")
cmd.color ("cyan", "Group20")


cmd.pseudoatom ("Centroid20", pos=[238.47899881998697,116.91600163777669,177.8838348388672])
cmd.color ("cyan", "Centroid20")


cmd.select("Group21", "(resi 262-271 & chain E, resi 381-391 & chain E, resi 429-434 & chain E, )")
cmd.color ("blue", "Group21")


cmd.pseudoatom ("Centroid21", pos=[230.8642216435185,106.49029597529659,155.84311252170139])
cmd.color ("blue", "Centroid21")


cmd.select("Group22", "(resi 156-158 & chain f, resi 173-177 & chain f, resi 210-213 & chain f, )")
cmd.color ("purple", "Group22")


cmd.pseudoatom ("Centroid22", pos=[231.93166732788086,193.74974950154623,181.58141581217447])
cmd.color ("purple", "Centroid22")


cmd.select("Group23", "(resi 262-271 & chain f, resi 381-391 & chain f, resi 429-434 & chain f, )")
cmd.color ("red", "Group23")


cmd.pseudoatom ("Centroid23", pos=[264.3089627866392,196.53966663501882,155.82003558123554])
cmd.color ("red", "Centroid23")


cmd.select("Group24", "(resi 156-158 & chain F, resi 173-176 & chain F, resi 210-212 & chain F, )")
cmd.color ("orange", "Group24")


cmd.pseudoatom ("Centroid24", pos=[211.24960021972657,133.8772003173828,181.03000183105468])
cmd.color ("orange", "Centroid24")


cmd.select("Group25", "(resi 262-271 & chain F, resi 381-391 & chain F, resi 429-434 & chain F, )")
cmd.color ("yellow", "Group25")


cmd.pseudoatom ("Centroid25", pos=[216.48033368145977,97.6798516732675,155.81803724500867])
cmd.color ("yellow", "Centroid25")


cmd.select("Group26", "(resi 262-271 & chain g, resi 381-391 & chain g, resi 429-434 & chain g, )")
cmd.color ("green", "Group26")


cmd.pseudoatom ("Centroid26", pos=[266.33903616446037,179.7659262197989,155.8208533393012])
cmd.color ("green", "Centroid26")


cmd.select("Group27", "(resi 156-158 & chain G, resi 173-176 & chain G, resi 210-212 & chain G, )")
cmd.color ("cyan", "Group27")


cmd.pseudoatom ("Centroid27", pos=[197.14819946289063,125.76689987182617,180.84730072021483])
cmd.color ("cyan", "Centroid27")


cmd.select("Group28", "(resi 262-271 & chain G, resi 381-391 & chain G, resi 429-434 & chain G, )")
cmd.color ("blue", "Group28")


cmd.pseudoatom ("Centroid28", pos=[200.6488890471282,91.78059245921948,155.85655664514613])
cmd.color ("blue", "Centroid28")


cmd.select("Group29", "(resi 174-177 & chain H, resi 210-213 & chain H, )")
cmd.color ("purple", "Group29")


cmd.pseudoatom ("Centroid29", pos=[194.57399940490723,91.88175010681152,177.3598747253418])
cmd.color ("purple", "Centroid29")


cmd.select("Group30", "(resi 262-271 & chain H, resi 381-391 & chain H, resi 429-434 & chain H, )")
cmd.color ("red", "Group30")


cmd.pseudoatom ("Centroid30", pos=[184.01429635507088,88.9594076651114,155.80777825249567])
cmd.color ("red", "Centroid30")


cmd.select("Group31", "(resi 155-158 & chain I, resi 173-177 & chain I, resi 210-213 & chain I, )")
cmd.color ("orange", "Group31")


cmd.pseudoatom ("Centroid31", pos=[181.03984774076022,121.12407625638522,182.0596923828125])
cmd.color ("orange", "Centroid31")


cmd.select("Group32", "(resi 262-271 & chain I, resi 381-391 & chain I, resi 429-434 & chain I, )")
cmd.color ("yellow", "Group32")


cmd.pseudoatom ("Centroid32", pos=[167.11574074074073,89.35196318449798,155.8555179172092])
cmd.color ("yellow", "Centroid32")


cmd.select("Group33", "(resi 156-158 & chain J, resi 173-177 & chain J, resi 210-213 & chain J, )")
cmd.color ("green", "Group33")


cmd.pseudoatom ("Centroid33", pos=[164.45358403523764,122.42566744486491,181.5326665242513])
cmd.color ("green", "Centroid33")


cmd.select("Group34", "(resi 262-271 & chain J, resi 381-391 & chain J, resi 429-434 & chain J, )")
cmd.color ("cyan", "Group34")


cmd.pseudoatom ("Centroid34", pos=[150.62607433177806,92.89974127875433,155.83329716435185])
cmd.color ("cyan", "Centroid34")


cmd.select("Group35", "(resi 262-271 & chain K, resi 381-391 & chain K, resi 429-434 & chain K, )")
cmd.color ("blue", "Group35")


cmd.pseudoatom ("Centroid35", pos=[135.0747754132306,99.53277785689743,155.8247025101273])
cmd.color ("blue", "Centroid35")


cmd.select("Group36", "(resi 156-158 & chain L, resi 173-176 & chain L, resi 210-212 & chain L, )")
cmd.color ("purple", "Group36")


cmd.pseudoatom ("Centroid36", pos=[149.20970001220704,130.12540130615236,181.0281997680664])
cmd.color ("purple", "Centroid36")


cmd.select("Group37", "(resi 262-271 & chain L, resi 381-391 & chain L, resi 429-434 & chain L, )")
cmd.color ("red", "Group37")


cmd.pseudoatom ("Centroid37", pos=[121.08251840096933,108.9940739384404,155.85859284577546])
cmd.color ("red", "Centroid37")


cmd.select("Group38", "(resi 174-177 & chain M, resi 210-213 & chain M, )")
cmd.color ("orange", "Group38")


cmd.pseudoatom ("Centroid38", pos=[118.92274951934814,113.64124965667725,177.25337600708008])
cmd.color ("orange", "Centroid38")


cmd.select("Group39", "(resi 262-271 & chain M, resi 381-391 & chain M, resi 429-434 & chain M, )")
cmd.color ("yellow", "Group39")


cmd.pseudoatom ("Centroid39", pos=[109.12744423195169,120.91566721598308,155.8349247685185])
cmd.color ("yellow", "Centroid39")


cmd.select("Group40", "(resi 155-158 & chain N, resi 173-176 & chain N, resi 210-212 & chain N, )")
cmd.color ("green", "Group40")


cmd.pseudoatom ("Centroid40", pos=[136.38554659756747,140.6469990123402,181.45991099964488])
cmd.color ("green", "Centroid40")


cmd.select("Group41", "(resi 262-271 & chain N, resi 381-391 & chain N, resi 429-434 & chain N, )")
cmd.color ("cyan", "Group41")


cmd.pseudoatom ("Centroid41", pos=[99.65407392713759,134.89659231680412,155.83544413248697])
cmd.color ("cyan", "Centroid41")


cmd.select("Group42", "(resi 156-158 & chain O, resi 173-177 & chain O, resi 210-213 & chain O, )")
cmd.color ("blue", "Group42")


cmd.pseudoatom ("Centroid42", pos=[126.55000241597493,153.5474993387858,181.48258336385092])
cmd.color ("blue", "Centroid42")


cmd.select("Group43", "(resi 262-271 & chain O, resi 381-391 & chain O, resi 429-434 & chain O, )")
cmd.color ("purple", "Group43")


cmd.pseudoatom ("Centroid43", pos=[92.98233314796731,150.40374134205007,155.83755719220196])
cmd.color ("purple", "Centroid43")


cmd.select("Group44", "(resi 174-177 & chain P, resi 210-213 & chain P, )")
cmd.color ("red", "Group44")


cmd.pseudoatom ("Centroid44", pos=[93.21624851226807,155.94975090026855,177.3420009613037])
cmd.color ("red", "Centroid44")


cmd.select("Group45", "(resi 262-271 & chain P, resi 381-391 & chain P, resi 429-434 & chain P, )")
cmd.color ("orange", "Group45")


cmd.pseudoatom ("Centroid45", pos=[89.35588949697988,166.90392670808015,155.83096369990596])
cmd.color ("orange", "Centroid45")


cmd.select("Group46", "(resi 156-158 & chain Q, resi 173-177 & chain Q, resi 210-213 & chain Q, )")
cmd.color ("yellow", "Group46")


cmd.pseudoatom ("Centroid46", pos=[121.68591626485188,169.76850001017252,181.56758499145508])
cmd.color ("yellow", "Centroid46")


cmd.select("Group47", "(resi 262-271 & chain Q, resi 381-391 & chain Q, resi 429-434 & chain Q, )")
cmd.color ("green", "Group47")


cmd.pseudoatom ("Centroid47", pos=[88.91325971815321,183.77803604691118,155.81603721336083])
cmd.color ("green", "Centroid47")


cmd.select("Group48", "(resi 156-158 & chain R, resi 173-176 & chain R, resi 210-212 & chain R, )")
cmd.color ("cyan", "Group48")


cmd.pseudoatom ("Centroid48", pos=[122.86819915771484,186.40500183105468,180.85050048828126])
cmd.color ("cyan", "Centroid48")


cmd.select("Group49", "(resi 262-271 & chain R, resi 381-391 & chain R, resi 429-434 & chain R, )")
cmd.color ("blue", "Group49")


cmd.pseudoatom ("Centroid49", pos=[91.72451923511646,200.4256309226707,155.85211181640625])
cmd.color ("blue", "Centroid49")


cmd.select("Group50", "(resi 174-177 & chain S, resi 210-213 & chain S, )")
cmd.color ("purple", "Group50")


cmd.pseudoatom ("Centroid50", pos=[94.95525074005127,205.6287498474121,177.43937492370605])
cmd.color ("purple", "Centroid50")


cmd.select("Group51", "(resi 262-271 & chain S, resi 381-391 & chain S, resi 429-434 & chain S, )")
cmd.color ("red", "Group51")


cmd.pseudoatom ("Centroid51", pos=[97.59303735803675,216.25207406503182,155.81485324435764])
cmd.color ("red", "Centroid51")


cmd.select("Group52", "(resi 155-158 & chain T, resi 173-177 & chain T, resi 210-213 & chain T, )")
cmd.color ("orange", "Group52")


cmd.pseudoatom ("Centroid52", pos=[126.86469268798828,202.69976924015924,182.01499938964844])
cmd.color ("orange", "Centroid52")


cmd.select("Group53", "(resi 262-271 & chain T, resi 381-391 & chain T, resi 429-434 & chain T, )")
cmd.color ("yellow", "Group53")


cmd.pseudoatom ("Centroid53", pos=[106.38414764404297,230.68944464789496,155.85344441731772])
cmd.color ("yellow", "Centroid53")


cmd.select("Group54", "(resi 156-158 & chain U, resi 173-177 & chain U, resi 210-213 & chain U, )")
cmd.color ("green", "Group54")


cmd.pseudoatom ("Centroid54", pos=[136.37383270263672,216.4991683959961,181.4962501525879])
cmd.color ("green", "Centroid54")


cmd.select("Group55", "(resi 262-271 & chain U, resi 381-391 & chain U, resi 429-434 & chain U, )")
cmd.color ("cyan", "Group55")


cmd.pseudoatom ("Centroid55", pos=[117.72585211859808,243.18859185112848,155.82170557092738])
cmd.color ("cyan", "Centroid55")


cmd.select("Group56", "(resi 262-271 & chain V, resi 381-391 & chain V, resi 429-434 & chain V, )")
cmd.color ("blue", "Group56")


cmd.pseudoatom ("Centroid56", pos=[131.23388841417102,253.35462838632088,155.82429730450664])
cmd.color ("blue", "Centroid56")


cmd.select("Group57", "(resi 156-158 & chain W, resi 173-177 & chain W, resi 210-213 & chain W, )")
cmd.color ("purple", "Group57")


cmd.pseudoatom ("Centroid57", pos=[149.83625157674155,226.9059181213379,181.56500116984049])
cmd.color ("purple", "Centroid57")


cmd.select("Group58", "(resi 262-271 & chain W, resi 381-391 & chain W, resi 429-434 & chain W, )")
cmd.color ("red", "Group58")


cmd.pseudoatom ("Centroid58", pos=[146.41311249909577,260.7228167498553,155.83574139630352])
cmd.color ("red", "Centroid58")


cmd.select("Group59", "(resi 174-177 & chain X, resi 210-213 & chain X, )")
cmd.color ("orange", "Group59")


cmd.pseudoatom ("Centroid59", pos=[151.45487213134766,260.38174629211426,177.41987419128418])
cmd.color ("orange", "Centroid59")


cmd.select("Group60", "(resi 262-271 & chain X, resi 381-391 & chain X, resi 429-434 & chain X, )")
cmd.color ("yellow", "Group60")


cmd.pseudoatom ("Centroid60", pos=[162.71399999547887,265.12274000379773,155.82755646882234])
cmd.color ("yellow", "Centroid60")


cmd.select("Group61", "(resi 156-158 & chain Y, resi 173-176 & chain Y, resi 210-212 & chain Y, )")
cmd.color ("green", "Group61")


cmd.pseudoatom ("Centroid61", pos=[166.1281005859375,231.61479797363282,180.97870178222655])
cmd.color ("green", "Centroid61")


cmd.select("Group62", "(resi 262-271 & chain Y, resi 381-391 & chain Y, resi 429-434 & chain Y, )")
cmd.color ("cyan", "Group62")


cmd.pseudoatom ("Centroid62", pos=[179.5648888481988,266.3485197844329,155.8315921359592])
cmd.color ("cyan", "Centroid62")


cmd.select("Group63", "(resi 156-158 & chain Z, resi 173-177 & chain Z, resi 210-213 & chain Z, )")
cmd.color ("blue", "Group63")


cmd.pseudoatom ("Centroid63", pos=[182.30308151245117,233.83875147501627,181.53591791788736])
cmd.color ("blue", "Centroid63")


cmd.select("Group64", "(resi 262-271 & chain Z, resi 381-391 & chain Z, resi 429-434 & chain Z, )")
cmd.color ("purple", "Group64")


cmd.pseudoatom ("Centroid64", pos=[196.3220740424262,264.34870175962095,155.84918495460792])
cmd.color ("purple", "Centroid64")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
