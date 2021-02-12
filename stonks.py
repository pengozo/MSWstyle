from yahoo_fin.stock_info import get_data
import matplotlib.pyplot as plt
import time

# Wie funktioniert dieser Haufen Schrott? Er zieht daily daten zu open,close,high,low und volumen von yahoo finances 
# und guckt ob die Aktien MSW gerecht pumpen. Wenn ja gibts am Ende Wachsmalbilder
# Die grüne Line ist der Close Kurs des Tages (das ist das aktuellest auf das ich zugreifen kann atm)
# Die schwarzen Linien sind High und Low Werte der Tage
# Rot zeigt das auf den ersten Tag der Suche normalisierte Handelsvolumen (erster Tag der Suche --> Volumen=1)
# Das ist alles nur Spass, bitte kauft nicht blind die Ticker die hier rausfallen. Das ist eine saudumme Idee....

# 1. In das Array stocks die zu testenden Ticker eintragen

#Der komplette NASDAQ SmallCaps
stocks=["MTRX","RLMD","FRLN","CRIS","SRCE","BATRA","KRYS","PRVB","CCRN","KBAL","LBAI","MIRM","ARQT","GRBK","NTGR","IMMR","SFST","CAMP","BTWN","FMTX","RMGB","ARTNA","CRTX","VECO","MATW","NOVN","GTHX","RICK","PCVX","MRUS","PSNL","ANIK","IMVT","PLAY","BBSI","HGEN","SWBI","EVFM","NESR","BGFV","PFC","IRCP","BDSX","CENX","IGAC","FIXX","RYTM","TGLS","LNDC","PRDO","SCVL","QADB","RNLX","PFBC","JBSS","BNFT","SVFA","BUSE","UCTT","HLIT","FANH","CFII","CALT","SOHU","BANR","RADI","FREE","ZYXI","PNTG","TTCF","CDAK","CBTX","HMPT","ERES","ADAP","BPYU","ORBC","OMER","BWMX","ALTO","CVLG","CRSA","RIGL","SIFY","NBEV","CMBM","VFF","ACRS","HBT","LOVE","APEI","OSW","ANNX","KNTE","USLM","DGII","BMTC","GBLI","FCAC","AMEH","UPLD","AOUT","DGICA","INSG","SUNW","YJ","KNDI","ALTM","IDEX","PGC","OXLC","MDGL","GHVI","DMRC","FTIV","THBR","UXIN","MESA","GNTY","NYMT","RTLR","CLVS","CTAQ","PRGS","HMCO","GNMK","TWNK","AKRO","HSTM","CRDF","GLTO","FLDM","FLXN","KDNY","BRKL","EQBK","HRTX","FLIC","GP","NDLS","MORF","CFAC","ANAB","CMTL","LOB","THCB","HBNC","CRAI","KLDO","AVDL","FTHM","GOSS","MGRC","ALEC","LTRPA","FBMS","SRGA","RMNI","NRC","AMNB","CUTR","AACQ","CGEM","WASH","AEGN","AKUS","VINP","PASG","AFMD","SIGA","AVID","JG","GBIO","ALPN","FPRX","CCNE","BCEL","VREX","SLP","BROG","VCTR","EQ","UONE","TLSA","CTBI","OMP","GLAD","ILPT","GSBC","FORR","BIVI","AGC","MGNX","EQOS","CSWC","GPRE","CNOB","CAN","GSM","SASR","HMHC","EHTH","GRSV","SAVA","MBII","ABUS","HSKA","HIFS","CLXT","HAYN","PFLT","BFST","GLSI","ALT","HTLF","LE","SY","NTUS","RDVT","ACBI","VERI","PSTX","ODT","PRTK","LANDM","MBUU","CSII","PHAT","SRAC","TCBK","BTAQU","ATNX","AMTB","PEBO","EPZM","TIG","OTLK","NPA","IMUX","CLMT","BOOM","NBLX","UFPT","GOGL","RMR","SSTI","BOWX","COWN","VSPR","MNTK","QNST","REDU","CASS","NGMS","FRTA","MDVL","FFIC","PHVS","BVS","NVEC","ANGN","ACEV","OSIS","OCSL","AXDX","ICLK","TVTX","KE","PI","PHAR","RRGB","ZUMZ","LOCO","FRSX","YMAB","FMNB","INVA","VSTA","SIEN","VACQ","DGNS","ATHA","JAGX","MARK","CLPT","APYX","JNCE","XENT","QTT","CTSO","MPAA","BTBT","LSEA","EIGR","BOMN","BWB","URGN","CHY","ROAD","MUDS","DCBO","SRRK","OCGN","PAGP","NODK","TPCO","TFFP","AWH","HARP","SYKE","WTRE","JFU","KMDA","HTLD","STKL","ARCB","CCBG","TVTY","PRCH","FSRV","CLSK","OTRK","ANIP","LAND","FLMN","FRGI","ICPT","EBON","CGNT","ALLT","BCOV","HIBB","KALV","SOLO","OFLX","SPNE","GLNG","CHW","AMAL","WLDN","VSEC","ATSG","USAT","PSAC","CERE","TILE","DSKE","NBTB","VRNA","PKOH","GLDD","YORW","BCAB","WIFI","DMTK","CNXN","VITL","HOFT","RUTH","SPWH","RDIB","AGEN","ATRO","SCSC","ROIC","GOOD","ERII","REKR","GGAL","ATRA","VYNE","VBTX","TCX","CSGS","TCMD","BTNB","EGLE","AVRO","CHPM","ALDX","ITOS","USCR","JRVR","MSBI","NSSC","DXPE","MNKD","EOSE","MRAC","SSP","AVO","KIDS","CASI","PTNR","EVLO","MGI","VRTS","KFRC","HA","NCBS","FBRX","INGN","WINA","NCNA","SESN","BCOR","CRTO","PROG","MCFT","CMRX","TSCAP","VRTU","AMTBB","BTAQ","QMCO","THRY","CLFD","LBC","HCKT","CNDT","SYRS","CPSI","ATOM","FMBH","UEIC","LQDT","SNRH","GDYN","PRTH","AMSWA","TRST","INDT","SLDB","OESX","IVA","CSSE","ORPH","ORIC","MASS","DLTH","XPEL","CGEN","PRTA","SPTN","IMTX","HEAR","CDZI","KOPN","PERI","UCL","CUE","EVOP","KELYB","CABA","RDWR","WPRT","DMLP","CHCO","HSII","OTTR","AAWW","EPIX","ALRS","SBLK","LCUT","CERS","AMWD","TTOO","DUO","HEES","IRWD","VIOT","AERI","TEKK","ACIU","ARCT","TA","MYRG","QURE","HUIZ","LAWS","MOFG","CSTE","GFN","DHIL","OFIX","ONCR","SNSE","MNOV","UVSP","DCRB","AGLE","EXPC","TRVN","SNDX","RBCAA","MBWM","ATRS","CRMD","RGP","STEP","PAE","BFC","MWK","VXRT","WRLD","HYMC","AMPH","NCMI","RVNC","PAYA","GIII","MITK","UFCS","VBIV","CTRN","EBSB","LOTZ","ADVM","SPFI","BPTS","WABC","TAST","IIIV","PAND","FFWM","GRTS","GXGX","VIH","CCCC","GDEN","CBMG","TRMD","HAFC","CDMO","NMFC","ONCT","MGPI","AMTI","NMIH","ZEAL","ZIXI","CDXC","FDUS","AROW","QADA","CODX","HMTV","IMKTA","CNST","PRTC","CDXS","CHEF","SCHN","CHUY","SPRB","LLNW","TTMI","LABP","LIVX","ZIOP","INZY","HLIO","KRON","OPI","SBSI","KALU","AMSF","GMDA","GSKY","PGEN","TCDA","TRVG","VRA","LKFN","TWCT","OXFD","ARKO","ARDX","LMAT","RRBI","ICFI","OAS","ATEX","GWRS","DTIL","CZNC","GPRO","TITN","OSBC","VKTX","STWO","IBEX","SG","SHYF","VIVO","CRNT","BCRX","CAMT","WILC","HAAC","NATR","ICAD","RBBN","APLT","IMGN","POWL","TBK","FULC","PUYI","IGIC","BTAI","HMST","ATLC","LORL","MGIC","UTMD","EGRX","ENTA","ATNI","DRIO","CMCO","CDEV","RUBY","FOSL","VTRU","KELYA","INTZ","SILC","DRNA","MBIN","ETAC","STIM","INBK","FRG","FBIO","RAPT","IMXI","NXTC","NCTY","LCY","WIMI","LAKE","CVGW","VOR","CLDX","SSPK","MOGO","KDMN","PTGX","SGMO","PLSE","EGAN","OPRT","CATM","ATHX","SPKE","OGI","BLCT","GAIN","LXRX","ATRI","CIVB","CMPS","DSPG","IBCP","NWPX","BEEM","VERU","PNNT","QQQX","SGTX","EVGN","STRL","SMBC","RILY","RDHL","CEVA","QTNT","PROF","NH","TRUE","ASLE","IRMD","SENEA","CTRM","XENE","PLL","LMNX","ACTG","STBA","SMCI","MSON","RDNT","HTBK","LCAP","VCVC","AXTI","CATC","HTBI","AEYE","ACLS","FISI","AQB","FREQ","HCCI","HOPE","CSWI","PATK","CIIC","FCBC","BMRC","OEG","ASTE","KROS","PRAA","TOWN","CRVL","TACO","AUDC","GABC","RDUS","ITRN","ANDE","QIWI","ARLP","BATRK","AKBA","SWIR","HWKN","QELL","AGYS","PDFS","ACET","GTYH","ATEC","HFFG","SMSI","CASA","TCRR","CMPI","JYNT","CPRX","RSVA","BJRI","HUBG","PLPC","FUV","TRS","SUPN","MGTX","SYBT","TNXP","CBAT","CMLF","POWW","MAXN","KOR","BOLT","LOOP","NWLI","NRIX","CALM","HEC","IIIN","FORTY","CIDM","ADUS","GRCL","HOLI","HLG","TCPC","CNSL","AGMH","DJCO","CLVR","AMSC","RBNC","ECHO","SPNS","UBX","AQMS","OSPN","TYME","ALGS","EGBN","TRHC","VOXX","CSTR","CLAR","LHDX","TELL","BYSI","FDMT","XBIT","MEIP","CVLB","GNUS","AKTS","BSRR","STFC","TXMD","SCPL","FTFT","CHRS","DZSI","NVEE","VLGEA","GOGO","MCRI","TSHA","CERC","CYTK","GAN","WSBF","SGC","WIRE","ICHR","RNA","CLNN","HFWA","VNDA","ULH","LUNA","PETS","CCD","SVAC","ONEW","OCUL","ZNTL","TRIT","STTK","IHRT","PBYI","MRSN","ANGO","IEA","LNTH","ORGO","CFFN","MTSC","FLNT","MESO","TSIA","KALA","NMRK","LASR","ISEE","TRIL","TRNS","CBAY","ADTN","FRPH","ORTX","LIND","RCEL","FNKO","KRNY","CLBK","FTOC","MLAB","MSGM","PAHC","SMBK","NWBI","NEPT","VRAY","TLND","AXGN","CARA","AOSL","OBNK","PLRX","PLUS","MERC","ONDS","AFIN","GERN","FHTX","RADA","MSEX","AMYT","ECPG","COGT","CASH","PMVP","MGTA","AMCX","ZGNX","CONN","PTSI","IPHA","CNBKA","LEGH","DVAX","INBX","APXT","SBCF","SFT","STXB","SLN","VSTM","ACTC","LRMR","DENN","OPT","MDXG","SONA","RAVN","AINV","SV","YELL","GRAY","ALTA","PLCE","ARAY","SPPI","WTBA","HURN","ABEO","NMTR","CRNX","MTEM","COLL","FBNC","WVE","IDYA","XERS","BDSI","ADN","APOG","TBBK","BPFH","VUZI","SCWX","RESN","EYPT","GRVY","KNSA","CLLS","CRMT","NEWT","HONE","NKTX","LMRK","BRY","SELB","SGH","EVER","GNPX","FIII","PETQ","THFF","EXTR","CCAP","SURF","TLMD","NLTX","XNET","TOUR","MRTN","MCBS","EBIX","HOL","AFIB","RBB","SBTX","KPTI","KSMT","PRIM","ECOL","ETNB","ESCA","CHI","EBTC","SIBN","SLRC","PRTS","EFSC","NFBK","GNOG","QH","AVXL","NBTX","DRRX","STRO","REPL","SENEB","GILT","QCRH","DFPH","OCFC","OPRX","ABTX","NAKD","OPRA","DBVT","SAFT","WTRH","BLBD","KIRK","LIZI","BGCP","HHR","PTEN","DYN","VMD","SNEX","CAC","TBPH","SP","PLAB","WETF","SRDX","BBCP","TRMK","FUSN","ABST","SPRO","PLYA","WNW","FARO","ALBO","AMOT","XOG","VRCA","OSUR","ITMR","ESTA","SCHL","CORE","AUTL","CFB","ARYA","OYST","TERN","TARS","NXGN","TRIN","LUXA","RPTX","CTMX","TSC","MRNS","HOOK","XOMA","IMOS","IESC","HPK","SMMT","CGBD","UROV","JOUT","PVAC","ESPR","CURI","BLFS","GRPN","DGICB","BCYC","BDTX","DCOM","XONE","TMDX","NISN","DHC","YI","ADAG","APTO"]

