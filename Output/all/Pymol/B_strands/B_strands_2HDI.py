from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HDI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 165+166+167+168+169+170+171+172+173+174+175 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 627+628+629+630+631+632+633+634 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 183+184+185+186+187+188+189+190+191+192+193+194+195 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 199+200+201+202+203+204+205+206+207+208+209+210 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 231+232+233+234+235+236+237+238+239+240+241+242+243 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 249+250+251+252+253+254+255+256+257+258+259+260+261+262+263 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 271+272+273+274+275+276+277+278+279+280+281+282+283+284 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 289+290+291+292+293+294+295+296+297+298+299+300+301+302 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 330+331+332+333+334+335+336+337+338+339+340+341+342+343+344 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 357+358+359+360+361+362+363+364+365+366+367+368+369+370+371+372+373 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 376+377+378+379+380+381+382+383+384+385+386+387 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 391+392+393+394+395+396+397+398+399+400+401+402+403 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 408+409+410+474+473+411+472+475+476+412+477+413+548+546+478+547+549+545+414+550+544+479+551+415+543+552+480+416+553+481+417+554+482+418+555+419+483+556+485+484+486+487+442+441+503+440+504+439+505+506+507+508 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 514+515+516+517+433+518+434+432+431+519+520+521+522+523+524+450+525+566+565+563+526+451+564+567+452+527+568+528+453+569+570+454+529+530+571+455+572+531+456+532+573+574+457+533+458+534+575+576+459+535+460+536+577+461+578+462+537+579+538 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 587+588+589+590+591+592+593+594+595+596 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 612+613+614+615+616+617+618+619+620+621+622+623+624 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 654+655+656+657+658+659+660+661+662 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
