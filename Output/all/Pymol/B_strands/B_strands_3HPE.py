from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3HPE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 28+29+30+31+32+33+34+35 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39+40+41+42+168+167+171+43+170+172+169+173+44+174+175+176+177+178+179+180 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48+49+50+51+52+53+54+55 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 60+61+62+63+64+65+66+67+68+69 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 119+120+121+122+123+124+125+126+127+128+129+130+131+132+133+134 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 97+98+99+100+101+102+103+104+105+106 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 109+110+111+112+113+114+115+116 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 141+142+143+144+145+146+147+148+149+150+151+152 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
