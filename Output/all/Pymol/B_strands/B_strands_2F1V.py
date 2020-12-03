from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F1V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13+14+15+16 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 71+72+73+74+75+76+77+78+79+82+83+84+85+86+87+88 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 96+97+98+99+100+101+102+103+104+105+106+61+107+62+63+108+109+64+110+65+111+112+66+67+113+114 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 131+132+133+134+135+136+137+138+139+140+141+142+143 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 51+52+53+54+55+56+57+58 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 148+149+150+151+152+153+154+155+156+157 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 36+37+38+39+40+41+42+43+44+45+46 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 181+182+183+184+185+186+187+188+189+190+191 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
