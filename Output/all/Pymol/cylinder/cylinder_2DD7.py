from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2DD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 4+4+5+6+7+8+9+10+11+12+13+14+17+18+19+20+21+22+23+24+25+26+27+28+31+32+33+34+35+36+37+38+107+108+109+110+111+112+113+114+115+116+117+94+95+96+97+98+99+100+101+102+103+104+81+82+83+84+85+86+87+88+89+163+164+165+166+167+168+169+170+171+172+173+174+147+148+149+150+151+152+153+154+155+156+157+158+130+131+132+133+136+137+138+139+140+141+142+143+188+189+190+191+192+193+194+195+196+197+198+202+203+204+205+206+207+208+209+210+211+212 & chain A")
cmd.load_cgo( [9.0, 81.25348,73.02426,45.235455, 66.35684, 79.53688, 89.05484, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")