from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6H3I.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 72+72+73+74+75+76+77+78+88+89+90+91+92+93+94+95+96+97+98+104+105+106+107+108+109+110+111+112+113+114+115+116+139+140+141+142+143+144+145+146+152+153+154+155+156+157+158+159+160+161+162+178+179+180+181+182+183+184+185+186+187+188+189+201+202+203+204+205+206+207+208+231+232+233+234+235+236+237+238+239+240+246+247+248+249+250+251+252+253+254+323+324+325+326+327+328+336+337+338+339+340+341+342+343+344+357+358+359+360+361+362+367+368+369+370+371+372+389+390+391+392+393+394 & chain F")
cmd.load_cgo( [9.0, 128.52872,137.5023,159.29332, 168.55557, 164.34563, 136.48482, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")