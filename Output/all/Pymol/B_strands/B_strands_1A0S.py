from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1A0S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Pstrand0", "resi 73+74+75+76+77+78+79+80+81+82+83+84+85+86 & chain P ")
cmd.color ("red", "Pstrand0")


cmd.select("Pstrand1", "resi 472+473+474+475+476+477+478+479+480+481+482 & chain P ")
cmd.color ("green", "Pstrand1")


cmd.select("Pstrand2", "resi 439+440+441+442+443+444+445+446+447+448+449 & chain P ")
cmd.color ("orange", "Pstrand2")


cmd.select("Pstrand3", "resi 413+414+415+416+417+418+419+420+421+422+423+424+425+426+427 & chain P ")
cmd.color ("teal", "Pstrand3")


cmd.select("Pstrand4", "resi 389+390+391+392+393+394+395+396+397+398+399+400+401+402+403 & chain P ")
cmd.color ("yellow", "Pstrand4")


cmd.select("Pstrand5", "resi 371+372+373+374+375+376+377+378+379+380+381+382+383+384 & chain P ")
cmd.color ("blue", "Pstrand5")


cmd.select("Pstrand6", "resi 351+352+353+354+355+356+357+358+359+360+361+362+363 & chain P ")
cmd.color ("red", "Pstrand6")


cmd.select("Pstrand7", "resi 335+336+337+338+339+340+341+342+343+344 & chain P ")
cmd.color ("green", "Pstrand7")


cmd.select("Pstrand8", "resi 306+307+308+309+310+311+312+313+314+315+316 & chain P ")
cmd.color ("orange", "Pstrand8")


cmd.select("Pstrand9", "resi 286+287+288+289+290+291+292+293+294+295+296 & chain P ")
cmd.color ("teal", "Pstrand9")


cmd.select("Pstrand10", "resi 256+257+258+259+260+261+262+263+264 & chain P ")
cmd.color ("yellow", "Pstrand10")


cmd.select("Pstrand11", "resi 241+242+243+244+245+246+247+248+249+250+251+252+253 & chain P ")
cmd.color ("blue", "Pstrand11")


cmd.select("Pstrand12", "resi 221+222+223+224+225+226+227+228+229+230+231+232+233 & chain P ")
cmd.color ("red", "Pstrand12")


cmd.select("Pstrand13", "resi 206+207+208+209+210+211+212+213+214+215+216+217 & chain P ")
cmd.color ("green", "Pstrand13")


cmd.select("Pstrand14", "resi 181+182+183+184+185+186+187+188 & chain P ")
cmd.color ("orange", "Pstrand14")


cmd.select("Pstrand15", "resi 159+160+161+162+163+164+165+166+167+168 & chain P ")
cmd.color ("teal", "Pstrand15")


cmd.select("Pstrand16", "resi 134+135+136+137+138+139+140+141+142+143+144+145 & chain P ")
cmd.color ("yellow", "Pstrand16")


cmd.select("Pstrand17", "resi 117+118+119+120+121+122+123+124+125+126+127+128 & chain P ")
cmd.color ("blue", "Pstrand17")


cmd.select("barrel", "Pstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
