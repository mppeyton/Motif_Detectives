#!/usr/bin/env pythonw

# 22Oct2022
# GUI and fasta motif extraction By: Mina Peyton
# gff motif extraction By: Chrissy Heil 
# CSHL Programming for Biology - Final Project: Motif Detective GUI
# Input: theorectically would take the organism name & motif sequence (incomplete) 
# Output: fasta and gff3 extraction of motif sequence positions & annotations


from Bio import SeqUtils
from Bio.Seq import Seq
import gzip
import wx
import sys
UPPERBOX = sys.stdout
LOWERBOX = sys.stdout

class Frame(wx.Frame):

    def __init__(self, parent, title):
        super(Frame, self).__init__(parent, title=title, size = (1500,1000))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        global UPPERBOX
        global LOWERBOX

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(18)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Organism')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        
        vbox.Add((-1, 10))
        
        hbox0 = wx.BoxSizer(wx.HORIZONTAL)
        st0 = wx.StaticText(panel, label= 'Motif Sequence')
        st0.SetFont(font)
        hbox0.Add(st0, flag=wx.RIGHT, border=8)
        tc0 = wx.TextCtrl(panel)
        hbox0.Add(tc0, proportion=1)
        vbox.Add(hbox0, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
    
        vbox.Add((-1,10))
     
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label = 'Fasta Motif Search Results: Chromosome | Sequence | Start - End Positions')
        st4.SetFont(font)
        hbox4.Add(st4)
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add ((-1,10))

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        tc3 = wx.TextCtrl(panel, style = wx.TE_MULTILINE | wx.TE_DONTWRAP)
        UPPERBOX = RedirectText(tc3)
        hbox6.Add(tc3, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox6, proportion=1,flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border =20)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Chromosome | Feature Type | Feature Start - End Positions | ID')
        st2.SetFont(font)
        hbox2.Add(st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.VSCROLL)
        LOWERBOX = RedirectText(tc2)
	#	sys.stdout = redir
     #  print('test')
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=20)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        btn1.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        hbox5.Add(btn1)
        
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        btn2.Bind(wx.EVT_BUTTON, self.onClose)
	
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)
	
    def onClose(self,e):
        """"""
        self.Close()

    def OnButtonClicked(self,e):

# fasta motif extraction

     #  print('Received click')
        seq = ''
        pattern = 'RGKTSANNNNNRGKTSA'
   #[AG]G[GT]T[CG]A.....[AG]G[GT]T[CG]A

        with gzip.open('Caenorhabditis_elegans.WBcel235.dna.chromosome.I.fa.gz','rt') as raw:
            for line in raw:
                line = line.rstrip()
                if line.startswith('>'):
  #                 print(line)
                    continue
                else:
                    seq += line
  
        sequence = seq
        results = SeqUtils.nt_search(str(sequence),pattern)
 
 #print(results)
        f_results = []
        for i,value in enumerate(results):
            if i == 0:
                continue
            else:
                print('Chromosome.I','\t',sequence[value:value+len(pattern)],'\t', str(value+1),'  ', str(value + len(pattern)),file = UPPERBOX)
###################################
###################################
        
   
   #This is the dict where I will save the matched positions
        gene_feature={}
        hit_dict = {}
        motif_dict = {}
#chromosome fastsa motif hit parser 
        with open('motif_hit_out.txt','r') as hits:
           for line in hits:
               line = line.rstrip()
               if line.startswith('#'):
                   continue
               chromosome,motif,p_start,p_end = line.split()
               motif_dict[motif] = [p_start, p_end]
               if chromosome not in hit_dict:
                   chromosome = 'c' + chromosome.lstrip('C').rstrip(':')
                   hit_dict[chromosome] = motif_dict
        
        for key in hit_dict:        
            file_gff = "Caenorhabditis_elegans.WBcel235.108.%s.gff3.gz" % key
#gff motif extraction from fasta motif hit positions
            with gzip.open(file_gff,'rt') as gff:
                for line in range(8):
                    next(gff)            
                for line in gff:
                    line = line.rstrip()
                    if line.startswith('#'):
                        continue
                    else:
                        Chromosome, Wormbase, feature, start, end, a, strand, b, description = line.split('\t')
                        split_description = description.split(';')
                    if feature == 'gene':
                        new_description = split_description[0] + ' ' + split_description[3]
                    else:
                        new_description = split_description[0]
                    line2 = 'Chromosome.'+Chromosome + '\t' + feature + '\t' + start + '\t ' + end + '\t' + new_description
# loop over hits and feed in start and end coordinates from hit_dict                       
                    for hit in motif_dict:
                        p_start = motif_dict[hit][0]
                        p_end = motif_dict[hit][1]
#                       line1 = motif + '\t' + p_start + '\t' + p_end
                        if int(p_start) >= int(start): 
                            if int(p_end) <= int(end):
              # With extend I add the data to be retrieved in the same dict
                                gene_feature.setdefault('Chromosome.'+Chromosome, []).extend([line2])
        for key, values in gene_feature.items():
            for i in values:
                print(i, file = LOWERBOX)
        e.Skip()

class RedirectText:
     def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
     def write(self,string):
        self.out.WriteText(string)
 
        
def main():

    app = wx.App()
    ex = Frame(None, title='Motif Detective')
    ex.Show()
    app.MainLoop()
    LOWERBOX.close()
    UPPERBOX.close()

if __name__ == '__main__':
    main()
	