# 2. Limits und Parameter bestimmen 

start_date   = "02/01/2021" # MM/DD/YYYY
end_date     = "02/15/2021" # MM/DD/YYYY #Es kommen nur Daten bis zum (also ohne) aktuellen Datum
gain_limit   = 20           # Mindest % Wachstum über den zu testenden Bereich
volume_limit = 2            # Das Peak Handelsvolumen realtiv zum ersten Tag der Suche (3 --> im Zeitraum muss das Volumen mindestens einmal 3mal so groß sein wie am ersten Tag)
time_sleep   = 1            # Pause in Sekunden zwischen den einzelnen Abfragen um nen Ban zu vermeiden. 

# Los gehts
found_stocks=[]

print("OK: " + str(len(stocks)) + " Ticker eingegeben")

for stock_name in stocks:
    
    try:   
        stock = get_data(stock_name, start_date, end_date, index_as_date = True, interval="1d")
        stock = stock.drop(columns=['adjclose', 'ticker'])

        open_first = stock['open'].iloc[0]
        close_last = stock['close'].iloc[-1]
        volume_first = stock['volume'].iloc[0]

        stock['volume'] /= volume_first # Volumen auf 1 Normalisieren
        max_volume = stock['volume'].max() # und das Maximum finden
        gain = (close_last - open_first)/open_first * 100

        if (gain > gain_limit and max_volume > volume_limit):
            found_stocks.append(stock_name)        

            # create figure and axis objects with subplots()
            fig,ax = plt.subplots()
            # make a plot
            ax.plot(stock.index, stock.close, color="green", linewidth=1)
            ax.plot(stock.index, stock.high, color="black", linewidth=1)
            ax.plot(stock.index, stock.low , color="black", linewidth=1)
            # set x-axis label
            ax.set_xlabel("Datum",fontsize=10)
            plt.xticks(rotation=45)
            # set y-axis label
            ax.set_ylabel("price",color="green",fontsize=10)
            # set title
            ax.set_title('TICKER: '+ stock_name+ " - Gain:" + gain.astype(str)[0:-12] + "%")
            # twin object for two different y-axis on the sample plot
            ax2=ax.twinx()
            # make a plot with different y-axis using second axis object
            ax2.plot(stock.index, stock.volume ,color="red", linewidth=1)
            ax2.set_ylabel("volume",color="red",fontsize=10)

            plt.show()
      
    except AssertionError:
        print("Problem bei Ticker: " + stock_name)
     
    time.sleep(time_sleep)
    
## Done    
print("Ich hab neue Stöcker gefunden:" );
print("Sind " + str(len(found_stocks)) + " Treffer dabei")
print(', '.join(found_stocks))
