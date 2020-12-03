from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3OHN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 141+142+143+144+145+146+147+148+149+150+151+152+153 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 645+646+647+648+649+650+651+652+653+654+655 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 633+634+635+636+637+638+639+640+641 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 619+620+621+622+623+624+625+626+627+628 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 602+603+604+605+606+607+608+609+610+611 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 586+587+588+589+590+591+592+593+594+595+596+597 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 575+576+577+578+579+580+581+582+583 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 545+546+547+548+549+550+551+552+553+554+555+556 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 529+530+531+532+533+534+535+536+537+538 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 513+514+515+516+517+518+519+520+521+522+523+524 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 496+497+498+499+500+501+502+503+504+505+506+507 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 480+481+482+483+484+485+486+487+488+489+490+491+492 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 408+409+410+411+412+413+414+415+416+417+418+419+420 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 430+431+432+433+434+435+436+437 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 375+376+377+378+379+380+381+382+383+384+385+386+387 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 390+391+392+393+394+395+396+397+398+399+400+401+402 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 364+365+366+367+368+369+370+371+372 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 349+350+351+352+353+354+355+356+357+358 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 329+330+331+332+333+334+335+336+337+338+339 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 232+233+234+235+236+237+238+239 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 214+215+216+217+218+219+220+221+222 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 197+198+199+200+201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 176+177+178+179+180+181+182+183+184+185+186+187 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 159+160+161+162+163+164+165+166+167+168+169+170+171 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
