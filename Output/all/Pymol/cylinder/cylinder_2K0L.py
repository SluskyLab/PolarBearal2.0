from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2K0L.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 19+19+20+21+22+23+24+25+26+53+54+55+56+57+58+59+60+61+62+63+66+67+68+69+70+71+72+73+74+93+94+95+96+97+98+99+100+101+102+103+108+109+110+111+112+113+114+115+116+117+118+119+120+139+140+141+142+143+144+145+146+147+148+149+150+151+152+158+159+160+161+162+163+185+186+187+188+189+190+191 & chain A")
cmd.load_cgo( [9.0, 15.121146,-14.026108,5.7746296, -13.439805, 18.031754, -12.065895, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
