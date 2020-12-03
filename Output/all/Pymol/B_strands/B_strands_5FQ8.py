from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FQ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 177+178+179+180+181+182+183+184+185+186+187+188 & chain B ")
cmd.color ("red", "Bstrand0")


cmd.select("Bstrand1", "resi 973+974+975+976+977+978+979+980+981+982+983 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 252+253+254+255+256+257+258+259+260+261+262+263+264 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 268+269+270+271+272+273+274+275+276+277+278+279+280 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 289+290+291+292+293+294+295+296+297+298+299+300+301+302+303 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 802+803+804+805+806+807+808+809+810+811+812 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 306+307+308+309+310+311+312+313+314+315+316+317+318+319+320 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 376+377+378+379+380+381+382+383+384+385+386+387+388+389+390+391+392+393+394 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 643+644+645+646+647+648+649+650+651+652+653+654+655+656 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 582+583+584+585+586+587+588+589+590+591+592+593+594+595+596 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 558+559+560+561+562+563+564+565+566+567+568+569 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 538+539+540+541+542+543+544+545+546+547+548+549 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 513+514+515+516+517+518+519+520+521+522+523+524+525+526+527+528+529+530+531+532+533+534 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 472+473+474+475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 661+662+663+664+665+666+667+668+669+670+671+672+673 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 697+698+699+700+701+702+703+704+705+706+707+708+709+710+711+712 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 398+399+400+401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 716+717+718+719+720+721+722+723+724+725+726+727+728+729+730+731 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 815+816+817+818+819+820+821+822+823+824+825 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 904+905+906+907+908+909+910+911+912+913+914+915 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 928+929+930+931+932+933+934+935+936+937+938+939+940+941 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("barrel", "Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
