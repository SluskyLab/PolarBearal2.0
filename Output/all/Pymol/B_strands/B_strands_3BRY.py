from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3BRY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 80+81+82+83+84+85+86+87+88+89+90+91 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 94+95+96+97+98+99+100+101+102+103 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 233+234+235+236+150+237+151+152+238+153+239+154+240+155+156+157+158+159+160+161+162+163+248+164+165+249+250+166+167+251+169+168+252 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 200+201+202+203+130+131+214+132+133+215+134+216+135+217+218+136+219+137+220+138+221+139+222+140+223+141+224+142+225+143+226+144+227+145+228+229+230 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 268+269+270+271+272+273+280+281+282+283+284+285+286+287+288 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 293+294+295+296+297+298+299+300+301+302+311+310+312+313+314+315 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 335+336+337+338+339+340+341+342+343+344+345+346+347 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 350+351+352+353+354+355+356+357+358+359+360 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 378+379+380+381+382+383+384+385+386+387 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 392+393+394+395+396+397+398+399+400+401 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 420+421+422+423+424+425+426+427+428+429+430+431+432+433+434+435 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
