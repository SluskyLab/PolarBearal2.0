using betaBarrelProgram.BarrelStructures;
using System.Collections;
using System.Collections.Generic;
using System;
using System.Linq;
using System.IO;
using System.Numerics;

namespace betaBarrelProgram
{
    public class AllProtein : BarrelStructures.Protein
    {
        public List<BarrelStructures.Chain> Chains { get; set; }
        public int ChainCount { get; set; }
        public int totalResNum { get; set; }
        public string PdbName { get; set; }

        public AllProtein(ref AtomParser.AtomCategory _myAtomCat, string PdbName)
        {
            this.Chains = new List<BarrelStructures.Chain>();
            this.ChainCount = 0;
            this.totalResNum = 0;
            this.PdbName = PdbName;

            AtomParser.AtomCategory myAtomCat = new AtomParser.AtomCategory();
            myAtomCat = _myAtomCat;

            var chainNumList = new Dictionary<int, int>();
            for (int chainNum = 0; chainNum < myAtomCat.chainAtomsList.Count; chainNum++)
            {
                bool IsItProtein = false;
                for (int atomNum = 0; atomNum < myAtomCat.ChainAtomList[chainNum].cartnAtoms.Count; atomNum++)
                {
                    if (myAtomCat.ChainAtomList[chainNum].CartnAtoms[atomNum].atomName == "CA") IsItProtein = true;
                }
                if (IsItProtein == true)
                {
                    BarrelStructures.Chain myChain = new BarrelStructures.Chain(ref myAtomCat, chainNum, PdbName, false, Global.DB_DIR);
                    this.Chains.Add(myChain);
                    chainNumList.Add(ChainCount, chainNum);
                    this.ChainCount++;
                }
            }

            this.Chains.Sort((x, y) => x.ChainName.CompareTo(y.ChainName)); //This sorts chains by letter 
            for (int i = 0; i < this.ChainCount; i++)
            {
                this.Chains[i].ChainNum = i;
                foreach (Res res in this.Chains[i].Residues) res.ChainNum = i;
            }
        }
    }

    internal class AllBarrel : BarrelStructures.Barrel
    {
        #region properties
        public List<Strand> Strands { get; set; }
        public List<Vector3> NellipseCoords { get; set; }
        public List<Vector3> CellipseCoords { get; set; }
        public Vector3 Ncentroid { get; set; }
        public Vector3 Ccentroid { get; set; }
        public Vector3 Axis { get; set; }
        public bool Direction { get; set; }
        public double AvgTilt { get; set; }
        public double AvgTilt_even { get; set; }
        public double AvgTilt_odd { get; set; }
        public List<List<List<int>>> protoBarrel { get; set; }
        public double AvgRadius { get; set; }
        public double MinRadius { get; set; }
        public double MaxRadius { get; set; }
        public List<Res> LoopResies { get; set; }
        public string PdbName { get; set; }
        public string ChainName { get; set; }
        public List<double> StrandLength { get; set; }
        public Vector3 OriginalNcentroid { get; set; }
        public Vector3 OriginalCcentroid { get; set; }
        public Vector3 AxisVector { get; set; }
        public Vector3 NewCaxisPt { get; set; }
        public Vector3 OldCaxisPt { get; set; }
        public int ShearNum { get; set; }
        public List<double> PrevTwists { get; set; }
        public bool Success { get; set; }
        public string barrelType { get; set; }

        #endregion

        public static string path = Global.OUTPUT_DIR;

        private Protein newProt;

