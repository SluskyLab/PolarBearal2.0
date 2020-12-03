from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4CU4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 161+162+163+164+165+166+167+168+169 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 716+717+718+719+720+721+722+723+724 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 686+687+688+689+690+691+692 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 666+667+668+669+670+671+672+673+674+675+676 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 641+642+643+644+645+646+647+648+649+650 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 623+624+625+626+627+628+629+630+631+632+633 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 593+594+595+596+597+598+599+600+601+602+603+604+605+606+607+608 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 570+571+572+573+574+575+576+577+578+579+580+581+582+583+584+585+586+587+588 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 527+528+529+530+531+532+533+534+535+536+537+538 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 501+502+503+504+505+506+507+508+509+510+511+512 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 545+546+547+548+549+550+551+552+553+554+555+556+557+558+559+560+561+562 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 456+457+458+370+459+371+372+460+373+374+461+375+462+376+294+463+295+377+296+297+464+378+379+298+465+299+380+466+300+381+467+301+382+468+302+383+469+303+384+304+305+470+385+471+306+307+386+387+472+308+473+309+388+389+315+313+314+311+316+310+391+312+390+317+392+393+394+396+397+400+395+399+401+398 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 340+341+342+343+344+345+346+431+347+274+432+275+348+433+434+276+349+435+277+350+436+278+351+437+438+352+279+439+353+440+280+354+281+441+355+442+356+282+443+283+357+444+358+284+285+445+446+359+448+286+447+360+287+450+449+361+362+451+288+452+363+289+364+453+365+366+367 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 227+228+229+230+231+232+233+234+235+236+237+238 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 209+210+211+212+213+214+215+216+217+218+219+220+221+222+223+224 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 190+191+192+193+194+195+196+197+198+199+200+201+202 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 173+174+175+176+177+178+179+180+181+182+183 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
