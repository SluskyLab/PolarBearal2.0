from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3EFM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 162+163+164+165+166+167+168+169+170 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 643+644+645+646+647+648+649+650+651 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 191+192+193+194+195+196+197+198+199+200+201+202 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 228+229+230+231+232+233+234+235+236+237+238+239+240+241 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 261+262+263+264+265+266+267+268+269+270+271+272+273+274+275 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 281+282+283+284+285+286+287+288+289+290+291+292+293+294+295+296+297 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342+343+344+345+346+347 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 410+411+412+413+369+368+370+371+414+372+373+415+510+374+416+375+511+417+460+512+376+418+513+419+461+377+462+420+421+378+463+517+379+422+518+464+423+380+519+465+381+520+424+559+466+560+522+425+521+382+561+562+467+523+383+524+426+468+563+564+384+427+526+525+469+470+527+385+565+428+471+386+472+566+429+528+387+473+529+567+568+530 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 576+577+578+579+533+580+534+535+581+536+582+537+478+583+479+538+584+480+539+585+481+540+482+586+434+541+483+435+436+542+484+437+485+543+438+439+391+486+390+393+544+487+441+392+440+443+442+394+395+488+545+444+445+489+397+396+399+398+490+401+400+492+403+402+491+405+404+493+406+407+494+495 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 211+212+213+214+215+216+217+218+219+220+221+222+223+224+225 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 597+598+599+600+601+602+603+604+605+606+607+608+609 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 612+613+614+615+616+617+618+619 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 174+175+176+177+178+179+180+181+182+183+184 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