        //barrel constructor
        public AllBarrel(ref Protein newProt)
        {
            this.newProt = newProt;
            this.PdbName = newProt.PdbName;
            this.protoBarrel = new List<List<List<int>>>();
            this.Strands = new List<Strand>();
            this.barrelType = "NA";
            this.Success = false;
            var resList = new List<Res>();
            StrandGroupMaker myStrandGroup=null;


            CreateStrandList(ref newProt);

            SharedFunctions.writePymolScriptForStrandsRik(Strands, Global.OUTPUT_DIR, Global.DB_DIR, PdbName);

            foreach (var chain in newProt.Chains)
            {
                foreach (var residue in chain)
                {
                    resList.Add(residue);
                }
            }

            #region find the barrel
            var isMonoFlag = false;
            var isPolyFlag = false;
            var flag = true;
            #region Hard code some PolyBarrels
            if (new List<string>() { "5GAQ", "6RB9", "3W9T", "5WC3", "3ANZ", "4P1X", "5JZT" }.Contains(PdbName))
            {
                flag = false;
            }
            #endregion

            if (flag)
            {
                foreach (var chain in newProt.Chains)//check for each chain first
                {
                    var monoStrands = new List<Strand>();
                    foreach (var strand in this.Strands)
                    {
                        if (strand.ChainName == chain.ChainName)
                        {
                            monoStrands.Add(strand);
                        }
                    }
                    if (monoStrands.Count != 0)
                    {
                        Console.WriteLine($"Starting strandGroupMaker for Chain {chain.ChainName}");
                        myStrandGroup = new StrandGroupMaker(newProt, monoStrands);
                        if (myStrandGroup.GroupOfGroup.Any(group => group.IsBarrel == true))
                        {
                            isMonoFlag = true;
                            this.Strands = myStrandGroup.BarrelStrands;
                            var group = myStrandGroup.GroupOfGroup.First(group => group.IsBarrel == true);
                            this.Ncentroid = group.Ncentroid;
                            this.Ccentroid = group.Ncentroid;
                            this.CellipseCoords = group.CellipseCoords;
                            this.NellipseCoords = group.NellipseCoords;
                            this.Axis = group.Axis;

                            Console.WriteLine($"Protein {PdbName} Chain {chain.ChainName} has a Mono barrel with {myStrandGroup.BarrelStrands.Count} strands");
                            this.barrelType = "mono";
                            this.Success = true;
                            LogBarrel(myStrandGroup);
                            
                            break;
                        }
                    }

                }
            }

            if (isMonoFlag == false)//if all the chain comes back as negative then check for poly
            {
                this.Strands = new List<Strand>(); //reseting the list of strands as it gets modified by the single chain StrandGroupMaker
                CreateStrandList(ref newProt);
                //Console.WriteLine($"\nStarting strandGroupMaker for whole protein");
                myStrandGroup = new StrandGroupMaker(newProt, Strands);
                if (myStrandGroup.GroupOfGroup.Any(group => group.IsBarrel == true))
                {
                    isPolyFlag = true;
                    this.Strands = myStrandGroup.BarrelStrands;
                    Console.WriteLine($"Protein {PdbName} has a Poly barrel with {myStrandGroup.BarrelStrands.Count} strands");
                    this.barrelType = "poly";
                    this.Success = true;
                    LogBarrel(myStrandGroup);
                }
            }
            #endregion

            if (!isMonoFlag && !isPolyFlag)
            {
                LogBarrel(null);
                
            }
            else
            {
                this.Strands = myStrandGroup.BarrelStrands;
                var barrel_strand_ctr = 0;
                foreach (Strand strand in this.Strands){
                    strand.StrandNum = barrel_strand_ctr++;
                    foreach(Res r in strand) r.StrandNum = barrel_strand_ctr;
                }
                /* ---------output information from mono --------- */
                this.StrandLength = SharedFunctions.getStrandLengths(this.Strands, path, this.PdbName);
                //this.PrevTwists = SharedFunctions.writeTwists(this.Strands, Global.OUTPUT_DIR, this.PdbName);

                SharedFunctions.AminoAcidPairs(Strands, Global.OUTPUT_DIR, Global.DB_DIR, PdbName);


                SharedFunctions.setInOut(this.Strands, path, this.PdbName, this.Axis, this.Ccentroid, this.Ncentroid);
                //SharedFunctions.setInOutM(this.Strands, Global.OUTPUT_DIR, this.PdbName, this.Ccentroid, this.Ncentroid);
                SharedFunctions.WritePymolScriptForInOutStrands(this.Strands, Global.OUTPUT_DIR, Global.DB_DIR, PdbName, Ccentroid, Ncentroid);
                this.AvgTilt = SharedFunctions.getTiltsByAA(this.Strands, path, this.PdbName, this.Axis, ref Global.AADict);

                bool detail_variable_output = true;
                if (detail_variable_output == true)
                {
                    if (!System.IO.Directory.Exists(path + "detailCheck")) System.IO.Directory.CreateDirectory(path + "detailCheck");

                    string fileLocation1 = path + "detailCheck/AllAtomVariables_" + this.PdbName + ".txt";
                    using (System.IO.StreamWriter file = new System.IO.StreamWriter(fileLocation1))
                    {
                        file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}t{15}", "strand.ChainName", "strand.ChainNum", "strand.betaStrandNum", "strand.StrandNum", "res.ThreeLetCode", "res.OneLetCode", "res.SeqID", "res.ResNum", "res.Inward", "res.Atoms.Count", "atom.AtomName", "atom.AtomNum", "atom.AtomType", "atom.Coords.X", "atom.Coords.Y", "atom.Coords.Z");

                        foreach (Strand strand in this.Strands)
                        {
                            foreach (Res res in strand)
                            {
                                foreach (Atom atom in res)
                                {
                                    if (atom.AtomName == "CA") file.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}", strand.ChainName, strand.ChainNum, strand.betaStrandNum, strand.StrandNum, res.ThreeLetCode, res.OneLetCode, res.SeqID, res.ResNum, res.Inward, res.Atoms.Count, atom.AtomName, atom.AtomNum, atom.AtomType, atom.Coords.X, atom.Coords.Y, atom.Coords.Z);
                                }
                            }
                        }
                    }
                }
                SharedFunctions.writePymolScriptForBarrelStrands(this.Strands, Global.OUTPUT_DIR, Global.DB_DIR, this.PdbName);
            }
        }


        private void LogBarrel(StrandGroupMaker myStrandGroup)
        {
            var numberOfStrands = 0;
            if (this.Success) numberOfStrands = myStrandGroup.BarrelStrands.Count;

            var chainID = "";
            if (this.barrelType == "mono") chainID = myStrandGroup.BarrelStrands[0].ChainName;
            else if (this.barrelType == "poly")
            {
                var curChain = myStrandGroup.BarrelStrands[0].ChainName;
                chainID += curChain;
                foreach (Strand curStrand in myStrandGroup.BarrelStrands)
                {
                    if(curStrand.ChainName!= curChain)
                    {
                        curChain = curStrand.ChainName;
                        chainID += "," + curChain;
                    }
                }

            }
            else chainID = "NA";
            

            string logFileLoc = Global.OUTPUT_DIR + "Log.txt";
            using (StreamWriter log = File.AppendText(logFileLoc))
            {
                log.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}", this.PdbName, this.Success, this.barrelType, chainID, numberOfStrands);
            }
        }

        private void CreateStrandList(ref Protein newProt)
        {
            this.protoBarrel = new List<List<List<int>>>();
            var chainCtr = 0;

            #region HardCoding
            var PDBList = new List<string>(){ "1E5P","1R0U","3PDF","3FHH","4E1T","6TZK","3QQ2","1QTT","4ALO","4WFU","1LFO","3A2S","4Q35", "1GL4" };//#Hard Coding# Use SSType for these
            bool useSSType = PDBList.Contains(PdbName);
            //useSSType = true;//RYAN//trying to see if Rik's SS is taking forever
            if (PdbName == "1GL4")
            {
                //manually remove few SSTypes
                var SeqIDList1 = new List<int>() { 471, 472, 473, 474, 475, 476, 477, 526, 527, 528, 529, 585, 586, 587 };
                foreach (var SeqID in SeqIDList1)
                {
                    newProt.Chains[0].Residues.Single(res => res.SeqID == SeqID).SSType = "";
                }
                //manually add few SSTypes
                var SeqIDList = new List<int>() { 425, 426 };
                foreach (var SeqID in SeqIDList)
                {
                    newProt.Chains[0].Residues.Single(res => res.SeqID == SeqID).SSType = "B";
                }
            }
            if (PdbName == "2RD7")
            {
                foreach (var res in newProt.Chains[0].Residues)
                {
                    res.DSSP = ""; //Remove strands from chain A
                }
            }
            if (PdbName == "3ANZ")
            {
                foreach (var chain in newProt.Chains)
                {
                    for (int i = 0; i < 1; i++)
                    {
                        Console.WriteLine("");
                    }
                }
            }
            #endregion

            foreach (var chain in newProt.Chains)
            {
                List<List<int>> tempList = new List<List<int>>();
                List<int> myStrand1 = new List<int>();
                int start = 0;
                int end = chain.ResidueCount;

                #region DefineStrands
                for (int res1ctr = start; res1ctr < end; res1ctr++)
                {
                    Res Residue1 = chain.Residues[res1ctr];
                    //var angle = Vector3.AngleBetween(Residue1.Direction, chain.Residues.Single(s => s.ResNum == myStrand1.Last()).Direction);
                    //Console.WriteLine($"res1ctr: {res1ctr}: DDSP = {Residue1.DSSP}");
                    if ((!useSSType && Residue1.DSSP == "E") || (useSSType && Residue1.SSType == "B")) //(Residue1.DSSP == "E" || Residue1.SSType == "B") //(Residue1.DSSP == "E")
                    {
                        
                        //add Residue1.ResNum
                        if (myStrand1.Count > 0)
                        {
                            //var angle = Vector3.AngleBetween(chain.Residues.Single(s => s.ResNum == myStrand1.Last()).Direction, Residue1.Direction);
                            //Console.WriteLine($"ResNum: {Residue1.ResNum} and myStrand1{myStrand1.Last()+1}");
                            
                            if ((Residue1.ResNum == myStrand1.Last() + 1))  // & (angle <= 71)
                            {
                                //Console.WriteLine($"Angle is between {Residue1.ResNum} and {myStrand1.Last()} is {angle}");
                                myStrand1.Add(Residue1.ResNum);
                            }
                            else if ((Residue1.ResNum <= myStrand1.Last() + 2)) // & (angle <= 71)
                            { //contiguous strands, only one residue missing at most
                                myStrand1.Add(Residue1.ResNum);
                            }
                            else
                            {
                                //have reached a break in strands, so add old strand and start a new one
                                List<int> newList = new List<int>();
                                for (int i = myStrand1[0]; i <= myStrand1.Last(); i++)
                                {
                                    newList.Add(i);
                                }
                                tempList.Add(newList);
                                myStrand1.Clear();
                                //Start new strand from here 
                                myStrand1.Add(Residue1.ResNum);
                            }
                        }
                        else
                        {
                            myStrand1.Add(Residue1.ResNum);
                        }
                    }

                } //end of going through each res and adding to barrel. 
                if (myStrand1.Count > 0) 
                {
                   tempList.Add(myStrand1); 
                }
                #endregion
                protoBarrel.Add(tempList);
                chainCtr++;

            }
            var strandCtr = 0;
            for (int i = 0; i < protoBarrel.Count; i++)
            {
                for (int j = 0; j < protoBarrel[i].Count; j++)
                {
                    // pass -1 for strandNum because we only know this strands number relitive to all beta conformation strands
                    Strand newStrand = new Strand(newProt.Chains[i], protoBarrel[i][j][0], protoBarrel[i][j][protoBarrel[i][j].Count-1], -1, strandCtr);
                    this.Strands.Add(newStrand);
                    strandCtr++;
                }
            }

        }


        public IEnumerator<Strand> GetEnumerator()
        {
            return Strands.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return this.GetEnumerator();
        }
    }
}