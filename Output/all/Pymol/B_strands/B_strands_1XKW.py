from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XKW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 188+189+190+191+192+193+194+195+196 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 200+201+202+203+204+205+206+207+208+209+210 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 217+218+219+220+221+222+223+224+225+226+227+228+229 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 236+237+238+239+240+241+242+243+244+245+246+247+248+249+250+251 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 254+255+256+257+258+259+260+261+262+263+264+265+266+267+268 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 297+298+299+300+301+302+303+304+305+306+307+308+309+310+311+312+313+314 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366+367+368+369+370+371+372+373+374+375 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 378+379+380+381+382+383+384+385+386+387+388+389+390+391+392+393+394+395+396+397+398 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447+448 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 451+452+453+454+455+456+457+458+459+460+461+462+463+464+465 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 491+492+493+494+495+496+497+498+499+500+501+502 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 536+537+538+539+540+541+542+543+544+545+546+547+548+549+550+551+552+553 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 476+477+478+479+480+481+482+483+484+485+486+487+488 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 518+519+520+521+522+523+524+525+526+527+528+529+530+531 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 566+567+568+569+570+571+572+573+574+575+576+577+578+579+580+581+582+583+584+585+586 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 589+590+591+592+593+594+595+596+597+598+599+600+601+602+603+604 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 621+622+623+624+625+626+627+628+629+630 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 638+639+640+641+642+643+644+645+646+647 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 664+665+666+667+668+669+670+671+672+673+674 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 679+680+681+682+683+684+685+686 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 711+712+713+714+715+716+717+718+719 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
